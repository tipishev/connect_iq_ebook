from io import StringIO


class Chunker:

    @staticmethod
    def utf8_bytes_length(string):
        return len(string.encode('utf-8'))

    def __init__(self, buffer,
                 max_chunk_size: int = None,
                 char_to_width: callable = None,
                 line_widths: list = None):
        self.buffer = StringIO(buffer.read())
        self.max_chunk_size = max_chunk_size
        self.char_to_width = char_to_width
        self.line_widths = line_widths

    def __iter__(self):
        return self.chunker

    def get_line(self, max_line_px_width):
        assert self.char_to_width, 'please initialize char_to_width'
        line = ''
        line_px_width = 0
        last_break = None

        is_line_ready = False
        while not is_line_ready:
            position_before_new_character = self.buffer.tell()

            new_char = self.buffer.read(1)
            is_end_of_line = not new_char
            if is_end_of_line:
                is_line_ready = True
            elif new_char == '\n':
                line += new_char
                is_line_ready = True
            else:
                char_px_width = self.char_to_width(new_char)
                prospective_px_width = line_px_width + char_px_width
                if prospective_px_width <= max_line_px_width:
                    line += new_char
                    line_px_width = prospective_px_width

                    if new_char in (' ', '—', '-'):
                        last_break = self.buffer.tell()
                else:  # doesn't fit
                    if last_break:
                        current_position = self.buffer.tell()
                        overflow = current_position - last_break - 1
                        if overflow:
                            line = line[:-overflow]
                        self.buffer.seek(last_break)
                    else:
                        self.buffer.seek(position_before_new_character)
                    is_line_ready = True
        return line

    @property
    def pager(self):
        assert self.line_widths, 'please initialize line_widths'
        while True:
            page_text = ''
            page_index = []

            start_position = self.buffer.tell()
            page_index.append(start_position)

            for line_width in self.line_widths:
                line = self.get_line(line_width)
                page_text += line
                page_index.append(len(line))

            end_position = self.buffer.tell()
            if start_position != end_position:
                yield page_text, page_index
            else:
                raise StopIteration()

    def debug_print_page(self, page_text, page_index):
        buffer = StringIO(page_text)
        lines = []
        for idx, line_width in enumerate(page_index):
            if idx == 0:  # first element is absolute offset
                continue
            lines.append(buffer.read(line_width))
        lines.append('---')
        page = '\n'.join(lines)
        print(page)

    @property
    def chunker(self):
        assert self.max_chunk_size, 'please initialize max_chunk_size'
        buffer_has_content = True
        while buffer_has_content:
            chunk_start = self.buffer.tell()
            chunk_text = ''
            chunk_index = []
            chunk_size_in_bytes = 0

            while True:  # collect pages for chunk
                before_page = self.buffer.tell()
                try:
                    page_text, page_index = next(self.pager)
                except StopIteration:
                    buffer_has_content = False
                    break
                page_size_bytes = self.utf8_bytes_length(page_text)
                prospective_bytes_size = chunk_size_in_bytes + page_size_bytes
                if prospective_bytes_size > self.max_chunk_size:
                    self.buffer.seek(before_page)  # next chunk deals with it
                    break
                else:
                    #  self.debug_print_page(page_text, page_index)  # FIXME
                    chunk_text += page_text
                    chunk_size_in_bytes = prospective_bytes_size
                    chunk_index.append(page_index)

            if chunk_text:
                for index in chunk_index:
                    index[0] -= chunk_start
                yield chunk_text, chunk_index
        raise StopIteration()
