Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;
>>> print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3)and (7<4)or (18==3))and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> False in "
SyntaxError: EOL while scanning string literal
>>> False is 'False'
False
>>> ((True==False)or (False>True))and(False<=True)
False
>>> s1="Nice to have it"
>>> s2="here"
>>> print(s1 +s2)
Nice to have ithere
>>> print(s1 + s2)
Nice to have ithere
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> a.insert(0,s1)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.insert(24,s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> number=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
>>> color_list_1=set(["White","Black","Red"])
>>> color_list_2=set(["Red","Green"])
>>> color_list_3=color_list_1.remove(2)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    color_list_3=color_list_1.remove(2)
KeyError: 2
>>> color_list_1.difference(color_list_2)
{'Black', 'White'}
>>> n=5
>>> n+nn+nn
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    n+nn+nn
NameError: name 'nn' is not defined
>>> n=5
>>> nn=((n*10)+n)
>>> nnn=((n*100)+(n*10)+n)
>>> print(n+nn+nnn)
615
>>> 