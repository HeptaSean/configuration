#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Script to print a list of pending Arch Linux updates in a format suitable for
# Conky to use as an update monitor
#
# This should be quite self-explanatory and be customised to your needs.
# NOTE: Please run it in a Conky instance with a long update_interval or use
# ${execpi} to run this script seldomly to keep the load on the Arch servers
# low.
#
# Main points for customisation are the constants at the beginning of the
# script.
# - line_width is the number of characters that fit in one line of your Conky
#   instance (in order to split package and version info on two lines if too
#   long).
# - *_template are templates for the lines written to stdout for Conky to
#   consume.
#
# Requirements:
# - python3 – to execute this script
# - yaourt – pacman extension that also handles AUR packages
#   (might be patched to use pacman only or even to package managers from other
#   distributions)

import sys
import subprocess

# Length of lines in characters in the calling Conky instance:
line_width = 46
# Templates for total number of updates information:
none_template = '${alignc}${color6}Everything up-to-date'
one_template = '${alignc}${color4}1 update'
many_template = '${alignc}${color4}%d updates'
# Template for information on packages on one line:
pkg_template = '${color}%s/${color3}%s ${alignr}${color5}%s ${color}=> ${color6}%s'
# Calculation of width of one line template instance:
width_calc = 'len(repo) + 1 + len(pkg) + 1 + len(old_version) + 4 + len(new_version)'
# Templates for information on packages on two lines:
pkg_first_template = '${color}%s/${color3}%s'
pkg_second_template = '${alignr}${color5}%s ${color}=> ${color6}%s'

def display(updates):
    if updates:
        if len(updates) > 1:
            print(many_template % len(updates))
        else:
            print(one_template)
        for repo, pkg, old_version, new_version in updates:
            total_width = eval(width_calc)
            if total_width <= line_width:
                print(pkg_template % (repo, pkg, old_version, new_version))
            else:
                print(pkg_first_template % (repo, pkg))
                print(pkg_second_template % (old_version, new_version))
    else:
        print(none_template)

def run_yaourt():
    # Update from repositories (stdout redirected to not clutter output to
    # Conky, needs sudo if pacman is used):
    subprocess.call(['yaourt', '--sync', '--refresh'],
                    stdout=sys.stderr.buffer)
    # Show pending updates (remove --aur if pacman is used):
    p = subprocess.Popen(['yaourt', '--query', '--upgrades', '--aur'],
                         stdout=subprocess.PIPE)
    return iter(p.stdout.readline, b'')

def get_version(pkg):
    p = subprocess.Popen(['yaourt', '--query', pkg],
                         stdout=subprocess.PIPE)
    version = '-'
    for line in iter(p.stdout.readline, b''):
        words = line.decode('utf-8').strip().split(' ')
        query_repo_pkg = words[0]
        query_version = words[1]
        words = query_repo_pkg.split('/')
        query_repo = words[0]
        query_pkg = words[1]
        if query_pkg == pkg:
            version = query_version
    return version

def get_updates(yaourt_output):
    updates = list()
    for line in yaourt_output:
        words = line.decode('utf-8').strip().split(' ')
        repo_pkg = words[0]
        new_version = words[1]
        words = repo_pkg.split('/')
        repo = words[0]
        pkg = words[1]
        old_version = get_version(pkg)
        updates.append((repo, pkg, old_version, new_version))
    return updates

if __name__ == "__main__":
    display(get_updates(run_yaourt()))
