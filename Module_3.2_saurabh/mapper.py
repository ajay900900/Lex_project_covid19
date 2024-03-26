import sys
import calendar
file_name=sys.argv[1]
import calendar

with open(file_name, 'r', encoding='latin-1') as fp:
	for line in fp:
		try: 
			date, content= line.split('::')    
			print(date,'::',content)   
		except ValueError:
			continue
