#!/bin/bash
# ---------------------------------------------------
# Script to create bootable ISO in Linux
# usage: make_iso.sh [ /tmp/slax.iso ]
# author: Tomas M. <http://www.linux-live.org>
# ---------------------------------------------------

if [ "$1" = "--help" -o "$1" = "-h" ]; then
  echo "Bu betik boot edilebilir iso yapmak ýcýndýr."
  echo "Gecerli dizin yazilabilir olmalidir."
  echo "Ornek: $0 /mnt/hda5/truva.iso"
  exit
fi

CDLABEL="Truva Linux 2.0"
ISONAME="$1"

if [ "$ISONAME" = "" ]; then
   SUGGEST="../`basename \`pwd\``.iso"
   echo -ne "Hedef iso dosyasi adi [ Hit enter for $SUGGEST ]: "
   read ISONAME
   if [ "$ISONAME" = "" ]; then ISONAME="$SUGGEST"; fi
fi

# isolinux.bin is changed during the ISO creation,
# so we need to restore it from backup.
cp -f boot/isolinux.bi_ boot/isolinux.bin
if [ $? -ne 0 ]; then
   echo "Can't recreate isolinux.bin, make sure your current directory is writable!"
   exit 1
fi

mkisofs -o "$ISONAME" \
-v -J -R -D -A "$CDLABEL" -V "$CDLABEL" \
-x ./truva/driver \
-x ./truva/en \
-x ./truva/extra \
-x ./truva/g \
-x ./truva/gnome \
-x ./truva/k \
-x ./truva/s \
-x ./truva/w \
-hide-rr-moved \
-no-emul-boot -boot-info-table -boot-load-size 4 \
-b boot/isolinux.bin \
-c boot/isolinux.boot \
-p "Truva-Current - TEST SURUMU" \
-A "Truva-Current (Kurulan CD) - Surum $DATE" .

