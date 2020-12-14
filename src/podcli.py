#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import time
import os
import json
import argparse
import requests
import locale
import gettext
from urllib.parse import urlparse
from plumbum import local
from markdownify import markdownify as md
from bs4 import BeautifulSoup


APP = 'podcli'
LANGDIR = os.path.join('usr', 'share', 'locale-langpack')
current_locale, encoding = locale.getdefaultlocale()
try:
    language = gettext.translation(APP, LANGDIR, [current_locale])
    language.install()
    _ = language.gettext
except Exception as exception:
    print(exception)
    _ = str


def option_list(items, first):
    for index, item in enumerate(items):
        print('{}. {}'.format(index + first + 1, item['title']))


def option_debug(items):
    print(json.dumps(items, sort_keys=True, indent=4))


def option_images(items):
    if os.path.exists('images'):
        os.removedirs('images')
    os.makedirs('images')
    for item in items:
        print(_('Downloading images for {}').format(item['title']))
        content = BeautifulSoup(item['content'][0]['value'], 'html.parser')
        for image in content.find_all('img'):
            url = image['src']
            filename = os.path.join('images',
                                    os.path.basename(urlparse(url).path))
            r = requests.get(url, allow_redirects=True)
            if r.status_code in [200, 201]:
                open(filename, 'wb').write(r.content)


def option_play(items, first):
    ffplay = local['ffplay']
    if not os.path.exists('audio'):
        os.makedirs('audio')
    for index, item in enumerate(items):
        for link in item.links:
            if link.type == 'audio/mpeg':
                ext = 'mp3'
            elif link.type == 'audio/x-m4a':
                ext = 'm4a'
            elif link.type == 'audio/ogg':
                ext = 'ogg'
            else:
                continue

            url = link['href']
            podcast_title = ''.join([c if c.isalnum() else
                                     '_' for c in item['title']])
            podcast_datetime = time.strftime(
                '%Y%m%d', item['published_parsed'])
            filename = '{}_{}.{}'.format(podcast_datetime, podcast_title, ext)
            output_name = os.path.join('audio', filename)
            if not os.path.exists(output_name):
                print(_('Downloading {}. "{}"').format(index + first + 1,
                                                       item['title']))
                r = requests.get(url, allow_redirects=True)
                if r.status_code == 200:
                    open(output_name, 'wb').write(r.content)
            if os.path.exists(output_name):
                print(_('Playing {}. {}\n').format(index + first + 1,
                                                   item['title']))
                ffplay['-nodisp', '-autoexit', output_name]()
            else:
                print(_('Can\'t play {}. "{}"').format(index + first + 1,
                                                       item['title']))


def option_audio(items):
    if not os.path.exists('audio'):
        os.makedirs('audio')
    for item in items:
        for link in item.links:
            if link.type == 'audio/mpeg':
                ext = 'mp3'
            elif link.type == 'audio/x-m4a':
                ext = 'm4a'
            elif link.type == 'audio/ogg':
                ext = 'ogg'
            else:
                continue
            url = link['href']
            podcast_title = ''.join([c if c.isalnum() else
                                     '_' for c in item['title']])
            podcast_datetime = time.strftime(
                '%Y%m%d', item['published_parsed'])
            filename = '{}_{}.{}'.format(podcast_datetime, podcast_title, ext)
            output_name = os.path.join('audio', filename)
            if not os.path.exists(output_name):
                print(_('* Downloading "{}"').format(item['title']))
                r = requests.get(url, allow_redirects=True)
                if r.status_code == 200:
                    open(output_name, 'wb').write(r.content)
            else:
                print(_('* "{}" is already downloaded').format(item['title']))


def option_docs(items, first):
    for index, item in enumerate(items):
        print('\n\n{}. {}\n'.format(index + first + 1, item['title']))
        content = item['content'][0]['value']
        print(content)


def option_show(items, first):
    for index, item in enumerate(items):
        print('\n\n# {}. {}\n'.format(index + first + 1, item['title']))
        content = item['content'][0]['value']
        print(md(content))


def create_parser():
    parser = argparse.ArgumentParser(description='Podcast parser')
    parser.add_argument('-a', '--audio', action='store_true',
                        help=_('Download audio'))
    parser.add_argument('-b', '--debug', action='store_true',
                        help=_('Only for debug'))
    parser.add_argument('-d', '--docs', action='store_true',
                        help=_('Show the content of the episode in html'))
    parser.add_argument('-e', '--enumerate', action='store_true',
                        help=_('List episodes'))
    parser.add_argument('-f', '--first', action='store', type=int,
                        help=_('Select first episode'))
    parser.add_argument('-i', '--images', action='store_true',
                        help=_('Download images'))
    parser.add_argument('-l', '--last', action='store', type=int,
                        help=_('Select last episode'))
    parser.add_argument('-p', '--play', action='store_true',
                        help=_('Play audio, and download if necessary'))
    parser.add_argument('-s', '--show', action='store_true',
                        help=_('Show the content of the episode in markdown'))
    parser.add_argument('-u', '--url', action='store', type=str,
                        help=_('The url or filename of the feed'),
                        required=True)
    return parser.parse_args()


def main():
    args = create_parser()
    feed = feedparser.parse(args.url)

    nitems = len(feed['items'])
    if nitems == 0:
        print(_('Empty feed'))
        exit(0)

    first = args.first if args.first else 0
    last = args.last if args.last else nitems
    first = first if first <= 0 else first - 1
    last = last if last <= 0 else last

    items = list(reversed(feed['items']))[first:last]
    fp = first + nitems + 1 if first < 0 else first + 1
    lp = last + nitems if last < 0 else last
    if len(items) == 0:
        print(_('No episode selected'))
        exit(0)
    print(_('Total of episodes: {}'.format(nitems)))
    print(_('First episode selected: {}. "{}"'.format(fp, items[0]['title'])))
    print(_('Last episode selected: {}. "{}"'.format(lp, items[-1]['title'])))
    print(_('Number of episodes selected: {}\n'.format(len(items))))

    first = first if first >= 0 else first + nitems
    if args.debug:
        option_debug(items)
    if args.enumerate:
        option_list(items, first)
    if args.audio:
        option_audio(items)
    if args.docs:
        option_docs(items, first)
    if args.images:
        option_images(items)
    if args.play:
        option_play(items, first)
    if args.show:
        option_show(items, first)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
