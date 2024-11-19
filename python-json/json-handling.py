'''
json.dumps() - converts python objects to json string.
json.dump() - converts python objects and writes it to a file.

1. Convert Python dict - Json Object.
2. Convert Python list/tuple - Json Array.
3. Convert Python int, float - Json number.
4. Convert Python string - Json string.
5. Convert None - null.
6. Convert True/False - true/false.
7. Python sets throws Error.

'''
import json 

class JSONSerializer:
    @staticmethod
    def object_to_jstr(python_object):
        result = json.dumps(python_object, indent=2, sort_keys=True, separators=(", ", ": "))
        return result
    
    @staticmethod
    def object_to_jfile(python_object, filename):
        with open(f"data/{filename}", 'w') as jfile:
            json.dump(python_object, jfile)

'''

json.loads - coverts json strings to python objects.
json.load - reads json string from the json file and converts it into python object.

'''

class JSONDeserializer:
    
    @staticmethod
    def jstr_to_obj(jstr):
        obj = json.loads(jstr)
        return obj
    
    @staticmethod
    def jfile_to_obj(file):
        with open(f"data/{file}", "r") as file:
            res = json.load(file)
            return res
        
if __name__ == "__main__":

    record = {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "painting"], "is_student": False}

    result = JSONSerializer.object_to_jstr(record)
    JSONSerializer.object_to_jfile(record, "data.json")
    print(f"Json String - {result}")

    res = JSONDeserializer.jfile_to_obj("data.json")
    resultant_dict = JSONDeserializer.jstr_to_obj(result)
    print(f"JSON string to python object - {res}", type(res))
    print(f"JSON string from file to python object - {resultant_dict}", type(resultant_dict))


