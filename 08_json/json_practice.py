import json

person = {
    "name": "Chelsiya",
    "age": 25,
    "role": "Python Developer",
    "skills": ["Python", "Git", "GitHub"]
}    

json_data = json.dumps(person, indent=4)

print(json_data) 

# Convert JSON string back to Python

person_data = json.loads(json_data)

print("Name:", person_data["name"])
print("Role:", person_data["role"])
print("Skills:", person_data["skills"]) 

# Write Python data into a JSON file

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

print("JSON file created successfully!")


# Read JSON data from a file

with open("person.json", "r") as file:
    saved_person = json.load(file)

print("Saved name:", saved_person["name"])
print("Saved age:", saved_person["age"])
print("Saved skills:", saved_person["skills"])    