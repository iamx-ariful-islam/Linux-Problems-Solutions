import os


folder = "tips_tricks"

# List all files inside the folder
for file_name in sorted(os.listdir(folder)):
    if file_name.endswith(".txt"):
        print(f"👉 [{file_name}](tips_tricks/{file_name})<br/>")