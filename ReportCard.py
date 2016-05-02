# Classes:
#   - BlankDatabase for initilizating
#   - StudentInitialize for entering students
#   - SubjectMarksInitialize for entering subjects and marks of each student
#   - MathematicslFunctions for everything else
class BlankDatabase(object):
    def __init__(self, count_students):
        self.count_students = count_students
    def db_initialize(self):
        a = []
        for i in range(self.count_students):
            a.append([])   
        return a
        print a
        
class StudentInitialize(object):
    def __init__(self, db):
        self.db = db
    def student_input(self):
        for i in range(len(self.db)):
            self.db[i] = raw_input("Enter Names: ") 
        return self.db

class SubjectMarksInitialize(object):
    def __init__(self, student_list, num_subjects, subjects):
        self.student_list = student_list
        self.num_subjects = num_subjects
        self.subjects = subjects
    def subject_marks_input(self):
        for i in range(len(self.student_list)):
            print "You are now entering marks for %s" % self.student_list[i]
            dictionary = {}
            for j in range(self.num_subjects):
                string = ""
                string = self.subjects[j]
                print "Subject: %s" % string
                name_student = ""
                name_student = self.student_list[i]
                print "Enter %s's marks in %s" % (name_student, string)
                marks = int(raw_input("> "))
                dictionary[string] = marks
            self.student_list[i] = self.student_list[i],dictionary
        print "Let's Print the Report Card First =>"
        print self.student_list
        return self.student_list
        
class MathematicalFunctions(object):
    def __init__(self, database):
        self.database = database
    def per_student_average(self):
        avg_dict = {}
        for name,dictionary in self.database:
            total = 0
            average = 0
            count = len(dictionary.keys())
            val = dictionary.values()
            total = sum(val)
            average = total/float(count)
            avg_dict[name] = average
        return avg_dict
    def per_student_grade(self):
        grade_eval_dict = self.per_student_average()
        grade_dict = {}
        for keys in grade_eval_dict:
            if grade_eval_dict.get(keys) >= 90:
                grade_dict[keys] = 'A'
            elif grade_eval_dict.get(keys) >= 80 and grade_eval_dict.get(keys) < 90:
                grade_dict[keys] = 'B'
            elif grade_eval_dict.get(keys) >= 70 and grade_eval_dict.get(keys) < 80:
                grade_dict[keys] = 'C'
            elif grade_eval_dict.get(keys) >= 60 and grade_eval_dict.get(keys) < 70:
                grade_dict[keys] = 'D'
            else: 
                grade_dict[keys] = 'F'            
        return grade_dict
    def per_student_max_marks_in_subjects(self):
        for name,dictionary in self.database:
            marks_list = []
            max_marks_subject_list = []
            marks_list = dictionary.values()
            max_marks = max(marks_list)
            for k in dictionary:
                if dictionary.get(k) == max_marks:
                    max_marks_subject_list.append(k)
            print "%s has obtained the Maximum marks %s in Subject(s): %s" % (name, max_marks,max_marks_subject_list)
    def highest_average_marks(self):
        avg_marks_dict = self.per_student_average()
        avg_marks_list = avg_marks_dict.values()
        max_avg_marks = max(avg_marks_list)
        students_with_highest_avg_marks = []
        for name in avg_marks_dict:
            if avg_marks_dict.get(name) == max_avg_marks:
                students_with_highest_avg_marks.append(name)
        print "Highest Average marks in the class is %s and it has been obtained by student(s): %s" % (max_avg_marks,students_with_highest_avg_marks)
    def subject_toppers(self):
        x,y = self.database[0]
        subjects = y.keys()
        subject_marks_dictionary = {}
        for subject in subjects:
            marks = []
            for name,dictionary in self.database:
                marks.append(dictionary.get(subject))
            max_marks = max(marks)
            subject_marks_dictionary[subject] = max_marks
        print subject_marks_dictionary
        for subject in subject_marks_dictionary:
            k = subject
            value = subject_marks_dictionary[subject]
            for name,dictionary in self.database:
                for keys in dictionary:
                    if (keys == k) and dictionary[keys] == value:
                        print "Highest marks in %s is %s and has been obtained by %s" % (keys,value,name)
    def class_average(self):
        all_marks_list = []
        for name,dictionary in self.database:
            for keys in dictionary:
                all_marks_list.append(dictionary[keys])
        total = sum(all_marks_list)
        count_total_marks = len(all_marks_list)
        class_avg = total/float(count_total_marks)
        return class_avg,all_marks_list
    def class_variance(self):
        avg,marks_list = self.class_average()
        sum_squares = 0
        varianace = 0
        for marks in marks_list:
            diff = (marks - avg)**2 
            sum_squares = sum_squares + diff
        variance = sum_squares/float(len(marks_list))
        return variance
    def class_sd(self):
        variance = self.class_variance()
        return float(variance**0.5)
            
# All Instances of classes below
                     
num_students = int(raw_input("How many students are there in your class? ")) 
count_students = BlankDatabase(num_students)
database = count_students.db_initialize()
student_list_send = StudentInitialize(database)
student_list = student_list_send.student_input()
print student_list
num_subjects = int(raw_input("How many subjects does each student study? "))
subjects = []
for i in range(num_subjects):
    name_subjects = raw_input("Name the subjects: ")
    subjects.append(name_subjects)
print subjects
base_initialize = SubjectMarksInitialize(student_list, num_subjects, subjects)
list_class = base_initialize.subject_marks_input()
calculations = MathematicalFunctions(list_class)
print "Let's Print the Average marks of each student now =>"
print calculations.per_student_average()
print "Let's Print the Grades for each student now =>"
print """
Grade Card:
A = 90-100
B = 80-90
C = 70-80
D = 60-70
F = less than 60     
"""
print calculations.per_student_grade()
print "\n"
calculations.per_student_max_marks_in_subjects()
print "Let's now print some Statistical Calculations to see where the Class Stands =>"
calculations.highest_average_marks()
print "Let's now print the maximum marks in each subject:"
calculations.subject_toppers()
print "Let's now print the class average => ",
class_avg,marks_list_all = calculations.class_average()
print class_avg
var = calculations.class_variance()
print "Class Variance: %s" % var
print "Class Standard Deviation: %s" % (calculations.class_sd())
