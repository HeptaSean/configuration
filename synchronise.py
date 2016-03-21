#!/usr/bin/env python3

import os
import filecmp
import shutil

def walk(repo_path, orig_path):
    for filename in os.listdir(repo_path):
        repo_file = os.path.join(repo_path, filename)
        orig_file = os.path.join(orig_path, filename)
        orig_dotfile = os.path.join(orig_path, '.' + filename)
        if os.path.isdir(repo_file):
            if os.path.isdir(orig_file):
                walk(repo_file, orig_file)
            elif os.path.isdir(orig_dotfile):
                walk(repo_file, orig_dotfile)
            else:
                print("Warning: {:s} is a directory, but neither {:s} nor {:s} is a directory.".format(
                    repo_file, orig_file, orig_dotfile))
        elif os.path.isfile(repo_file):
            if os.path.isfile(orig_file):
                if not filecmp.cmp(repo_file, orig_file):
                    print ("Copying {:s} to {:s}.".format(
                        orig_file, repo_file))
                    shutil.copyfile(orig_file, repo_file)
            elif os.path.isfile(orig_dotfile):
                if not filecmp.cmp(repo_file, orig_dotfile):
                    print ("Copying {:s} to {:s}.".format(
                        orig_dotfile, repo_file))
                    shutil.copyfile(orig_dotfile, repo_file)
            else:
                print("Warning: {:s} is a file, but neither {:s} nor {:s} is a file.".format(
                    repo_file, orig_file, orig_dotfile))

walk("etc", "/etc")
walk("home","/home/sean")
