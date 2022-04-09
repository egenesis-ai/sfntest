import os


step_input = os.getenv("STEP_TWO", default="Default 2")
print("this is step one with input: {i}.".format(i=step_input))
with open("somefile.txt", 'r') as f:
    f.read()
