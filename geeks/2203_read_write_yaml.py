"""
YAML - Python parser
https://www.w3schools.io/file/yaml-python-read-write/

yaml is a superset of json. It contains key and value pairs with included indentation and tabs.

pip search yaml
pip install pyyaml

In Linux or ubuntu:
sudo apt-get install PyYAML  // ubuntu
sudo yum install PyYAML  //Linux
sudo aptitude install // debinal OS flavor


"""

import yaml
from pprint import pformat


def read_my_yaml(yaml_file):
    with open(yaml_file, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)
        return config


def replace_port_in_yaml(yaml_file, service, port):
    # config_dict = yaml.full_load(open(yaml_file))
    config_dict = yaml.safe_load(open(yaml_file))
    config_dict["sut"]["service"][service] = int(port)
    with open(yaml_file, 'w') as file:
        # yaml.dump(config_dict, file, sort_keys=False)
        yaml.dump(config_dict, file, default_flow_style=False)


yaml_file = "myyaml1.yaml"
print(pformat(read_my_yaml(yaml_file)))
replace_port_in_yaml(yaml_file, "elasticsearch", 39300)
print(pformat(read_my_yaml(yaml_file)))
replace_port_in_yaml(yaml_file, "elasticsearch", 39200)
print(pformat(read_my_yaml(yaml_file)))

print()
with open(yaml_file) as file:
    try:
        data = yaml.safe_load(file)
        for key, value in data.items():
            print(key, ":", value)
    except yaml.YAMLError as exception:
        print(exception)

