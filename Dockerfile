# Use an official Python runtime as a parent image
FROM debian:latest

RUN apt update && apt upgrade -y
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt

# Run the bot when the container launches
CMD ["bash", "start.sh"]
