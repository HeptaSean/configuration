#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Script to check running against installed kernel and warn the user to
# restart if they differ (to be used in a Conky instance)
#
# This should be quite self-explanatory and be customised to your needs.
#
# Main points for customisation are the constants at the beginning of the
# script.
# - *_template are templates for the lines written to stdout for Conky to
#   consume.
#
# Requirements:
# - python3 – to execute this script
# - uname – used to get running kernel version
# - pacman – Arch Linux package manager
#   (might be patched to use package managers from other distributions)

import sys
import subprocess

# Templates for displaying information:
running_template = '${color}Running:   ${color3}%s'
installed_template = '${color}Installed: ${color3}%s'
warning_template = '${alignc}${color4}Versions differ! You should reboot!'

def display(running_kernel, installed_kernel):
    postfix_index = running_kernel.rfind('-ARCH')
    running_kernel = running_kernel[0:postfix_index]
    if running_kernel != installed_kernel:
        print(warning_template)
    print(running_template % running_kernel)
    print(installed_template % installed_kernel)

def query_running_kernel():
    p = subprocess.Popen(['uname', '-r'],
                         stdout=subprocess.PIPE)
    version = '-'
    for line in iter(p.stdout.readline, b''):
        version = line.decode('utf-8').strip()
    return version

def query_installed_kernel():
    p = subprocess.Popen(['pacman', '-Q', 'linux'],
                         stdout=subprocess.PIPE)
    version = '-'
    for line in iter(p.stdout.readline, b''):
        words = line.decode('utf-8').strip().split(' ')
        version = words[1]
    return version

if __name__ == "__main__":
    running_kernel = query_running_kernel()
    installed_kernel = query_installed_kernel()
    display(running_kernel, installed_kernel)
