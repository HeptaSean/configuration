#!/usr/bin/env python3

import os
import filecmp
import shutil

def walk(repo_path, orig_path):
    for filename in os.listdir(repo_path):
        repo_file = os.path.join(repo_path, filename)
        orig_file = os.path.join(orig_path, filename)
        if os.path.isdir(repo_file):
            if os.path.isdir(orig_file):
                walk(repo_file, orig_file)
            else:
                print("Warning: {:s} is directory, but {:s} is not.".format(
                    repo_file, orig_file))
        elif os.path.isfile(repo_file):
            if os.path.isfile(orig_file):
                if not filecmp.cmp(repo_file, orig_file):
                    print ("Copying {:s} to {:s}.".format(
                        orig_file, repo_file))
                    shutil.copyfile(orig_file, repo_file)
            else:
                print("Warning: {:s} is file, but {:s} is not.".format(
                    repo_file, orig_file))

walk("etc", "/etc")
