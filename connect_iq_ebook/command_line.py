from argparse import ArgumentParser

from . import Chunker, FileMaker, devices


def make_ebook():
    parser = ArgumentParser(
        description='Garmin Connect IQ eBook maker',
        epilog='Report bugs to fascinus.team@gmail.com',
    )
    parser.add_argument('--input', help='path to input text')
    parser.add_argument('--device', help='target device')

    args = parser.parse_args()

    print(f'Making you Garmin eBook with {args}')
    #  self.file = open(in_this_dir('catch22_full.txt'), 'r')
    #  self.file = open(in_this_dir('tom_sawyer.txt'), 'r')
    #  self.file = open(in_this_dir('dracula.txt'), 'r')
    #  device = Fenix5x()
    #  chunker = Chunker(self.file,
    #                    char_to_width=device.char_to_width,
    #                    line_widths=device.line_widths,
    #                    max_chunk_size=8000)
    #  self.file_maker = FileMaker(chunker, device=device)
    #  self.file_maker.write_files()
