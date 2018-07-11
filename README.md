This is a client implementation of the XML API of the game NationStates 
(https://www.nationstates.net), allowing different queries on the game data.

## Installation

System:

    sudo python3 setup.py install

User:

    python3 setup.py install --user

***If you intend to use this client a lot, please consider setting the
`NATIONSTATES_EMAIL` environment variable to your email address.***

This will make your requests identifiable in the NationStates server logs, and allow
admins to contact you in case of problems.

## Usage

The client provides a simple command-line script for getting region and nation data.

```
usage: nationstates [-h] [--format {json,yaml,txt}]
                    {nation,region} name [fields [fields ...]]

Access the NS API.

positional arguments:
  {nation,region}       The type of entity to access.
  name                  Name of entity.
  fields                Fields to query.

optional arguments:
  -h, --help            show this help message and exit
  --format {json,yaml,txt}
                        Format. Defaults to txt for single scalar values, json
                        otherwise.
```

Sample:

    $ nationstates nation ermarian motto flag population

    $ nationstates region the_north_pacific delegate

## Features

Aside from a library that allows general queries, this client comes with
multiple scripts for specific purposes, such as building a regional map of 
endorsements.

The client automatically throttles itself to at most fifty queries in thirty 
seconds. Note that this throttling is only done on a per-thread basis, so only 
one instance of the client may run simultaneously; your address will otherwise
be temporarily blocked by the NationStates server.

## License

This code is provided under the MIT License; see `LICENSE.txt` for more information.