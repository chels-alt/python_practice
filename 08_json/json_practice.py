import json

person = {
    "name": "Chelsiya",
    "age": 25,
    "role": "Python Developer",
    "skills": ["Python", "Git", "GitHub"]
}    

json_data = json.dumps(person, indent=4)

print(json_data) 