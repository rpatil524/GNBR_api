# swagger-client
This API provides access to the relationships between entities in the global network of biomedical relationships (GNBR) derived from text

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
entity1 = 'entity1_example' # str | GNBR-ID for first entity
entity2 = 'entity2_example' # str | GNBR-ID for second entity

try:
    # Query for an edge
    api_response = api_instance.get_edge(entity1, entity2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_edge: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/NCATS_GNBR/GNBR_API/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DevelopersApi* | [**get_edge**](docs/DevelopersApi.md#get_edge) | **GET** /queryEdge | Query for an edge
*DevelopersApi* | [**get_identifier**](docs/DevelopersApi.md#get_identifier) | **GET** /findEntity | Find GNBR identifier
*DevelopersApi* | [**get_node_neighbors**](docs/DevelopersApi.md#get_node_neighbors) | **GET** /getNodeNeighbors | Get all neighbors of a particular node
*DevelopersApi* | [**get_subgraph**](docs/DevelopersApi.md#get_subgraph) | **GET** /getInducedSubgraph | Get a GNBR subgraph


## Documentation For Models

 - [GnbrAssociation](docs/GnbrAssociation.md)
 - [GnbrEdge](docs/GnbrEdge.md)
 - [GnbrEntity](docs/GnbrEntity.md)
 - [GnbrSubgraph](docs/GnbrSubgraph.md)
 - [IdMapping](docs/IdMapping.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

alavertu@stanford.edu

