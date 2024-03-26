import os
import subprocess




import ply.lex as lex
###DEFINING TOKENS###
tokens = ('BEGIN','CONTENT','END','OPEN_H3','CLOSE_H3')
t_ignore = ' \t'
from collections import defaultdict
extracted_data = defaultdict(list)

#####################
# t_OPEN_UL= r'<ul.*?>'
# t_CLOSE_UL= r'</ul.*?>'
# t_OPEN_LI= r'<li.*?>'
# t_CLOSE_LI= r'</li.*?>'
t_OPEN_H3= r'<h3.*?>'
import datetime
t_CLOSE_H3= r'</h3.*?>'
# t_OPEN_P= r'<p.*?>'
# t_CLOSE_P= r'</p.*?>'

###############Tokenizer Rules################



def t_ignore_TAGS(t):
    r'<h4>|</h4>|<i>|</i>|</b>|<b>|<ul>|</ul>|<li>|</li>|</p>|<p>|<h2[^>]*>.*?<\/h2>|<img.*?>|<table.*?>.*?</table>|<style.*?>.*?</style>|<figure[^>]*>.*?<\/figure>|<script.*?>.*?</script>|<sup.*?>.*?</sup>|<span.*?>|</span>|<a.href.*?>|</a>|<span.class="mw-editsection">.*?]</span></span>'
    pass
    return
def t_CONTENT(t):
    r'[A-Za-z0-9, .,\'-0-9/():–;]+'
    return t


def t_BEGIN(t):
    r'<div.id="siteSub".class="noprint">From.Wikipedia,.the.free.encyclopedia</div>'
    return t


import ply.yacc as yacc
def t_ignnore_situation_report(t):
    r'<b>WHO</b>Situation.Report.\(\d+\)|<b>WHO</b>Situation.Report.\(\d+\):|<b>WHO</b>Situation.Report.\(\d+\);'
    pass

def t_error(t):
    t.lexer.skip(1)
    
def t_END(t):
    r'<h2[^>]*><span.class="mw-headline".id="See_also">See.also</span>.*?<\/h2>|<h2[^>]*><span.class="mw-headline".id="Summary">Summary</span>.*?<\/h2>'
    dum=0
    return t
    
     
####################################################################################################################################################################################################
def p_start(p):
    '''start : table'''
    p[0] = p[1]
import ply.yacc as yacc

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''
import ply.yacc as yacc

def p_table(p):
    '''table : BEGIN skiptag data skiptag END'''
    p[0] = p[3]
    min_len=3
    
def p_header(p):
    '''header : OPEN_H3 CONTENT content CLOSE_H3'''
    min_le=2
    p[0]=p[2]

def p_data(p):
    '''data : data header content
            | header content'''
    global extracted_data
    miin_len=3
    if(len(p)==3):
        if(p[1] not in ['Background','Timeline']):
            to_add=[p[1]].append(p[2])
            extracted_data[p[1]].append(p[2])
    else:
        extr_dat={}
        if(p[2] not in ['Background','Timeline']):
            extr_data=[]
            extracted_data[p[2]].append(p[3])
        

def p_empty(p):
    '''empty :'''
    pass
    pass

def p_content(p):
    '''content : CONTENT content
               | empty'''
    if len(p) == 3:
        to_add=""
        p[0] = p[1] + p[2]
    else:
        store=[]
        p[0] = ""

import ply.yacc as yacc

def p_error(p):
    pass

###################DRIVER CODE################################
def main():
    directory_web_new = "Downloaded-Webpages-news"  # Replace "/path/to/directory" with the desired directory path
    directory_res = "Responses"  # Replace "/path/to/directory" with the desired directory path
    directory_new = "News"  # Replace "/path/to/directory" with the desired directory path
    directory_web_res = "Downloaded-Webpages-responses"  # Replace "/path/to/directory" with the desired directory path

    if not os.path.exists(directory_web_new):
        os.makedirs(directory_web_new)
    if not os.path.exists(directory_web_res):
        os.makedirs(directory_web_res)
    if not os.path.exists(directory_new):
        os.makedirs(directory_new)
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    if not os.path.exists(directory_res):
        os.makedirs(directory_res)
    # month = ['January'], 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for year in [2020,2021,2022]:
        for m in month:
            extracted_data.clear()
            fie_obj=None
            name=f"{m}_{year}"
            url="https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_"+name
            # url="https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_January_2020"
            subprocess.run(["python3", "webpage_download_mod2.py", f"./Downloaded-Webpages-news/{name}.html", url])
            parser = yacc.yacc()
            file_obj= open(f"./Downloaded-Webpages-news/{name}.html",'r',encoding="utf-8")
            
            lexer = lex.lex()
            

            data=file_obj.read()
            lexer.input(data)
            # for tok in lexer:
            #     print(tok)
            parser.parse(data)

            with open(f'./News/{name}_news.txt', 'w') as file:
                for date, content in extracted_data.items():
                    to_add={" ".join(map(str, content))}
                    file.write(f'{date}:: {" ".join(map(str, content))}\n')
            print(f"extracted news: {m} {year}")
            ans_=[]
            file_obj.close()
    url1="https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_2023"
    subprocess.run(["python3", "webpage_download_mod2.py", f"./Downloaded-Webpages-news/2023_news.html", url1])
    to_run_subpre=[]
    url2="https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_2024"

    subprocess.run(["python3", "webpage_download_mod2.py", f"./Downloaded-Webpages-news/2024_news.html", url2])       
    subprocess.run(["python3", "2023_2024_util.py"])
    month_wise=[]
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for year in [2020,2021,2022]:
        for m in month:
            extracted_data.clear()
            url_new=""
            if(year==2022 and m in ['November', 'December']):
                continue
            name=f"{m}_{year}"
            url="https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_"+name
            subprocess.run(["python3", "webpage_download_mod2.py", f"./Downloaded-Webpages-responses/{name}.html", url])
            run_sub=url
            file_obj= open(f"./Downloaded-Webpages-responses/{name}.html",'r',encoding="utf-8")
            file_ob=name
            parser = yacc.yacc()
            lexer = lex.lex()

            data=file_obj.read()
            
            lexer.input(data)
            # for tok in lexer:
            #     print(tok)
            parser.parse(data)

            with open(f'./Responses/{name}_response.txt', 'w') as file:
                for date, content in extracted_data.items():
                    to_add={" ".join(map(str, content))}
                    file.write(f'{date}:: {" ".join(map(str, content))}\n')

            file_obj.close()
            file_obj.close()

            print(f"extracted response: {m} {year}")


if __name__ == "__main__":
    main()

