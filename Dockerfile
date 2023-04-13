FROM python:3.10

#environment
ENV PYTHONUNBUFFERED=1

# creer dossier travail "code"
WORKDIR /code

# install depencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the code of the project
COPY . .

# port
EXPOSE 8000

# command to run the application
CMD ["python", "manage.py", "runserver"]
