import sys
import calendar

def parse_date(date_str):
    """Parse a date string into day, month, and year integers."""
    day, month, year = map(int, date_str.split('-'))
    return day, month, year

def is_date_within_range(year, month, day, start_year, start_month, start_day, end_year, end_month, end_day):
    """Check if a given date is within the start and end date range."""
    if year < start_year or year > end_year:
        return False
    if year == start_year and month < start_month:
        return False
    if year == end_year and month > end_month:
        return False
    if year == start_year and month == start_month and day < start_day:
        return False
    if year == end_year and month == end_month and day > end_day:
        return False
    return True

def process_file(file_name, start_year, start_month, start_day, end_year, end_month, end_day):
    """Process each line of the file within the date range."""
    month_names = list(calendar.month_name)
    with open(file_name, 'r', encoding='latin-1') as fp:
        file_year = int(file_name.split("_")[1])
        file_month = month_names.index(file_name.split("_")[0].split("/")[1])
        
        for line in fp:
            date_str, content = line.split('::')
            date_components = date_str.split(" ")
            day = int(date_components[0])
            
            if is_date_within_range(file_year, file_month, day, start_year, start_month, start_day, end_year, end_month, end_day):
                print(" ".join(date_components), file_year, "::", content)

if __name__ == "__main__":
    file_name = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    
    start_day, start_month, start_year = parse_date(start_date)
    end_day, end_month, end_year = parse_date(end_date)
    
    print(start_date, end_date)
    process_file(file_name, start_year, start_month, start_day, end_year, end_month, end_day)
