from .. import Chunker, FileMaker


class BaseDevice:

    max_chunk_size = 8000  # an arbitrary reasonable default

    def __repr__(self):
        return self.__class__.__name__.lower()

    def char_to_width(self, character: str) -> int:
        raise NotImplementedError

    def __init__(self):
        super().__init__()

    def make_ebook(self, buffer):  # TODO make customizable
        chunker = Chunker(
            buffer,
            max_chunk_size=self.max_chunk_size,
            char_to_width=self.char_to_width,
            line_widths=self.line_widths,
        )
        file_maker = FileMaker(chunker, self)
        file_maker.write_files()

    @property
    def lines_geometry(self):
        raise NotImplementedError

    @property
    def line_widths(self):
        return [width for (x, y, width, height) in self.lines_geometry]
