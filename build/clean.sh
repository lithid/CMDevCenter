#!/bin/bash
save='changelog cmdevcenter.install compat control dirs rules'
rm ../*.deb
rm ../*.tar.gz
rm ../*.changes
rm ../*.dsc

for x in `ls debian/`; do
    chk=$(echo $save |grep $x |wc -l)
    if [ $chk -eq 0 ]; then
        rm debian/$x
    fi
done

if [ -d debian/tmp ]; then
    rm -r debian/tmp
fi

gdialog --title "Success" --msgbox "clean-up run complete" 200 200
