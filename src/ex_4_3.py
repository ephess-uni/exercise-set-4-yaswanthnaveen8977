""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<

def time_between_shutdowns(logfile):
    shutdown_events = get_shutdown_events(logfile)

    if len(shutdown_events) < 2:
        raise ValueError("There should be at least two shutdown events to calculate time difference.")

    # Convert the date fields to datetime objects
    first_shutdown_datetime = logstamp_to_datetime(shutdown_events[0])
    last_shutdown_datetime = logstamp_to_datetime(shutdown_events[-1])

    # Calculate the time difference
    time_difference = last_shutdown_datetime - first_shutdown_datetime

    return time_difference

# Example usage:
if __name__ == "__main__":
    time_difference = time_between_shutdowns(FILENAME)
    print(f"Time between first and last shutdowns: {time_difference}")
