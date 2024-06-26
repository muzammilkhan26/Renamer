import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from openpyxl import Workbook

def create_template():
    folder_path = folder_entry.get()
    if not folder_path:
        log_text.insert(tk.END, "Please select a folder path first.\n")
        return
    
    current_directory = os.getcwd()
    template_path = os.path.join(folder_path, "template.xlsx")

    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet["A1"] = "OldName"
        sheet["B1"] = "NewName"

        index = 2
        for root, _, files in os.walk(folder_path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), folder_path)
                sheet[f"A{index}"] = relative_path
                index += 1
        
        workbook.save(template_path)
        log_text.insert(tk.END, f"Template created at '{template_path}'\n")
    except Exception as e:
        log_text.insert(tk.END, f"Error creating template: {e}\n")

def rename_files():
    excel_file_path = excel_entry.get()
    folder_path = folder_entry.get()

    if not excel_file_path or not folder_path:
        log_text.insert(tk.END, "Please select both the folder path and the Excel file path.\n")
        return

    try:
        df = pd.read_excel(excel_file_path)
        for index, row in df.iterrows():
            old_name = str(row['OldName'])
            new_name = str(row['NewName'])
            old_path = os.path.join(folder_path, old_name)
            file_extension = os.path.splitext(old_name)[1]
            new_path = os.path.join(folder_path, os.path.dirname(old_name), new_name + file_extension)

            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                log_text.insert(tk.END, f"Renamed '{old_name}' to '{new_name}{file_extension}' successfully!\n")
            else:
                log_text.insert(tk.END, f"File '{old_name}' not found.\n")
    except Exception as e:
        log_text.insert(tk.END, f"Error: {e}\n")

window = tk.Tk()
window.title("File Renamer")

# Styling
window.configure(bg="#F0F0F0")
window.geometry("500x450")

title_label = tk.Label(window, text="Bulk File Renamer", font=("Arial", 18, "bold"), bg="#F0F0F0")
title_label.pack(pady=10)

folder_frame = tk.Frame(window, bg="#F0F0F0")
folder_frame.pack(pady=10)

folder_label = tk.Label(folder_frame, text="Folder Path:", font=("Arial", 12), bg="#F0F0F0")
folder_label.pack(side=tk.LEFT, padx=10)

folder_entry = tk.Entry(folder_frame, width=40)
folder_entry.pack(side=tk.LEFT, padx=10)

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

browse_button = tk.Button(folder_frame, text="Browse", command=browse_folder)
browse_button.pack(side=tk.LEFT, padx=10)

template_button = tk.Button(window, text="Create Template", font=("Arial", 14), bg="#2196F3", fg="white", command=create_template)
template_button.pack(pady=10)

excel_frame = tk.Frame(window, bg="#F0F0F0")
excel_frame.pack(pady=10)

excel_label = tk.Label(excel_frame, text="Excel File Path:", font=("Arial", 12), bg="#F0F0F0")
excel_label.pack(side=tk.LEFT, padx=10)

excel_entry = tk.Entry(excel_frame, width=40)
excel_entry.pack(side=tk.LEFT, padx=10)

def browse_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    excel_entry.delete(0, tk.END)
    excel_entry.insert(0, file_path)

browse_button = tk.Button(excel_frame, text="Browse", command=browse_excel)
browse_button.pack(side=tk.LEFT, padx=10)

rename_button = tk.Button(window, text="Rename Files", font=("Arial", 14), bg="#4CAF50", fg="white", command=rename_files)
rename_button.pack(pady=20)

log_label = tk.Label(window, text="Log:", font=("Arial", 12), bg="#F0F0F0")
log_label.pack()

log_text = tk.Text(window, height=8, width=60)
log_text.pack(pady=10)

window.mainloop()
