Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:/Users/asus/Desktop/Python_GTB/01-PythonBasic.py ========
Addition is 27
>>> 
======== RESTART: C:/Users/asus/Desktop/Python_GTB/02-PythonInput.py ========
Enter first number : 2
Enter second number : 5
Result is 25
>>> 
======== RESTART: C:/Users/asus/Desktop/Python_GTB/02-PythonInput.py ========
Enter first number : 12
Enter second number : 4
Result is 16
>>> 
========== RESTART: C:/Users/asus/Desktop/Python_GTB/03-ForLoop.py ==========
Value of i 5
Inside For loop
Value of i 6
Inside For loop
Value of i 7
Inside For loop
Value of i 8
Inside For loop
Value of i 9
Inside For loop
Value of i 10
Inside For loop
Value of i 11
Inside For loop
Outside for loop
>>> for i in range(0,6)
SyntaxError: invalid syntax
>>> for i in range(0,6):
	print('*' * i)

	

*
**
***
****
*****
>>> for i in range(0,10):
	print(' ' * (10-i) + '*' * (2*i + 1))

	
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
>>> 
