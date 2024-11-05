## Apollo Python Protobuf

This project provides Python bindings for the Apollo modules' protobufs, enabling seamless integration and usage of Apollo’s protobuf definitions in Python.

### Installation

#### Option 1: Install via pip
```bash
pip install apollo_modules==[version]  # Supported versions: see release https://pypi.org/manage/project/apollo-modules/releases/
```
Note that, to accommodate changes across different versions of Apollo, we provide multiple versions of our package.

#### Option 2: Build from Source
```bash
git clone -b [version] https://github.com/MingfeiCheng/ApolloPyProto.git
cd ApolloPyProto
pip install -e .
```

### Usage

#### 1. Verify Installation
To verify the installation, open a Python shell and run the following:
```python
python
>>> import apollo_modules
>>> from apollo_modules.modules.planning.proto.planning_pb2 import ADCTrajectory
```
If there are no errors, the installation was successful, and the package is ready to use.

#### 2. Example Usage
Here’s an example of importing the `planning_pb2` protobuf used in Apollo’s planning module:
```python
from apollo_modules.modules.planning.proto.planning_pb2 import ADCTrajectory
```

### (Optional) Generate Python Protobuf Files from the Apollo Project
We provide a shell script to automatically generate the Python versions of the protobufs from Apollo’s modules. Use the following command:

```bash
bash proto_generate.sh /path/to/apollo_root /path/to/output
```