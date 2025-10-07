import glob

myfiles = glob.glob("files/*.csv")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(f"Contents of {filepath}:")
        print(file.read())