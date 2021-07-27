#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   This Module for to generate summary reports.
"""


import csv
import config
from collections import OrderedDict
import os


def gen_summary_report():
    """
        This function populate report.
    """
    li = []
    robo_type_list = []
    robo_name_list = []

    #Open csv file
    all_rows = []
    total_exec_time = 0
    #all_rows.append(["Robot Type", "Executed count"])
    with open(config.details_report_path, 'r') as csvFile:
        for line in csvFile:
            lst = line.split(",")
            if len(lst) > 1:
                robo_name = lst[0]
                robo_type = lst[1]
                eta_time = lst[3]
                if (robo_type != "Type") and (robo_type not in robo_type_list):
                    robo_type_list.append(robo_type)
                if (robo_name != "Robot Name") and (robo_name not in robo_name_list):    
                    robo_name_list.append(robo_name)
                if eta_time != "ETA(ms)":
                    total_exec_time += int(eta_time)

    # Summary report                
    print("\r")
    print("\r")        
    print("***********************************************************")
    print("*******************Summary Report**************************")         
    print("***********************************************************")
    print("\r")
    print("*******************Robot Type Selected**********************")
    print(",".join(robo_type_list))
    print("************************************************************")
    print("\r")
    print("*******************Robot Users Selected**********************")
    print(",".join(robo_name_list))
    print("************************************************************")
    print("\r")
    print("\r")
    print("*******************Total Execution time for tasks(ms)*******")
    print(total_exec_time)
    print("************************************************************")
    print("\r")



#Starting point for program.
if __name__ == '__main__':
    gen_summary_report()
