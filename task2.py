students = {}


class Student_Management:
      def __init__(self, students) -> None:
        self.students = students

      def register_student(self, name, id):
          details = {"name" : name, "grades": []}
          self.students[str(id)] = details
          return f"New student {name} registered"
      
      def record_grade(self, id, *grade):
          for i in grade:
            self.students[id]["grades"].append(i)
          return f'Grade recorded for {students[id]["name"]}'
          
      def calculate_average_grade(self, id):
          average = 0
          grades = self.students[id]["grades"]
          if grades:
            for i in grades:
              average += i
            return round(average/(len(grades)),2)
          else:
             return average
      
      def find_top_student(self):
          top_average = 0
          count = 0
          top_students = []
          for i in self.students:
            average = self.calculate_average_grade(i)
            if average > top_average:
                top_average = average
          for i in self.students:
            average = self.calculate_average_grade(i)
            if average == top_average:
                count += 1
                top_students.append(i)
          if count == 1:
                return f'The top student is {"".join([self.students[i]["name"] for i in top_students])} with average grade: {top_average}'
          else:
               top_students = [self.students[i]["name"] for i in top_students]
               return f'The top students are {", ".join(top_students[0:-1])} and {top_students[-1]} with average grade: {top_average}'
          
      def list_all_students(self):
          list = []
          for i in self.students:
              list.append(f"name: {self.students[i]["name"]} ID: {i} grades: {",".join((str(i) for i in self.students[i]["grades"]))}")          
          return "\n".join(list)

admin = Student_Management(students)

print(admin.register_student("John",1))
print(admin.register_student("Favour",2))
print(admin.register_student("Godswill",3))
print(admin.record_grade("1",70,80,10,15))
print(admin.record_grade("2",80,100,90,2))
print(admin.record_grade("3",90,100,10,40))

print(admin.find_top_student())
print(admin.list_all_students())