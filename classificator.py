import os
import sys

from PyQt5.Qt import *

from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import LinearLayer, SigmoidLayer


def main():
    get_data()


def init_brain():
    net = buildNetwork(4096, 4096, 5, bias=True)
    ds = ClassificationDataSet(4096, nb_classes=5, class_labels=['a', 'b', 'c', 'd', 'e'])


def load_data():
    list_dir = os.listdir('img')
    list_dir.sort()
    list_for_return = []
    print('Loading data...')


def get_data():
    img = QImage(64, 64, QImage.Format_RGB32)
    data = []
    img.load('img/a.png')
    test = img.pixel(32, 32)
    print(test)


if __name__ == '__main__':
    sys.exit(main())
