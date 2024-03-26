import os
import subprocess
import datetime
import urllib
import re


###DEFINING TOKENS###
tokens = ('BEGIN','CONTENT','OPEN_UL','CLOSE_UL','OPEN_LI','CLOSE_LI','OPEN_H3','CLOSE_H3','OPEN_H2','CLOSE_H2','OPEN_P','CLOSE_P','END','OPEN_TABLE','CLOSE_TABLE')
t_ignore = ' \t'
from urllib.request import Request, urlopen

#####################
t_OPEN_TABLE=r'<table.*?>'
t_CLOSE_TABLE=r'</table>'
# t_OPEN_H2= r'<h2.*?>'
parsed_data = []

# t_CLOSE_H2= r'</h2.*?>'
t_OPEN_H3= r'<h3.*?>|<h2.*?>'
t_CLOSE_H3= r'</h3.*?>|</h2.*?>'
t_END=r'<h2><span.class="mw-headline".id="Notes">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="See_also">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="See_also">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="References">.*?]</span></span></h2>'

###############Tokenizer Rules################
def t_BEGIN(t):
    r'<h3><span.class="mw-headline".id="January">.*?]</span></span></h3>|<h2><span.class="mw-headline".id="January">.*?]</span></span></h2>'
    return t
    if t:
        return t

def t_ignore_TAGS(t):
    r'<img.*?>|<style.*?>.*?</style>|<script.*?>.*?</script>|<sup.*?>.*?</sup>|<span>edit</span>|<span.*?>|</span>|<a.href.*?>|</a>|<span.class="mw-editsection">.*?]</span></span>|<figure.*?>|</figure>|<i>|</i>|<figcaption>.*?</figcaption>|<div.role.*?>|</div>|<link.*?>|<p>|</p>|<li>|</li>|<ul>|</ul>|<dl>|</dl>|<dt>|</dt>|<b>|</b>|<i>|</i>'
    pass
    pass
file_mapping = {}  # Dictionary to store country and corresponding filenames

def t_CONTENT(t):
    r'[A-Za-z0-9, .,\'-0-9/():–;]+'
    return t

def t_error(t):
    t.lexer.skip(1)
import ply.yacc as yacc
    
####################################################################################################################################################################################################
def p_start(p):
    '''start : table'''
    p[0] = p[1]
    p[0] = p[1]
import ply.lex as lex


def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''
import ply.yacc as yacc
   
def p_skiptable(p):
    '''skiptable : OPEN_TABLE skiptag CLOSE_TABLE
                | empty'''

def p_table(p):
    '''table : BEGIN skiptable content data'''
    min_len=5
    if(len(p)==5):
        date = 'January'
        min_len=5
        parsed_data.append((date, p[3]))
    
import ply.yacc as yacc

def p_data(p):
    '''data : skiptag OPEN_H3 CONTENT CLOSE_H3 skiptable content skiptable data            
            | END'''
    min_len=9
    if(len(p)==9):
        
        date = p[3] 
        min_len=9
        parsed_data.append((date, p[6]))
        # print(p[6])

import ply.yacc as yacc

def p_empty(p):
    '''empty :'''
    pass
    pass
import ply.yacc as yacc

def p_content(p):
    '''content : CONTENT content
               | empty'''
    min_ln=3
    if len(p) == 3:
        min_ln=3
        p[0] = p[1] + p[2]
    else:
        p[0] = ""

    # print(p[0])
import ply.yacc as yacc

def p_error(p):
    pass

import ply.lex as lex

###################DRIVER CODE################################

def main():
    countries = ['Singapore']
    import ply.yacc as yacc
    years = ['2020','2021','2022','2023']

    for country in countries:
        file_mapping[country] = []  # Initialize empty list for each country
        import ply.yacc as yacc

        for year in years:
            # Reset parsed_data for each year
            parsed_data.clear()
            bas_url=""
            base_url = f'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{country}_'
            url = f'{base_url}({year})'
            # print(url)
            # exit()
            ans=[]
            encoded_url = urllib.parse.quote(url, safe=':/')
            
            try:
                urll=encoded_url
                req = Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                mydata = webpage.decode("utf8")
                save_dat=mydata
            except urllib.error.HTTPError as e:
                
                print(f"No data for {country} in {year}")
                continue
            file_nma=""
            f = open(f'webpage_{country}_{year}.html', 'w', encoding="utf-8")
            f.write(mydata)
            lexer = lex.lex()

            file_obj = open(f'webpage_{country}_{year}.html', 'r', encoding="utf-8")
            data = file_obj.read()
            parser = yacc.yacc()

            lexer.input(data)
            # with open(f"abc_{country}_{year}.txt", 'w', encoding='utf-8') as h:
            #     for tok in lexer:
            #         # print(tok)
            #         h.write(str(tok) + '\n')
            parser.parse(data)
            file_obj.close()
            f.close
            my_fil=[]
            # Write data to the corresponding output file for the country and year
            output_filename = f"{country}_{year}.txt"
            
            with open(output_filename, "w", encoding="utf-8") as output_file:
                datee=""
                for date, content in reversed(parsed_data):
                    output_file.write(f"{date}::{content}\n")
            file_mapping[country].append(output_filename)  # Add filename to the list for the country
    filee="file_mapping.txt"
    # Write the file mapping to a text file
    with open("file_mapping.txt", "a", encoding="utf-8") as mapping_file:
        my_file=mapping_file
        mapping_file.write(str(file_mapping))
        mapping_file.write('\n')

if __name__ == '__main__':
    main()