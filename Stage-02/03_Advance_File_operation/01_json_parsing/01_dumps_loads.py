import json

# dump s convert python to json string 

data_py = {
        'student':[
        {
            'name' : "kesha",
            'age' : 20,
            'has_licenece' : True
        },{
            'name' : "Benny",
            'age' : 10,
            'has_licenece' : False
        }
        ]
    }

print(type(data_py))

#----------------------------------------------------------------

#indent make readable format nd sort_keys is sort key wise in ascending order

data_json = json.dumps(data_py, indent=3 , sort_keys=True)

print(data_json)        #this is json string
print(type(data_json))

#---------------------------------------------------------------------

new_py = json.loads(data_json)      #this is load from json string to pyhton

print(new_py)
print(type(new_py))