# File Handling

## What is File Handling?

1. File handling refers to the process of working with files in a computer system. 
2. Key operations of file handling include:
    - Creating new files
    - Opening existing files
    - Reading data from files
    - Writing data to files
    - Appending data to existing files
    - Closing files after operations are complete

## What problem does it solve? Developed?

1. **Data persistence:** It allows programs to store and retrieve information beyond the program's runtime.
2. It provides a way to read and write from existing files in the computer memory.

## Use case?

1. Data storage and retrieval: Saving user information, application settings, or large datasets for later access.
2. Log management: Recording system events, errors, or user activities for debugging and auditing purposes.

## What is a file? Types?

1. **File** - Named location in computer memory that stores data permanently.
2. **Text files** - stores data as plain text, human readable format. (E.g., txt)
3. **Binary files** - stores data in binary format, machine readable (E.g., config, exe, image)

## **Key points on file handling**

1. **Stream** - pipeline through data flows in and out.
2. `open()` - creates a stream.
3. File descriptor:
    1. Unique Id assigned by the OS to the opened file.
    2. Role - used to track the file during I/O operations.
    3. `fileObject.fileno()`
4. A file should be closed after I/O operation to avoid memory leak, resource wastage and data loss.

## Operations:

1. **Modes:**
    1. **r** - read only.
    2. **r+** - read and write
    3. **w** - create and write 
    4. **a** - create and append
    5. **x** - create and write

2. **Creating a file:**
    1. `w` and `x` are used to create new files (with `x` raising an `FileExistsError` if the file exists).
    2. `a` also creates a file if it doesn’t already exist but appends data instead of overwriting.
    3. `open("filename.txt", "x")`

3. **Opening an existing file:**
    1. Open function - Initiates access to files with specific mode.
    2. default mode - “r”
    3. `open("filename.txt", "r")`  - assigns a file descriptor id, return a file object.

4. **Reading file:**
    1. modes - **r** and **r+**
    2. `file.read(size(optional))` to read the entire content as a string. returns - whole text.
    
    3.  `file.readline()` to read one line at a time. returns - line
    
    4.  `file.readlines()` to read all lines as a list of strings. returns - list of lines.
    
    5.  loop through the file to read line by line.
    
5. **Writing to files:**
    1. modes - w, x, r+
    2. w - creates a new file, clears existing file.
    3. x - exclusive to create and write.
    4. r+ - to read and write. does overwrite due to pointer.
    5. `file.write("text")` to write a string to the file.
    6. `file.writelines(["line1", "line2"])` to write multiple lines.

6. **Appending to files:**
    1. mode - a
    2. a - creates and adds or adds data at the end of the existing file.

7. **Closing file:**
    1. `file.close()` to free resources and ensure data is saved.

 8. **Context manager:**

    1.  Automatic Resource Management

    2. Exception Handling.

1. **Seek and tell:**
    1. `file.seek(0)` - used to move the file pointer.
    2. `file.tell()` - returns the current pointer location.

## **Binary File Handling:**

1. **Modes** 
    - **`rb`**: Read binary
    - **`wb`**: Write binary
    - **`ab`**: Append binary
    - **`rb+`**: Read and write binary (for existing files)

2. **Reading a bin file:**
    - `file.read(size)`: Reads `size` bytes from the file.
    - `file.read()`: Reads the entire content of the file as bytes.
    
3. **Writing to bin file:**
    - `file.write(bytes)`: Writes a sequence of bytes to the file.
    
    ```python
    data = b"Hello, binary world!"
    with open("image.jpg", "rb") as file:
        image_data = file.read()
    
    with open("copied_image.jpg", "wb") as file:
        file.write(image_data)
    ```