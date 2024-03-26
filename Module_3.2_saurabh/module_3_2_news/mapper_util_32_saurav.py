import calendar
import os

def parse_date(date_str):
    """Parse a date string and return day, month, and year as integers."""
    day, month, year = map(int, date_str.split('-'))
    return day, month, year

def generate_file_paths(start_year, end_year, start_month, end_month):
    """Generate file paths based on the start and end dates."""
    month_names = list(calendar.month_name)
    file_paths = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == start_year and month < start_month:
                continue
            if year == end_year and month > end_month:
                break
            file_paths.append(f"{month_names[month]}_{year}_news.txt")
    return file_paths

def main(start_date, end_date):
    start_day, start_month, start_year = parse_date(start_date)
    end_day, end_month, end_year = parse_date(end_date)
    
    file_paths = generate_file_paths(start_year, end_year, start_month, end_month)
    print("\n".join(file_paths))

if __name__ == "__main__":
    start_date = os.environ.get("START_DATE", "1-1-2020")  # Default start date if not set
    end_date = os.environ.get("END_DATE", "31-12-2020")  # Default end date if not set

    main(start_date, end_date)
