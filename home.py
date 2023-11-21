dog = {}
dog["name"] = "баклашка"
dog["color"] = "кара" 
dog["legs"] = 4
dog["age"] = 2
student = {} 
student["first_name"] = "Бекежан " 
student["last_name"] = "Бека"
student["gender"] = "Бека" 
student["age"] = 17
student["marital status"] = "Single"
student["skills"] = ["programming", "problem solving"]
student["country"] = "kaz" 
student["city"] = "Almatu" 
student["address"] = "jomart 7l 71home"
len(student)
skills_data_type = type(student["skills"])
student["skills"].append("teamwork") 
student["skills"].extend(["communication", "leadership"])
keys_list = list(student.keys())
values_list = list(student.values())
student_list = list(student.items())
del student["marital status"]