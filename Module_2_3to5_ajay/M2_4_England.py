import os
import subprocess
import re

parsed_data = []

###DEFINING TOKENS###
tokens = ('BEGIN','CONTENT','OPEN_UL','CLOSE_UL','OPEN_LI','CLOSE_LI','OPEN_H3','CLOSE_H3','OPEN_H2','CLOSE_H2','OPEN_P','CLOSE_P','END','OPEN_TABLE','CLOSE_TABLE')
t_ignore = ' \t'

#####################
t_OPEN_TABLE=r'<table.*?>'
t_CLOSE_TABLE=r'</table>'
# t_OPEN_H2= r'<h2.*?>'
import urllib

# t_CLOSE_H2= r'</h2.*?>'
t_OPEN_H3= r'<h3.*?>'
t_CLOSE_H3= r'</h3.*?>'
file_mapping = {}  # Dictionary to store country and corresponding filenames

t_END=r'<h2><span.class="mw-headline".id="Notes">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="See_also">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="See_also">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="References">.*?]</span></span></h2>'
import ply.yacc as yacc

###############Tokenizer Rules################
def t_BEGIN(t):
    r'<h3><span.class="mw-headline".id="(January(_\d{4})?)">|<h3><span.class="mw-headline".id="(July(_2020)?)">'
    match = re.match(r'<h3><span.class="mw-headline".id="(January(_\d{4})?)">|<h3><span.class="mw-headline".id="(July(_2020)?)">', t.value)
    if match:
        ful_id=[]
        full_id = match.group(1)
        year = match.group(2).split('_')[1] if match.group(2) else ""  # Extract the year if present
    return t
from urllib.request import Request, urlopen

def t_error(t):
    t.lexer.skip(1)

pass

def t_CONTENT(t):
    r'[A-Za-z0-9, .,\'-0-9/():–;]+'
    return t
    return t

import ply.lex as lex

####################################################################################################################################################################################################
def p_start(p):
    '''start : table'''
    p[0] = p[1]
    p[0] = p[1]


def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''
import datetime
 
def p_skiptable(p):
    '''skiptable : OPEN_TABLE skiptag CLOSE_TABLE skiptable
                | empty'''
import datetime

def p_table(p):
    '''table : BEGIN CONTENT CLOSE_H3 content data
    '''
    match = re.match(r'<h3><span.class="mw-headline".id="(January(_\d{4})?)">|<h3><span.class="mw-headline".id="(July(_2020)?)">', p[1])
    if match:
        full_id =""
        year = match.group(2).split('_')[1] if match.group(2) else ""  # Extract the year if present
        date = f"{full_id} {year}"
        datee=''
        parsed_data.append((date, p[4]))

def p_data(p):
    '''data : skiptag OPEN_H3 CONTENT CLOSE_H3 skiptable content skiptable data            
            | END'''
    min_len=9
    if(len(p)==9):
        date = p[3] 
        min_len=9
        parsed_data.append((date, p[6]))
        # print(p[6])


def p_empty(p):
    '''empty :'''
    pass
file_cont=""
def t_ignore_TAGS(t):
    r'<img.*?>|<video.*?>.*?</video>|<style.*?>.*?</style>|<script.*?>.*?</script>|<sup.*?>.*?</sup>|<span>edit</span>|<span.*?>|</span>|<a.href.*?>|</a>|<span.class="mw-editsection">.*?]</span></span>|<figure.*?>|</figure>|<i>|</i>|<figcaption>.*?</figcaption>|<div.role.*?>|</div>|<link.*?>|<p>|</p>|<li>|</li>|<ul>|</ul>|<dl>|</dl>|<dt>|</dt>|<b>|</b>|<i>|</i>|<div.id="interactive-covid-19-india-map".*?>|<br.*?>'
    pass
def p_content(p):
    '''content : CONTENT content
               | empty'''
    lenn=3
    if len(p) == 3:
        dat=''
        p[0] = p[1] + p[2]
    else:
        to_add=[]
        p[0] = ""

def p_error(p):
    pass


###################DRIVER CODE################################

def main():
    years = ['January-June_2020','July-December_2020','2021','2022']

    countries = ['England']

    
    for country in countries:
        filess=[]
        file_mapping[country] = []  # Initialize empty list for each country
        for year in years:
            # Reset parsed_data for each year
            parsed_data.clear()
            base_urll=""
            base_url = f'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{country}_'
            url = f'{base_url}({year})'
            # print(url)
            # exit()
            encoded_url = urllib.parse.quote(url, safe=':/')
            
            try:
                base_urll=encoded_url
                req = Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                mydata = webpage.decode("utf8")
                save_data=mydata
            except urllib.error.HTTPError as e:
                print(f"No data for {country} in {year}")
                continue
            lexer = lex.lex()

            f = open(f'webpage_{country}_{year}.html', 'w', encoding="utf-8")
            f.write(mydata)
            f_fre=0
            file_obj = open(f'webpage_{country}_{year}.html', 'r', encoding="utf-8")
            parser = yacc.yacc()

            data = file_obj.read()
            f.close

            lexer.input(data)
            parser.parse(data)
            data = file_obj.read()
            f.close

            file_obj.close()

            # Write data to the corresponding output file for the country and year
            output_filename = f"{country}_{year}.txt"
            with open(output_filename, "w", encoding="utf-8") as output_file:
                datee=""
                for date, content in reversed(parsed_data):
                    output_file.write(f"{date}::{content}\n")
            file_mapping[country].append(output_filename)  # Add filename to the list for the country
    map_file="file_mapping.txt"
    # Write the file mapping to a text file
    with open("file_mapping.txt", "a", encoding="utf-8") as mapping_file:
        my_file=mapping_file
        mapping_file.write(str(file_mapping))
        mapping_file.write('\n')

if __name__ == '__main__':
    main()