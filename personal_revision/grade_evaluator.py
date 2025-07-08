student_name = input("what is your name ?: ")
print("Enter your scores for the following : ")
subject_1 = int(input("Enter the score :  "))
subject_2 = int(input("Enter the score :  "))
subject_3 = int(input("Enter the score :  "))

average = subject_1 + subject_2 + subject_3
average_score = average/3

if average_score >= 90 :
    GRADE = "A"
elif average_score >= 80:
    GRADE = "B"
elif average_score >=  70:
    GRADE = "C"
elif average_score >= 60:
    GRADE = "D"
else :
    GRADE = "F"


print("\n 📘Student Grade Report")
print("-----------------------")
print(f"Name : {student_name}")
print(f"Average Score  : {average_score}")
print(f"Grade  : {GRADE}")