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

    try:
        device = getattr(devices, args.device)
    except AttributeError:
        print(f'device {args.device} not found, choose from {devices.__all__}')
        return

    try:
        with open(args.input, 'rt') as f:
            chunker = Chunker(f,
                              char_to_width=device.char_to_width,
                              line_widths=device.line_widths,
                              max_chunk_size=8000)  # TODO encapsulate
    except FileNotFoundError as e:
        print(e)
        return

    file_maker = FileMaker(chunker, device=device)

    file_maker.write_files()
