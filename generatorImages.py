import sys
from PyQt5.Qt import *
from PyQt5.QtGui import *


def image(letter='A', dir='./img'):
    png_file = dir + '/' + letter + '.png'
    createimage(letter, png_file)


def createimage(letter, png_file):
    img = QImage(64, 64, QImage.Format_RGB32)
    img.fill(Qt.white)
    p = QPainter(img)
    p.setPen(Qt.black)
    p.setFont(QFont('Arial', 40))
    p.drawText(img.rect(), Qt.AlignCenter, letter)
    p.end()
    img.save(png_file)


def main():
    app = QApplication([])

    # abc = (
    #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    #    'w', 'x', 'y', 'z')

    abc = ('a', 'b', 'c', 'd', 'e')

    for i in abc:
        image(i)


if __name__ == '__main__':
    sys.exit(main())