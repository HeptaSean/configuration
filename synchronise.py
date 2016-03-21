#!/usr/bin/env python3

import os
import filecmp
import shutil
import re

def walk(repo_path, orig_path):
    for repo_filename in os.listdir(repo_path):
        orig_filename = re.sub('^DOT', '.', repo_filename)
        repo_file = os.path.join(repo_path, repo_filename)
        orig_file = os.path.join(orig_path, orig_filename)
        if os.path.islink(repo_file):
            repo_target = os.readlink(repo_file)
            if os.path.islink(orig_file):
                orig_target = os.readlink(orig_file)
                if repo_target != orig_target:
                    print ("Linking {:s} to target {:s} of symlink {:s}.".format(
                        repo_file, orig_target, orig_file))
                    os.symlink(orig_target, repo_file)
            elif os.path.isfile(orig_file):
                print("Warning: {:s} is a symlink, but {:s} is a regular file.".format(
                    repo_file, orig_file))
            elif os.path.isdir(orig_file):
                print("Warning: {:s} is a symlink, but {:s} is a directory.".format(
                    repo_file, orig_file))
            else:
                print("Warning: {:s} is a symlink, but {:s} is neither a symlink nor a directory nor a regular file.".format(
                    repo_file, orig_file))
        elif os.path.isdir(repo_file):
            if os.path.islink(orig_file):
                print("Warning: {:s} is a directory, but {:s} is a symlink.".format(
                    repo_file, orig_file))
            elif os.path.isfile(orig_file):
                print("Warning: {:s} is a directory, but {:s} is a regular file.".format(
                    repo_file, orig_file))
            elif os.path.isdir(orig_file):
                walk(repo_file, orig_file)
            else:
                print("Warning: {:s} is a directory, but {:s} is neither a directory nor a regular file nor a symlink.".format(
                    repo_file, orig_file))
        elif os.path.isfile(repo_file):
            if os.path.islink(orig_file):
                print("Warning: {:s} is a regular file, but {:s} is a symlink.".format(
                    repo_file, orig_file))
            elif os.path.isdir(orig_file):
                print("Warning: {:s} is a regular file, but {:s} is a directory.".format(
                    repo_file, orig_file))
            elif os.path.isfile(orig_file):
                if not filecmp.cmp(repo_file, orig_file):
                    print ("Copying {:s} to {:s}.".format(
                        orig_file, repo_file))
                    shutil.copyfile(orig_file, repo_file)
            else:
                print("Warning: {:s} is a regular file, but {:s} is neither a regular file nor a directory nor a symlink.".format(
                    repo_file, orig_file))

repo_path = os.path.abspath(os.path.dirname(__file__))
repo_etc_path = os.path.join(repo_path, "etc")
repo_home_path = os.path.join(repo_path, "home")
walk(repo_etc_path, "/etc")
user_home_path = os.path.expanduser("~")
walk(repo_home_path, user_home_path)
