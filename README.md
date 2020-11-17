# KML Slipway SDK

In keeping with Kubernetes nautical theme, the slipway, or ramp for launching
boats, is a light-weight container launcher and deployment management system
for KML.

Slipway enables the launching of any freeform container image into Kubernetes.
Additionally, this SDK can be used as a tool for container development; allowing
for the simplicity of the Slipway subsystem but with some integration with KML
and the database.

## Usage

Create a new python module with your code as a callable function inside.
Reference this code with the environment variables SLIP_MODULE and SLIP_FUNCTION
when launching your container with the slipway start endpoint. Include `sdk.py`
in your container.

A simple build and release script is included. Edit `repo_uri` to reflect your
desired container name and tag, then run `release.sh`.
