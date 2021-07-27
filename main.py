#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   This Module for to select robot assign work to robot.
"""


import os
import config
import csv
import random
import time
import sys


class Main:  
      
    # init method or constructor   
    def __init__(self, name):  
        self.name = name 
        self.get_input_from_user()
        self.final_dict = {
            "roboname" : self.roboname,
            "robotype" : self.robotype,
            "task": []
        }
        self.assign_task_to_robot(self.roboname, self.robotype)


    def pick_robot_type(self):
        """
            Select the robot type from avaialable options.
        """
        options = { 
                "1": 'Unipedal',
                "2": 'Bipedal',
                "3": 'Quadrupedal',
                "4": 'Arachnid',
                "5": 'Radial',
                "6": 'Aeronautical'
                }
        print("select robot type:")
        for idx, element in enumerate(options):
            print("{}) {}".format(idx+1,options[element]))
        i = input("Enter number: ")
        try:
            if 0 < int(i) <= len(options):
                return options[i]
        except:
            pass
        return None

    def assign_task_to_robot(self, roboname, robotype):
        """
            This function is for assign the Robot a set of five tasks.
        """
        #check robotask is already executed or 
        task_lst = []
        task_lst.append(roboname)
        task_lst.append(robotype)
        #task_lst.append([random.sample(config.robo_task_list, 5)])
        task_rec = random.sample(config.robo_task_list, 5)
        five_task = ",".join(task_rec)
        task_lst.append(five_task)
        task_record = ",".join(task_lst)
        self.execute_task(roboname, robotype, task_rec)
            
    def task_exec_in_eta(self, roboname, robotype, task, eta):
        """
            This function execute the task in given ETA.
            After execution the task remove from the Queue.
        """
        seconds=int((eta/1000)%60)
        print("\r")
        bar_length = 30  # should be less than 100
        for i in range(seconds+1):
            percent = 100.0*i/seconds
            sys.stdout.write('\r')
            sys.stdout.write('Roboname "{}({})" Executing Task "{}" '.format(roboname.upper(), robotype, task.upper()))
            sys.stdout.write("[{:{}}] {:>3}% Completed"
                            .format('='*int(percent/(100.0/bar_length)),
                                    bar_length, int(percent)))
            sys.stdout.flush()
            time.sleep(0.002)

    def execute_task(self, roboname, robotype, task_rec):
        """
            This function execute the task.
            @roboname : Robot name
            @robotype : Robot type
        """
        #self.assign_task_to_robot(roboname, robotype)
        filename = config.details_report_path
        file_exists = os.path.isfile(filename)
        op_task_list = []
        fields = ['Robot Name', 'Type', 'Task', 'ETA(ms)', 'Status'] 
        for task in task_rec:
            status_list = []
            task_eta = config.robo_task_dict_with_eta[task]
            self.task_exec_in_eta(roboname, robotype, task, task_eta)
            status_list.append(roboname)
            status_list.append(robotype)
            status_list.append(task)            
            status_list.append(task_eta)
            status_list.append("Completed")
            op_task_list.append(status_list)
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            if not file_exists:
                csvwriter.writerow(fields)
            csvwriter.writerows(op_task_list)
        return None


    def get_input_from_user(self) :
        """
            This function read the input from user.
        """
        self.roboname = input("Enter robot name:")
        self.robotype = self.pick_robot_type()
        #self.execute_task(self.roboname, self.robotype)

    # Main Method   
    def main(self):
        self.get_input_from_user()  
  
#Starting point for program.
if __name__ == '__main__':
    obj = Main("Niket")  
    #obj.main()
  
    