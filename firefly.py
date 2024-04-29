from util import *
import os
from analyze_firefly import *


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
    path = "firefly/graphs/"

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


if __name__ == '__main__':
    data_32, data_64, data_128, data_all_around, data_speed = load_data_from_files()

    analyse_all_around("firefly", data_all_around)
