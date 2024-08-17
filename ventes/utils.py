import json

def get_agency_names():
    with open('data.json', 'r') as f:
        data = json.load(f)
    agency_names = [item['agence'] for item in data]
    return agency_names