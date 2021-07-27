#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   This Module for to generate reports by Robot name.
"""

import csv
import config
import csv
from collections import OrderedDict
import os

def gen_efficient_robo_byname_report():
    """
        This function populate report.
    """
    li = []
    robo_name_dict = {}

    #Open csv file
    all_rows = []
    with open(config.details_report_path, 'r') as csvFile:
        for line in csvFile:
            lst = line.split(",")
            if len(lst) > 1:
                robo_name = lst[0]
                if robo_name != "Robot Name":
                    if robo_name in robo_name_dict:
                        count += 1
                        robo_name_dict[robo_name] = count
                    else:
                        count = 1
                        robo_name_dict[robo_name] = count


    sorted_dict = sorted(robo_name_dict, key=robo_name_dict.get, reverse=True)                                  
    for robo_name in sorted_dict:
        all_rows.append([robo_name, robo_name_dict[robo_name]])

    filename = config.robot_name_report_path
    fields = ['Robot Name', 'Executed count'] 
    file_exists = os.path.isfile(filename)
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(all_rows)


def pad_col(col, max_width):
    return col.ljust(max_width)

def gen_report():
    """
        This function generate report.
    """
    with open(config.robot_name_report_path) as csvfile:
        reader = csv.reader(csvfile)
        all_rows = []
        for row in reader:
            all_rows.append(row)

    max_col_width = [0] * len(all_rows[0])
    for row in all_rows:
        for idx, col in enumerate(row):
            max_col_width[idx] = max(len(col), max_col_width[idx])

    for row in all_rows:
        to_print = ""
        for idx, col in enumerate(row):
            to_print += pad_col(col, max_col_width[idx]) + " | "
        print("-"*len(to_print))
        print(to_print)


#Starting point for program.
if __name__ == '__main__':
    gen_efficient_robo_byname_report()
    gen_report()

