# robotproject

**Project structure.**

1. reports :- Folder for reports generation
2. config file
3.  get_efficient_roborepo_name
4.  get_efficient_robotype
5.  main
6.  summary_report
7.  view_detail_report
8.  view_report

**How to Run the project:**
1. Run python main.py

**C:\Users\A740479\Desktop\python_project>python main.py**


Enter robot name:Niket
select robot type:
1) Unipedal
2) Bipedal
3) Quadrupedal
4) Arachnid
5) Radial
6) Aeronautical


Enter number: 3

Roboname "NIKET(Quadrupedal)" Executing Task "MAKE A SAMMICH" [==============================] 100% Completed

Roboname "NIKET(Quadrupedal)" Executing Task "RAKE THE LEAVES" [==============================] 100% Completed

Roboname "NIKET(Quadrupedal)" Executing Task "GIVE THE DOG A BATH" [==============================] 100% Completed

Roboname "NIKET(Quadrupedal)" Executing Task "BAKE SOME COOKIES" [==============================] 100% Completed

Roboname "NIKET(Quadrupedal)" Executing Task "SWEEP THE HOUSE" [==============================] 100% Completed


**2. Run reports �**

**C:\Users\A740479\Desktop\python_project>python view_report.py**

select report type:
1) View detail report
2) View report by RobotType
3) View report by RobotName
4) Summary Report


Enter number: 1
-----------------------------------------------------------------------
Robot Name | Type        | Task                | ETA(ms) | Status    |


-----------------------------------------------------------------------
Niket      | Quadrupedal | make a sammich      | 7000    | Completed |


-----------------------------------------------------------------------
Niket      | Quadrupedal | rake the leaves     | 18000   | Completed |


-----------------------------------------------------------------------
Niket      | Quadrupedal | give the dog a bath | 14500   | Completed |


-----------------------------------------------------------------------
Niket      | Quadrupedal | bake some cookies   | 8000    | Completed |


-----------------------------------------------------------------------
Niket      | Quadrupedal | sweep the house     | 3000    | Completed |


**C:\Users\A740479\Desktop\python_project>python view_report.py**

select report type:
1) View detail report
2) View report by RobotType
3) View report by RobotName
4) Summary Report


Enter number: 2
-------------------------------
Robot Type  | Executed count |


-------------------------------
Quadrupedal | 5              |


**C:\Users\A740479\Desktop\python_project>python view_report.py**


select report type:
1) View detail report
2) View report by RobotType
3) View report by RobotName
4) Summary Report


Enter number: 3
------------------------------
Robot Name | Executed count |


------------------------------
Niket      | 5              |

**C:\Users\A740479\Desktop\python_project>python view_report.py**


select report type:
1) View detail report
2) View report by RobotType
3) View report by RobotName
4) Summary Report


Enter number: 4


***********************************************************
*******************Summary Report**************************
***********************************************************

*******************Robot Type Selected**********************
Quadrupedal
************************************************************

*******************Robot Users Selected**********************
Niket
************************************************************


*******************Total Execution time for tasks(ms)*******
50500
************************************************************

**Reports populated Under Reports folder:-**

We can view this data in CSV format too.

detail_task_records.csv

robot_name.csv

robot_type.csv




