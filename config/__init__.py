import os
import yaml

from easydict import EasyDict


def create_config():
    result = None

    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'config.yml')

    try:
        with open(file_path, 'r') as f:
            result = yaml.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            'You should generate the config.yml with configure.sh')

    if not result:
        print('Loading YAML failed')

    config = EasyDict(result)
    return config


config = create_config()
