#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from functools import partial
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot


class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()