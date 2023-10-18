class StudentManagement:
    
    def __init__(self):
        self.students = {}
        self.next_matriculation_number = 1
    
    def enroll_student(self, first_name, surname):
        if len(self.students) >= 999:
            return -1  # no more matriculation numbers available
        number = None
        for i in range(1, 1000):
            if i not in self.students:
                number = i
                break
        self.students[number] = {'first_name': first_name, 'surname': surname, 'courses': {}}
        return number
    
    def disenroll_student(self, number):
        if number in self.students:
            del self.students[number]
            return True
        else:
            return False

    
    def take_exam(self, number, courseID, grade):
        if number not in self.students:
            return print("Student not enrolled ")
        student = self.students[number]
        if courseID not in student['courses']:
            student['courses'][courseID] = {'grade': None, 'attempts': 0}
        course = student['courses'][courseID]
        if course['grade'] is not None and course['grade'] < 5.0:
            return print("Course already passed with grade", course['grade'], "and attempts", course['attempts'])
        course['attempts'] += 1
        if course['grade'] is None or grade < 5.0:
            course['grade'] = grade
        if course['attempts'] > 3:
            self.disenroll_student(number) # exmatriculate the student 
            return print("More than 3 attempts are not allowed !!!")
        if course['attempts'] == 3 and course['grade'] == 5.0:
            self.disenroll_student(number) # exmatriculate the student 
            return print("Student failed in three attempts !!!")
        return print("Course added")


    
    def get_student(self, number):
        if number not in self.students:
            return []
        student = self.students[number]
        result = [student['first_name'], student['surname'], str(number)]
        for courseID, course_data in student['courses'].items():
            course_str = f"{courseID} {course_data['grade']} {course_data['attempts']}"
            result.append(course_str)
        return result
