# -*- coding: utf-8 -*-
"""
@author: pawel@kasprowski.pl
"""

print("hello world")

# Import całego modułu
import module0
print(module0.mult(2,'3'))

# Import konkretnej funkcji
from module0 import mult
print(mult(10,20))


