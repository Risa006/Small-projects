
import tkinter as tk
import os, subprocess, datetime
from tkinter import messagebox


ide = "C:/Users/risan/AppData/Local/Programs/Microsoft VS Code/Code.exe"


def create_new_project():
    # Get the project name, assignment, and URL from the entry fields
    name = entry_name.get()
    global project_directory, project_file, ide
    if name[-3:] != ".py" and name[-4:] != ".pyw":
        project_directory = f"C:/Users/risan/Plocha/škola/PVA/PVA-3.rocnik/{name}"

    if name == "" or "/" in name or "\\" in name:
        messagebox.showerror("Jsi Tupec", "Chybný vstup")
        return
    if name[-3:] != ".py" and name[-4:] != ".pyw" and not os.path.exists(project_directory):
        project_file = f"{name}.py"
        assignment = entry_assignment.get()
        url = entry_url.get()

        # Create a new project directory and file
        os.makedirs(project_directory, exist_ok=True)
        with open(os.path.join(project_directory, project_file), "w", encoding="UTF-8") as f:
            f.write(f"# -*- coding: UTF-8 -*-\n")
            f.write(f"# Program:\t\t{project_file}\n")
            f.write(f"# Zadání:\t\t{assignment}\n")
            f.write(f"# URL zadání:\t\t{url}\n")
            f.write(f"# Datum:\t\t{datetime.date.today()}\n")
            f.write(f"# Verze:\t\t1.0\n")
            f.write(f"# Autor:\t\tRichard Rutterle\n")
            f.write(f"# Třída:\t\t3.PT\n\n")
    if name[-3:] == ".py" or name[-4:] == ".pyw":
        project_file = f"{name}"
        project_directory = f"C:/Users/risan/Plocha/škola/PVA/PVA-3.rocnik/{name[:-3]}" if name[-3:] == ".py" else f"C:/Users/risan/Plocha/škola/PVA/PVA-3.rocnik/{name[:-4]}"
    # Open the project file in ide
    print(ide, os.path.join(project_directory, project_file))
    subprocess.call([ide, os.path.join(project_directory, project_file)])
    
def open_project_directory():
    # Open the project directory
    os.startfile("C:/Users/risan/Plocha/škola/PVA/PVA-3.rocnik")

def list_existing_projects():
    # Get the project directory
    project_directory = "C:/Users/risan/Plocha/škola/PVA/PVA-3.rocnik"

    # List the project names
    projects = [f for f in os.listdir(project_directory) if (f.endswith(".py") or f.endswith(".pyw") or "." not in f and "__" not in f and f != "soubory")]

    # Display the project names
    message = "\n".join(projects)
    messagebox.showinfo("Existující projekty", message)
    
def ide_change_VSCode():
    global ide
    ide = "C:/Users/risan/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    messagebox.showinfo("Změna", f"IDE: {ide}")

def ide_change_IDLE():
    global ide
    ide = "C:/Users/risan/AppData/Local/Programs/Python/Python312/Lib/idlelib/idle.bat"
    messagebox.showinfo("Změna", f"IDE: {ide}")

# Create the main window
root = tk.Tk()
root.geometry("200x300")
root.resizable(False, False)
root.title("Python Project Manager")


# Create a label and entry field for the project name
label = tk.Label(root, text="Název projektu:")
label.pack(pady=10)
entry_name = tk.Entry(root)
entry_name.pack(padx=2, pady=2)

# Create a label and entry field for the assignment
label = tk.Label(root, text="Zadání:")
label.pack()
entry_assignment = tk.Entry(root)
entry_assignment.pack(padx=2, pady=2)

# Create a label and entry field for the URL
label = tk.Label(root, text="URL:")
label.pack()
entry_url = tk.Entry(root)
entry_url.pack(padx=2, pady=2)

# Create a button to create a new project
button_new = tk.Button(root, text="Nový projekt", command=create_new_project)
button_new.pack(padx=2, pady=2)

# Create a button to open the project directory
button_open = tk.Button(root, text="Otevřít složku s projekty", command=open_project_directory)
button_open.pack(padx=2, pady=2)

# Create a button to list existing project names
button_list = tk.Button(root, text="Seznam existujících projektů", command=list_existing_projects)
button_list.pack(padx=2, pady=2)

check_button = tk.Button(root, text = "VSCode", command = ide_change_VSCode)
check_button.pack(padx = 2, pady = 2)

check_button = tk.Button(root, text = "IDLE", command = ide_change_IDLE)
check_button.pack(padx = 2, pady = 2)



root.mainloop()
