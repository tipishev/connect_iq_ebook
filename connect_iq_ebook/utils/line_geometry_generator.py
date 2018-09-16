import math

r = 109


def get_width(y):
    return math.ceil(2*math.sqrt(2*y*r - y**2))


def make_lines(font_height=22, max_y=2*r, first_y=8,
               get_width=get_width, spacing=1.2):

    y = first_y
    fits_on_screen = True
    while fits_on_screen:
        top_width = get_width(y)
        bottom_width = get_width(y + font_height)
        width = min(top_width, bottom_width)
        x = r - math.ceil(width/2)
        yield [x, y, width, font_height]
        y += math.ceil(spacing*font_height)
        fits_on_screen = y + font_height < max_y


#  [70, 8, 83, 23],
#  [30, 34, 159, 22],
#  [10, 66, 200, 22],
#  [3, 96, 215, 22],
#  [7, 126, 203, 22],
#  [20, 152, 180, 22],
#  [50, 181, 120, 22]
