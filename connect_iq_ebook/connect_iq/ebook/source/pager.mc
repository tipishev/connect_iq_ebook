using Toybox.Application as App;
using Toybox.Graphics as Gfx;
using Toybox.WatchUi as Ui;
using Toybox.Timer;
using Toybox.Sensor;
using Toybox.Math;

const DEFAULT_SETTINGS = {
  "colors" => "dark",
  "shake_to_flip" => false,
};

class PagerView extends Ui.View {

    public var currentPageNumber, lastPageNumber;
    private var _currentChunkNumber, _bigString, _index;
    public var settings;

    function initialize() {
      View.initialize();

      self.settings = App.getApp().getProperty("settings");

      // TODO handle newly-appearing keys: check all necessary keys
      // hint: check if `has` an appropriate keyword
      // TODO settings manager
      if (self.settings == null) {
        self.settings = DEFAULT_SETTINGS;
      }


      self.lastPageNumber = CHUNKS[CHUNKS.size() - 1][1] - 1;
      print(format("Last Page Number: $1$", [self.lastPageNumber]));
      self.currentPageNumber = self._loadCurrentPageNumber();
      self._currentChunkNumber = _getChunkNumber(self.currentPageNumber);
      self._setChunkVariables(self._currentChunkNumber);

    }

    // Chunks
    function _getChunkNumber(pageNumber) {
      var i, chunk, firstPage, stopPage;
      for (i=0; i<CHUNKS.size(); i++) {
        chunk = CHUNKS[i];
        firstPage = chunk[0];
        stopPage = chunk[1];
        if (pageNumber >= firstPage && pageNumber < stopPage) {
          return i;
        }
      }
      return null;
    }

    function _setChunkVariables(chunkNumber) {
      self._bigString = null;
      self._index = null;
      var chunk = CHUNKS[chunkNumber];
      self._bigString = Ui.loadResource(chunk[2]);
      self._index = Ui.loadResource(chunk[3]);
    }

    function shakeToFlipTimerCallback() {
	    print("shake_to_flip timer callback");
      var sensorInfo = Sensor.getInfo();
      if (sensorInfo has :accel && sensorInfo.accel != null) {
	      var accel = sensorInfo.accel;
	      var xAccel = accel[0];
	      var yAccel = accel[1];
	      var zAccel = accel[2];

        // FIXME magic number to settings or configurable
        if (Math.sqrt(xAccel * xAccel + yAccel * yAccel + zAccel * zAccel) > 1500) {
          self.showNextPage();
        }

      }
    }

    function onLayout(dc) {

    // FIXME enable/disable timer without restarting the app
      if (self.settings["shake_to_flip"]) {
        var _timer = new Timer.Timer();
        _timer.start(method(:shakeToFlipTimerCallback), 100, true);
      }

      View.onLayout(dc);
    }

    // Persistent Storage
    function _loadCurrentPageNumber() {
      var currentPageNumber;
      currentPageNumber = App.getApp().getProperty("currentPageNumber");
      if ((currentPageNumber == null) || (currentPageNumber > self.lastPageNumber)) {
        currentPageNumber = 0;
      }
      return currentPageNumber;
    }

    function _saveCurrentPageNumber(currentPageNumber) {
        App.getApp().setProperty("currentPageNumber", currentPageNumber);
    }


    // Text
    function _getStrings(validPageNumber) {
      var chunkNumber, firstPageInChunk, pageNumberInChunk, pageIndex;
      chunkNumber = self._getChunkNumber(validPageNumber);

      if (chunkNumber != self._currentChunkNumber) {  // flip the chunk
        self._currentChunkNumber = chunkNumber;
        self._setChunkVariables(chunkNumber);
      }
      firstPageInChunk = CHUNKS[self._currentChunkNumber][0];
      pageNumberInChunk = validPageNumber - firstPageInChunk;
      pageIndex = self._index[pageNumberInChunk];

      var i, lineStart, lineEnd, result, string;
      lineStart = pageIndex[0];
      result = [];
      for (i=1/*NB*/; i < pageIndex.size(); i++) {
        lineEnd =  lineStart + pageIndex[i];
        string = self._bigString.substring(lineStart, lineEnd);
        result.add(string);
        lineStart = lineEnd;
      }
      return result;
    }

    // Graphics
    function drawLineBoxes(dc) {
      var i, line_box, x, y, width, height;
      for (i=0; i<LINE_BOXES.size(); i++) {
        line_box = LINE_BOXES[i];
        x = line_box[0];
        y = line_box[1];
        width = line_box[2];
        height = line_box[3];
	dc.drawRectangle(x, y, width, height);
      }
    }

    function drawStrings(dc, strings) {
      var i, x, y, string;
      for (i=0; i<strings.size(); i++) {
        x = LINE_BOXES[i][0];
        y = LINE_BOXES[i][1];
        string = strings[i];
        dc.drawText(x, y, Gfx.FONT_SYSTEM_XTINY,
                    string, Gfx.TEXT_JUSTIFY_LEFT);
      }
    }

    function drawPage(dc, validPageNumber) {
      self.drawStrings(dc, self._getStrings(validPageNumber));
    }

    // Navigation
    function goToPage(pageNumber) {
      print("Going to page " + pageNumber);
      if (pageNumber >= 0 && pageNumber <= self.lastPageNumber) {
          self.currentPageNumber = pageNumber;
          Ui.requestUpdate();
          self._saveCurrentPageNumber(self.currentPageNumber);
      } else {
        print(pageNumber + " is not in the book");
      }
    }

    function showNextPage() {
      self.goToPage(self.currentPageNumber + 1);
    }

    function showPreviousPage() {
      self.goToPage(self.currentPageNumber - 1);
    }

    function openNavigationMenu() {
      var navigationMenuView = new Rez.Menus.NavigationMenu();
      var title = self.showHumanPosition();
      navigationMenuView.setTitle(title);

      var navigationMenuDelegate = new NavigationMenuDelegate(self);
      Ui.pushView(navigationMenuView, navigationMenuDelegate, Ui.SLIDE_RIGHT);
    }

    // Human presentation
    function showHumanPosition() {
      return format("$1$/$2$", [self.currentPageNumber + 1,  // because humans count from 1, not 0
                                self.lastPageNumber + 1]);
    }

    // Settings
    function openSettingsMenu() {

      var settingsMenuView = new Rez.Menus.SettingsMenu();
      settingsMenuView.setTitle("Settings");  // TODO set in XML

      var shakeToFlipIndex = settingsMenuView.findItemById(:shake_to_flip);
      var shakeToFlipMenuItem = settingsMenuView.getItem(shakeToFlipIndex);
      shakeToFlipMenuItem.setEnabled(self.settings["shake_to_flip"]);

      var settingsDelegate = new SettingsMenuDelegate(self.settings);

      Ui.pushView(settingsMenuView, settingsDelegate, Ui.SLIDE_LEFT);
    }

    function onUpdate(dc) {
      if (self.settings["colors"].equals("light")) {
        dc.setColor(Gfx.COLOR_BLACK, Gfx.COLOR_WHITE);
      } else {
        dc.setColor(Gfx.COLOR_WHITE, Gfx.COLOR_BLACK);
      }
      dc.clear();
      self.drawPage(dc, self.currentPageNumber);
      /* drawLineBoxes(dc); */
    }

    function onHide() {
      App.getApp().setProperty("settings", self.settings);
    }
}

class PagerDelegate extends Ui.BehaviorDelegate
{
    hidden var _view;
    function initialize(view) {
        self._view = view;
        BehaviorDelegate.initialize();
    }

    function onBack() {
        Ui.popView(Ui.SLIDE_IMMEDIATE);
    }

    function onPreviousPage() {
      self._view.showPreviousPage();
    }

    function onNextPage() {
      self._view.openNavigationMenu();
    }

    function onSelect() {
      self._view.showNextPage();
    }

    function onMenu() {
      self._view.openSettingsMenu();
    }

}
