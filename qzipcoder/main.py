#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PySide.QtGui import QApplication
from window import MainWindow


def main(argv):
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    window.raise_()
    window.clearFocus()
    app.exec_()


if __name__ == '__main__':
    import sys
    main(sys.argv)
