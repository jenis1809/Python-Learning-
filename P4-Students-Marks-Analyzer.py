marks = []
n = int(input("Enter the number of subjects: "))
for i in range(n):
    mark = float(input("Enter the mark for subject " + str(i+1) + ":"))
    marks.append(mark)
def average():
    return sum(marks) / len(marks)
print("The average is:", average())
print("The highest marks is:", max(marks))
print("The lowest marks is:", min(marks))