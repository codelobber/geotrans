FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
ADD ./start.sh ./
ADD ./scripts/* ./
ADD ./requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ./start.sh
