import os

import matplotlib.pyplot as plt

SOURCE = "scaled"


def print_overhead(path, dataset, data):
    print("Overhead {}".format(dataset))
    print("Text: " + str(data["TEXT1"][SOURCE]['overhead']))
    print("ARTICLE1: " + str(data["ARTICLE1"][SOURCE]["overhead"]))


def plot_articles_and_text(path, dataset, data):
    x = [1, 16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE1"][SOURCE]["mean"], data["ARTICLE16"][SOURCE]["mean"],
                  data["ARTICLE32"][SOURCE]["mean"], data["ARTICLE64"][SOURCE]["mean"],
                  data["ARTICLE128"][SOURCE]["mean"]]
    y_text = [data["TEXT1"][SOURCE]["mean"], data["TEXT16"][SOURCE]["mean"],
              data["TEXT32"][SOURCE]["mean"], data["TEXT64"][SOURCE]["mean"],
              data["TEXT128"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Articles & Text")
    ax.set_xlabel("Workers")
    ax.set_ylabel("Milliseconds")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_and_text.svg')

    plt.show()


def plot_application_speedup(path, dataset, data):
    x = [1, 16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE1"][SOURCE]["application_speedup"], data["ARTICLE16"][SOURCE]["application_speedup"],
                  data["ARTICLE32"][SOURCE]["application_speedup"], data["ARTICLE64"][SOURCE]["application_speedup"],
                  data["ARTICLE128"][SOURCE]["application_speedup"]]
    y_text = [data["TEXT1"][SOURCE]["application_speedup"], data["TEXT16"][SOURCE]["application_speedup"],
              data["TEXT32"][SOURCE]["application_speedup"], data["TEXT64"][SOURCE]["application_speedup"],
              data["TEXT128"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Application Speedup")
    ax.set_xlabel("Workers")

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


def plot_computational_speedup(path, dataset, data):
    x = [16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE16"][SOURCE]["computational_speedup"],
                  data["ARTICLE32"][SOURCE]["computational_speedup"],
                  data["ARTICLE64"][SOURCE]["computational_speedup"],
                  data["ARTICLE128"][SOURCE]["computational_speedup"]]
    y_text = [data["TEXT16"][SOURCE]["computational_speedup"],
              data["TEXT32"][SOURCE]["computational_speedup"],
              data["TEXT64"][SOURCE]["computational_speedup"],
              data["TEXT128"][SOURCE]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Computational Speedup")
    ax.set_xlabel("Workers")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/computational_speedup.svg')

    plt.show()


def plot_efficiency(path, dataset, data):
    x = [16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE16"][SOURCE]["efficiency"],
                  data["ARTICLE32"][SOURCE]["efficiency"],
                  data["ARTICLE64"][SOURCE]["efficiency"],
                  data["ARTICLE128"][SOURCE]["efficiency"]]
    y_text = [data["TEXT16"][SOURCE]["efficiency"],
              data["TEXT32"][SOURCE]["efficiency"],
              data["TEXT64"][SOURCE]["efficiency"],
              data["TEXT128"][SOURCE]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Efficiency")
    ax.set_xlabel("Workers")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/efficiency.svg')

    plt.show()


def plot_runtime_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["mean"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_runtime.svg')

    plt.show()


# def plot_application_speedup_text_cutoffs(path, dataset, data):
#     x = [1000, 2500, 5000]  # cutoff
#
#     y_text_application_speedup = [data["TEXT_1000_12"][SOURCE]["application_speedup"],
#                                   data["TEXT_2500_12"][SOURCE]["application_speedup"],
#                                   data["TEXT_5000_12"][SOURCE]["application_speedup"]]
#
#     fig, ax = plt.subplots()
#     ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
#     ax.set_xlabel("Characters Sequential")
#
#     ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')
#     # ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')
#
#     ax.legend(loc='upper right')
#
#     fig.savefig(path + '/text_cutoffs_speedup.svg')
#
#     plt.show()
#
#
# def plot_computational_speedup_text_cutoffs(path, dataset, data):
#     x = [1000, 2500, 5000]  # cutoff
#
#     y_text_computational_speedup = [data["TEXT_1000_12"][SOURCE]["computational_speedup"],
#                                     data["TEXT_2500_12"][SOURCE]["computational_speedup"],
#                                     data["TEXT_5000_12"][SOURCE]["computational_speedup"]]
#
#     fig, ax = plt.subplots()
#     ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
#     ax.set_xlabel("Characters Sequential")
#
#     ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')
#
#     ax.legend(loc='upper right')
#
#     fig.savefig(path + '/text_cutoffs_comp.svg')
#
#     plt.show()
#
#
# def plot_efficiency_speedup_text_cutoffs(path, dataset, data):
#     x = [1000, 2500, 5000]  # cutoff
#
#     y_text_efficiency = [data["TEXT_1000_12"][SOURCE]["efficiency"],
#                          data["TEXT_2500_12"][SOURCE]["efficiency"],
#                          data["TEXT_5000_12"][SOURCE]["efficiency"]]
#
#     fig, ax = plt.subplots()
#     ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
#     ax.set_xlabel("Characters Sequential")
#
#     ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')
#
#     ax.legend(loc='upper right')
#
#     fig.savefig(path + '/text_cutoffs_efficiency.svg')
#
#     plt.show()
#
#
def plot_runtime_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["mean"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_runtime.svg')

    plt.show()


# def plot_application_speedup_article_cutoffs(path, dataset, data):
#     x = [1000, 2500, 5000]  # cutoff
#
#     y_text_application_speedup = [data["ARTICLE_1000_12"][SOURCE]["application_speedup"],
#                                   data["ARTICLE_2500_12"][SOURCE]["application_speedup"],
#                                   data["ARTICLE_5000_12"][SOURCE]["application_speedup"]]
#
#     fig, ax = plt.subplots()
#     ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
#     ax.set_xlabel("Articles Sequential")
#
#     ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')
#     # ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')
#
#     ax.legend(loc='upper right')
#
#     fig.savefig(path + '/article_cutoffs_speedup.svg')
#
#     plt.show()
#
#
# def plot_computational_speedup_article_cutoffs(path, dataset, data):
#     x = [1000, 2500, 5000]  # cutoff
#
#     y_text_computational_speedup = [data["ARTICLE_1000_12"][SOURCE]["computational_speedup"],
#                                     data["ARTICLE_2500_12"][SOURCE]["computational_speedup"],
#                                     data["ARTICLE_5000_12"][SOURCE]["computational_speedup"]]
#
#     fig, ax = plt.subplots()
#     ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
#     ax.set_xlabel("Articles Sequential")
#
#     ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')
#
#     ax.legend(loc='upper right')
#
#     fig.savefig(path + '/article_cutoffs_comp.svg')
#
#     plt.show()
#
#
# def plot_efficiency_speedup_article_cutoffs(path, dataset, data):
#     x = [1000, 2500, 5000]  # cutoff
#
#     y_text_efficiency = [data["ARTICLE_1000_12"][SOURCE]["efficiency"],
#                          data["ARTICLE_2500_12"][SOURCE]["efficiency"],
#                          data["ARTICLE_5000_12"][SOURCE]["efficiency"]]
#
#     fig, ax = plt.subplots()
#     ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
#     ax.set_xlabel("Articles Sequential")
#
#     ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')
#
#     ax.legend(loc='upper right')
#
#     fig.savefig(path + '/article_cutoffs_efficiency.svg')
#
#     plt.show()


def plot_computational_speedup_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["computational_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Computational')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_computational_speedup.svg')

    plt.show()


def plot_application_speedup_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["application_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Application')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_application_speedup.svg')

    plt.show()


def plot_computational_speedup_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["computational_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Computational')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_computational_speedup.svg')

    plt.show()


def plot_application_speedup_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["application_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Application')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_application_speedup.svg')

    plt.show()
