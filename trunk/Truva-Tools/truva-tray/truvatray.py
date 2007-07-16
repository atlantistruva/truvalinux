#!/usr/bin/python

import os
import pygtk
pygtk.require("2.0")
import gtk
import egg.trayicon
import gobject

__version__="0.0.3"

def exit_applet( *args ):
    gtk.main_quit();
    return;

def applet_face_click( window, event, *data ):
    if event.button == 3 :
        menu.popup( None, None, None, 0, event.time );
    return;

def repo_control( window, event, *data ):
	if event.button == 1 :
		try:
			stat = open("/sys/class/net/eth0/operstate")
			#print stat.readline()
			STATUS = stat.readline
			
			if ( STATUS == "down" ):
				image_widget.set_from_stock(gtk.STOCK_DISCONNECT, gtk.ICON_SIZE_SMALL_TOOLBAR)
				tooltips.set_tip(event_box, "Baglanti yok...")
			else:
				image_widget.set_from_stock(gtk.STOCK_CONNECT, gtk.ICON_SIZE_SMALL_TOOLBAR)
				tooltips.set_tip(event_box, "Baglanti Var...")
				download_list = "wget -c ftp://ftp.linux.org.tr/pub/truva/truva/current/packages/truva/PACKAGES.TXT &"
				os.system( download_list )			
		except:
			image_widget.set_from_stock(gtk.STOCK_DISCONNECT, gtk.ICON_SIZE_SMALL_TOOLBAR)
			tooltips.set_tip(event_box, "Baglantinizi kontrol ediniz...")
			
	return;

def package_manager( *args ):
	os.system("kdesu /usr/sbin/gslapt &")
	return;

def control_center( *args ):
	os.system("/opt/kde/bin/kcontrol &")
	return;

def about (*args):
	hakkinda = gtk.AboutDialog()
	hakkinda.set_name('TruvaTray')
	hakkinda.set_version(__version__)
	hakkinda.set_copyright('Truva Linux - 2007')
	hakkinda.set_comments('Sistem Yonetim Uygulamasi')
	hakkinda.set_authors(['Onur OZDEMIR <atlantis@truvalinux.org.tr>'])
	hakkinda.set_website('http://www.truvalinux.org.tr')
	#hakkinda.set_logo('/opt/kde/share/icons/crystalsvg/64x6416/apps/kmenu.png')
	#hakkinda.set_icon(self.icon_pixbuf)
	hakkinda.show()

event_box = gtk.EventBox( );
image_widget = gtk.Image( );

tooltips = gtk.Tooltips()
tooltips = tooltips
tooltips.set_tip(event_box, "Baglanti kontrol ediliyor...")

event_box.set_events( gtk.gdk.BUTTON_PRESS_MASK |
    gtk.gdk.POINTER_MOTION_MASK |
    gtk.gdk.POINTER_MOTION_HINT_MASK | gtk.gdk.CONFIGURE );

event_box.add( image_widget );
event_box.connect("button_press_event", applet_face_click );
event_box.connect("button_press_event", repo_control );

status = open("/sys/class/net/eth0/operstate")
net_stat = status.readline()
print net_stat

if (net_stat == 'down'):
	image_widget.set_from_stock(gtk.STOCK_DISCONNECT, gtk.ICON_SIZE_SMALL_TOOLBAR)	
	tooltips.set_tip(event_box, "Baglanti saglanamadi...")
else:
	image_widget.set_from_stock(gtk.STOCK_CONNECT, gtk.ICON_SIZE_SMALL_TOOLBAR)	
	tooltips.set_tip(event_box, "Baglanti saglandi...")

menu = gtk.Menu()
menu.set_title("TruvaTray")

item = gtk.ImageMenuItem( "Kontrol Merkezi" )
item.connect("activate", control_center)
_img = gtk.Image()
_img.set_from_stock("gtk-properties", gtk.ICON_SIZE_BUTTON)
item.set_image(_img)
menu.append(item)

item = gtk.ImageMenuItem( "Paket Yoneticisi" )
item.connect("activate", package_manager)
_img = gtk.Image()
_img.set_from_stock("gtk-harddisk", gtk.ICON_SIZE_BUTTON)
item.set_image(_img)
menu.append(item)

item = gtk.TearoffMenuItem()
menu.append(item)

item = gtk.ImageMenuItem( "Hakkinda" )
item.connect("activate", package_manager)
_img = gtk.Image()
_img.set_from_stock("gtk-about", gtk.ICON_SIZE_BUTTON)
item.set_image(_img)
menu.append(item)

item = gtk.TearoffMenuItem()
menu.append(item)

item = gtk.ImageMenuItem(stock_id=gtk.STOCK_QUIT)
item.connect("activate", exit_applet)
menu.append(item)
menu.show_all()

t = egg.trayicon.TrayIcon("MyFirstTrayIcon")
t.add(event_box)
t.show_all()


gtk.main() 