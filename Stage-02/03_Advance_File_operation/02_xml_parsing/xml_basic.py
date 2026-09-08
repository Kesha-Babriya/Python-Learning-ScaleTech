import xml.etree.ElementTree as et

# Load students.xml.
tree = et.parse("students.xml")

# Get the root element

root = tree.getroot()
print(root)
print(root.tag)

# Print the total number of students and details of them

total_student = 0
for _ in root.iter("student"):
    total_student += 1

print("Total students", total_student)

for student in root.iter("student"):
    id = student.get("id")
    name = student.find("name").text
    branch = student.findtext("branch")
    year = int(student.findtext("year"))
    marks = int(student.findtext("marks"))
    skills = [skill.text for skill in student.find("skills").findall("skill")]
    print(id ,name ,branch ,year ,marks ,"Skills : ",skills )

# Find and print students whose marks are greater than 80.

for student in root.findall("student"):
    marks = int(student.find("marks").text)
    if marks > 80:
        print(student.findtext("name") , marks)
    

# Update Existing Data
# Change Rahul's marks from 85 → 88.

for student in root.iter("student"):
    if student.findtext("name").lower() == "rahul":
        marks = student.find("marks")
        marks.text = '88'

# et.indent(tree)
# tree.write("students_updated.xml" , encoding="utf-8" , xml_declaration=True)

# Add a new student

new_student = et.SubElement(root,"student")
new_student.set("id","105")
name = et.SubElement(new_student , "name")
name.text = "Kesha"
branch = et.SubElement(new_student , "branch")
branch.text = "CSE"
year = et.SubElement(new_student , "year")
year.text = "3"
marks = et.SubElement(new_student , "marks")
marks.text = "95"
skills = et.SubElement(new_student , "skills")
skill = et.SubElement(skills , "skill")
skill.text = "Python"
skill = et.SubElement(skills , "skill")
skill.text = "Django"

# Add a new skill Django to Rahul.

for student in root.iter("student"):
    if student.findtext("name").lower() == "rahul":
        skill = et.SubElement(student.find("skills") , "skill")
        skill.text = "Django"

# Remove Neha's Arduino skill.

for student in root.findall("student"):
    if student.findtext("name").lower() == "neha":
        skills = student.find("skills")
        for skill in skills.findall("skill"):
            if skill.text.lower() == 'arduino':
                skills.remove(skill)

et.indent(tree)
tree.write("students_updated.xml" , encoding="utf-8" , xml_declaration=True)
