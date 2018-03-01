Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [12,3,45,6,8,15,34,'Hi','Hello',10.5,True]
>>> list_1[0]
12
>>> list_1[6]
34
>>> len(list_1)
11
>>> list_1[-1]
True
>>> list_1[0:5]
[12, 3, 45, 6, 8]
>>> list_1[:]
[12, 3, 45, 6, 8, 15, 34, 'Hi', 'Hello', 10.5, True]
>>> list_1[0:]
[12, 3, 45, 6, 8, 15, 34, 'Hi', 'Hello', 10.5, True]
>>> list
<class 'list'>
_
>>> list_1[:100]
[12, 3, 45, 6, 8, 15, 34, 'Hi', 'Hello', 10.5, True]
>>> even = []
>>> even.append(2)
>>> even.append(4)
>>> even
[2, 4]
>>> even = []
>>> for i in range(2,51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even = []
>>> even = [i for i in range(2,51)]
>>> even
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> even = [i for i in range(2,51) if i % 2 == 0]
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> for i in even:
	print(i)

	
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
>>> emp_age = [25,27,34,31,22,28,32,29]
>>> emp_name = ['Ram','Shyam','Amit','Ravi','Mohan','Ajay', 'Rohan', 'Dhruv']
>>> sorted(emp_age)
[22, 25, 27, 28, 29, 31, 32, 34]
>>> sorted(emp_age, reverse = True)
[34, 32, 31, 29, 28, 27, 25, 22]
>>> 'Ravi' in emp_name
True
>>> emp_name[-1]
'Dhruv'
>>> import os
>>> os.system('notepad')
0
>>> os.startfile('dhoni.mp4')
>>> import sys
>>> emp_age
[25, 27, 34, 31, 22, 28, 32, 29]
>>> sys.getsizeof(emp_name)
128
>>> os.system('notepad')
0
>>> emp_age = (25,27,34,31,22,28,32,29)
>>> type(emp_age)
<class 'tuple'>
>>> emp_age[2]
34
>>> emp_age[0:5]
(25, 27, 34, 31, 22)
>>> emp_age[0] = 45
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    emp_age[0] = 45
TypeError: 'tuple' object does not support item assignment
>>> emp_data = name, age, salary = 'Ram', 28, 20000
>>> emp_data
('Ram', 28, 20000)
>>> name
'Ram'
>>> age
28
>>> names = 'Ram', 'Shyam', 'Gopal'
>>> names
('Ram', 'Shyam', 'Gopal')
>>> emp_data = {'name':}
SyntaxError: invalid syntax
>>> emp_data = {'name':'Ram', 'age':27, 'salary':25000}
>>> emp_data[0]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    emp_data[0]
KeyError: 0
>>> emp_data['name']
'Ram'
>>> emp_data.keys()
dict_keys(['name', 'age', 'salary'])
>>> emp_data.values()
dict_values(['Ram', 27, 25000])
>>> emp_data.items()
dict_items([('name', 'Ram'), ('age', 27), ('salary', 25000)])
>>> emp_data['company'] = 'TCS'
>>> emp_data
{'name': 'Ram', 'age': 27, 'salary': 25000, 'company': 'TCS'}
>>> x = {23,45,67,12,25,33,7}
>>> set_1 = {23,45,67,12,25,33,7}
>>> set_2 = {3,54,7,12,25,13,17}
>>> set_1 & set_2
{25, 12, 7}
>>> set_1 | set_2
{33, 67, 3, 7, 12, 45, 13, 17, 54, 23, 25}
>>> set_1.intersection(set_2)
{25, 12, 7}
>>> 
