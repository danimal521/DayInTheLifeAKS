# #Download Python from DockerHub and use it
# FROM python:3.7.4

# #Set the working directory in the Docker container
# WORKDIR /code

# #Copy the dependencies file to the working directory
# COPY requirements.txt .

# #Install the dependencies
# RUN pip install -r requirements.txt

# #Copy the Flask app code to the working directory
# COPY . .

# #Run the container
# CMD [ "python", "./app.py" ]



# FROM python:3.8-slim-buster
# #FROM registry1.dso.mil/ironbank/redhat/dotnet-core/dotnetcore-sdk5:5.0

# WORKDIR /python-docker

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


FROM python:3.10
ENV PYTHONUNBUFFERED=1
ADD . /python-flask
WORKDIR /python-flask
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install -r requirements.txt
COPY . .
RUN ls
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD ["waitress-serve", "--call", "CoreApi:create_app"]