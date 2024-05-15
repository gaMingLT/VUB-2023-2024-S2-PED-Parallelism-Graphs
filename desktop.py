import time
import os

from analyse import util
from analyse.desktop import application, computational, efficiency, overhead, runtime, general


def load_data_from_files():
    # Load the data for the small data
    filename = "desktop/runtimes_Small_desktop.csv"
    data_small = util.read_from_file(filename)

    # Load the data for the larger dataset
    filename = "desktop/runtimes_Medium_desktop.csv"
    data_medium = util.read_from_file(filename)

    # Load the data for the large data
    filename = "desktop/runtimes_Large_desktop.csv"
    data_large = util.read_from_file(filename)

    # Load the data for the larger dataset
    filename = "desktop/runtimes_Larger_desktop.csv"
    data_larger = util.read_from_file(filename)

    return data_small, data_medium, data_large, data_larger


def analyse_dataset_desktop(dataset, data):
    path = "desktop/graphs/"+dataset

    if not os.path.exists(path):
        os.mkdir(path)

    dataset_parameters = util.get_dataset_parameters(data)
    scaled = util.scale_data(dataset_parameters)
    data = scaled

    data = util.overhead(data)
    overhead.print_overhead(path, dataset, data)
    overhead.plot_thresholds_article_and_text_overhead(path, dataset, data)

    # # Confidence Interval
    # general.plot_confidence_interval_for_articles_between(path, dataset, data)
    # general.plot_confidence_interval_text_between(path, dataset, data)

    # runtime.plot_articles_and_text(path, dataset, data)

    # Application Speedup
    data = util.application_speedup(data)
    # plot_application_speedup(path, dataset, data)

    # Computational Speedup
    data = util.computational_speedup(data)
    # plot_computational_speedup(path, dataset, data)

    # Efficiency
    data = util.efficiency(data)
    # plot_efficiency(path, dataset, data)

    # # The following plots are for different cutoffs of the text
    # runtime.plot_runtime_text_cutoffs(path, dataset, data)
    # application.plot_application_speedup_text_cutoffs(path, dataset, data)
    #
    # time.sleep(1)
    #
    # computational.plot_computational_speedup_text_cutoffs(path, dataset, data)
    # efficiency.plot_efficiency_speedup_text_cutoffs(path, dataset, data)
    #
    # time.sleep(2)
    #
    # # The following plots are for different cutoffs of the text
    # runtime.plot_runtime_article_cutoffs(path, dataset, data)
    # application.plot_application_speedup_article_cutoffs(path, dataset, data)
    #
    # time.sleep(1)
    #
    # computational.plot_computational_speedup_article_cutoffs(path, dataset, data)
    # efficiency.plot_efficiency_speedup_article_cutoffs(path, dataset, data)
    #
    # runtime.plot_thresholds_article_and_text_runtime(path, dataset, data)

    return data


def plot_combinations(small, medium, large, larger):
    combined = "combined"
    path = "desktop/graphs/"+combined

    if not os.path.exists(path):
        os.mkdir(path)

    dataset_parameters = {'small': small, 'medium': medium, 'large': large, 'larger': larger}
    dataset_keys = ['small', 'medium', 'large', 'larger']

    general.plot_confidence_interval_articles_combined_inbetween(path, dataset_parameters, ['medium', 'large', 'larger'])
    general.plot_confidence_interval_text_combined_inbetween(path, dataset_parameters, ['medium', 'large', 'larger'])

    time.sleep(2)

    application.plot_application_speedup_combined(path, dataset_parameters, dataset_keys)
    computational.plot_computational_speedup_combined(path, dataset_parameters, dataset_keys)
    runtime.plot_articles_and_text_combined(path, dataset_parameters, dataset_keys)

    time.sleep(2)

    application.plot_articles_and_text_application_combined(path, dataset_parameters, dataset_keys)
    computational.plot_articles_and_text_computational_combined(path, dataset_parameters, dataset_keys)

    overhead.plot_thresholds_article_and_text_overhead_combined(path, dataset_parameters, ['medium', 'large', 'larger'])
    overhead.plot_overhead_combined(path, dataset_parameters, ['small', 'medium', 'large', 'larger'])


if __name__ == '__main__':
    small, medium, large, larger = load_data_from_files()
    path = "desktop/graphs/"

    if not os.path.exists(path):
        os.mkdir(path)

    data_small = analyse_dataset_desktop("small", small)
    time.sleep(2)

    data_medium = analyse_dataset_desktop("medium", medium)
    time.sleep(2)

    data_large = analyse_dataset_desktop("large", large)
    time.sleep(2)  # so we don't get error when generating a lot of graphs

    data_larger = analyse_dataset_desktop("larger", larger)
    time.sleep(2)

    plot_combinations(data_small, data_medium, data_large, data_larger)
