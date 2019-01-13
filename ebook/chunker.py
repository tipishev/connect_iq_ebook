from os import path
from io import StringIO
from string import Template

import json
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString


def in_this_dir(filename):
    this_dir = path.dirname(path.realpath(__file__))
    return path.join(this_dir, filename)


class Chunker:

    @staticmethod
    def utf8_bytes_length(string):
        return len(string.encode('utf-8'))

    def __init__(self, buffer,
                 max_chunk_size=None, char_to_width=None, line_widths=None):
        self.buffer = StringIO(buffer.read())  # to avoid tell() bytes bullshit
        self.max_chunk_size = max_chunk_size
        self.char_to_width = char_to_width
        self.line_widths = line_widths

    def __iter__(self):
        return self.chunker

    def get_line(self, max_width):
        assert self.char_to_width, 'please initialize char_to_width'
        line = ''
        line_px_width = 0
        last_break = None

        is_line_ready = False
        while not is_line_ready:
            position_before_new_character = self.buffer.tell()

            new_char = self.buffer.read(1)
            if not new_char:
                is_line_ready = True
            elif new_char == '\n':
                line += new_char
                is_line_ready = True
            else:
                char_px_width = self.char_to_width(new_char)
                prospective_px_width = line_px_width + char_px_width
                if prospective_px_width > max_width:
                    if last_break:
                        current_position = self.buffer.tell()
                        tail = current_position - last_break - 1
                        if tail:
                            line = line[:-tail]
                        self.buffer.seek(last_break)
                    else:
                        self.buffer.seek(position_before_new_character)
                    is_line_ready = True
                else:
                    line += new_char
                    line_px_width = prospective_px_width

                    if new_char in (' ', '—', '-'):
                        last_break = self.buffer.tell()
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
            chunk_bytes_size = 0

            while True:  # collect pages for chunk
                before_page = self.buffer.tell()
                try:
                    page_text, page_index = next(self.pager)
                    #  self.debug_print_page(page_text, page_index)
                except StopIteration:
                    buffer_has_content = False
                    break
                page_size_bytes = self.utf8_bytes_length(page_text)
                prospective_bytes_size = chunk_bytes_size + page_size_bytes
                if prospective_bytes_size > self.max_chunk_size:
                    self.buffer.seek(before_page)  # next chunk deals with it
                    break
                else:
                    chunk_text += page_text
                    chunk_bytes_size = prospective_bytes_size
                    chunk_index.append(page_index)

            if chunk_text:
                for index in chunk_index:
                    index[0] -= chunk_start
                yield chunk_text, chunk_index

        raise StopIteration()


class FileMaker:

    def __init__(self, chunker, device=None):
        self.chunker = chunker
        self.chunk_page_counts = None
        self.device = device

    def make_xml(self):
        resources = ET.Element('resources')
        self.chunk_page_counts = []
        for idx, (text, index) in enumerate(self.chunker):
            ET.SubElement(resources, 'string', id=f'Chunk{idx}').text = text
            self.chunk_page_counts.append(len(index))
            ET.SubElement(resources, 'jsonData',
                          id=f'Index{idx}').text = json.dumps(index)
        return parseString(ET.tostring(resources)).toprettyxml(indent='  ')

    def make_mc(self):
        assert self.device, 'please initialize device'
        assert self.chunk_page_counts, 'please generate XML first'
        with open(in_this_dir('template.mc')) as f:
            template = Template(f.read())

        current_page = 0
        chunk_records = []
        for idx, chunk_page_count in enumerate(self.chunk_page_counts):
            first = current_page
            stop = first + chunk_page_count
            chunk_records.append(f'  [{first}, {stop}, '
                                 f'Rez.Strings.Chunk{idx}, '
                                 f'Rez.JsonData.Index{idx}]')
            current_page = stop

        chunks_index = ',\n'.join(chunk_records)
        line_boxes = ',\n'.join(f'  {lg}' for lg in self.device.lines_geometry)
        context = {
            'chunks_index': chunks_index,
            'line_boxes': line_boxes,
        }
        rendered = template.substitute(context)
        return rendered

    def write_files(self,
                    xml_filename='book.xml', mc_filename='chunks_index.mc'):
        with open(xml_filename, 'w') as f:
            f.write(self.make_xml())
        with open(mc_filename, 'w') as f:
            f.write(self.make_mc())
