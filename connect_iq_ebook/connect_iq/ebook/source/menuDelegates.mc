using Toybox.WatchUi as Ui;

class ColorsMenuDelegate extends Ui.MenuInputDelegate {
  private var _settings;
  function initialize(settings) {
    MenuInputDelegate.initialize();
    self._settings = settings;
  }
  function onMenuItem(item) {
    self._settings["colors"] = item == :colors_dark ? "dark" : "light";
    Ui.popView(Ui.SLIDE_RIGHT);
  }
}

class SettingsMenuDelegate extends Ui.Menu2InputDelegate {
  private var _settings;

  function initialize(settings) {
    MenuInputDelegate.initialize();
    self._settings = settings;
  }

  function onSelect(item) {

    var itemId = item.getId();
    if ( itemId == :settings_colors ) {
      var colorsMenuView = new Rez.Menus.ColorsMenu();
      var colorsMenuDelegate = new ColorsMenuDelegate(self._settings);
      Ui.pushView(colorsMenuView, colorsMenuDelegate, Ui.SLIDE_LEFT);
    }

    else if ( itemId == :about ) {
      var aboutView = new AboutView();
      var aboutDelegate = new AboutDelegate(aboutView);
      Ui.pushView(aboutView, aboutDelegate, Ui.SLIDE_LEFT);
    }

    else if ( itemId == :shake_to_flip ) {
      self._settings["shake_to_flip"] = item.isEnabled();
    }

  }

}


class NavigationMenuDelegate extends Ui.MenuInputDelegate {
  public var view;

  function initialize(view_) {
    MenuInputDelegate.initialize();

    // package as a navigator dict/object or something
    self.view = view_;

  }

  function onMenuItem(item) {
    if ( item == :go_to_page ) {
      var pagePicker =  new PagePicker(self.view);
      var pagePickerDelegate = new PagePickerDelegate(pagePicker);
      Ui.popView(Ui.SLIDE_IMMEDIATE);  // to show picker immediately
      Ui.pushView(pagePicker, pagePickerDelegate, Ui.SLIDE_RIGHT);
    }
  }
}
