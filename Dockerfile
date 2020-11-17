# Demonstration container for direct runner (slipway launcher)

FROM ubuntu:18.04

RUN mkdir -p /opt/demo
WORKDIR "/opt/demo"

# Install the required libraries and dependencies
ADD requirements.txt  ./
RUN apt -y update && apt -y upgrade
RUN apt -y install python3-pip
RUN pip3 install -r requirements.txt --no-cache-dir

# Install the demo script
ADD sdk.py ./
ADD demo.py ./

RUN ["chmod", "+x",  "sdk.py"]
ENTRYPOINT ["/opt/demo/sdk.py"]
