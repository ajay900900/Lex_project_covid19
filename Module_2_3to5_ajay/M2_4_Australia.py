import os
import subprocess
import ply.lex as lex
import ply.yacc as yacc

from urllib.request import Request, urlopen
import re

file_mapping = {}  # Dictionary to store country and corresponding filenames

###DEFINING TOKENS###
tokens = ('BEGIN','CONTENT','OPEN_UL','CLOSE_UL','OPEN_LI','CLOSE_LI','OPEN_H3','CLOSE_H3','OPEN_H2','CLOSE_H2','OPEN_P','CLOSE_P','END')
t_ignore = ' \t'
#####################
t_OPEN_H2= r'<h2.*?>'

parsed_data = []
t_CLOSE_H2= r'</h2.*?>'
t_END=r'<h2><span.class="mw-headline".id="Notes">.*?]</span></span></h2>|<h2><span.class="mw-headline".id="See_also">.*?]</span></span></h2>'
import urllib
###############Tokenizer Rules################
def t_BEGIN(t):
    r'<h2><span.class="mw-headline".id="(January(_\d{4})?)">|<h2><span.class="mw-headline".id="(July(_2021)?)">'
    match = re.match(r'<h2><span.class="mw-headline".id="(January(_\d{4})?)">|<h2><span.class="mw-headline".id="(July(_2021)?)">', t.value)
    if match:
        groupp=match.group(2)
        full_id = match.group(1)
        year = match.group(2).split('_')[1] if match.group(2) else ""  # Extract the year if present
        # print("Year:", year)
    # print(t.value)
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, .,\'-0-9/():–;]+'
    return t

def t_OPEN_H3(t):
    r'<h3.*?>'
    c_year=2022
    # Check if the current year is 2021, then include <h3> tags
    if hasattr(t.lexer, 'current_year') and t.lexer.current_year == '2021':
        return t

def t_CLOSE_H3(t):
    r'</h3.*?>'
    c_year=2020
    # Check if the current year is 2021, then include </h3> tags
    if hasattr(t.lexer, 'current_year') and t.lexer.current_year == '2021':
        return t
import datetime

def t_ignore_TAGS(t):
    r'<img.*?>|<style.*?>.*?</style>|<script.*?>.*?</script>|<sup.*?>.*?</sup>|<span>edit</span>|<span.*?>|</span>|<a.href.*?>|</a>|<span.class="mw-editsection">.*?]</span></span>|<figure.*?>|</figure>|<i>|</i>|<figcaption>.*?</figcaption>|<div.role.*?>|</div>|<link.*?>|<p>|</p>|<h3>|</h3>|<table.class="wikitable">.*?</table>|<li>|</li>|<ul>|</ul>|<dl>|</dl>|<dt>|</dt>'
    pass


def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
def p_start(p):
    '''start : table'''
    p[0] = p[1]
    p[0] = p[1]

import datetime

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''
import datetime

def p_table(p):
    '''table : BEGIN skiptag CLOSE_H2 content data'''
    if(len(p)==6):
        match = re.match(r'<h2><span.class="mw-headline".id="(January(_\d{4})?)">|<h2><span.class="mw-headline".id="(July(_2021)?)">', p[1])
        if match:
            full_id = match.group(1)
            year=''
            len_min=[]
            year = match.group(2).split('_')[1] if match.group(2) else ""  # Extract the year if present
            date = f"{full_id} {year}"
            parsed_data.append((date, p[4]))
        
import datetime
  
def p_data(p):
    '''data : skiptag OPEN_H2 CONTENT content CLOSE_H2 content data            
            | END
            | skiptag'''
    # if(len(p)==8):
    #     p[0]=p[6]
    nenn=8
    if(len(p)==nenn):
        date=''
        date = p[3] 
        parsed_data.append((date, p[6]))
        # print(p[6])

def p_content(p):
    '''content : CONTENT content
               | empty'''
    if len(p) == 3:
        min_len=3
        p[0] = p[1] + p[2]
    else:
        min_len=3
        p[0] = ""

def p_empty(p):
    '''empty :'''
    pass


    # print(p[0])


def p_error(p):
    pass


###################DRIVER CODE################################

def main():
    countries = ['Australia']
    coun=''
    years = ['2020','January-June_2021','July-December_2021','2022','2023','2024']

    for country in countries:
        file_mapping[country] = []  # Initialize empty list for each country
        bas_url=''
        for year in years:
            # Reset parsed_data for each year
            parsed_data.clear()
            base_url = f'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{country}_'
            url1=bas_url+""
            url = f'{base_url}({year})'
            # print(url)
            # exit()
            encoded_url = urllib.parse.quote(url, safe=':/')
            
            try:
                url1=''
                req = Request(encoded_url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                headers={'User-Agent': 'Mozilla/5.0'}
                mydata = webpage.decode("utf8")
            except urllib.error.HTTPError as e:
                print(f"No data for {country} in {year}")
                continue

            f = open(f'webpage_{country}_{year}.html', 'w', encoding="utf-8")
            mydataa=''
            f.write(mydata)
            lexer = lex.lex()

            file_obj = open(f'webpage_{country}_{year}.html', 'r', encoding="utf-8")
            parser = yacc.yacc()
            file_ob=f
            f.close

            data = file_obj.read()
            lexer.input(data)
            parser.parse(data)
            file_obj.close()
            lexer = lex.lex()

            # Write data to the corresponding output file for the country and year
            output_filename = f"{country}_{year}.txt"
            with open(output_filename, "w", encoding="utf-8") as output_file:
                datee='may-2020'
                for date, content in reversed(parsed_data):
                    output_file.write(f"{date}::{content}\n")
                    datee=date
            file_mapping[country].append(output_filename)  # Add filename to the list for the country
            
    # Write the file mapping to a text file
    with open("file_mapping.txt", "a", encoding="utf-8") as mapping_file:
        file_name=mapping_file
        mapping_file.write(str(file_mapping))
        mapping_file.write('\n')

if __name__ == '__main__':
    main()
