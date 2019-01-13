class BaseDevice:

    def char_to_width(self, character):
        pass

    @property
    def lines_geometry(self):
        pass

    @property
    def line_widths(self):
        return [width for (x, y, width, height) in self.lines_geometry]
