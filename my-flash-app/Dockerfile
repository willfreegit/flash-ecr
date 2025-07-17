#Parent Image
FROM python:3.9-slim-buster
#Set the working directory in the container
WORKDIR /app
#Copy the current directory contains into the container at /app
COPY . /app
#Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt
#Make port 80 available to the world
EXPOSE 80
#Run app.py withh the container lauches
CMD ["python", "app.py"]