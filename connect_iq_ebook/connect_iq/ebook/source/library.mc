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

  function initialize(bookNames) {
    // TODO :focus=> on current book
    Ui.Menu2.initialize({:title=>"Lib Menu"});

    var bookIndex, bookName, menuItem;
    for(bookIndex = 0; bookIndex < bookNames.size(); bookIndex++ ) {
      bookName = bookNames[bookIndex];

      // TODO use IconMenuItem for fanciness
      menuItem = new Ui.MenuItem(
        bookName, // label
        "read 47%", // sublabel
        bookName,  // identifier
        {});

      self.addItem(menuItem);
    }
  }

}

class LibraryMenuDelegate extends Ui.Menu2InputDelegate {

}
