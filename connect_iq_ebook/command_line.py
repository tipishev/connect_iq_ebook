from argparse import ArgumentParser

from . import Chunker, FileMaker, devices


def make_ebook():
    parser = ArgumentParser(
        description='Garmin Connect IQ eBook maker',
        epilog='Report bugs to fascinus.team@gmail.com',
    )
    parser.add_argument('-i', '--input',
                        metavar='book.txt', help='path to input text')
    parser.add_argument('-d', '--device',
                        metavar='fenix5', help='target device')
    args = parser.parse_args()

    device_name = args.device

    try:
        device = getattr(devices, device_name)
    except AttributeError:
        print(f'Device {device_name} not found, choose from {devices.__all__}')
        return

    input_file_name = args.input
    # TODO check for file existence

    print(f'Making you Garmin eBook with {args}')
    #  self.file = open(in_this_dir('dracula.txt'), 'r')
    #  device = Fenix5x()
    #  chunker = Chunker(self.file,
    #                    char_to_width=device.char_to_width,
    #                    line_widths=device.line_widths,
    #                    max_chunk_size=8000)
    #  self.file_maker = FileMaker(chunker, device=device)
    #  self.file_maker.write_files()
