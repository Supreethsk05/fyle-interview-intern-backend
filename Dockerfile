# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001
# Define environment variable
ENV FLASK_APP=core/server.py


#Command to reset the database
RUN rm -f core/store.sqlite3 && flask db upgrade -d core/migrations/

#Command to start the server
CMD ["bash", "run.sh"]