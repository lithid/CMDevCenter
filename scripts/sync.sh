#!/bin/bash

device=$1
branch=$2
force=$3

echo "Syncing device: $device"
echo "Branch: $branch"

if [ "$force" == "True" ]; then
	echo
	echo "Removing repo dir for force re-sync"
	rm -rf .repo/
	read -p "Force clean complete [Enter]"
fi

if [ ! -d .repo ]; then
	echo
	echo "First time syncing, need to answer a few questions..."
	read -p "Ok [Enter]"
	repo init -u https://github.com/CyanogenMod/android.git -b $2
fi

read -p "Press [Enter] to start sync"
repo sync -j4

echo
if [ $? -eq 0 ]; then
	read -p "Sync complete [Enter] to quit"
else
	read -p "Error [Enter] to quit"
fi

exit 0
