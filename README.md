6001x
=====

code notebooks for edx mooc 6.001x

### how to travel around files and directories in python
>>> import os

>>> os.getcwd()
'/home/ubuntu'

###get access to a sub-directory
>>> os.chdir('Github')

>>> os.getcwd()
'/home/ubuntu/Github'

>>> os.listdir(os.curdir)
['machine_learning', 'Quantmod', 'datasci_course_materials']
###get access to a sub-directory
>>> os.chdir('machine_learning')
###list all files in the current directory
>>> os.listdir(os.curdir)
['README.md', 'week3', '.git', 'week4', 'week2']
### get the current directory
>>> os.getcwd()
'/home/ubuntu/Github/machine_learning'
