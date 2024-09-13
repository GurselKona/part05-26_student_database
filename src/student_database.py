def add_student(students:dict, name:str): 

    students[name] = []


def add_course(students:dict, name:str, course:tuple):
    find = 0
    if course[1] == 0:
        return
    if students[name] == []:
        students[name].append(course)
    if students[name] != []:
        for v in students[name]:
            if v[0].lower() != course[0].lower():
                find += find
            else:
                find += 1
        if find == 0:
            students[name].append(course)
        for v in students[name]:
            if v[0].lower() == course[0].lower() and course[1] > students[name][students[name].index(v)][1]:
                students[name][students[name].index(v)] = course
        
        


def print_student(students:dict, name:str):
        
    message = ""
    if name in students:
        message += f"\n{name}:"
        if students[name] == []:
            message += "\n no completed courses"
        else:
            message += f"\n {len(students[name])} completed courses:"
            total = 0
            for course in students[name]:
                message += f"\n  {course[0]} {course[1]}"
                total += course[1]
            message += f"\n average grade {total/len(students[name])}"
    else:
        message += f"\n{name}: no such person in the database"
    print(message)
    

def summary(students:dict):

    message = ""
    num_of_students = len(students)
    message = f"\nstudents {num_of_students}"
    max_no_of_courses = 0
    best_average_grade = 0
    for name, course in students.items():
        if len(course) > max_no_of_courses: 
            max_no_of_courses = len(course)
            max_student = name
        total = 0
        for c in course:
            total += c[1]
        average_grade = total/len(course)
        if average_grade > best_average_grade:
            best_average_grade = average_grade
            best_student = name
        
    message += f"\nmost courses completed {max_no_of_courses} {max_student}"
    message += f"\nbest average grade {best_average_grade} {best_student}"
    print(message)



if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    print_student(students,"Peter")
    print_student(students,"Eliza")