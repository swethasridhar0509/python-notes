# JSON

---

### **JSON Overview**

1. **JSON**: A lightweight, popular format for storing and sharing data over the web.
2. **Based on JavaScript Objects**: Structured similarly to objects in JavaScript.
3. **Language Independent**: Supported by many programming languages.
4. **Common Use Cases**:
    - API requests and responses.
    - Configuration files.
    - Data storage.
5. **Characteristics**: Lightweight and human-readable.
6. **Advantages over XML**:
    - Smaller size, leading to faster transmission.
    - Easier to read and write.
7. **Disadvantages**: Limited data types (e.g., no date or custom types).

### Structure of JSON

JSON is built on two main structures:

1. A collection of key/value pairs (similar to a Python dictionary)
2. An ordered list of values (similar to a Python list)

JSON data is represented in key-value pairs, enclosed in curly braces `{}`. Arrays are enclosed in square brackets `[]`.

### **Data Types in JSON**

1. **Objects**: Key-value pairs `{ "key": "value" }`.
2. **Arrays**: Ordered lists `[1, 2, 3]`.
3. **String**: Text `"Hello, World!"`.
4. **Number**: Integer or floating-point `42`, `3.14`.
5. **Boolean**: `true`, `false`.
6. **Null**: Empty value `null`.

### **Rules for JSON**

1. No leading zeroes (e.g., `01` is invalid).
2. Keys and values must be enclosed in double quotes (`"key": "value"`).
3. No trailing commas in objects or arrays.
4. Comments are not allowed.
5. No trailing decimal points (e.g., `1.` is invalid).

### Handling JSON using Python

Python and JSON have fewer differences in their data types:

1. JSON has no equivalent for complex structures like **sets** and **tuples**.
2. Python - **None**; JSON - **null**.
3. Python - **True** & **False**; JSON -uses **lowercase**.

**Serialization and Deserialization**:

1. **Serialization** - Converting an object (e.g., dictionary, list) into a format (like JSON, XML, or binary) that can be stored or transmitted.
2. **Deserialization**: Converting the serialized data back into the original object.
3. Python has an in-built **Json module** to handle this case.

**JSON Module:**

1. **JSON dumps**
- **Purpose** - To convert a Python object to json string. (i.e., Serialization)
- **Argument** - Python object.
- **Optional Arguments** - indent, sort_keys, and separators.
- **Return** - JSON string.

1. **JSON loads**
- **Purpose** - Converts Json strings to Python objects. (i.e., Deserialization)
- **Argument** - Json string.
- **Return** - Python object.

1. **JSON dump**
- Purpose - Convert Python object to json strings and write it to a json file.
- Argument - data and file name.
- Return - None

 

1. **JSON load**
- Purpose - Reads json string from a json file and converts it to a Python object.
- Argument - file name.
- Return - Python object.