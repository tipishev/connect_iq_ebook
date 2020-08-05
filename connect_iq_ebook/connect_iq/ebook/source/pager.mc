using Toybox.Application as App;
using Toybox.Graphics as Gfx;
using Toybox.WatchUi as Ui;
using Toybox.Timer;
using Toybox.Sensor;
using Toybox.Math;

// TODO settings manager/module
const DEFAULT_SETTINGS = {
  "colors" => "dark",
  "shake_to_flip" => false,
};

class PagerView extends Ui.View {

    public var settings;
    private var  _book, _shakeToFlipTimer;  // TODO camelcase

    function initialize() {
      View.initialize();

      self.settings = App.getApp().getProperty("settings");

      // TODO handle newly-appearing keys: check all necessary keys
      // TODO settings manager
      if (self.settings == null) {
        self.settings = DEFAULT_SETTINGS;
      }

      /* = new TextBackends.RezTextBackend(CHUNKS); */
      self._book = new Book("Dummy", new TextBackends.DummyTextBackend());

      self._shakeToFlipTimer = new Timer.Timer();

    }

    // TODO move out
    function shakeToFlipTimerCallback() {
      var sensorInfo = Sensor.getInfo();
      if (sensorInfo has :accel && sensorInfo.accel != null) {
	      var accel = sensorInfo.accel;
	      var xAccel = accel[0];
	      var yAccel = accel[1];
	      var zAccel = accel[2];

        // TODO debounce timer
        // TODO better shake detection
        // TODO magic number to settings or configurable
        if (Math.sqrt(xAccel * xAccel + yAccel * yAccel + zAccel * zAccel) > 1250) {
          self.showNextPage();
        }

      }
    }


    function onLayout(dc) {
      View.onLayout(dc);
      self.applySettings(); // TODO move to initialize?
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

    function drawPage(dc) {
      self.drawStrings(dc, self._book.getStrings());
    }

    // Navigation
    
    function showNextPage() {
      self._book.goToNextPage();
      Ui.requestUpdate();
    }

    function showPreviousPage() {
      self._book.goToPreviousPage();
      Ui.requestUpdate();
    }


    function openNavigationMenu() {
      var navigationMenuView = new Rez.Menus.NavigationMenu();
      var title = self._book.showHumanPosition();
      navigationMenuView.setTitle(title);

      var navigationMenuDelegate = new NavigationMenuDelegate(self);
      Ui.pushView(navigationMenuView, navigationMenuDelegate, Ui.SLIDE_RIGHT);
    }

    function applySettings() {
      if (self.settings["shake_to_flip"]) {
        self._shakeToFlipTimer.start(method(:shakeToFlipTimerCallback), 100, true);
      } else {
        self._shakeToFlipTimer.stop();
      }
    }

    // Settings
    function openSettingsMenu() {

      var settingsMenuView = new Rez.Menus.SettingsMenu();
      settingsMenuView.setTitle("Settings");  // TODO set in XML

      var shakeToFlipIndex = settingsMenuView.findItemById(:shake_to_flip);
      var shakeToFlipMenuItem = settingsMenuView.getItem(shakeToFlipIndex);
      shakeToFlipMenuItem.setEnabled(self.settings["shake_to_flip"]);

      var settingsDelegate = new SettingsMenuDelegate(self.settings,
                                                      method(:applySettings));

      Ui.pushView(settingsMenuView, settingsDelegate, Ui.SLIDE_LEFT);
    }

    function onUpdate(dc) {

      // TODO split reading settings and changing dc
      print("setting colors");
      if (self.settings["colors"].equals("light")) {
        dc.setColor(Gfx.COLOR_BLACK, Gfx.COLOR_WHITE);
      } else {
        dc.setColor(Gfx.COLOR_WHITE, Gfx.COLOR_BLACK);
      }

      dc.clear();
      self.drawPage(dc);
      /* drawLineBoxes(dc); */
    }

    function onHide() {
      // TODO settings manager
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

    // because this button is more sturdy on Fenix 5
    function onSelect() {
      self._view.showNextPage();
    }

    function onMenu() {
      self._view.openSettingsMenu();
    }

}
