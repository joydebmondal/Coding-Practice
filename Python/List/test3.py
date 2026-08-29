# a=[10,20,30], b=a → b[0]=100 এর Output Predict করো।
# a = [10, 20, 30]
# b = a
# b[0] = 100
# print(a)
# print(b)

# copy() ব্যবহার করে Independent Copy তৈরি করো।
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)

# Nested List Copy করে দেখো কেন Original পরিবর্তন হয়।
import copy
a = [
    [10, 20],
    [30, 40],
    [50, 60]
]
# b = a.copy()
# b[0][0] = [70, 80]
# print(a)
# print(b)

# deepcopy() ব্যবহার করে Problem Solve করো।
b = copy.deepcopy(a)
b[0][0] = [70, 80]
print(a)
print(b)
# == এবং is এর Difference Demonstrate করো।
print(a == b)
print(a is b)

# id() ব্যবহার করে Memory Compare করো।
print(id(a))
print(id(b))