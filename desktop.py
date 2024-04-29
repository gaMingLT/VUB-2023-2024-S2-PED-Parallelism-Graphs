from util import *
from analyze_desktop import *


def load_data_from_files():
    # Load the data for the large data
    filename = "desktop/runtimes_Large_desktop.csv"
    data_large = read_from_file(filename)

    # Load the data for the larger dataset
    filename = "desktop/runtimes_Larger_desktop.csv"
    data_larger = read_from_file(filename)

    return data_large, data_larger


def analyse_dataset_desktop(dataset, data):
    path = "desktop/graphs/"+dataset

    if not os.path.exists(path):
        os.mkdir(path)

    mean = get_mean(data)
    scaled = scale_data(mean)

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

    # The following plots are for different cutoffs of the text
    plot_runtime_text_cutoffs(path, dataset, data)
    plot_application_speedup_text_cutoffs(path, dataset, data)
    plot_computational_speedup_text_cutoffs(path, dataset, data)
    plot_efficiency_speedup_text_cutoffs(path, dataset, data)

    # The following plots are for different cutoffs of the text
    plot_runtime_article_cutoffs(path, dataset, data)
    plot_application_speedup_article_cutoffs(path, dataset, data)
    plot_computational_speedup_article_cutoffs(path, dataset, data)
    plot_efficiency_speedup_article_cutoffs(path, dataset, data)


if __name__ == '__main__':
    large, larger = load_data_from_files()

    analyse_dataset_desktop("large", large)
    analyse_dataset_desktop("larger", larger)
