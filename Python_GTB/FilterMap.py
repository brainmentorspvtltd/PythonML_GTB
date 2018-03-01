Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def temp_conv(c):
	return 9/5 * c + 32

>>> temp = [33.4,35.5,32.1,29.8,28.7]
>>> for t in temp:
	temp_conv(t)

	
92.12
95.9
89.78
85.64
83.66
>>> list(map(lambda c : 9/5 * c + 32, [33.4,35.5,32.1,29.8,28.7]))
[92.12, 95.9, 89.78, 85.64, 83.66]
>>> map(temp_conv, temp)
<map object at 0x000002015ADA1BE0>
>>> list(map(temp_conv, temp))
[92.12, 95.9, 89.78, 85.64, 83.66]
>>> list(map(lambda c : 9/5 * c + 32, [33.4,35.5,32.1,29.8,28.7]))
[92.12, 95.9, 89.78, 85.64, 83.66]
>>> data
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> def even_num(num):
	return num % 2 == 0

>>> even_num(23)
False
>>> even_num(12)
True
>>> numbers = [i for i in range(2,51)]
>>> list(map(even_num, numbers))
[True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
>>> list(filter(even_num, numbers))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even = []
>>> def filter_1(num):
	if num % 2 == 0:
		even.append(num)

		
>>> for n in numbers:
	filter_1(n)

	
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> 
