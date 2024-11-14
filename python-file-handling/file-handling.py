import os

class FileHandler:
    
    def __init__(self):
        pass 

    def create_file(self, name):
        file = self.open_file(name, "x")
        return file

    def remove_file(self, name):
        os.remove(name)
        print(f"removed file - {name}")
        

    def rename_file(self, curr, new):
        os.rename(curr, new)
        print(f"renamed file - {curr} to {new}")

    def delete_contents(self, name):
        file = self.open_file(name, "r+")
        file.truncate(0)
        file.write("")
        self.close_file(file)

    def read_full_content(self, name): 
        file = self.open_file(name, "r") # r+ - read write mode
        contents = file.read()
        self.close_file(file)

        return contents

    def read_partial_content(self, name, size):
        file = self.open_file(name, "r+")
        contents = file.read(size)
        self.close_file(file)

        return contents

    def read_lines(self, name):
        file = self.open_file(name, "r")
        lines = file.readlines()
        print(lines)
        self.close_file(file)

    def read_line_by_line(self, name):
        file = self.open_file(name, "r")
        line1 = file.readline()
        line2 = file.readline()
        print(line1, line2)
        self.close_file(file)

    def read_thr_loop(self, name):
        file = self.open_file(name, "r")
        for line in file:
            print(line, end="")
        self.close_file(file)

    def move_pointer(self, file_object, pos = 0):
        file_object.seek(pos)

    def view_pointer(self, file_object):
        return file_object.tell()

    def write_to_file(self, name, contents):
        file = self.open_file(name, "w")
        file.write(contents)
        self.close_file(file)
    
    def append_file(self, name, contents):
        file = self.open_file(name, "a")
        file.write(contents)
        self.close_file(file)

    def write_from_list_to_file(self, name, list_of_content):
        file = self.open_file(name, "w")
        file.writelines(list_of_content)
        self.close_file(file)
    
    def overwrite_file(self, name, content):
        file = self.open_file(name, "r+")
        file.write(content)
        self.close_file(file)

    def open_file(self, name, mode = 'r'):
        file = open(f"data/{name}", mode)
        print(f"File descriptor - {file.fileno()}")
        return file
        
    def close_file(self, file_object):
        file_object.close()


if __name__ == "__main__" :

    filehandler = FileHandler()



    




