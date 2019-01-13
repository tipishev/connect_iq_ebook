from string import Template
import json
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from os import path


def in_this_dir(filename):
    this_dir = path.dirname(path.realpath(__file__))
    return path.join(this_dir, filename)


class FileMaker:

    def __init__(self, chunker, device=None):
        self.chunker = chunker
        self.chunk_page_counts = None
        self.device = device

    def make_xml(self) -> str:
        resources = ET.Element('resources')
        self.chunk_page_counts = []
        for idx, (text, index) in enumerate(self.chunker):
            ET.SubElement(resources, 'string', id=f'Chunk{idx}').text = text
            self.chunk_page_counts.append(len(index))
            ET.SubElement(resources, 'jsonData',
                          id=f'Index{idx}').text = json.dumps(index)
        return parseString(ET.tostring(resources)).toprettyxml(indent='  ')

    def make_mc(self) -> str:
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
