#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   This is a config module for configuration.
"""

# Tasks for robot
robo_tasks = [
  {
    "description": 'do the dishes',
    "eta": 1000,
  },{
    "description": 'sweep the house',
    "eta": 3000,
  },{
    "description": 'do the laundry',
    "eta": 10000,
  },{
    "description": 'take out the recycling',
    "eta": 4000,
  },{
    "description": 'make a sammich',
    "eta": 7000,
  },{
    "description": 'mow the lawn',
    "eta": 20000,
  },{
    "description": 'rake the leaves',
    "eta": 18000,
  },{
    "description": 'give the dog a bath',
    "eta": 14500,
  },{
    "description": 'bake some cookies',
    "eta": 8000,
  },{
    "description": 'wash the car',
    "eta": 20000,
  },
]

robo_task_dict_with_eta = { 
                "do the dishes": 1000,
                "sweep the house": 3000,
                "do the laundry": 10000,
                "take out the recycling": 4000,
                "make a sammich": 7000,
                "mow the lawn": 20000,
                "rake the leaves":  18000,
                "give the dog a bath":  14500,
                "bake some cookies":  8000,
                "wash the car": 20000
                }

robo_task_list = ["do the dishes",
                "sweep the house",
                "do the laundry",
                "take out the recycling",
                "make a sammich",
                "mow the lawn",
                "rake the leaves",
                "give the dog a bath",
                "bake some cookies",
                "wash the car"

]

details_report_path = "./reports/detail_task_records.csv"
robot_type_report_path = "./reports/robot_type.csv"
robot_name_report_path = "./reports/robot_name.csv"
        