# ধরো grading policy:
# Marks           Grade
# 90-100          A+
# 80-89           A
# 70-79           B
# 60-69           C
# 33-59           D
# 0-32            Fail


marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("Fail")
