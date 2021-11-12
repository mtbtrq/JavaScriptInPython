import os

os.system("title Python to JavaScript REPL")
print("Welcome to the Python to JavaScript REPL!")

code = None
stop = None

file = open("index.js", "a")

while stop != True:
    if code != "run":
        code = input("> ")
        file.write("\n" + code)
    else:
        file.close()
        os.system("node index.js")
        os.system("del index.js")
        stop = True