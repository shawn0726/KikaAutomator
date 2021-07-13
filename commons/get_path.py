import os

import yaml


def get_path_data(path):  # '/layout/candidate_layout'
    script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = script_path_up + path
    test_case_data = yaml.safe_load(open(data_path, 'r'))
    return test_case_data


def get_path(path):  # '/layout/candidate_layout'
    script_path_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = script_path_up + path
    return data_path
