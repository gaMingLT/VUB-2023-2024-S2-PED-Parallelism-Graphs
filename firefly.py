import time

from analyze_firefly import *
from util import *


def load_data_from_files():
    filename = "firefly/runtimes_Firefly_all_around.csv"
    data_all_around = read_from_file(filename)

    filename = "firefly/runtimes_Firefly_speed.csv"
    data_speed = read_from_file(filename)

    filename = "firefly/runtimes_Firefly_32.csv"
    data_32 = read_from_file(filename)

    filename = "firefly/runtimes_Firefly_64.csv"
    data_64 = read_from_file(filename)

    filename = "firefly/runtimes_Firefly_128.csv"
    data_128 = read_from_file(filename)

    return data_32, data_64, data_128, data_all_around, data_speed


def analyse_all_around(dataset, data):
    mean = get_dataset_parameters(data)
    scaled = scale_data(mean)

    overhead_data = overhead(data)
    print_overhead(path, dataset, overhead_data)

    plot_articles_and_text(path, dataset, scaled)

    # Application Speedup
    data = application_speedup(scaled)
    plot_application_speedup(path, dataset, data)

    # Computational Speedup
    data = computational_speedup(data)
    plot_computational_speedup(path, dataset, data)

    # Efficiency
    data = efficiency(data)
    plot_efficiency(path, dataset, data)


def analyze_128(dataset, data):
    workers = 128
    path = "firefly/graphs/" + str(workers)

    if not os.path.exists(path):
        os.mkdir(path)

    mean = get_dataset_parameters(data)
    data = overhead(mean)
    scaled = scale_data(data)

    # Application Speedup
    data = application_speedup(scaled)
    # plot_application_speedup(path, dataset, data)

    # Computational Speedup
    data = computational_speedup(data)
    # plot_computational_speedup(path, dataset, data)

    # Efficiency
    data = efficiency(data)
    # plot_efficiency(path, dataset, data)

    text_cutoffs = [100, 250, 500, 750, 1000, 2500, 5000]
    text_keys = ['TEXT100_128', 'TEXT250_128', 'TEXT500_128', 'TEXT750_128', 'TEXT1000_128', 'TEXT2500_128',
                 'TEXT5000_128']

    plot_runtime_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)
    plot_computational_speedup_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)
    plot_application_speedup_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)

    article_cutoffs = [250, 500, 750, 1000, 2500, 5000]
    article_keys = ['ARTICLE_250_128', 'ARTICLE_500_128', 'ARTICLE_750_128', 'ARTICLE_1000_128', 'ARTICLE_2500_128',
                    'ARTICLE_5000_128']

    plot_runtime_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)
    plot_computational_speedup_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)
    plot_application_speedup_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)

    return data


def analyze_64(dataset, data):
    workers = 64
    path = "firefly/graphs/" + str(workers)

    if not os.path.exists(path):
        os.mkdir(path)

    mean = get_dataset_parameters(data)
    data = overhead(mean)
    scaled = scale_data(data)

    # Application Speedup
    data = application_speedup(scaled)
    # plot_application_speedup(path, dataset, data)

    # Computational Speedup
    data = computational_speedup(data)
    # plot_computational_speedup(path, dataset, data)

    # Efficiency
    data = efficiency(data)
    # plot_efficiency(path, dataset, data)

    text_cutoffs = [100, 250, 500, 750, 1000, 2500, 5000]
    text_keys = ['TEXT100_64', 'TEXT250_64', 'TEXT500_64', 'TEXT750_64', 'TEXT1000_64', 'TEXT2500_64', 'TEXT5000_64']

    plot_runtime_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)
    plot_computational_speedup_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)
    plot_application_speedup_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)

    article_cutoffs = [250, 500, 750, 1000, 2500, 5000]
    article_keys = ['ARTICLE_250_64', 'ARTICLE_500_64', 'ARTICLE_750_64', 'ARTICLE_1000_64', 'ARTICLE_2500_64',
                    'ARTICLE_5000_64']

    plot_runtime_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)
    plot_computational_speedup_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)
    plot_application_speedup_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)

    return data


def analyze_32(dataset, data):
    workers = 32
    path = "firefly/graphs/" + str(workers)

    if not os.path.exists(path):
        os.mkdir(path)

    mean = get_dataset_parameters(data)
    data = overhead(mean)
    scaled = scale_data(data)

    # Application Speedup
    data = application_speedup(scaled)
    # plot_application_speedup(path, dataset, data)

    # Computational Speedup
    data = computational_speedup(data)
    # plot_computational_speedup(path, dataset, data)

    # Efficiency
    data = efficiency(data)
    # plot_efficiency(path, dataset, data)

    text_cutoffs = [100, 250, 500, 750, 1000, 2500, 5000]
    text_keys = ['TEXT100_32', 'TEXT250_32', 'TEXT500_32', 'TEXT750_32', 'TEXT1000_32', 'TEXT2500_32', 'TEXT5000_32']

    plot_runtime_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)
    plot_computational_speedup_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)
    plot_application_speedup_text_cutoffs(path, dataset, data, text_cutoffs, text_keys, workers)

    article_cutoffs = [250, 500, 750, 1000, 2500, 5000]
    article_keys = ['ARTICLE_250_32', 'ARTICLE_500_32', 'ARTICLE_750_32', 'ARTICLE_1000_32', 'ARTICLE_2500_32',
                    'ARTICLE_5000_32']

    plot_runtime_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)
    plot_computational_speedup_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)
    plot_application_speedup_article_cutoffs(path, dataset, data, article_cutoffs, article_keys, workers)

    return data


def plot_combinations(data_128, data_64, data_32):
    combined = "combined"
    path = "firefly/graphs/" + combined

    if not os.path.exists(path):
        os.mkdir(path)

    datasets = {'128': {'values': data_128,
                        'text': ['TEXT250_128',
                                 'TEXT500_128', 'TEXT750_128',
                                 'TEXT1000_128', 'TEXT2500_128',
                                 'TEXT5000_128'],
                        'article': ['ARTICLE_250_128', 'ARTICLE_500_128',
                                    'ARTICLE_750_128', 'ARTICLE_1000_128',
                                    'ARTICLE_2500_128',
                                    'ARTICLE_5000_128']
                        },
                '64': {
                    'values': data_64,
                    'text': ['TEXT250_64', 'TEXT500_64', 'TEXT750_64',
                             'TEXT1000_64', 'TEXT2500_64', 'TEXT5000_64'],
                    'article': ['ARTICLE_250_64', 'ARTICLE_500_64',
                                'ARTICLE_750_64', 'ARTICLE_1000_64',
                                'ARTICLE_2500_64',
                                'ARTICLE_5000_64']
                },
                '32': {
                    'values': data_32,
                    'text': ['TEXT250_32', 'TEXT500_32', 'TEXT750_32', 'TEXT1000_32', 'TEXT2500_32', 'TEXT5000_32'],
                    'article': ['ARTICLE_250_32', 'ARTICLE_500_32', 'ARTICLE_750_32', 'ARTICLE_1000_32',
                                'ARTICLE_2500_32',
                                'ARTICLE_5000_32']
                }}

    plot_thresholds_article_and_text_overhead_combined(path, datasets, ['128', '64', '32'])


if __name__ == '__main__':
    data_32, data_64, data_128, data_all_around, data_speed = load_data_from_files()

    path = "firefly/graphs/"

    if not os.path.exists(path):
        os.mkdir(path)

    analyse_all_around("firefly", data_all_around)


    # 128 Workers
    data_128['SEQ'] = {'original': {'values': data_all_around['SEQ']['original']['values']}}
    data_128['TEXT1'] = {'original': {'values': data_all_around['TEXT1']['original']['values']}}
    data_128['ARTICLE1'] = {'original': {'values': data_all_around['ARTICLE1']['original']['values']}}

    data_128 = analyze_128("firefly", data_128)

    time.sleep(2)

    # 64 Workers
    data_64['SEQ'] = {'original': {'values': data_all_around['SEQ']['original']['values']}}
    data_64['TEXT1'] = {'original': {'values': data_all_around['TEXT1']['original']['values']}}
    data_64['ARTICLE1'] = {'original': {'values': data_all_around['ARTICLE1']['original']['values']}}

    data_64 = analyze_64("firefly", data_64)

    time.sleep(2)

    # 32 Workers
    data_32['SEQ'] = {'original': {'values': data_all_around['SEQ']['original']['values']}}
    data_32['TEXT1'] = {'original': {'values': data_all_around['TEXT1']['original']['values']}}
    data_32['ARTICLE1'] = {'original': {'values': data_all_around['ARTICLE1']['original']['values']}}

    data_32 = analyze_32("firefly", data_32)

    plot_combinations(data_128, data_64, data_32)
