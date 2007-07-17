#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from  PyQt4 import QtGui,QtCore,uic

class TsmClass:
    def __init__(self,window):
        self.window = window
    def alert(self):
        print "test"

app    = QtGui.QApplication(sys.argv)
window = uic.loadUi("tsm.ui")

tsm    = TsmClass(window)

QtCore.QObject.connect(window.pushButton,QtCore.SIGNAL("clicked()"),tsm.alert)

window.show()
sys.exit(app.exec_())
