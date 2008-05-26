MODULES = Changelog gpl.txt netlib.py pye-u.glade pye-u.py pytrayicon.so TODO trayicon.py wifitools.py tray.png wpaconf.demo wpalib.py logo.png config.py wiflib.py enc.png non_enc.png
PROGRAMS = pye-u
PREFIX ?= /usr/
TO = share/pye-u
TODEP = lib/pye-u

all:
	@/bin/echo -n "Checking for Python... "
	@which python || ( echo "Not found." && /bin/false )

make-install-dirs:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)$(PREFIX)/$(TO)

install: make-install-dirs install-programs
	install -m 644 $(MODULES) $(DESTDIR)$(PREFIX)/$(TO)

install-programs: $(addprefix app-install-, $(PROGRAMS))

dir-install-%: make-install-dirs
	mkdir -p $(DESTDIR)$(PREFIX)/$(TO)/$*
	install -m 644 $*/*.py $(DESTDIR)$(PREFIX)/$(TO)/$*

app-install-%: make-install-dirs 
	install -m 755 $*.py $(DESTDIR)$(PREFIX)/$(TO)
	install -D -m 644 tray.png $(DESTDIR)$(PREFIX)/share/pixmaps/tray.png
	install -m 644 tray.png $(DESTDIR)$(PREFIX)/$(TO)
	install -m 644 enc.png $(DESTDIR)$(PREFIX)/$(TO)
	install -m 644 non_enc.png $(DESTDIR)$(PREFIX)/$(TO)
	install -m 644 logo.png $(DESTDIR)$(PREFIX)/$(TO)
	-install -D -m 644 $*.desktop $(DESTDIR)$(PREFIX)/share/applications/$*.desktop
	echo '#!/bin/bash' > pye-u
	echo python $(PREFIX)/$(TO)/$(PROGRAMS).py >> pye-u
	install -m 755 pye-u $(DESTDIR)$(PREFIX)/bin

clean:
	rm -f pye-u
	rm -f *.py[co] */*.py[co] 
	cd ..
	rm -f *~ */*~ \#* */\#* *.bak */*.bak *.orig */*.orig
	
deb:
	#dpkg-buildpackage -rfakeroot
	fakeroot debian/rules binary

night:
	svn checkout http://pye-u.googlecode.com/svn/trunk nightly/
	rm -rf nightly/.svn/
	tar -cf pyeU.nightly.tar nightly/
	gzip pyeU.nightly.tar
	rm -rf nightly
	
night_deb:
	svn checkout http://pye-u.googlecode.com/svn/trunk nightly/
	cd nightly
	fakeroot debian/rules binary
	cd ..
	rm -rf nightly
	

.PHONY: all make-install-dirs install install-% clean deb
