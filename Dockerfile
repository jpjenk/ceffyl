# Demonstration container for direct runner (slipway launcher)

FROM ubuntu:18.04

RUN mkdir -p /opt/demo
WORKDIR "/opt/demo"

# Install the required libraries and dependencies
ADD requirements.txt  ./
# ADD gpudb-api-python/gpudb-*-cp36-cp36m-manylinux1_x86_64.whl ./
# RUN pip install ./gpudb-*.whl
RUN apt update && apt upgrade
RUN apt -y install python3-pip
RUN pip3 install -r requirements.txt --no-cache-dir

# Install the demo script
ADD demo_inserter.py ./

RUN ["chmod", "+x",  "demo_inserter.py"]
ENTRYPOINT ["/opt/demo/demo_inserter.py"]
