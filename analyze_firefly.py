import os

import matplotlib.pyplot as plt


def plot_articles_and_text(path, dataset, data):
    x = [1, 16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE1"]["scaled"]["mean"], data["ARTICLE16"]["scaled"]["mean"],
                  data["ARTICLE32"]["scaled"]["mean"], data["ARTICLE64"]["scaled"]["mean"],
                  data["ARTICLE128"]["scaled"]["mean"]]
    y_text = [data["TEXT1"]["scaled"]["mean"], data["TEXT16"]["scaled"]["mean"],
              data["TEXT32"]["scaled"]["mean"], data["TEXT64"]["scaled"]["mean"],
              data["TEXT128"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Articles & Text")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_and_text.pdf')

    plt.show()


def plot_application_speedup(path, dataset, data):
    x = [1, 16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE1"]["scaled"]["mean"], data["ARTICLE16"]["scaled"]["mean"],
                  data["ARTICLE32"]["scaled"]["mean"], data["ARTICLE64"]["scaled"]["mean"],
                  data["ARTICLE128"]["scaled"]["mean"]]
    y_text = [data["TEXT1"]["scaled"]["mean"], data["TEXT16"]["scaled"]["mean"],
              data["TEXT32"]["scaled"]["mean"], data["TEXT64"]["scaled"]["mean"],
              data["TEXT128"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Application Speedup")

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/application_speedup.pdf')

    plt.show()


def plot_computational_speedup(path, dataset, data):
    x = [16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE16"]["scaled"]["computational_speedup"],
                  data["ARTICLE32"]["scaled"]["computational_speedup"],
                  data["ARTICLE64"]["scaled"]["computational_speedup"],
                  data["ARTICLE128"]["scaled"]["computational_speedup"]]
    y_text = [data["TEXT16"]["scaled"]["computational_speedup"],
              data["TEXT32"]["scaled"]["computational_speedup"],
              data["TEXT64"]["scaled"]["computational_speedup"],
              data["TEXT128"]["scaled"]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Computational Speedup")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/computational_speedup.pdf')

    plt.show()


def plot_efficiency(path, dataset, data):
    x = [16, 32, 64, 128]  # cores
    y_articles = [data["ARTICLE16"]["scaled"]["efficiency"],
                  data["ARTICLE32"]["scaled"]["efficiency"],
                  data["ARTICLE64"]["scaled"]["efficiency"],
                  data["ARTICLE128"]["scaled"]["efficiency"]]
    y_text = [data["TEXT16"]["scaled"]["efficiency"],
              data["TEXT32"]["scaled"]["efficiency"],
              data["TEXT64"]["scaled"]["efficiency"],
              data["TEXT128"]["scaled"]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Efficiency")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/efficiency.pdf')

    plt.show()
