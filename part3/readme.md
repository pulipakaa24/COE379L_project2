# How to Use

## Option 1: Docker Compose (easiest)
Run ```docker-compose up```. Ensure ```docker-compose``` is installed by running ```sudo apt install docker-compose``` beforehand.

## Option 2: Build Docker Image
run ```docker build -t {username}/{imagename} .``` in this directory. I used ```adipu24/project02```. The required files are all included in this directory, so just ensure all files in the github repo are cloned properly.

## Example requests
A ```GET``` request can be sent to the ```/summary``` endpoint to retrieve a model summary including the purpose of the model, the version, and the number of parameters it has. Example in python using ```requests```: ```rsp = requests.get(f"{base_url}/summary")``` -> ```{'description': "Classify satellite images of buildings in the aftermath of a hurricane into 'damage' or 'no_damage' categories", 'name': 'Katrina_damage', 'number_of_parameters': 16812353, 'version': 'vgg16Variant'}```

A ```POST``` request can be sent to the ```/inference``` endpoint, with an image sent as a binary message payload under the files attribute of the request. The response will be a JSON similar to ```{"prediction": "damage" (or "no_damage")}```. Example request from grader script in python using ```requests```: 
```
def make_post_request(path):
    url = f"{base_url}/inference"
    
    # send multipart POST
    data = {"image": open(path, 'rb')}
    rsp = requests.post(url, files=data)
    # ------

    try:
        rsp.raise_for_status()
    except Exception as e:
        print(f"ERROR: POST /inference is INVALID. Non-200 status code; Status code received: {rsp.status_code}")
        return None
    return rsp
```

# Other info
The inference server runs on port 5000, and the docker-compose.yml file ensures that port 5000 is forwarded to the running container. This was tested with the grader code and it functions as expected.
