from argparse import ArgumentParser
from . import devices

'''
dracula 1090

/usr/lib/jvm/java-11-openjdk-amd64/bin/java
-Dfile.encoding=UTF-8
-Dapple.awt.UIElement=true
-jar /home/user/connectiq/connectiq-sdk-lin-3.0.7-2018-12-17-efeb3e3/bin/monkeybrains.jar
-o /home/user/fascinus/ebook/bin/ebook.prg
-w -y /home/user/connectiq/fascinus_connect_key
-d fenix5_sim
-s 3.0.0
-f /home/user/fascinus/ebook/monkey.jungle
'''

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

    device_name = args.device, args.input
    try:
        device = getattr(devices, device_name)
    except AttributeError:
        print(f'device {device_name} not found, choose from {devices.__all__}')
        return

    input_filename = args.input
    try:
        with open(input_filename, 'rt') as f:
            device.make_ebook(buffer=f)
    except FileNotFoundError as e:
        print(e)
        return
