Configuration Repository
========================

This repository contains the configuration files of my Arch Linux system.

The files and directories in home/ are to be placed in the user's home
directory.
The files and directories in etc/ are to be placed in the /etc/
directory.

For hidden files (leading dot), the dot is replaced by 'DOT'.
Hopefully, this will never conflict with a real configuration file
starting with 'DOT'.

Moreover, efibootmgr-output is the output of the command 'efibootmgr -v',
which shows the current state of the UEFI variables concerning the boot
options and order.
Note that only the first entries are to be added manually, while the rest
are recreated by the Lenovo BIOS if they are missing.

The Python script synchronise.py walks through both, etc/ and home/,
searches for the original configuration files and copies them into the
repository if they have changed.
