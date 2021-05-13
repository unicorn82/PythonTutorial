import json

json1 = { "firstName": "Eason", "lastName": "Y", "hobbies": ["reading", "hiking", "game"], "age": 40}

jsonObj1 = json.dumps(json1)

jsonObj2 = json.dumps(json1, indent=4, separators=(', ', '= ' ), sort_keys=True)
print(jsonObj2)

with open('example2.json', 'w') as file:
    json.dump(json1, file, indent=4)

json2 = json.loads(jsonObj1)
print(json2)

with open('example1.json', 'r') as file:
    jsonObj3 = json.load(file)
    print(jsonObj3)

#Dump a class to json
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_student(obj):
    if isinstance(obj, Student):
        return {"name": obj.name, "age":obj.age, obj.__class__.__name__:True}
    else:
        raise TypeError("This is not a student")

student1 = Student("Eason", 29)
print(student1.name)
student_json = json.dumps(student1, default=encode_student)
print(student_json)

#Solution2
from json import JSONEncoder

class StudentEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self,obj)

student_json2 = json.dumps(student1, cls=StudentEncoder)
print(student_json2)
student_json3 = StudentEncoder().encode(student1)
print(student_json3)

student2 = json.loads(student_json3)
print(student2)
print(type(student2))
# print(student2.name) AttributeError: 'dict' object has no attribute 'name'

#dict -> Student()
def decode_Student(dict):
    if Student.__name__ in dict:
        return Student(name=dict['name'], age=dict['age'])
    return dict
student3 = json.loads(student_json3, object_hook=decode_Student)
print(type(student3))
print(student3.name)

