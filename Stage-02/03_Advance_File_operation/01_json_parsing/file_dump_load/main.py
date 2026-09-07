import json

# dump => write from pyhton object to json file
# load => load from json file to python object

try:
    with open('emp.json','r') as file:
        data = json.load(file)

    print(data['company'])

    for item in data['employees']:
        print(item['id'] , item['name'])

    print(data['employees'][0]['skills'])

    

    emp ={"id": 1005,
         "name": "kinni",
         "department": "Designer",
         "skills": [
            "Recruitment",
            "Communication"
         ],
         "active": True}

    data['employees'].append(emp)
    data['employees'][0]['skills'].append("Cpp")
    with open("emp.json",'w') as file:
        json.dump(data , file , indent=3)

except json.JSONDecodeError:
    print("Invalid json")