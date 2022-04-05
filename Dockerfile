FROM public.ecr.aws/bitnami/python:3.7


COPY *.py ./

# Install the function's dependencies using file requirements.txt
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "python",  "step_one.py" ]