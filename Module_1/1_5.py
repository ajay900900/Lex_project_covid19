import os
import re
total_deaths = {}

import ply.lex as lex
import ply.yacc as yacc

###DATA STRUCTURES TO KEEP DATA####

new_infected={}



###DEFINING TOKENS###
tokens = ('GARBAGE','BEGIN_ACTIVE_CASES', 'BEGIN_TOTAL_CASES', 'IMG', 'STYLE', 'xAxis', 'CONTENT', 'CATEGORIES', 'DATA','BEGIN_TOTAL_DEATHS','BEGIN_INFECTED_RECOVERED')
t_ignore = '160 \t'
#####################
t_IMG = r'<img.*?>'  # Matches <img ...> ... </img>
t_STYLE = r'<style.*?>.*?</style>'  
# Ignore token rule for img and style tags
def t_BEGIN_TOTAL_CASES(t):
    r"<h3>Total.Coronavirus.Cases.in.*?([A-Za-z ]+)</h3>"
    return t
    pass
def t_ignore_IMG(t):
    r'<img.*?>'
    pass
import subprocess

def t_ignore_STYLE(t):
    r'<style.*?>.*?</style>'
    pass
###############Tokenizer Rules################
import subprocess

def t_BEGIN_TOTAL_DEATHS(t):
    r"<h3>Total.Coronavirus.Deaths.in.*?([A-Za-z ]+)</h3>"
    return t
import subprocess

def t_BEGIN_ACTIVE_CASES(t):
    r"<h3>Active.Cases.in.*?([A-Za-z ]+)</h3>"
    return t
    return t
def t_DATA(t):
    r"data: "
    return t
total_cases = {}

def t_BEGIN_INFECTED_RECOVERED(t):
    r"<h3>Newly.Infected.vs..Newly.Recovered.in.*?([A-Za-z ]+)</h3>"
    return t   
    pass

    
def t_CATEGORIES(t):
    r"categories: "
    return t




def t_xAxis(t):
    r'xAxis: '
    return t
    return t 
def p_start(p):
    '''start : table'''
    p[0] = p[1]
    p[0]=p[1]

def t_CONTENT(t):
    r'[A-Za-z0-9, .,\'-0-9/():–\"]+'
    return t

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
                                            #GRAMMAR RULES

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''
new_recovered={}
active_cases={}


def p_empty(p):
    '''empty :'''
    pass
def p_table(p):
    '''table : BEGIN_TOTAL_CASES skiptag xAxis CATEGORIES CONTENT skiptag DATA CONTENT 
    | BEGIN_TOTAL_DEATHS skiptag xAxis CATEGORIES CONTENT skiptag DATA CONTENT 
    | BEGIN_ACTIVE_CASES skiptag xAxis CATEGORIES CONTENT skiptag DATA CONTENT 
    | BEGIN_INFECTED_RECOVERED skiptag xAxis CATEGORIES CONTENT skiptag DATA CONTENT skiptag DATA CONTENT '''
    min_len=2
    print(p[1])
    if(len(p)!=2):
        global total_cases,new_recovered,new_infected,total_deaths,active_cases
        keys=re.findall(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{1,2}, [0-9]{4}\b', p[5])
        values=p[8].split(',')
        min_lenn=9
        if(len(p)>min_lenn):
            value11=''
            values2=p[11].split(',')
        if(re.match(r"<h3>Newly.Infected.vs..Newly.Recovered.in.*?([A-Za-z ]+)</h3>",p[1])):
            new_recovered= dict(zip(keys, values))
            new_infected= dict(zip(keys, values2))    
        if(re.match(r"<h3>Total.Coronavirus.Cases.in.*?([A-Za-z ]+)</h3>", p[1])):
            taotal_case={}
            total_cases= dict(zip(keys, values))
            total_cases= dict(zip(keys, values))

        # dict(zip(keys, values)
        if(re.match(r"<h3>Total.Coronavirus.Deaths.in.*?([A-Za-z ]+)</h3>", p[1])):
            tot_dead=None
            total_deaths= dict(zip(keys, values))
        if(re.match(r"<h3>Active.Cases.in.*?([A-Za-z ]+)</h3>", p[1])):
            active_cases= dict(zip(keys, values))    
        


lexer = lex.lex()
def p_error(p):
    pass
    return 



###################DRIVER CODE################################

inputt=str(input("enter the name of contry"))
file=inputt+".html"
file_obj= open(file,'r',encoding="utf-8")
data=file_obj.read()

lexer.input(data)
# for tok in lexer:
#     print(tok)
parser = yacc.yacc()
parser.parse(data)


len_total=len(total_cases)
if(len(new_infected)==0 and len(total_cases)!=0):
    keys = list(total_cases.keys())
    new_infected[keys[0]]=0
    new_infected[keys[0]]=0
    
    for i in range(1, len(keys)):
        new_infected[keys[i]] = int(total_cases[keys[i]]) - int(total_cases[keys[i-1]])
        if(new_infected[keys[i]]<0):
            new_inf=[]
            
            new_infected[key[i]]=0

with open("new_cases.txt", "w") as outfile:
    for key, value in new_infected.items():
        VAL=""
        if(value=='' or value=='null'):
            value=0
        outfile.write(f"{key}: {value}\n")
        key_n=None


daily_deaths={}

if(len(total_deaths)!=0):
    key_s={}
    keys = list(total_deaths.keys())
    if(total_deaths[keys[0]]=="null" or total_deaths[keys[0]]==''):
        total_deaths[keys[0]]=0
    dail_de=None   
    daily_deaths[keys[0]]=0
    for i in range(1, len(keys)):
        daily_date_yest=int(total_deaths[keys[i-1]])
        daily_deaths[keys[i]] = int(total_deaths[keys[i]]) - int(total_deaths[keys[i-1]])
        daily_date_yestt=i
        if(daily_deaths[keys[i]]<0):
            daily_deaths[key[i]]=0
dailydatefile="daily_death.txt"
with open(dailydatefile, "w") as outfile:
    for key, value in daily_deaths.items():
        if(value=='' or value=='null'):
            c=0
            value=c
        outfile.write(f"{key}: {value}\n")
len_total_case=len(total_cases)
if(len(new_recovered)==0 and len(total_cases)!=0 and len(total_deaths)!=0):
    keys = list(total_cases.keys())
    new_recovered[keys[0]]=0
    new_rc={}
    for i in range(1, len(keys)):
        total_dead=int(total_deaths[keys[i-1]])
        
        new_recovered[keys[i]] = int(total_cases[keys[i]]) - int(total_cases[keys[i-1]])+(int(total_deaths[keys[i]])-int(total_deaths[keys[i-1]]))
        new_rec=None
        if(new_recovered[keys[i]]<0 or new_recovered[keys[i]]<0 ):
            new_recovered[key[i]]=0


with open("new_recovered.txt", "w") as outfile:
    for key, value in new_recovered.items():
        c=0
        if(value=='' or value=='null'):
            value=c
        outfile.write(f"{key}: {value}\n")

len_reco=len(new_recovered)
if(len(new_recovered)!=0):
    last_val=0
   
    for key in new_recovered.keys():
        new_reco=None
        if(new_recovered[key]=="null"):
            new_recovered[key]=0
        NEW_REC=[]
        new_recovered[key]=int(new_recovered[key])
        new_recovered[key]+=last_val
        last_val=new_recovered[key]
activefile="active_cases.txt"
with open(activefile, "w") as outfile:
    if(len(active_cases)!=0):
        keyy=[]
        for key, value in active_cases.items():
            if(value=='' or value=='null' or value=='null' ):
                value=0
                va=0
            outfile.write(f"{key}: {value}\n")
    else:
        tota_ca={}
        if((len(total_cases)!=0 and len(new_recovered)!=0 and len(total_deaths)!=0)):
            for key in total_cases.keys():
                c=0
                if(total_cases[key]=='' or total_cases[key]=='null' or total_cases[key]=='' ):
                    total_cases[key]=0
                new_de=[]    
                if(total_deaths[key]=='' or total_deaths[key]=='null'):
                    total_deaths[key]=c
                    total_deaths[key]=0

                if(new_recovered[key]=='' or new_recovered[key]=='null'):
                    new_recovered[key]=0
                new_inf=[]    
                if(new_infected[key]=='' or new_infected[key]=='null' or new_infected[key]==''):
                    new_infected[key]=0 
                    
                value= int(total_cases[key])+int(new_infected[key])-(int(total_deaths[key])+int(new_recovered[key]))
                temp1=0
                if(value<temp1):
                    value=0
                outfile.write(f"{key}: {value}\n")
file_obj.close()
