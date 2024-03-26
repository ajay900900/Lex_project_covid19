import sys
import calendar

def parse_date(date_str):
    """Parse a date string into day, month, and year integers."""
    day, month, year = map(int, date_str.split('-'))
    return day, month, year

def parse_file_name(file_name):
    """Extract the year and month from the file name."""
    parts = file_name.split("_")
    year = int(parts[1])
    month = parts[0].split("/")[1]  # Assuming the month is embedded as described
    return year, month

def is_date_within_range(date_components, year, month, start_year, start_month, start_day, end_year, end_month, end_day):
    """Determine if the date is within the given start and end date range."""
    day = int(date_components[0])
    month_index = month_names.index(month)
    if year == start_year and month_index < start_month:
        return False
    if year == start_year and month_index == start_month and day < start_day:
        return False
    if year == end_year and month_index > end_month:
        return False
    if year == end_year and month_index == end_month and day > end_day:
        return False
    return True

def process_file(file_name, start_year, start_month, start_day, end_year, end_month, end_day):
    """Process each line of the file, printing content within the date range."""
    year, month = parse_file_name(file_name)
    with open(file_name, 'r', encoding='latin-1') as fp:
        for line in fp:
            date_str, content = line.split('::')
            date_components = date_str.split(" ")
            if is_date_within_range(date_components, year, month, start_year, start_month, start_day, end_year, end_month, end_day):
                print(" ".join(date_components), year, "::", content)

if __name__ == "__main__":
    file_name = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]

    start_day, start_month, start_year = parse_date(start_date)
    end_day, end_month, end_year = parse_date(end_date)

    month_names = list(calendar.month_name)
    print(start_date, end_date)
    process_file(file_name, start_year, start_month, start_day, end_year, end_month, end_day)
