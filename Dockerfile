# Use an official Python runtime as a parent image
FROM debian:latest

RUN apt update && apt upgrade -y

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the bot when the container launches
CMD ["bash", "start.sh"]
