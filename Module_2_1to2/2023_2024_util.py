import ply.lex as lex
from collections import defaultdict

extracted_data = defaultdict(list)

###DEFINING TOKENS###
tokens = ('BEGIN','CONTENT','END','OPEN_H3','CLOSE_H3','OPEN_H4','CLOSE_H4')
t_ignore = ' \t'
#####################
# t_OPEN_UL= r'<ul.*?>'
# t_CLOSE_UL= r'</ul.*?>'
# t_OPEN_LI= r'<li.*?>'
# t_CLOSE_LI= r'</li.*?>'
t_OPEN_H3= r'<h3.*?>'
t_CLOSE_H3= r'</h3.*?>'
import subprocess

t_OPEN_H4= r'<h4.*?>'
t_CLOSE_H4= r'</h4.*?>'
import subprocess


###############Tokenizer Rules################
def t_BEGIN(t):
    r'<div.id="siteSub".class="noprint">From.Wikipedia,.the.free.encyclopedia</div>'
    return t
import ply.yacc as yacc

def t_END(t):
    r'<h2[^>]*><span.class="mw-headline".id="See_also">See.also</span>.*?<\/h2>|<h2[^>]*><span.class="mw-headline".id="Summary">Summary</span>.*?<\/h2>'
    return t
    return
def t_ignnore_situation_report(t):
    r'<b>WHO</b>Situation.Report.\(\d+\)|<b>WHO</b>Situation.Report.\(\d+\):|<b>WHO</b>Situation.Report.\(\d+\);'
    pass

def t_CONTENT(t):
    r'[A-Za-z0-9, .,\'-0-9/():–;]+'
    return t
def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
import subprocess

def p_start(p):
    '''start : table'''
    p[0] = p[1]
import ply.yacc as yacc

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''
import os

def p_table(p):
    '''table : BEGIN skiptag data skiptag END'''
    p[0] = p[3]
    p[0] = p[3]

def p_date(p):
    '''date : OPEN_H4 CONTENT content CLOSE_H4'''
    p[0]=p[2]
    return
def t_ignore_TAGS(t):
    r'<i>|</i>|</b>|<b>|<ul>|</ul>|<li>|</li>|</p>|<p>|<h2[^>]*>.*?<\/h2>|<img.*?>|<table.*?>.*?</table>|<style.*?>.*?</style>|<figure[^>]*>.*?<\/figure>|<script.*?>.*?</script>|<sup.*?>.*?</sup>|<span.*?>|</span>|<a.href.*?>|</a>|<span.class="mw-editsection">.*?]</span></span>'
    pass


def p_month(p):
    '''month : OPEN_H3 CONTENT content CLOSE_H3'''
    p[0]=p[2]
    return 
    return



def p_elements(p):
    '''elements : elements date content
                | date content'''

    global extracted_data
    if(len(p)==4):
        to_add=None
        extracted_data[p[2]].append(p[3])
    else:
        extracted_data[p[1]].append(p[2])
    
import ply.yacc as yacc

def p_empty(p):
    '''empty :'''
    pass
    pass
def p_data(p):
    '''data : data month elements
            | month elements'''
        
 
def p_error(p):
    pass

import datetime


def p_content(p):
    '''content : CONTENT content
               | empty'''
    p_len=3           
    if len(p) == 3:
        to_add=[]
        p[0] = p[1] + p[2]
    else:
        p[0] = ""
def main():
    extracted_data.clear()
    name=f"2023_news"
    parser = yacc.yacc()

    file_obj= open(f"./Downloaded-Webpages-news/{name}.html",'r',encoding="utf-8")

    data=file_obj.read()
    lexer = lex.lex()

    lexer.input(data)
    parser.parse(data)
    pares_data=lexer
    files_by_month = {
    'January': open('./News/January_2023_news.txt', 'w'),
    'February': open('./News/February_2023_news.txt', 'w'),
    'March': open('./News/March_2023_news.txt', 'w'),
    'April': open('./News/April_2023_news.txt', 'w'),
    'May': open('./News/May_2023_news.txt', 'w'),
    'June': open('./News/June_2023_news.txt', 'w'),
    'July': open('./News/July_2023_news.txt', 'w'),
    'August': open('./News/August_2023_news.txt', 'w'),
    'September': open('./News/September_2023_news.txt', 'w'),
    'October': open('./News/October_2023_news.txt', 'w'),
    'November': open('./News/November_2023_news.txt', 'w'),
    'December': open('./News/December_2023_news.txt', 'w'),
    }
    for date, content in extracted_data.items():
        monnthh=None
        year_=[]
        month = date.split()[1]
        mont=[]
        files_by_month[month].write(f'{date}:: {" ".join(map(str, content))}\n')
        auto={" ".join(map(str, content))}
    name=f"2024_news"
    
    print("extracted news: 2023")    
    extracted_data.clear()
    file_obj= open(f"./Downloaded-Webpages-news/{name}.html",'r',encoding="utf-8")
    parser = yacc.yacc()
    lexer = lex.lex()


    data=file_obj.read()
    lexer.input(data)
    parser.parse(data)
    files_by_month_2024={
    'January': open('./News/January_2024_news.txt', 'w'),
    'February': open('./News/February_2024_news.txt', 'w')
    }
    content_=data
    for date, content in extracted_data.items():
        month = date.split()[1]
        motn=""
        files_by_month_2024[month].write(f'{date}:: {" ".join(map(str, content))}\n')
        to_add={" ".join(map(str, content))}
    print("extracted news: 2024")
    


if __name__ == "__main__":
    main()

