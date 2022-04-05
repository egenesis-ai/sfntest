import os


step_input = os.getenv("STEP_ONE", default="Default 1")
print("this is step one with input: {i}.".format(i=step_input))
