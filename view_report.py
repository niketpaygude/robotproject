#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   This Module for to generate reports.
"""

import config
from collections import OrderedDict
import os
import summary_report
import view_detail_report
import get_efficient_robotype
import get_efficient_roborepo_name

def pick_report_type():
    """
        Select the robot type from avaialable options.
    """
    options = { 
            "1": 'View detail report',
            "2": 'View report by RobotType',
            "3": 'View report by RobotName',
            "4": 'Summary Report',
            }
    print("select report type:")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,options[element]))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return options[i]
    except:
        pass
    return None

#Starting point for program.
if __name__ == '__main__':
    report_type = pick_report_type()  
    if report_type == "View detail report":
        obj = view_detail_report.ViewReport()
    if report_type == "View report by RobotType":
        get_efficient_robotype.gen_efficient_robo_report()
        get_efficient_robotype.gen_report()
    if report_type == "View report by RobotName":
        get_efficient_roborepo_name.gen_efficient_robo_byname_report()
        get_efficient_roborepo_name.gen_report()
    if report_type == "Summary Report":
        summary_report.gen_summary_report()

