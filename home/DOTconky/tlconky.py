#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Script to print a list of pending TeXlive updates in a format suitable for
# Conky to use as an update monitor
#
# This should be quite self-explanatory and be customised to your needs.
# NOTE: Please run it in a Conky instance with a long update_interval or use
# ${execpi} to run this script seldomly to keep the load on the TeXlive servers
# low.
#
# Main points for customisation are the constants at the beginning of the
# script.
# - tlmgr_path is the path to tlmgr on your TeXlive installation (depends on
#   version of TeXlive, your architecture and operating system and user or
#   system installation). Full path is needed in case Conky gets executed
#   without proper $PATH.
# - line_width is the number of characters that fit in one line of your Conky
#   instance (in order to split package and version info on two lines if too
#   long).
# - *_template are templates for the lines written to stdout for Conky to
#   consume.
#
# Requirements:
# - python3 – to execute this script
# - tlmgr – from a local TeXlive installation to check for updates
#   (adapt path in tlmgr_path constant according to your installation)

import subprocess

# Path to tlmgr on your system:
tlmgr_path = '/usr/local/texlive/texlive-dist/bin/x86_64-linux/tlmgr'
# Length of lines in characters in the calling Conky instance:
line_width = 46
# Templates for total number of updates information:
none_template = '${alignc}${color6}Everything up-to-date'
one_template = '${alignc}${color4}1 update'
many_template = '${alignc}${color4}%d updates'
# Template for information on packages on one line:
pkg_template = '${color3}%s ${alignr}${color5}%s ${color}=> ${color6}%s'
# Calculation of width of one line template instance:
width_calc = 'len(name) + 1 + len(old_version) + 4 + len(new_version)'
# Templates for information on packages on two lines:
pkg_first_template = '${color3}%s'
pkg_second_template = '${alignr}${color5}%s ${color}=> ${color6}%s'

def display(updates):
    if updates:
        if len(updates) > 1:
            print(many_template % len(updates))
        else:
            print(one_template)
        for name, old_version, new_version in updates:
            total_width = eval(width_calc)
            if total_width <= line_width:
                print(pkg_template % (name, old_version, new_version))
            else:
                print(pkg_first_template % name)
                print(pkg_second_template % (old_version, new_version))
    else:
        print(none_template)

def run_tlmgr():
    p = subprocess.Popen([tlmgr_path, 'update', '--list', '--self', '--all',
                          '--machine-readable'],
                         stdout=subprocess.PIPE)
    return iter(p.stdout.readline, b'')

def get_updates(tlmgr_output):
    updates = list()
    header = True
    content = False
    for line in tlmgr_output:
        if header:
            if line == b'end-of-header\n':
                header = False
                content = True
            continue
        if content:
            if line == b'end-of-updates\n':
                content = False
                continue
            fields = line.decode('utf-8').strip().split('\t')
            updates.append((fields[0], fields[2], fields[3]))
    return updates

if __name__ == "__main__":
    display(get_updates(run_tlmgr()))
