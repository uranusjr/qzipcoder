#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import zipcodetw
from PySide.QtCore import QUrl
from PySide.QtGui import (
    QDesktopServices,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QVBoxLayout,
    QWidget,
)


class MenuBar(QMenuBar):
    def __init__(self, *args, **kwargs):
        super(MenuBar, self).__init__(*args, **kwargs)
        menu = self.addMenu('About')
        menu.addAction('About ZipCodeTW...').triggered.connect(
            self.openZipCodeTWAbout
        )

    def openZipCodeTWAbout(self, *args, **kwargs):
        QDesktopServices.openUrl(QUrl('http://zipcode.mosky.tw/about'))


class MainWidget(QWidget):

    stylesheet = """
        QLineEdit {
            font-size: 20px;
        }
    """

    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self._setupUi()
        self.iField.textChanged.connect(self.updateZipCode)

    def _setupUi(self):
        self.iField = QLineEdit()
        self.iField.setFixedHeight(40)
        self.oField = QLineEdit()
        self.oField.setReadOnly(True)
        self.oField.setFixedHeight(40)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(QLabel('請在上面這欄輸入地址'))
        mainLayout.addWidget(self.iField)
        mainLayout.addStretch(1)
        mainLayout.addWidget(QLabel('郵遞區號會出現在這邊'))
        mainLayout.addWidget(self.oField)
        self.setLayout(mainLayout)
        self.setStyleSheet(MainWidget.stylesheet)

    def focusInEvent(self, event):
        super(MainWidget, self).focusInEvent(event)
        self.focusWidget().clearFocus()

    def updateZipCode(self, text):
        code = zipcodetw.find(text)
        self.oField.setText(' '.join([code, text]))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Zip Code Finder for Addresses in Taiwan')
        self.setCentralWidget(MainWidget())
        self.setMenuBar(MenuBar())
        self.resize(500, 175)
