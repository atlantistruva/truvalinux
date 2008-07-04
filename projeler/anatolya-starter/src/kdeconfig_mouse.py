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

from kdecore import *
import sys
from qt import *

hand = sys.argv[1]
clickselect = sys.argv[2]
clickbool = None

if clickselect == "DoubleClick":
	clickbool = False
else:
	clickbool = True

app = KApplication([''], "mouseconfig")

config = KConfig("kcminputrc")
config.setGroup("Mouse")

config.writeEntry("MouseButtonMapping", QString(str(hand)))

config.sync()

KIPC.sendMessageAll(KIPC.SettingsChanged, KApplication.SETTINGS_MOUSE)

config = KConfig("kdeglobals")
config.setGroup("KDE")
config.writeEntry("SingleClick", clickbool)
config.sync()

KIPC.sendMessageAll(KIPC.SettingsChanged, KApplication.SETTINGS_MOUSE)