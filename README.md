Configuration Repository
========================

This repository contains the configuration files of my Arch Linux system.

The files and directories in home/ are to be placed in the user's home
directory.
Except for the bin/ directory a dot has to be prepended, since these
are hidden configuration files.

The files and directories in etc/ are to be placed in the /etc/
directory.

Moreover, efibootmgr-output is the output of the current state of the
UEFI variables concerning the boot order. Note that only the first entries
are to be added manually, while the rest are recreated by the Lenovo BIOS
if they are missing.

The Python script synchronise.py walks through both, etc/ and home/,
searches for the original configuration files (possibly with prepended dot)
and copies them into the repository if they have changed.
