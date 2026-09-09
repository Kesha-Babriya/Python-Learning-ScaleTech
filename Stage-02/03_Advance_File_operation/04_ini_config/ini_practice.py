# INI is a simple configuration-file format based on sections and key-value pairs.
import configparser

config = configparser.ConfigParser()

#write in .ini file as key value pair in section
config["database"] ={
    'host':'localhost',
    'nested':{
        'hi':'kesha',
        'ini':'nested-key'
    },
    'port':'3306'
}

config['server']={
    "host": "127.0.0.1",
    "port": "8000",
    "debug": "true"
}

# with open("config.ini",'w') as file:
#     config.write(file)

# Modify existing value

config['database']['port'] = '5432'

# Add a new value

config['database']['password'] ='1234@#'

# Add new section

config["logging"] = {
    "level": "INFO",
    "file": "app.log"
}

# with open("config_updated.ini",'w') as file:
#     config.write(file)


# remove section and key

config.remove_option('database','password')
config.remove_section('logging')

# with open("config_updated.ini",'w') as file:
#     config.write(file)

#load data of config.ini

config.read("config.ini")
print(config.getint("database","port"))
print(config['database']['port'],"it gives as string")
print(config.getboolean("server",'debug'))
print(config.get("database",'nested'))

#Get all sections
print(config.sections())
print(config.has_section("logging"))
print(config.has_option("database",'nested'))