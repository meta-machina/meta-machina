# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import githf
import yaml
import ruamel.yaml as ryaml


MACHINE_ORGANIZATION_NAME = 'name-of-the-machine'  # or other organization
PRIVATE_REPO_WITH_TEXT = 'machine-machine'

try:
    gh = githf.connectto_repo(organization=MACHINE_ORGANIZATION_NAME,
                              repository_name=PRIVATE_REPO_WITH_TEXT,
                              private=True)
    MACHINE_YAML = githf.read_file(repository=gh, file_path='texts_of_the_machine.yaml')
    NAME_OF_THE_MACHINE = yaml.load(MACHINE_YAML, Loader=yaml.FullLoader)
except Exception as e:
    with open('machina.yaml', 'r') as f:
        NAME_OF_THE_MACHINE= ryaml.load(f)
"""
"""


if __name__ == '__main__':
    print('You have launched main')

