using Toybox.Application as App;

class Book {
  public var name, currentPageNumber;
  private var _textBackend;

  function toString() {
    return "<Book \"" + self.name + "\">";
  }

  function initialize(name, textBackend) {
    self.name = name;
    self._textBackend = textBackend;
    self.currentPageNumber = self._loadCurrentPageNumber();
  }

  function goToPage(pageNumber) {
    print("Going to page " + pageNumber);
    if (pageNumber >= 0 && pageNumber <= self._textBackend.getLastPageNumber()) {
        self.currentPageNumber = pageNumber;
        self._saveCurrentPageNumber();
    } else {
      print(pageNumber + " is not in the book");
    }
  }

  function goToNextPage() {
    self.goToPage(self.currentPageNumber + 1);
  }

  function goToPreviousPage() {
    self.goToPage(self.currentPageNumber - 1);
  }

  // Human presentation
  function showHumanPosition() {
    // because humans count from 1, not 0
    return format("$1$/$2$", [self.currentPageNumber + 1,
                              self._textBackend.getLastPageNumber() + 1]);
  }

  function getStrings() {
    return self._textBackend.getStrings(self.currentPageNumber);
  }

  // TODO use Storage for better persistence guarantee
  function _loadCurrentPageNumber() {
    var bookmarks = App.getApp().getProperty("bookmarks");
    if (bookmarks == null || bookmarks[self.name] == null) {
      return 0;
    } else {
      return bookmarks[self.name];
    }
    // FIXME handle under/overflow with min/max on 0 and lastPage
  }

  function _saveCurrentPageNumber() {
    var bookmarks = App.getApp().getProperty("bookmarks");
    if (bookmarks == null) {
      bookmarks = {};
    }
    bookmarks[self.name] = self.currentPageNumber;
    App.getApp().setProperty("bookmarks", bookmarks);
  }
}
