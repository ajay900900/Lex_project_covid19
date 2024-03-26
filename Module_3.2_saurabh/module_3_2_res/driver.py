import os

def parse_date(date_str):
    """Parse a date string into day, month, and year integers."""
    day, month, year = map(int, date_str.split('-'))
    return day, month, year

def set_environment_dates(start_date, end_date):
    """Set START_DATE and END_DATE environment variables based on the input dates."""
    os.environ['START_DATE'] = f"{start_date[0]}-{start_date[1]}-{start_date[2]}"
    os.environ['END_DATE'] = f"{end_date[0]}-{end_date[1]}-{end_date[2]}"

# # def run_makefile(directory):
#     """Change directory and run the Makefile within the specified directory."""
#     os.chdir(directory)
#     os.system('make -f Makefile')

def main():
    print("Input Date Range for Response:")
    start_input = input()
    end_input = input()

    start_date = parse_date(start_input)
    end_date = parse_date(end_input)

    set_environment_dates(start_date, end_date)
    os.system('make -f Makefile')

    # makefile_directory = '../Module_2_1to2/module_3_2_res'
    # run_makefile(makefile_directory)

if __name__ == "__main__":
    main()
