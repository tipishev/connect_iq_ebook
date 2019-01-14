class BaseDevice:

    def __repr__(self):
        return self.__class__.__name__.lower()

    def char_to_width(self, character: str) -> int:
        pass

    @property
    def lines_geometry(self):
        pass

    @property
    def line_widths(self):
        return [width for (x, y, width, height) in self.lines_geometry]
