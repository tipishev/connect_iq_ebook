using Toybox.Application as App;
using Toybox.WatchUi as Ui;

class eBookApp extends App.AppBase {

    function initialize() {
        AppBase.initialize();
    }

    function onStart(state) {
    }

    function onStop(state) {
    }

    function getInitialView() {
     var pagerView = new PagerView();
     var pagerDelegate = new PagerDelegate(pagerView);
     return [pagerView, pagerDelegate];
    }

}
