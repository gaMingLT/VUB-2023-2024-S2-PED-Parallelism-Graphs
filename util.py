import numpy as np


divide = 1000000  # naar seconden


def scale_data(data):
    for value in data:
        data[value]['scaled']['mean'] = data[value]['original']['mean'] / divide  # discard the first 5 values
    return data


def get_mean(data):
    for value in data:
        data[value]['original']['mean'] = np.mean(data[value]['original']['values'][4:])  # discard the first 5 values
    return data


# Divide by the SEQ
def overhead(data):
    data["TEXT1"]["scaled"]["overhead"] = data["TEXT1"]["scaled"]["mean"] / data["SEQ"]["scaled"]["mean"]
    data["ARTICLE1"]["scaled"]["overhead"] = data["ARTICLE1"]["scaled"]["mean"] / data["SEQ"]["scaled"]["mean"]

    return data


# Divide any by the SEQ
def application_speedup(data):
    seq_mean = data["SEQ"]["scaled"]["mean"]

    for value in data:
        if value != 'SEQ':
            data[value]['scaled']['application_speedup'] = seq_mean / data[value]['scaled']['mean']

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

            data[value]['scaled']['computational_speedup'] = data[to]['scaled']['mean'] / data[value]['scaled']['mean']

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

            data[value]['scaled']['efficiency'] = data[to]['scaled']['mean'] / (workers * data[value]['scaled']['mean'])

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

