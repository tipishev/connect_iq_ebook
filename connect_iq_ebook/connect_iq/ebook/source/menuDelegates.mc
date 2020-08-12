using Toybox.Application as App;
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
  private var _settings, _apply_settings_callback;

  function initialize(settings, apply_settings_callback) {
    Menu2InputDelegate.initialize();
    self._settings = settings;
    self._apply_settings_callback = apply_settings_callback;
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

  function onBack() {
    self._apply_settings_callback.invoke();
    Menu2InputDelegate.onBack();
  }

}


class NavigationMenuDelegate extends Ui.Menu2InputDelegate {
  public var pager;

  function initialize(pager_) {
    Menu2InputDelegate.initialize();

    // package as a navigator dict/object or something
    self.pager = pager_;

  }

  function onSelect(item) {

    var itemId = item.getId();

    if ( itemId == :go_to_page ) {
      var pagePicker =  new PagePicker(self.pager);
      var pagePickerDelegate = new PagePickerDelegate(pagePicker);
      Ui.popView(Ui.SLIDE_IMMEDIATE);  // to show picker immediately
      Ui.pushView(pagePicker, pagePickerDelegate, Ui.SLIDE_RIGHT);
    } else if ( itemId == :library ) {
      var libraryMenu = new LibraryMenu();
      var libraryMenuDelegate = new LibraryMenuDelegate(pager);
      Ui.popView(Ui.SLIDE_IMMEDIATE);  // to show picker immediately
      Ui.pushView(libraryMenu, libraryMenuDelegate, Ui.SLIDE_RIGHT);
    }
  }
}
