Configuration Files from /boot
==============================

The files and directories in here are to be placed in the /boot
directory, which is the mount point for the UEFI partition.

In contrast to the configuration files from the user's home, these
files are copies, not hardlinks, of the files in /boot, since hardlinks
are not possible across filesystem boundaries and ownership also differs.

Hence, consistency with the current state of /boot has to be maintained
manually.

Moreover, efibootmgr-output is the output of the current state of the
UEFI variables concerning the boot order. Note that only the first entries
are to be added manually, while the rest are recreated by the Lenovo BIOS
if they are missing.
