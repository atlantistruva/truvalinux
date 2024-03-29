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

# all windows
allwindows = ("mainWindow", "mouseWindow", "kickerWindow", "wallpaperWindow", "networkWindow", "endWindow")

# screen position code
defaultposition = \
"""
screen = QtGui.QDesktopWidget().screenGeometry()
size =  self.geometry()
self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
"""

# default button signals code
defaultsignals = \
"""
QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked(bool)"), app.exit)
QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL("clicked(bool)"), self.nextWindow)
QtCore.QObject.connect(self.backButton, QtCore.SIGNAL("clicked(bool)"), self.backWindow)
"""