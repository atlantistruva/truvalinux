#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Onur Yerlikaya <onur@truvalinux.org.tr>

# this file is under construction 
# file status = development
import sys,os
from  PyQt4 import QtGui,QtCore,uic

class TsmClass:
    def __init__(self,window):
        self.window = window
    def setServName(self,name):
        self.servname = name
    def start(self):
        # python_console.py [ServiceName] start
    def stop(self):
        # python_console.py [ServiceName] stop
    def status(self):
        # python_console.py [ServiceName] status

app    = QtGui.QApplication(sys.argv)
window = uic.loadUi("tsm.ui")

tsm    = TsmClass(window)
tsm.setServName('cron')
QtCore.QObject.connect(window.pushButton,QtCore.SIGNAL("clicked()"),tsm.start)
QtCore.QObject.connect(window.pushButton_2,QtCore.SIGNAL("clicked()"),tsm.stop)
QtCore.QObject.connect(window.pushButton_3,QtCore.SIGNAL("clicked()"),tsm.status)

window.show()
sys.exit(app.exec_())
