import calendar
import os

def parse_date(date_str):
    """Parse a date string and return day, month, and year as integers."""
    day, month, year = map(int, date_str.split('-'))
    return day, month, year

def generate_file_paths(start_year, end_year, start_month, end_month):
    """Generate file paths for the specified date range."""
    month_names = list(calendar.month_name)
    file_paths = []
    for year in range(start_year, end_year + 1):
        start_m = start_month if year == start_year else 1
        end_m = end_month if year == end_year else 12
        for month in range(start_m, end_m + 1):
            month_name = month_names[month]
            file_paths.append(f"{month_name}_{year}_response.txt")
    return file_paths

def main():
    start_date_str = os.environ.get("START_DATE", "1-1-2020")  # Provide default start date
    end_date_str = os.environ.get("END_DATE", "31-12-2020")  # Provide default end date

    start_day, start_month, start_year = parse_date(start_date_str)
    end_day, end_month, end_year = parse_date(end_date_str)

    file_paths = generate_file_paths(start_year, end_year, start_month, end_month)
    print("\n".join(file_paths))

if __name__ == "__main__":
    main()
