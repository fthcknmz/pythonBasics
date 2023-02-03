# JSON is a syntax for storing and exchanging data
# JSON is a text, written with JavaScript object notation
import json
# if you have a JSON string, you can parse it by using the json.loads() method
x = '{"name":"Fethi", "age":20, "city":"Istanbul"}' # some json text
y = json.loads(x) # parse json text
print(y["city"]) # the result is a Python dictionary
# if you have a Python object, you can convert it into a JSON string by using the json.dumps() method
x = {
     "name": "Fethi",             # some Python dictionary
     "age": 20,
     "city": "Istanbul"
     }
y = json.dumps(x)  # convert into JSON
print(y,"\n")
"""
You can convert Python objects of the following types, into JSON strings:
dict
list
tuple
string
int
float
True
False
None

"""
"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
PYTHON          JSON

dict	        Object
list	        Array
tuple	        Array
str	            String
int	            Number
float       	Number
True	        true
False       	false
None	        null

"""
# json.dumps() method has parameters to mak it easier to read
y = json.dumps(x, indent=4)  #    to define the number of indents
print(y,"\n")
# use separators parameter to change the deafault separator
y = json.dumps(x, indent=4, separators=("; "," = "))
print(y,"\n")
# order the result
y = json.dumps(x, indent=4, sort_keys=True)
print(y,"\n")