Configuration Files from /etc
=============================

The files and directories in here are to be placed in the /etc
directory.

In contrast to the configuration files from the user's home, these
files are copies, not hardlinks, of the files in /etc, since hardlinks
are not possible across filesystem boundaries and ownership also differs.

Hence, consistency with the current state of /etc has to be maintained
manually.
