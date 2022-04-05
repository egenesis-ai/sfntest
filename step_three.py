import os


step_input = os.getenv("STEP_THREE", default="Default 3")
print("this is step one with input: {i}.".format(i=step_input))
