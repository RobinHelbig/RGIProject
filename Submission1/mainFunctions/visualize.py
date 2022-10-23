from turtle import title
from typing import List, Dict

import os


# (document: [str], ranking: [str]) document -> all sentences in order they appear in article, ranking -> all sentences of summary orderd by rank
def visualize(name: str, ranking: Dict[str, int], option: int):
    # Creating the HTML file
    cur_dir = os.getcwd()
    with open(cur_dir + "/" + name + ".html", "w") as file_html:
        file_html.write('''<html>
    <head>
    <title>''')

        file_html.write(name)

        file_html.write(
            '''</title>
        </head> 
        <body>
        <p>''')
        if option == 1:
            for sentence, importance in ranking.items():
                if importance > 1:
                    write_just_strong(sentence, file_html)
                elif importance > 0:
                    write_just_bold(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        if option == 2:
            for sentence, importance in ranking.items():
                if importance > 1:
                    write_bold_big(sentence, file_html)
                    write_just_strong(sentence, file_html)
                elif importance > 0:
                    write_just_bold(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        if option == 3:
            for sentence, importance in ranking.items():
                if importance > 2:
                    write_just_bold_red(sentence, file_html)
                elif importance > 0:
                    write_just_bold(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        if option == 4:
            file_html.write('</p>')
            for sentence, importance in ranking.items():
                if importance > 0:
                    write_plain_bigger_font(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        if option == 5:
            file_html.write('</p>')
            for sentence, importance in ranking.items():
                if importance > 0:
                    write_bold_bigger_font(sentence, file_html)
                if importance > 0:
                    write_plain_bigger_font(sentence, file_html)
                else:
                    write_plain(sentence, file_html)

        file_html.write('''</p> 
    </body>
    </html>''')

def write_just_strong(sentence: str, file_html):
    file_html.write("<strong>" + sentence + "</strong>")


def write_just_bold(sentence: str, file_html):
    file_html.write("<b>" + sentence + "</b>")


def write_bold_big(sentence: str, file_html):
    file_html.write("<b><big>" + sentence + "</big></b>")


def write_just_bold_red(sentence: str, file_html):
    file_html.write('<b> <span style="color:red;">' + sentence + "</span></b>")


def write_plain(sentence: str, file_html):
    file_html.write(sentence)


def write_plain_bigger_font(sentence: str, file_html):
    file_html.write('<font size="4"> ' + sentence + '</font')


def write_bold_bigger_font(sentence: str, file_html):
    file_html.write('<b><font size="4"> ' + sentence + '</font><b>')
