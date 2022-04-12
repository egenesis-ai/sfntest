import os
import boto3

client = boto3.client('stepfunctions', region_name="us-east-1")


step_input = os.getenv("STEP_ONE", default="Default 1")
task_token = os.getenv("TASK_TOKEN", default="TASK TOKEN PLACEHOLDER")

print("this is step one with input: {i}.".format(i=step_input))

client.send_task_success(
    taskToken=task_token,
    output='{"status": "task one completed successfully"}'
)