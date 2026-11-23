# Writing to a file

note =  "I am learning Python file handling!"

with open("learning_notes.md", "w") as file:
    file.write(note)

print("Note saved successfully!")

# Reading from a file

with open("learning_notes.md", "r") as file:
    content = file.read()

print("File content:", content)

# Appending to a file

with open("learning_notes.md", "a") as file:
    file.write("\nI am also learning Git and GitHub!")

print("New note added!")

# Reading the updated file

with open("learning_notes.md", "r") as file:
    updated_content = file.read()

print("Updated file content:")
print(updated_content)
