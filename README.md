# Mod6
Mod 6
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
>>> from Thomas import*
>>> from TF import*
>>> r1 = create_rectangle(10,20,30,40)
>>> print(str_rectangle(r1))
(10, 20, 30, 40)
>>> shift_rectangle(r1,-10,-20)
>>> print(str_rectangle(r1))
(0, 0, 30, 40)
>>> r2 = offset_rectangle(r1,100,100)
>>> print(str_rectangle(r1))
(0, 0, 30, 40)
>>> print(str_rectangle(r2))
(100, 100, 30, 40)
>>>
