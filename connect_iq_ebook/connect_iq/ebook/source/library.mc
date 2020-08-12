using Toybox.Application as App;
using Toybox.WatchUi as Ui;


class Library {  // or BookFactory? :)
  // class to manage available books

  public var books;

  function toString() {
    return "<Library " + self.books.toString() + ">";
  }
  
  function initialize() {
    // TODO make it a dict?
    // TODO book database? to store name, metadata, current progress
    // TODO load book-making recipies from Rez
    self.books = ["Chunks", "Dummy"];
  }

  function loadBook(name) {
    if (name.equals("Dummy")) {
      return new Book("Dummy", new TextBackends.DummyTextBackend());
    } else if (name.equals("Chunks")) {
      return new Book("Chunks", new TextBackends.RezTextBackend(CHUNKS));
    }
  }

  function loadCurrentBook() {
    var currentBookName = App.getApp().getProperty("currentBookName");
    if (currentBookName == null) {
      currentBookName = self.books[0];
      App.getApp().setProperty("currentBookName", currentBookName);
    }
    return self.loadBook(currentBookName);
  }
}

class LibraryMenu extends Ui.Menu2 {

  function initialize() {
    var library = App.getApp().library;

    // TODO :focus=> on current book
    Ui.Menu2.initialize({:title=>"Library"});

    var bookIndex, bookName, menuItem;
    for(bookIndex = 0; bookIndex < library.books.size(); bookIndex++ ) {
      bookName = library.books[bookIndex];

      // TODO use IconMenuItem for fanciness
      menuItem = new Ui.MenuItem(
        bookName, // label
        "read 47%", // sublabel  // TODO show real progress
        bookName,  // identifier
        {});

      self.addItem(menuItem);
    }
  }

}

class LibraryMenuDelegate extends Ui.Menu2InputDelegate {

  var pager;  // FIXME make a method

  function initialize(pager_) {
    Menu2InputDelegate.initialize();
    self.pager = pager_;
  }

  function onSelect(item) {
    var bookName = item.getId();
    print("Opening book " + bookName);
    var library = App.getApp().library;
    self.pager.book = library.loadBook(bookName);
    Ui.popView(Ui.SLIDE_IMMEDIATE);
  }
}
