import os

import matplotlib.pyplot as plt

SOURCE = "original"


# DONE
def print_overhead(path, dataset, data):
    print("Overhead {}".format(dataset))
    print("Text: " + str(data["TEXT1"]["original"]['overhead']))
    print("ARTICLE1: " + str(data["ARTICLE1"]["original"]["overhead"]))


# DONE
def plot_articles_and_text(path, dataset, data):
    x = [1, 16, 32, 64, 128]  # cores
    SOURCE = 'scaled'
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


# DONE
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
    ax.set_xlabel("Application Speedup")

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper left')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


# DONE
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
    ax.set_xlabel("Computational Speedup")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper left')

    fig.savefig(path + '/computational_speedup.svg')

    plt.show()


# DONE
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
    ax.set_xlabel("Efficiency")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper left')

    fig.savefig(path + '/efficiency.svg')

    plt.show()


# DONE
def plot_runtime_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    SOURCE = "scaled"

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["mean"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("Characters Sequential")
    ax.set_ylabel("Milliseconds")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_runtime.svg')

    plt.show()


# DONE
def plot_runtime_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    SOURCE = "scaled"

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["mean"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("Articles Sequential")
    ax.set_ylabel("Milliseconds")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_runtime.svg')

    plt.show()


# DONE
def plot_computational_speedup_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["computational_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("Articles Sequential")
    ax.set_ylabel("Computational Speedup")

    ax.plot(x, y_text_runtime, '-o', label='Computational')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_computational_speedup.svg')

    plt.show()


# DONE
def plot_application_speedup_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["application_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("Articles Sequential")
    ax.set_ylabel("Application Speedup")

    ax.plot(x, y_text_runtime, '-o', label='Application')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_application_speedup.svg')

    plt.show()


# DONE
def plot_computational_speedup_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["computational_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("Characters Sequential")
    ax.set_ylabel("Computational Speedup")

    ax.plot(x, y_text_runtime, '-o', label='Computational')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_computational_speedup.svg')

    plt.show()


# DONE
def plot_application_speedup_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["application_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("Characters Sequential")
    ax.set_ylabel("Computational Speedup")

    ax.plot(x, y_text_runtime, '-o', label='Application')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_application_speedup.svg')

    plt.show()


# DONE
def plot_thresholds_article_and_text_overhead_combined(path, datasets, dataset_values):
    x = [250, 500, 750, 1000, 2500, 5000]  # cutoff

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        dataset_object = datasets[dataset]
        data = dataset_object['values']

        y_articles = []
        for key in dataset_object['article']:
            y_articles.append(data[key][SOURCE]['overhead'])

        y_text = []
        for key in dataset_object['text']:
            y_text.append(data[key][SOURCE]['overhead'])

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Article & Text Cutoffs")
    ax.set_xlabel("Text & Articles Sequentially")
    ax.set_ylabel("Overhead")

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_overhead.svg')

    plt.show()
