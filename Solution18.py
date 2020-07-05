import json

sample_data = {
    "myinfo":{
        "name": "Suyen Shrestha",
        "age": 24
    }
}

print(f'Sample python data: {sample_data}\n')

# serializing into json
json_string = json.dumps(sample_data, indent=4)

print(f'Serialized json data: {json_string}\n')



#deserializing back to python
deserialized_data = json.loads(json_string)

print(f'Deserialized python data: {deserialized_data}')