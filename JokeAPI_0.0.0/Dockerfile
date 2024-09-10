FROM python:3.10
ENV PYTHONUNBUFFERED=1
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
COPY . .
RUN ls
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
