# How to Use

## Option 1: Docker Compose (easiest)
Run ```docker-compose up```. Ensure ```docker-compose``` is installed by running ```sudo apt install docker-compose``` beforehand.

## Option 2: Build Docker Image
run ```docker build -t {username}/{imagename} .``` in this directory. I used ```adipu24/project02```. The required files are all included in this directory, so just ensure all files in the github repo are cloned properly.

## Example requests
A ```GET``` request can be sent to the ```/summary``` endpoint to retrieve a model summary including the purpose of the model, the version, and the number of parameters it has.

A ```POST``` request can be sent to the ```/inference``` endpoint, with an image sent as a binary message payload under the files attribute of the request. The response will be a JSON similar to ```{"prediction": "damage" (or "no_damage")}```

# Other info
The inference server runs on port 5000, and the docker-compose.yml file ensures that port 5000 is forwarded to the running container. This was tested with the grader code and it functions as expected.
