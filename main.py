import datetime
import time
import os
import ascii_char as ascii
import re

class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def conv_seconds_to_time(total_seconds):
    _hours = total_seconds // 3600
    total_seconds %= 3600
    _minutes = total_seconds // 60
    _seconds = total_seconds % 60
    return _hours, _minutes, _seconds


def is_valid_time_format(time_str):
    try:
        int(time_str)
        if isinstance(int(time_str), int):
            return int(time_str) >= 0
    except:
        if isinstance(time_str, str):
            pattern = r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
            return re.match(pattern, time_str) is not None
    return False


def conv_str_to_time(time_str) -> datetime.datetime:
    try:
        int(time_str)
        _h, _m, _s = conv_seconds_to_time(int(time_str))
    except:
        _h, _m, _s = time_str.split(':')
    finally:
        return datetime.datetime(year=1, month=1, day=1, hour=int(_h), minute=int(_m), second=int(_s))


def print_time_as_ascii(t: datetime.datetime):
    def colorize_digit(digit, color):
        return f"{color}{digit}{bcolors.ENDC}"

    # Get time components
    _time_comp_str = list(str(t.time()))
    _time_comp_int = [int(c) if c != ":" else c for c in _time_comp_str]

    # Get ascii art representation for each component
    _time_comp_ascii_art = [ascii.char.get(a) for a in _time_comp_int]

    # Colorize digits
    green_indices = [0, 1, 3, 4]
    for idx in green_indices:
        _time_comp_ascii_art[idx] = [colorize_digit(a, bcolors.GREEN) for a in _time_comp_ascii_art[idx]]

    color = bcolors.YELLOW if t < datetime.datetime(year=1, month=1, day=1, hour=0, minute=1, second=0) else bcolors.CYAN

    _time_comp_ascii_art[6] = [colorize_digit(a, color) for a in _time_comp_ascii_art[6]]
    _time_comp_ascii_art[7] = [colorize_digit(a, color) for a in _time_comp_ascii_art[7]]

    # Print ASCII
    for c in zip(*_time_comp_ascii_art):
        print(*c)


def count_down(t):
    while t > datetime.datetime(year=1, month=1, day=1, hour=0, minute=0, second=0):
        t = t - datetime.timedelta(seconds=1)
        time.sleep(1)
        # print(t)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_time_as_ascii(t)
    time.sleep(3600)


if __name__ == '__main__':
    is_valid = False
    time_str = ""
    while is_valid == False:
        time_str = input("Set Timer (HH:MM:SS): ")
        is_valid = is_valid_time_format(time_str)
    count_down(conv_str_to_time(time_str))

