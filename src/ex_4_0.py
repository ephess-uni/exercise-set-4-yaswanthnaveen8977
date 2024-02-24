""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
        shutdown_events = []

        with open(logfile, 'r') as file:
            for line in file:
                if "Shutdown initiated" in line:
                    shutdown_events.append(line.strip())

        return shutdown_events
        logfile_path = "data/messages.log"
        shutdown_events = get_shutdown_events(logfile_path)

        if shutdown_events:
            for event in shutdown_events:
                print(event)
        else:
            print("No shutdown events found.")


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
