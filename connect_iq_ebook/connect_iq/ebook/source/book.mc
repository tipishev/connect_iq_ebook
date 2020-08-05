using Toybox.Application as App;

class Book {
  public var name, currentPageNumber;
  private var _textBackend;

  function initialize(name, text_backend) {
    self.name = name;
    self._text_backend = text_backend;
  }

  // TODO use Storage for better persistence guarantee
  function _loadCurrentPageNumber() {
    var bookmarks = App.getApp().getProperty("bookmarks");
    if (bookmarks == null) {
      return 0;
    } else if (bookmarks[self.name] == null) {
      return 0;
    } else {
      return bookmarks[self.name];
    }
  }

  function _saveCurrentPageNumber() {
    var bookmarks = App.getApp().getProperty("bookmarks");
    if (bookmarks == null) {
      bookmarks = {};
    }
    bookmarks[self.name] = self.currentPageNumber;
    App.getApp().setProperty("bookmarks", bookmarks)
  }

}
