import os
import boto3

client = boto3.client('stepfunctions')


step_input = os.getenv("STEP_THREE", default="Default 3")
task_token = os.getenv("TASK_TOKEN", default="TASK TOKEN PLACEHOLDER")


print("this is step three with input: {i}.".format(i=step_input))
try:
    with open("/mount/data/somefile.txt", 'r') as f:
        content = f.read()
except Exception as e:
    client.send_task_failure(
        taskToken=task_token,
        error=str(e)
    )
else:
    client.send_task_success(
        taskToken=task_token,
        output='{"content":"' + content + '"}'
    )
