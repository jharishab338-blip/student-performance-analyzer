students=[]
n=int(input("enter no of student"))
for j in range(n):
    student={}
    student['name']=input("enter your name")
    student['marks']={}
    subjects=['physics','chemistry','maths']
    for sub in subjects:
        while True:
            try:
                score=int(input(f"enter your {sub} marks",))
                if  0<=score<=100:
                    student['marks'][sub]=score
                    break
                else:
                    print("invalid input try to enter the number between 0 to 100")
            except ValueError:
                print("invalid input! please enter a number")
    students.append(student)
        

def total_calculate(marks):
    total_marks=0
    for sub,sco in marks.items():
        total_marks+=sco
    return total_marks

def calculate_average(marks):
    if len(marks)==0:
        return 0
    else:
        result=total_calculate(marks)
        avg=result/len(marks)
        return avg


def get_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return"D"
    else:
        return "F"

class_total=0
  

for student in students:
    print("\n===== STUDENT REPORT =====")
    print(f"Name: {student['name']}")

    marks = student['marks']
    for sub, score in marks.items():
        print(f"Subject: {sub}, Score: {score}")

    avg = calculate_average(marks)
    class_total+=avg
    print(f"Average: {avg:.2f}")

    grade = get_grade(avg)
    print(f"Grade: {grade}")

    highest = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)

    print(f"Highest: {highest} - {marks[highest]}")
    print(f"Lowest: {lowest} - {marks[lowest]}")
if n>0:
    class_avg=class_total/n
    print("class average",class_avg) 
else:
    print("no student enter")   
    