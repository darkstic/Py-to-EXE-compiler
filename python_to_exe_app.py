import subprocess
import sys
import os.path
import os

# destination_path="Placeholder"
# initial_path="placeholder"
installcheck_file_path = "C:\\Users\\Public\\Documents\\install_check.txt"

username=os.environ.get("USERNAME")

def install_dependancies():
    command = 'pip install pyinstaller'

    subprocess.run(command, shell=True)

    def install_package(package_name):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing package '{package_name}'.")

    if __name__ == "__main__":
        package_to_install = "tk"  
        install_package(package_to_install)

    try:
        with open(installcheck_file_path, 'x') as file:
         print(f"{installcheck_file_path} created successfully.")
    except FileExistsError:
        print(f"{installcheck_file_path} already exists.")


if os.path.isfile(installcheck_file_path):
    print("This isn't your first rodeo huh?")
else:
    install_dependancies()

import tkinter as tk
from tkinter import *
from tkinter import filedialog

def file_dialog(binary):

    root = tk.Tk()
    root.withdraw() 

    # Open the file explorer dialog
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
    )

    # Print the selected file path
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")

    def mod_destination(binary):
        if binary=="py":
            global destination_path
            destination_path=file_path
        elif binary=="exe":
            global initial_path
            initial_path=file_path


    mod_destination("py")

global file_path


def convert_file(file_path):
    command=f"pyinstaller --onefile {file_path}"
    subprocess.run(command, shell=True)

def show_endfile():
    path_to_open = f"C:\\Users\\{username}\\dist"
    subprocess.run(f'explorer "{path_to_open}"', shell=True)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def converter_page(file_path):
    root=tk.Tk()
    root.title("Py to exe")
    root.geometry("420x420")

    exe_filepath_instructions=tk.Label(root, font="helvetica", bg="silver", fg="black", text=(rf"Your new .exe file will appear in C:\Users\{username}\dist"))
    exe_filepath_instructions.grid(row=1, column=1)

    def convert_button_cmd():
        convert_file(file_path)
        root.destroy()
        show_endfile()

    convert_button=tk.Button(root, font="impact", bg="gray", fg="orange", text="Convert", command=lambda: convert_button_cmd())
    convert_button.grid(row=3, column=1)

    root.mainloop()

def greeting_page():

    root=tk.Tk()
    root.title("Py to exe")
    root.geometry("600x200")

    page_heading=tk.Label(root, font="helvetica", bg="black", fg="white", text="     Covert your Python files into executable apps!")
    page_heading.grid(row=1, column=1)

    py_filepath_instructions=tk.Label(root, font="helvetica", bg="silver", fg="black", text="Select the filepath of the .py file you would like to convert:")
    py_filepath_instructions.grid(row=3, column=1)

    def py_selection_completion():
        file_dialog("py")
        root.destroy()
        converter_page(destination_path)

    py_file_select=tk.Button(root, font="impact", bg="gray", fg="orange", text="Browse", command=lambda: py_selection_completion())
    py_file_select.grid(row=5, column=1)

    error_notice=tk.Label(root, font="helvetica", bg="black", fg="red", text="Please ensure that the filename contains no spaces to ensure stable operation.")
    error_notice.grid(row=8, column=1)

    # exe_file_select=tk.Button(root, font="impact", bg="gray", fg="orange", text="Browse", command=lambda: file_dialog("exe"))
    # exe_file_select.grid(row=8, column=1)

    root.mainloop()

greeting_page()