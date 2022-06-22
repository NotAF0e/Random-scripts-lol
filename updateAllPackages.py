import os

os.system("pip freeze > requirements.txt")

with open('requirements.txt', 'r') as file:
    data = file.read()
    data = data.replace("==", ">=")

with open('requirements.txt', 'w') as file: file.write(data)


file.close()

os.system("pip install -r requirements.txt --upgrade")
os.remove("requirements.txt")
os.system('cmd /k "echo Finished updating all packages!"')

#test