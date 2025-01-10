import subprocess
import sys
import os.path
import os
import tkinter as tk
from tkinter import filedialog, messagebox

installcheck_file_path = os.path.join("C:", "Users", "Public", "Documents", "install_check.txt")

username = os.environ.get("USERNAME")

def install_dependencies():
    command = [sys.executable, '-m', 'pip', 'install', 'pyinstaller']

    try:
        subprocess.run(command, check=True)
        print("PyInstaller installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing PyInstaller.")

    def install_package(package_name):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing package '{package_name}'.")

    package_to_install = "tk"
    install_package(package_to_install)

    try:
        with open(installcheck_file_path, 'x') as file:
            print(f"{installcheck_file_path} created successfully.")
    except FileExistsError:
        print(f"{installcheck_file_path} already exists.")
    except Exception as e:
        print(f"Error creating {installcheck_file_path}: {e}")

if os.path.isfile(installcheck_file_path):
    print("This isn't your first rodeo huh?")
else:
    install_dependencies()

def file_dialog():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
    )

    if file_path:
        print(f"Selected file: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return None

def convert_to_exe(file_path):
    if file_path:
        command = [sys.executable, '-m', 'PyInstaller', '--onefile', file_path]
        try:
            subprocess.run(command, check=True)
            print(f"Successfully converted {file_path} to .exe")
            messagebox.showinfo("Success", f"Successfully converted {file_path} to .exe")
            open_explorer_to_dist()
        except subprocess.CalledProcessError:
            print(f"Error converting {file_path} to .exe")
            messagebox.showerror("Error", f"Error converting {file_path} to .exe")

def open_explorer_to_dist():
    dist_path = os.path.join("C:\\", "Users", username, "dist")
    if os.path.exists(dist_path):
        subprocess.run(['explorer', dist_path])
    else:
        print(f"Path {dist_path} does not exist.")

def open_file_dialog():
    file_path = file_dialog()
    if file_path:
        convert_to_exe(file_path)

def create_gui():
    root = tk.Tk()
    root.title("Python to EXE Converter")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Convert Python script to EXE")
    label.pack(pady=5)

    button = tk.Button(frame, text="Select Python File", command=open_file_dialog)
    button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()