grade = input("请输入成绩: ")
grade = int(grade)
if grade<60 :
    print("成绩不及格")
elif grade >= 60 and grade <=74 :
    print("成绩为合格")
elif grade >=75 and grade <=89:
    print("成绩为良好")
else :
    print("成绩为优秀")
