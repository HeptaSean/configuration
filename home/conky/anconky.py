#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Script to display the latest news from www.archlinux.org in Conky
#
# This should be quite self-explanatory and be customised to your needs.
# NOTE: Please run it in a Conky instance with a long update_interval or use
# ${execpi} to run this script seldomly to keep the load on the Web server
# low.
#
# Main points for customisation are the constants at the beginning of the
# script.
# - feed_url is the feed that is displayed
# - cache_filename is the file to cache the feed
# - number_entries is the number of entries to display
# - line_width is the number of characters that fit in one line of your Conky
#   instance (in order to split package and version info on two lines if too
#   long).
# - time_format is the strftime format used for published date of entries
# - time_width is the length of the previous time format (used as indent)
# - *_template are templates for the lines written to stdout for Conky to
#   consume.
#
# Requirements:
# - python3 – to execute this script
# - feedparser Python module – to get the news feed
#   (found in extra/python-feedparser on Arch Linux)

import os
import time
import textwrap
import pickle
import feedparser

# URL of feed to parse:
feed_url = 'https://www.archlinux.org/feeds/news/'
# Filename for the cache:
cache_filename = os.path.expanduser('~/.conky/ancache.pickle')
# Number of entries to display:
number_entries = 2
# Length of lines in characters in the calling Conky instance:
line_width = 46
# Format for published dates:
time_format = '%F %R'
# Length of previous time format (used as indent for continued lines):
time_width = 17
# Template for feed title:
title_template = '${color1}%s ${hr 6}'
# Templates for news entries:
news_template = '${color3}%s ${color}%s'
continued_template = time_width*' ' + '%s'

modified = None
etag = None

if os.path.exists(cache_filename):
    with open(cache_filename, 'rb') as file:
        cached_feed = pickle.load(file)
        modified = cached_feed.modified

feed = feedparser.parse(feed_url, modified=modified)

if feed.status == 304:
    feed = cached_feed
elif feed.status == 200:
    with open(cache_filename, 'wb') as file:
        pickle.dump(feed, file)

print(title_template % feed.feed.title)

if len(feed.entries) < number_entries:
    number_entries = len(feed.entries)

for entry in range(number_entries):
    published = time.strftime('%F %R', feed.entries[entry].published_parsed)
    title = feed.entries[entry].title
    wrapped = textwrap.wrap(title, line_width - time_width)
    print(news_template % (published, wrapped[0]))
    for i in range(1, len(wrapped)):
        print(continued_template % wrapped[i])
