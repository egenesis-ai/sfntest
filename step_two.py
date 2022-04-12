import os
import boto3

client = boto3.client('stepfunctions', region_name="us-east-1")


step_input = os.getenv("STEP_TWO", default="Default 2")
task_token = os.getenv("TASK_TOKEN", default="TASK TOKEN PLACEHOLDER")


print("this is step two with input: {i}.".format(i=step_input))
try:
    with open("/mount/data/somefile.txt", 'w') as f:
        f.write("Writing from step 2...")
except Exception as e:
    client.send_task_failure(
        taskToken=task_token,
        error=str(e)
    )
else:
    client.send_task_success(
        taskToken=task_token,
        output='{"status": "task two completed successfully"}'
    )

