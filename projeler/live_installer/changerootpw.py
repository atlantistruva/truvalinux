#!/usr/bin/env python
# -*- coding: latin-1 -*-

import gtk, sys, os

msgtext  = "Bu, sistem yöneticisi için oldukça güçlü bir şifre koruması sağlar.\n"
msgtext += "Şifreleme ile elde edilen yönetici hakları kurulum sonrası devreye girer."

dialog = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, msgtext ) 

dialog.run()

#os.spawnlp( os.P_NOWAIT, 'userpasswd' )

dialog.destroy()
