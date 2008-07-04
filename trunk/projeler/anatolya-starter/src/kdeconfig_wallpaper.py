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
import dcopext
import sys

picture_file = sys.argv[1]

app = KApplication([''], "wallpaperconfig")

dcopclient = KApplication.dcopClient()
dcopclient.registerAs("changewp")
dcopapp = dcopext.DCOPApp("kdesktop", dcopclient)
current = dcopapp.KBackgroundIface.currentWallpaper(1)[1]

dcopapp.KBackgroundIface.setWallpaper(str(picture_file), 6)