"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = list()
    with open(neo_csv_path) as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            neo = NearEarthObject(designation=line[3], name=line[4], hazardous=line[7], diameter=line[15])
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    collection_of_CloseApproach = list()
    with open(cad_json_path) as f:
        content = json.load(f)

        for data in content['data']:
            ca = CloseApproach(_designation=data[0], time=data[3], distance=data[4], velocity=data[7])
            collection_of_CloseApproach.append(ca)

    return collection_of_CloseApproach
