pusty_zbior = set()

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#A = set([1, 2, 3, 4])
#B = set([3, 4, 5, 6])

print(A | B)
print(A & B) # część wspólna
print(A - B)
print(B - A)
print(A ^ B)

#print(dir(A))

#['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# #'__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
# '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', #
# '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', #
# 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

thisset = {"apple", "banana", "cherry", "apple"} #nie może mieć duplikatów

print(thisset)