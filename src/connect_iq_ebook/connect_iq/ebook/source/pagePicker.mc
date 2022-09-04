using Toybox.Graphics as Gfx;
using Toybox.WatchUi as Ui;
using MyStringUtils;

class PagePicker extends Ui.Picker {
    const CURSOR = "_";
    public var currentInput;
    private var _factory;
    private var _currentInputLabel;
    public var view;

    function initialize(view_) {
        self.view = view_;

        self._factory = new CharacterFactory("0123456789");
        self.currentInput = "";

        self._currentInputLabel = new Ui.Text(
          {
            :text=>CURSOR,
            :locX =>Ui.LAYOUT_HALIGN_CENTER,
            :locY=>Ui.LAYOUT_VALIGN_BOTTOM,
            :color=>Gfx.COLOR_WHITE,
           }
        );

        Picker.initialize(
          {
           :title=>self._currentInputLabel,
           :pattern=>[self._factory],
           :defaults=>[10],  // OK label position
          }
        );
    }

    function onUpdate(dc) {
        dc.setColor(Gfx.COLOR_BLACK, Gfx.COLOR_BLACK);
        dc.clear();
        Picker.onUpdate(dc);
    }

    function addCharacter(character, showCursor) {
        self.currentInput += character;
        self._currentInputLabel.setText(
          self.currentInput + (showCursor ? CURSOR : ""));
    }

    function setCurrentInput(obj) {  // for dire cases
        self.currentInput = obj.toString();
        self._currentInputLabel.setText(self.currentInput);
    }

    function removeCharacter() {
        self.currentInput = self.currentInput.substring(
          0, self.currentInput.length() - 1);
          self._currentInputLabel.setText(self.currentInput + CURSOR);
    }

    function isDone(value) {
        return self._factory.isDone(value);
    }
}

class PagePickerDelegate extends Ui.PickerDelegate {
    const charAt = MyStringUtils.charAt;
    private var _picker;

    function initialize(picker) {
        PickerDelegate.initialize();
        self._picker = picker;
    }

    function onCancel() {
        if(self._picker.currentInput.length() == 0) {
            Ui.popView(Ui.SLIDE_IMMEDIATE);
        }
        else {
            self._picker.removeCharacter();
        }
    }

    function onAccept(values) {
        var the_value = values[0];
        var currentInput = self._picker.currentInput;
        var endOfInput = self._picker.isDone(the_value);
        if (!endOfInput) {
            var preview = currentInput + the_value;
            if (!preview.equals("0")) {  // no leading zeroes
              var previewPageNumber = preview.toNumber();
              var lastPageNumber = self._picker.view.lastPageNumber + 1;
              if (previewPageNumber <= lastPageNumber) {
                var showCursor = previewPageNumber * 10 < lastPageNumber;
                self._picker.addCharacter(the_value, showCursor);
              }
            }
        }
        else {
            if (currentInput.length() == 0) {  // um ok, next time, dude
              Ui.popView(Ui.SLIDE_IMMEDIATE);
            } else {
              var pageNumber = currentInput.toNumber() - 1;
              self._picker.view.goToPage(pageNumber);
              Ui.popView(Ui.SLIDE_IMMEDIATE);  // to pager view
            }
        }
    }

}
