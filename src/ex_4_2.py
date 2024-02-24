""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    # Parse the input date string using the specified format
    date_format = "%Y-%m-%dT%H:%M:%S"
    datetime_object = datetime.strptime(datestr, date_format)

    return datetime_object

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')