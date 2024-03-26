import os

def parse_date(date_str):
    """
    Parses a date string in 'DD-MM-YYYY' format and returns day, month, and year as integers.
    """
    day, month, year = map(int, date_str.split('-'))
    return day, month, year

def set_environment_dates(start_date, end_date):
    """
    Sets the START_DATE and END_DATE environment variables.
    """
    os.environ['START_DATE'] = f"{start_date[0]}-{start_date[1]}-{start_date[2]}"
    os.environ['END_DATE'] = f"{end_date[0]}-{end_date[1]}-{end_date[2]}"

# def run_make_command(makefile_directory):
#     """
#     Changes the current directory to 'makefile_directory' and executes the make command.
#     """
#     os.chdir(makefile_directory)
#     os.system('make -f Makefile')

def main():
    print("Input Date Range:")
    start_date_str = input()
    end_date_str = input()
    
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)
    
    set_environment_dates(start_date, end_date)
    
    # makefile_directory = '../Module_2_1to2/module_3_2_news'
    # run_make_command(makefile_directory)
    os.system('make -f Makefile')
if __name__ == "__main__":
    main()
