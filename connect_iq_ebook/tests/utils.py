import os


def in_this_dir(filename):
    this_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(this_dir, filename)


def unity(char):
    return 1
