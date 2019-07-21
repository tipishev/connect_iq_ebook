from sys import stderr
from argparse import ArgumentParser

from . import devices
from .compiler import Compiler


def err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)


def make_ebook():
    parser = ArgumentParser(
        description='Garmin Connect IQ eBook maker',
        epilog='Report bugs to fascinus.team@gmail.com',
    )
    parser.add_argument('-d', '--device',
                        metavar='fenix5', help='target device')
    parser.add_argument('-i', '--input',
                        metavar='book.txt', help='path to input text')
    args = parser.parse_args()

    device_name = args.device

    try:  # TODO maybe compiler should check device name?
        device = getattr(devices, device_name)
    except AttributeError:
        err(f'device {device_name} not found, choose from {devices.__all__}')
        return

    input_filename = args.input
    assert input_filename.endswith('.txt'), 'The input should be a .txt file'
    app_name = input_filename[:-4]  # drop '.txt'

    try:
        with open(input_filename, 'rt') as f:
            compiler = Compiler(
                app_name=app_name,
                source_buffer=f,
                devices=[device],
            )
            compiler.compile(output_filename=f'{app_name}.prg')
    except FileNotFoundError as e:
        err(e)
        return
