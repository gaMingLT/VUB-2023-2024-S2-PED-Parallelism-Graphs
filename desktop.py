import time
import os

from analyse import util
from analyse.desktop import application, computational, efficiency, overhead, runtime, general


def load_data_from_files():
    # Load the data for the large data
    filename = "desktop/runtimes_Large_desktop.csv"
    data_large = util.read_from_file(filename)

    # Load the data for the larger dataset
    filename = "desktop/runtimes_Larger_desktop.csv"
    data_larger = util.read_from_file(filename)

    return data_large, data_larger


def analyse_dataset_desktop(dataset, data):
    path = "desktop/graphs/"+dataset

    if not os.path.exists(path):
        os.mkdir(path)

    dataset_parameters = util.get_dataset_parameters(data)
    scaled = util.scale_data(dataset_parameters)
    data = scaled

    overhead_data = util.overhead(data)
    overhead.print_overhead(path, dataset, overhead_data)

    # Confidence Interval
    general.plot_confidence_interval_for_keys(path, dataset, data)

    runtime.plot_articles_and_text(path, dataset, data)

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
    # computational.plot_computational_speedup_text_cutoffs(path, dataset, data)
    # efficiency.plot_efficiency_speedup_text_cutoffs(path, dataset, data)

    # # The following plots are for different cutoffs of the text
    # runtime.plot_runtime_article_cutoffs(path, dataset, data)
    # application.plot_application_speedup_article_cutoffs(path, dataset, data)
    # computational.plot_computational_speedup_article_cutoffs(path, dataset, data)
    # efficiency.plot_efficiency_speedup_article_cutoffs(path, dataset, data)
    #
    # runtime.plot_thresholds_article_and_text_runtime(path, dataset, data)

    return data


def plot_combinations(large, larger):
    combined = "combined"
    path = "desktop/graphs/"+combined

    if not os.path.exists(path):
        os.mkdir(path)

    application.plot_application_speedup_combined(path,{'large': large, 'larger': larger}, ['large', 'larger'])
    computational.plot_computational_speedup_combined(path,{'large': large, 'larger': larger}, ['large', 'larger'])

    runtime.plot_articles_and_text_combined(path,{'large': large, 'larger': larger}, ['large', 'larger'])

    application.plot_articles_and_text_application_combined(path, {'large': large, 'larger': larger}, ['large', 'larger'])
    computational.plot_articles_and_text_computational_combined(path, {'large': large, 'larger': larger}, ['large', 'larger'])

    overhead.plot_thresholds_article_and_text_overhead_combined(path, {'large': large, 'larger': larger}, ['large', 'larger'])


if __name__ == '__main__':
    large, larger = load_data_from_files()
    path = "desktop/graphs/"

    if not os.path.exists(path):
        os.mkdir(path)

    data_large = analyse_dataset_desktop("large", large)
    time.sleep(2)  # so we don't get error when generating a lot of graphs

    data_larger = analyse_dataset_desktop("larger", larger)
    time.sleep(2)

    # plot_combinations(data_large, data_larger)
