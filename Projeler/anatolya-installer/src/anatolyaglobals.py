# -*- coding: utf-8 -*-
#
# Copyright (C) 2008, Truva Linux
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

allWindows = ("mainWindow", "partedWindow", "discWindow", "installWindow", "userWindow", "grubWindow", "endWindow")

packageDir = "/var/log/mount/Paketler/"
pictureDir = "/home/rohanrhu/Resim/"

defaultSignals = \
"""
self.connect(self.nextButton, QtCore.SIGNAL("clicked(bool)"), self.nextWindow)
self.connect(self.backButton, QtCore.SIGNAL("clicked(bool)"), self.backWindow)
"""

defaultPosition = \
"""
screen = QtGui.QDesktopWidget().screenGeometry()
size =  self.geometry()
self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
"""

# for i in a: os.system("pyuic4 %s -o screens/%s.py" % (os.getcwd() + "/screens/ui/" + i, str(i[0:-3])))