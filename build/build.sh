#!/bin/bash
dpkg-buildpackage -rfakeroot

if [ $? -eq 0 ]; then
    gdialog --title "Success" --msgbox "deb created" 200 200
else
    gdialog --title "Error" --msgbox "deb not created" 200 200
fi
