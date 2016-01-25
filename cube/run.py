#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

css_path = "css/base.css"

from cube_manager import main


app = QtGui.QApplication(sys.argv)
app.setStyleSheet(open('{}'.format(css_path), "r").read())
m = main.BaseWindow()
m.show()
sys.exit(app.exec_())

