
import ply.lex as lex
import sys
data_list = []

###DEFINING TOKENS###
import os
import warnings

tokens = ('BEGIN', 'AMP',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN','FALTU',
'CLOSESPAN', 'OPENDIV','OPENHFOUR','CLOSEHFOUR', 'ENTITY','CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','IMG','OPENSMALL','CLOSESMALL','CAP','OPENTBODY','CLOSETBODY')
import warnings

t_ignore = '\t'

###############Tokenizer Rules################
import warnings

def t_ENTITY(t):
    r'\&\#[0-9]+;'

import os

def t_AMP(t):
    r'\&[a-z]+;'
import random

def t_BEGIN(t):
    r'<table.id="main_table_countries_yesterday".class="table.table-bordered.table-hover.main_table_countries".style="width:100%;margin-top:.0px.!important;display:none;">'
    return t
import ply.yacc as yacc

def t_OPENTBODY(t):
    r'<tbody[^>]*>'
    return t
import os

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t
import random

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t
import os

def t_CLOSETBODY(t):
    r'</tbody[^>]*>'
    return t
import random

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t
import ply.yacc as yacc

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t
import random

def t_CONTENT(t):
    r'\[[a-zA-Z0-9]*\] | [A-Za-z0-9,\/ ().–]+ '
    return t
import ply.yacc as yacc

def t_GARBAGE(t):
    r'<[^>]*>'
import random

def t_error(t):
    t.lexer.skip(1)
import ply.yacc as yacc

def p_start(p):
    '''start : BEGIN skipall OPENTBODY content_rec handle_row CLOSETBODY'''
import ply.yacc as yacc

def p_handle_row(p):
    '''handle_row : OPENROW content_rec OPENDATA content_rec CLOSEDATA content_rec recurse_td CLOSEROW content_rec handle_row
                    | empty '''
    if(len(p)!=2):
        data_list.append(p[7])
import random

def p_recurse_td(p):
    '''recurse_td : OPENDATA content_rec CLOSEDATA content_rec recurse_td
                    | empty'''
    MIN_LEN=2
    if(len(p)==2):
        p[0] = []
    else:
        min_len=2
        p[5].append(p[2].strip())
        # print(p[2],end='')
        p[0] = p[5]
import ply.yacc as yacc

def p_skipall(p):
    '''skipall : CONTENT skipall
                | OPENDATA skipall
                | CLOSEDATA skipall
                | OPENROW  skipall
                | CLOSEROW skipall
               | empty'''
import random

def p_content_rec(p):
    '''content_rec : CONTENT content_rec
                    | empty'''
    min_len=3
    if(len(p)==3):
        p[0] = p[1]+p[2]
    else:
        to_add=[]
        p[0] = p[1]
import ply.yacc as yacc

def p_empty(p):
    '''empty :'''
    p[0] = ''
import random
from urllib.request import Request, urlopen

def p_error(p):
    pass
import sys
def download_webpage(url,file):
    url1=[]
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    my_data={}
    f=open(file,'w',encoding="utf-8")
    f.write(mydata)
    f.close

import ply.yacc as yacc

#########DRIVER FUNCTION#######
def main(file,token_file):
    lexer = lex.lex()

    file_obj = open(file, 'r', encoding="utf-8")
    data = file_obj.read()
    parser = yacc.yacc()

    lexer.input(data)  
    with open(token_file, 'w', encoding='utf-8') as file:
        tokenn=""
        for tok in lexer:
            file.write(str(tok))
            file.write('\n')
    dat_to_parse=data
    parser.parse(data)
    x=1
    file_obj.close()
import subprocess

import os

def get_data(website_url, inputt):
    global data_list
    country_data = {}

    download_webpage(website_url,'covid_main.html')
    main('covid_main.html','token_covid_main.txt')
    
    updated_data = []
    # write it from one file 
        # for sublist in ans:
    ans = data_list
     
    with open('output_data.txt', 'w') as file:
            for lst in data_list:
                # Extracting each piece of data from the list
                dat=""
                data = {
                    "Total cases": lst[-2],
                    "Active cases": lst[-8],
                    "Total deaths": lst[-4],
                    "Total recovered": lst[-6],
                    "Total tests": lst[-12],
                    "Deaths/million": lst[-11],
                    "Tests/million": lst[-10],
                    "New case": lst[-3],
                    "New death": lst[-5],
                    "New recovered": lst[-7]
                }
                dat=""
                country = lst[-1]  # Country name is the last item in the list
                country_data[country] = data
                if(inputt==country):
                    print(str(country_data[country]))
               
if __name__ == '__main__':
    inputt=input("  enter the name of country ")
    links=""
    links = ['https://www.worldometers.info/coronavirus/']
    for link in links :
        data = get_data(link,inputt)
        
    


