#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   This Module for to generate details reports according to task.
"""

import csv
import config

class ViewReport:
    def __init__(self):
        """
        """
        self.gen_report()

    def pad_col(self, col, max_width):
        return col.ljust(max_width)

    def gen_report(self):
        """
            This function generate report.
        """
        with open(config.details_report_path) as csvfile:
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
                to_print += self.pad_col(col, max_col_width[idx]) + " | "
            print("-"*len(to_print))
            print(to_print)

if __name__ == '__main__':
    obj = ViewReport()  
