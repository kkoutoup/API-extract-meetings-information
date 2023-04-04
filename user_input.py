# Python modules
import re
from datetime import datetime, date
import time
import sys

# local modules
from helper_functions import calculate_days_of_the_week

def get_user_input():
    while True:
        print("Please choose a valid timespan\n 1.'today' for the day's meetings\n 2.'week' for this week's meetings \n 3.any other timespan in the following format: dd/mm/yyyy-dd/mm/yyyy\n 4.or type 'out' to exit")
        user_input = input()
        # check for 'today' or 'week'
        accepted_values = ['today', 'week']
        # check for other formats if user enters date range instead
        date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}\-\d{2}\/\d{2}\/\d{4}')
        date_match = re.match(date_regex, user_input)
        # exit application on relevant user input otherwise check and return user_input
        if user_input.lower() == 'out':
            sys.exit()
        if user_input in accepted_values:
            return user_input
        if date_match:
            return date_match.group()

def translate_user_input():
    # possible scenarios: 'today', 'week', date range
    user_input = get_user_input()
    if user_input == 'today':
        todays_date = date.today()
        time.sleep(1) # in some cases 'today' was returning 'None'. Pausing script to avoid that.
        return f"{todays_date}/{todays_date}" # api endpoint needs two values (from/to) - in this case they match
    elif user_input == 'week':
       result = calculate_days_of_the_week()
       return result
    else:
        date_range = user_input.split('-')
        date_range_array = [datetime.strptime(item,'%d/%m/%Y').strftime('%Y-%m-%d') for item in date_range] # string to datetime object and formatted with strftime
        return'/'.join(date_range_array)
