def creating_file (file_name):
    import datetime
    x = datetime.datetime.now()
    with open(file_name,"w") as f:
        f.write(f"FILE CREATED[{x}]"'\n')
    return
file_name=input("Enter File Name (with .txt)")

creating_file(file_name)

from colorama import Fore, Back, Style

def display_school_name (school_name):
    massage1=print(Fore.BLACK,
     Back.BLUE,
     Style.BRIGHT,
     school_name.center(110),
     Style.RESET_ALL)
    with open(file_name, "a") as f:
        f.write(school_name.center(110))
        f.write('\n')
    return massage1

display_massage1=display_school_name('ABC SCHOOL')

def TitleOnPaper (title):
    massage2=print(Fore.BLACK,
     Back.BLUE,
     Style.BRIGHT,
     title.center(110),
     Style.RESET_ALL)
    with open(file_name, "a") as f:
        f.write(title.center(110))
        f.write('\n')
    return massage2

display_massage2=TitleOnPaper('Student Result Card')

def take_inputs ():
    student_name=input('\n'"Enter the Student Name:"'\t\t\t\t')
    with open(file_name, "a") as f:
        f.write('\n'"Enter the Student Name:"'\t\t\t\t')
        f.write(student_name)
        f.write('\n')
    sub1=float(input('\n'"Enter the marks of Subject 1:"'\t\t\t'))
    with open(file_name, "a") as f:
        f.write('\n'"Enter the marks of Subject 1:"'\t\t\t\t')
        f.write(str(sub1))
        f.write('\n')
    sub2=float(input('\n'"Enter the marks of Subject 2:"'\t\t\t'))
    with open(file_name, "a") as f:
        f.write('\n'"Enter the marks of Subject 2:"'\t\t\t\t')
        f.write(str(sub2))
        f.write('\n')
    sub3=float(input('\n'"Enter the marks of Subject 3:"'\t\t\t'))
    with open(file_name, "a") as f:
        f.write('\n'"Enter the marks of Subject 3:"'\t\t\t\t')
        f.write(str(sub3))
        f.write('\n')
    sub4=float(input('\n'"Enter the marks of Subject 4:"'\t\t\t'))
    with open(file_name, "a") as f:
        f.write('\n'"Enter the marks of Subject 4:"'\t\t\t\t')
        f.write(str(sub4))
        f.write('\n')
    sub5=float(input('\n'"Enter the marks of Subject 5:"'\t\t\t'))
    with open(file_name, "a") as f:
        f.write('\n'"Enter the marks of Subject 5:"'\t\t\t\t')
        f.write(str(sub5))
        f.write('\n')
    sub6=float(input('\n'"Enter the marks of Subject 6:"'\t\t\t'))
    with open(file_name, "a") as f:
        f.write('\n'"Enter the marks of Subject 6:"'\t\t\t\t')
        f.write(str(sub6))
        f.write('\n')
    print('\n')
    return sub1,sub2,sub3,sub4,sub5,sub6

sub1,sub2,sub3,sub4,sub5,sub6=take_inputs()

def display_subj_massage (sub1,sub2,sub3,sub4,sub5,sub6):
    if sub1<50.0:
        print(Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         f"You have FAILED in Suject 1 with obtain marks:{sub1}",
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'f"You have FAILED in Suject 1 with obtain marks:{sub1}")
            f.write('\n')
    if sub2<50.0:
        print(Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         f"You have FAILED in Suject 2 with obtain marks:{sub2}",
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'f"You have FAILED in Suject 2 with obtain marks:{sub2}")
            f.write('\n')
    if sub3<50.0:
        print(Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         f"You have FAILED in Suject 3 with obtain marks:{sub3}",
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'f"You have FAILED in Suject 3 with obtain marks:{sub3}")
            f.write('\n')
    if sub4<50.0:
        print(Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         f"You have FAILED in Suject 4 with obtain marks:{sub4}",
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'f"You have FAILED in Suject 4 with obtain marks:{sub4}")
            f.write('\n')
    if sub5<50.0:
        print(Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         f"You have FAILED in Suject 5 with obtain marks:{sub5}",
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'f"You have FAILED in Suject 5 with obtain marks:{sub5}")
            f.write('\n')
    if sub6<50.0:
        print(Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         f"You have FAILED in Suject 6 with obtain marks:{sub6}",
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'f"You have FAILED in Suject 6 with obtain marks:{sub6}")
            f.write('\n')
    if sub1>50.0 and sub2>50.0 and sub3>50.0 and sub4>50.0 and sub5>50.0 and sub6>50.0:
        print(Fore.BLACK,
         Back.GREEN,
         Style.BRIGHT,
         "You have Passed all the subjects".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write('\n'"You have Passed all the subjects")
            f.write('\n')
    return

display_subj_massage(sub1,sub2,sub3,sub4,sub5,sub6)

def calculations (sub1,sub2,sub3,sub4,sub5,sub6):
    total_marks=sub1+sub2+sub3+sub4+sub5+sub6
    print('\n'f"TOTAL MARKS: {total_marks}")
    with open(file_name, "a") as f:
        f.write('\n'f"TOTAL MARKS: {total_marks}"'\n')
    per=round((total_marks/600)*100,2)
    print(f"PERCENTAGE: {per}")
    with open(file_name, "a") as f:
        f.write(f"PERCENTAGE: {per}"'\n')
    return total_marks,per

total_marks,per=calculations(sub1,sub2,sub3,sub4,sub5,sub6)

def grading ():
    if per>=90.0:
        print('\n',Fore.BLACK,
         Back.GREEN,
         Style.BRIGHT,
         "Grade: A+".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write("Grade: A+")
    elif 80.0<per<90.0:
        print('\n',Fore.BLACK,
         Back.LIGHTGREEN_EX,
         Style.BRIGHT,
         "Grade: A".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write("Grade: A")
    elif 70.0<per<80.0:
        print('\n',Fore.BLACK,
         Back.YELLOW,
         Style.BRIGHT,
         "Grade: B".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write("Grade: B")
    elif 60.0<per<70.0:
        print('\n',Fore.BLACK,
         Back.CYAN,
         Style.BRIGHT,
         "Grade: C".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write("Grade: C")
    elif 50.0<per<60.0:
        print('\n',Fore.BLACK,
         Back.MAGENTA,
         Style.BRIGHT,
         "Grade: D".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write("Grade: D")
    else:
        print('\n',
          Fore.BLACK,
         Back.RED,
         Style.BRIGHT,
         "FAILED".center(110),
         Style.RESET_ALL)
        with open(file_name, "a") as f:
            f.write("FAILED")
    return

grading ()

input()
