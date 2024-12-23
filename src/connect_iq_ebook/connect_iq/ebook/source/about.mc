using Toybox.WatchUi as Ui;
using Toybox.Graphics as Gfx;

class AboutView extends Ui.View {
    private var _page;
    const ABOUT = 0;

    function initialize() {
      View.initialize();
      self._page = ABOUT;
    }

    function showAbout() {
      self._page = ABOUT;
      Ui.requestUpdate();
    }

    function onUpdate(dc) {

      dc.setColor(Gfx.COLOR_WHITE, Gfx.COLOR_WHITE);
      dc.clear();
      dc.setColor(Gfx.COLOR_BLACK, Gfx.COLOR_WHITE);
      setLayout(Rez.Layouts.AboutLayout(dc));
      View.onUpdate(dc);
    }
}

class AboutDelegate extends Ui.BehaviorDelegate
{
    hidden var _view;

    function initialize(view) {
        self._view = view;
        BehaviorDelegate.initialize();
    }

    /* function onBack() { */
    /*     Ui.popView(Ui.SLIDE_IMMEDIATE); */
    /* } */

    function onPreviousPage() {
      print("showing about");
      self._view.showAbout();
    }
}
