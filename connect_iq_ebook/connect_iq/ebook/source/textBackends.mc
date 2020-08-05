using Toybox.WatchUi as Ui;

module TextBackends {

  class BaseTextBackend {

    function getLastPageNumber() { /* not implemented */ }
    function getStrings(validPageNumber) { /* not implemented */ }

  }

  class DummyTextBackend extends BaseTextBackend {
    private var _pages;

    function initialize() {
      self._pages = [
        ["fo1", "ba1", "ba1", "q1", "qz1", "bar1", "oo1"],
        ["fo2", "ba2", "ba2", "q2", "qz2", "bar2", "oo2"],
        ["fo3", "ba3", "ba3", "q3", "qz3", "bar3", "oo3"],
      ];
      BaseTextBackend.initialize();
    }
    function getLastPageNumber() { return self._pages.size() - 1; }
    function getStrings(validPageNumber) { return self._pages[validPageNumber]; }
  }

  class RezTextBackend extends BaseTextBackend{
    private var _chunks, _currentChunkNumber, _bigString, _index, _lastPageNumber;
    
    // public

    function initialize(chunks) {
      self._chunks = chunks;

      // caching to variable
      self._lastPageNumber = self._chunks[self._chunks.size() - 1][1] - 1;

      BaseTextBackend.initialize();
    }

    function getLastPageNumber() {
      return self._lastPageNumber;
    }

    function getStrings(validPageNumber) {
      var chunkNumber, firstPageInChunk, pageNumberInChunk, pageIndex;
      chunkNumber = self._getChunkNumber(validPageNumber);

      if (chunkNumber != self._currentChunkNumber) {  // flip the chunk
        self._currentChunkNumber = chunkNumber;
        self._setChunkVariables(chunkNumber);
      }
      firstPageInChunk = self._chunks[self._currentChunkNumber][0];
      pageNumberInChunk = validPageNumber - firstPageInChunk;
      pageIndex = self._index[pageNumberInChunk];

      var i, lineStart, lineEnd, result, string;
      lineStart = pageIndex[0];
      result = [];
      for (i=1/*NB*/; i < pageIndex.size(); i++) {
        lineEnd =  lineStart + pageIndex[i];
        string = self._bigString.substring(lineStart, lineEnd);
        result.add(string);
        lineStart = lineEnd;
      }
      return result;
    }

    // private

    // Chunks
    function _getChunkNumber(pageNumber) {
      var i, chunk, firstPage, stopPage;
      // TODO binary search instead of linear scan
      for (i=0; i<self._chunks.size(); i++) {
        chunk = self._chunks[i];
        firstPage = chunk[0];
        stopPage = chunk[1];
        if (pageNumber >= firstPage && pageNumber < stopPage) {
          return i;
        }
      }
      return null;
    }

    function _setChunkVariables(chunkNumber) {
      self._bigString = null;
      self._index = null;
      var chunk = self._chunks[chunkNumber];
      self._bigString = Ui.loadResource(chunk[2]);
      self._index = Ui.loadResource(chunk[3]);
    }

  }

  class PersistentStorageTextBackend extends BaseTextBackend{

  }

}
