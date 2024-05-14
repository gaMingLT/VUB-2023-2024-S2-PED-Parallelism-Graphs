import logging

import numpy as np
from scipy.stats import t

MILLISECONDS = 1000000
SECONDS = 1000000000

divide = SECONDS  # to value

confidence_level = 0.95
alpha = 1 - confidence_level

util_logger = logging.getLogger('util')
util_logger.setLevel(logging.INFO)


def scale_data(data):
    for value in data:
        value_data = data[value]['original']['values'][4:]  # discard the first 5 values
        mean = data[value]['original']['mean'] / divide
        std = data[value]['original']['std'] / divide
        min_value = data[value]['original']['min'] / divide
        max_value = data[value]['original']['max'] / divide
        margin_of_error = data[value]['original']['margin_of_error'] / divide
        lower_bound = data[value]['original']['lower_bound'] / divide
        upper_bound = data[value]['original']['upper_bound'] / divide

        data[value] = {'scaled': {}, 'original': data[value]['original']}

        data[value]['scaled']['mean'] = mean
        data[value]['scaled']['std'] = std
        data[value]['scaled']['min'] = min_value
        data[value]['scaled']['max'] = max_value
        data[value]['scaled']['margin_of_error'] = margin_of_error
        data[value]['scaled']['lower_bound'] = lower_bound
        data[value]['scaled']['upper_bound'] = upper_bound

        # n = len(value_data)
        # df = n - 1
        # t_critical = t.ppf(1 - alpha / 2, df)
        # margin_of_error = t_critical * (std / np.sqrt(n))

        # print("=== Dataset Parameters ===")
        # print("Dataset parameters: " + str(value))
        # print("Confidence level: " + str(alpha))
        # print("Margin of error: {}".format(margin_of_error))
        # print("lower_bound: {}, upper_bound: {}".format(lower_bound, upper_bound))
        # print("======== End of Dataset Parameters ======")

    return data


def get_dataset_parameters(data):
    for value in data:

        len_values = np.array(data[value]['original']['values']).size
        if len_values != 15 and len_values != 35:
            raise ValueError("Length of data is not in expected ranges: " + str(len_values))

        value_data = data[value]['original']['values'][4:]  # discard the first 5 values
        mean = np.mean(value_data)
        min_value = np.min(value_data)
        max_value = np.max(value_data)
        std = np.std(value_data)

        n = len(value_data)
        df = n - 1

        t_critical = t.ppf(1 - alpha / 2, df)
        margin_of_error = t_critical * (std / np.sqrt(n))
        lower_bound = mean - margin_of_error
        upper_bound = mean + margin_of_error

        data[value]['original']['without_warmups'] = value_data  # replace the original data values with 5 less runs
        data[value]['original']['mean'] = mean
        data[value]['original']['min'] = min_value
        data[value]['original']['max'] = max_value
        data[value]['original']['std'] = std
        data[value]['original']['margin_of_error'] = margin_of_error
        data[value]['original']['lower_bound'] = lower_bound
        data[value]['original']['upper_bound'] = upper_bound

    return data


# Divide by the SEQ
def overhead(data):
    data["TEXT1"]["original"]["overhead"] = data["TEXT1"]["original"]["mean"] / data["SEQ"]["original"]["mean"]
    data["ARTICLE1"]["original"]["overhead"] = data["ARTICLE1"]["original"]["mean"] / data["SEQ"]["original"]["mean"]

    to = data["SEQ"]["original"]["mean"]
    for value in data:
        if value != 'SEQ':
            data[value]["original"]["overhead"] = data[value]["original"]["mean"] / to

    return data


# Divide any by the SEQ
def application_speedup(data):
    seq_mean = data["SEQ"]["original"]["mean"]

    for value in data:
        if value != 'SEQ':
            data[value]["original"]['application_speedup'] = seq_mean / data[value]["original"]['mean']

    return data


# Divide to either TEXT1 or ARTICLE
def computational_speedup(data):
    for value in data:
        if value != 'SEQ' and value != 'TEXT1' and value != 'ARTICLE1':
            to = ""
            if "ARTICLE" in value:
                to = "ARTICLE1"
            elif "TEXT" in value:
                to = "TEXT1"

            data[value]["original"]['computational_speedup'] = data[to]["original"]['mean'] / data[value]["original"]['mean']

    return data


def efficiency(data):
    for value in data:
        if value != 'SEQ' and value != 'TEXT1' and value != 'ARTICLE1':
            to = ""
            if "ARTICLE" in value:
                to = "ARTICLE1"
            elif "TEXT" in value:
                to = "TEXT1"

            workers = 0
            if "4" in value:
                workers = 4
            elif "8" in value:
                workers = 8
            elif "12" in value:
                workers = 12
            elif "16" in value:
                workers = 16
            elif "32" in value:
                workers = 32
            elif "64" in value:
                workers = 64
            elif "128" in value:
                workers = 128

            data[value]["original"]['efficiency'] = data[to]["original"]['mean'] / (workers * data[value]["original"]['mean'])

    return data


def read_from_file(filename):
    data = {}
    f = open(filename, 'r')

    for line in f:
        split = line.split(',')
        data[split[0]] = {
            'original': {
                'values': np.array(split[1:], dtype=float),
                'mean': 0
            },
            'scaled': {
                'values': [],
                'mean': 0
            }
        }
        # data[split[0]]['original'] = {}
        # data[split[0]]['original']['values'] = np.array(split[1:], dtype=float)

    return data
