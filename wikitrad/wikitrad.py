"""
Usage:
    wikitrad [options] WORD TARGET_LANG
    wikitrad [options] SOURCE_LANG WORD TARGET_LANG

Options:
    -v --verbose    Show links of wikipedia pages, source language used
"""

from bs4 import BeautifulSoup
from docopt import docopt
import rich
from langdetect import detect as detect_lang
from sys import stdout
import requests

def clear_line():
    print('\r', end='')
    stdout.flush()

def run(argv=None):
    args = docopt(__doc__, argv=argv)
    source = args['SOURCE_LANG']
    word = args['WORD']
    target = args['TARGET_LANG']

    def p(text_verbose, text_simple="", **kwargs):
        if args['--verbose']:
            kwargs['end'] = ''
            rich.print(text_verbose, **kwargs)
            stdout.flush()
        elif text_simple:
            print(text_simple)

    
    # detect language
    if not source:
        p(f"[bold]{word}[/] [dim italic](auto)[/] [magenta]->[/magenta] ")
        source = detect_lang(word)
        clear_line()

    p(f"[bold]{word}[/] [dim italic]({source})[/] [magenta]->[/magenta] ")


    # find wikipedia page
    response = requests.get(f"https://{source}.wikipedia.org/wiki/{word}")
    if not response.ok:
        rich.print(f"[red bold]Page {response.url} not found")
        return 1

    page = BeautifulSoup(response.text, features="html.parser")
    p(f"[bold]{page.find('h1').text}[/] [dim italic link={response.url}]({response.url})[/] [magenta]->[/] ")

    # set language
    link_to_target_language = page.find('a', class_='interlanguage-link-target', lang=target)
    if not link_to_target_language:
        rich.print(f"[red bold]No equivalent page in {target}")
        return 1

    response = requests.get(link_to_target_language.attrs['href'])
    if not response.ok:
        rich.print(f"[red bold]No equivalent page in {target}")
        return 1

    page = BeautifulSoup(response.text, features="html.parser")
    p("[bold]" + page.find('h1').text, page.find('h1').text)
    
    p("\n")



    
