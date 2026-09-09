import yaml

with open("config.yaml",'r') as file:
    data = yaml.safe_load(file)

print("Project ",data['project']['name'])
print("Version ",data['project']['version'])
print("Name ",data['developer']['name'])
print("Branch ",data['developer']['branch'])
print("Year ",data['developer']['year'])

skills = [skill for skill in data["developer"]["skills"]]
print("Skills : " , skills)


#modify data

data["settings"]["max_students"] = 200
data["developer"]["skills"].append("Git")


# Add a new configuration:
#settings is dict so do not use append
data["settings"]["theme"] = "dark"

#write operation

with open("config_updated.yaml" , 'w') as file:
    yaml.safe_dump(data , file , sort_keys=False)