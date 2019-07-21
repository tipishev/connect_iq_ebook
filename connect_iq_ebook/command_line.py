from sys import stderr
from argparse import ArgumentParser
from . import devices

'''
dracula 1090

/usr/lib/jvm/java-11-openjdk-amd64/bin/java
-Dfile.encoding=UTF-8
-Dapple.awt.UIElement=true
-jar monkeybrains.jar
-o /home/user/fascinus/ebook/bin/ebook.prg
-w -y /home/user/connectiq/fascinus_connect_key
-d fenix5
// -s 3.0.0
-f /home/user/fascinus/ebook/monkey.jungle
'''


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
    try:
        device = getattr(devices, device_name)
    except AttributeError:
        err(f'device {device_name} not found, choose from {devices.__all__}')
        return

    input_filename = args.input
    try:
        with open(input_filename, 'rt') as f:
            device.make_ebook(buffer=f)
    except FileNotFoundError as e:
        err(e)
        return
    else:
        with open('output.prg', 'w') as f:
            f.write('awesome binary output goes here')
