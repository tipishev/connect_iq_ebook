// TODO think about index providers, should they be included?

module TextProviders {

  class BaseTextProvider {

    function getLastPageNumber() { /* not implemented */ }
    function getStrings(validPageNumber) { /* not implemented */ }

  }

  class ResourceTextProvider extends BaseTextProvider{
    private var _chunks, _currentChunkNumber, _bigString, _index;
    
    // public

    function initialize(chunks) {
      self._chunks = chunks;
      BaseTextProvider.initialize();
    }

    function getLastPageNumber() {
      return self._chunks[self._chunks.size() - 1][1] - 1;
    }

    function getStrings(validPageNumber) {
      var chunkNumber, firstPageInChunk, pageNumberInChunk, pageIndex;
      chunkNumber = self._getChunkNumber(validPageNumber);

      if (chunkNumber != self._currentChunkNumber) {  // flip the chunk
        self._currentChunkNumber = chunkNumber;
        self._setChunkVariables(chunkNumber);
      }
      firstPageInChunk = CHUNKS[self._currentChunkNumber][0];
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
      for (i=0; i<CHUNKS.size(); i++) {
        chunk = CHUNKS[i];
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
      var chunk = CHUNKS[chunkNumber];
      self._bigString = Ui.loadResource(chunk[2]);
      self._index = Ui.loadResource(chunk[3]);
    }

  }

  class PersistentStorageTextProvider extends BaseTextProvider{

  }

}
