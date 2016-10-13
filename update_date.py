#!/usr/bin/python3

import os
from datetime import datetime


def replace_file():
    """REPLACE THE DATE."""
    file_path = os.path.join(os.path.dirname(__file__), 'apps/scalable/office-calendar.svg')
    new_file_path = os.path.join(os.path.dirname(__file__), 'apps/scalable/office-calendarXXX.svg')
    with open(new_file_path, 'w') as new_file:
        with open(file_path) as old_file:
            for index, line in enumerate(old_file):
                if ('date_indicator_line') in line:
                    new_file.write('       id="date_indicator_line" >' + str(datetime.now().day) + '</tspan></text>\n')
                elif ('month_indicator_line') in line:
                    new_file.write('       id="month_indicator_line" >' + str(datetime.now().strftime("%b")).upper() + '</tspan></text>\n')
                else:
                    new_file.write(line)
    # os.remove(file_path)
    print(file_path, new_file_path)
    os.rename(new_file_path, file_path)

replace_file()
# print(str(datetime.now().strftime("%b")).lower())
