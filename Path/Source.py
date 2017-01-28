
import os

def walk(dir_name, include_subdir):

    for name in os.listdir(dir_name):

        file_name = os.path.join(dir_name, name)

        if os.path.isfile(file_name):
            print(file_name)
        elif os.path.isdir(file_name) and include_subdir:
            walk(file_name)



walk("C:/Users/USER/OneDrive/C++ books", False)


walk(os.getcwd(), False) 