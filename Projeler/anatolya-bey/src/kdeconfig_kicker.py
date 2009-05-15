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

from qt import *
from kdecore import *
import sys

selection = sys.argv[1]

app = KApplication([''], "kickerconfig")

kickerConfig = KConfig("kickerrc")
kickerConfig.setGroup("General")

if selection == "transparent":
	kickerConfig.writeEntry(QString("Position"), 3)
	kickerConfig.writeEntry(QString("Transparent"), 1)
if selection == "toptransparent":
	kickerConfig.writeEntry(QString("Position"), 2)
	kickerConfig.writeEntry(QString("Transparent"), 1)
if selection == "classic":
	kickerConfig.writeEntry(QString("Position"), 3)
	kickerConfig.writeEntry(QString("Transparent"), 0)
if selection == "modern":
	kickerConfig.writeEntry(QString("Position"), 2)
	kickerConfig.writeEntry(QString("Transparent"), 0)

client = KApplication.dcopClient()
client.send("kicker", "kicker", "restart()", "")