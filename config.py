# Copyright [c] KVL314 [Derek Stiles](https://github.com/KVL314)

import yaml
yaml_file = 'settings.yaml'
config_dict = {}

with open(yaml_file, 'r') as file:
    try:
        config_dict = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

if not config_dict:
    raise Exception("Parse settings file failed.  Cannot run")


# Helper functions
def get_collection_url():
    return config_dict['collectionLink']

def get_moxfield_creds():
    return config_dict['moxfield']
