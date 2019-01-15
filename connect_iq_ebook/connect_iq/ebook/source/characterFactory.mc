using Toybox.Graphics as Gfx;
using Toybox.WatchUi as Ui;
using MyStringUtils;


class CharacterFactory extends Ui.PickerFactory {
    private var _characterSet;
    const DONE = -1;
    const charAt = MyStringUtils.charAt;

    function initialize(characterSet) {
        PickerFactory.initialize();
        self._characterSet = characterSet;
    }

    function getIndex(value) {
        var index = self._characterSet.find(value);
        return index;
    }

    function getSize() {
        return self._characterSet.length() + 1;
    }

    function getValue(index) {
        if (index == self._characterSet.length()) {
            return DONE;
        }

        return charAt(self._characterSet, index);
    }

    function getDrawable(index, selected) {
        if (index == self._characterSet.length()) {
            return new Ui.Text(
            {
             :text=>"OK",
             :color=>Gfx.COLOR_WHITE,
             :font=>Gfx.FONT_LARGE,
             :locX =>Ui.LAYOUT_HALIGN_CENTER,
             :locY=>Ui.LAYOUT_VALIGN_CENTER,
             }
           );
        }

        return new Ui.Text(
        {
         :text=>getValue(index),
         :color=>Gfx.COLOR_WHITE,
         :font=> Gfx.FONT_LARGE,
         :locX =>Ui.LAYOUT_HALIGN_CENTER,
         :locY=>Ui.LAYOUT_VALIGN_CENTER,
        });
    }

    function isDone(value) {
        return value == DONE;
    }
}
