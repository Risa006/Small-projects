from pathlib import Path
import tkinter as tk
import os, subprocess, datetime, shlex
from pprint import pprint
from tkinter import messagebox

class Paths:
    def __init__(self) -> None:
        self.folder = f"{Path.cwd()}\\PVA-3.rocnik\\"
        self.idle = "C:/Users/risan/AppData/Local/Programs/Python/Python312/Lib/idlelib/idle.bat"
        self.VSCode = "C:/Users/risan/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        self.ide = self.VSCode
        
class Funkce(Paths):
    def __init__(self) -> None:
        super().__init__()
        
    def new_project(self):
        self.name = entry_name.get()

        if self.name[-3:] != ".py" and self.name[-4:] != ".pyw":
            self.project_directory = self.folder + self.name

        if self.name == "" or "/" in self.name or "\\" in self.name:
            messagebox.showerror("Jsi Tupec", "Chybný vstup")
            return
        
        if self.name[-3:] != ".py" and self.name[-4:] != ".pyw" and not os.path.exists(self.project_directory):
            self.project_file = f"{self.name}.py"
            self.assignment = entry_assignment.get()
            self.url = entry_url.get()

            os.makedirs(self.project_directory, exist_ok=True)
            
            with open(os.path.join(self.project_directory, self.project_file), "w", encoding="UTF-8") as f:
                f.write(f"# -*- coding: UTF-8 -*-\n")
                f.write(f"# Program:\t\t{self.project_file}\n")
                f.write(f"# Zadání:\t\t{self.assignment}\n")
                f.write(f"# URL zadání:\t\t{self.url}\n")
                f.write(f"# Datum:\t\t{datetime.date.today()}\n")
                f.write(f"# Verze:\t\t1.0\n")
                f.write(f"# Autor:\t\tRichard Rutterle\n")
        if self.name[-3:] == ".py" or self.name[-4:] == ".pyw":
            self.project_file = f"{self.name}"
            self.project_directory = f"{self.project_directory}/{self.name[:-3]}" if self.name[-3:] == ".py" else f"{self.project_directory}/{self.name[:-4]}"
        else:
            self.project_file = f"{self.name}.py"
        self.script_path = os.path.join(self.project_directory, self.project_file).replace("\\","/")
        # Open the project file in ide
        if self.ide:
            self.version()
            subprocess.run(shlex.split(f"{self.ide} {self.script_path}"))
        else:
            messagebox.showwarning("IDE", "Vyber IDE")
        
    def open_dir(self):
        os.startfile(f.folder)
    def list_projects(self):
        # List the project names
        projects = [f for f in os.listdir(self.folder) if (f.endswith(".py") or f.endswith(".pyw") or "." not in f and "__" not in f and f != "soubory")]

        # Display the project names
        message = "\n".join(projects)
        messagebox.showinfo("Existující projekty", message)
    
    def change_ide(self, arg):
        match arg:
            case "Vscode":
                self.ide = self.VSCode
            case "Idle":
                self.ide = self.idle
        print(f"{self.ide = }")
        
    def version(self):
        lines = []
        with open(self.script_path, "r", encoding="UTF-8") as f:
            for line in f :
                lines.append(line.strip())
            version = lines[5]
            dot_index = version.find(".")+1 if version.find(".") !=-1 else version.find(".")
            version_number = int(version[dot_index:])+1
            version = version[:dot_index] + str(version_number)
            lines[5] = version
        with open(self.script_path,"w", encoding="UTF-8") as f:
            for line in lines:
                f.write(f"{line}\n")
            
f = Funkce()

# Create the main window
root = tk.Tk()
width, height = 200, 300,
x, y = (root.winfo_screenwidth()//2)-(width//2), (root.winfo_screenheight()//3)-(height//2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False, False)
root.title("Python Project Manager")

ide = tk.StringVar()
ide.set("VScode")

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
button_new = tk.Button(root, text="Nový projekt", command=f.new_project)
button_new.pack(padx=2, pady=2)

# Create a button to open the project directory
button_open = tk.Button(root, text="Otevřít složku s projekty", command=f.open_dir)
button_open.pack(padx=2, pady=2)

# Create a button to list existing project names
button_list = tk.Button(root, text="Seznam existujících projektů", command=f.list_projects)
button_list.pack(padx=2, pady=2)

drop_dowm = tk.OptionMenu( root , ide , "Vscode", "Idle", command=f.change_ide) 
drop_dowm.pack() 

root.mainloop()
