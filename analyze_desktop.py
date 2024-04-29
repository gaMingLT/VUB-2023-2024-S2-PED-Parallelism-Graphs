import os.path
import matplotlib.pyplot as plt


def plot_articles(data):
    x = [1, 4, 8, 12]  # cores
    y = [data["ARTICLE1"]["scaled"]["mean"], data["ARTICLE4"]["scaled"]["mean"], data["ARTICLE8"]["scaled"]["mean"],
         data["ARTICLE12"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title("Article Statistics")

    ax.plot(x, y, '-o', label='Articles')
    ax.legend(loc='upper right')

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    fig.savefig('desktop/graphs/articles.pdf')

    plt.show()


def plot_text(data):
    x = [1, 4, 8, 12]  # cores
    y = [data["TEXT1"]["scaled"]["mean"], data["TEXT4"]["scaled"]["mean"], data["TEXT8"]["scaled"]["mean"],
         data["TEXT12"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title("Text Statistics")

    ax.plot(x, y, '-o', label='Text')
    ax.legend(loc='upper right')

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    fig.savefig('desktop/graphs/text.pdf')

    plt.show()


def plot_articles_and_text(path, dataset,  data):
    x = [1, 4, 8, 12]  # cores
    y_articles = [data["ARTICLE1"]["scaled"]["mean"], data["ARTICLE4"]["scaled"]["mean"],
                  data["ARTICLE8"]["scaled"]["mean"], data["ARTICLE12"]["scaled"]["mean"]]
    y_text = [data["TEXT1"]["scaled"]["mean"], data["TEXT4"]["scaled"]["mean"],
              data["TEXT8"]["scaled"]["mean"], data["TEXT12"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Articles & Text")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_and_text.pdf')

    plt.show()


def plot_application_speedup(path, dataset, data):
    x = [1, 4, 8, 12]  # cores
    y_articles = [data["ARTICLE1"]["scaled"]["application_speedup"], data["ARTICLE4"]["scaled"]["application_speedup"],
                  data["ARTICLE8"]["scaled"]["application_speedup"], data["ARTICLE12"]["scaled"]["application_speedup"]]
    y_text = [data["TEXT1"]["scaled"]["application_speedup"], data["TEXT4"]["scaled"]["application_speedup"],
              data["TEXT8"]["scaled"]["application_speedup"], data["TEXT12"]["scaled"]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Application Speedup")

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/application_speedup.pdf')

    plt.show()


def plot_computational_speedup(path, dataset,  data):
    x = [4, 8, 12]  # cores
    y_articles = [data["ARTICLE4"]["scaled"]["computational_speedup"],
                  data["ARTICLE8"]["scaled"]["computational_speedup"],
                  data["ARTICLE12"]["scaled"]["computational_speedup"]]
    y_text = [data["TEXT4"]["scaled"]["computational_speedup"],
              data["TEXT8"]["scaled"]["computational_speedup"],
              data["TEXT12"]["scaled"]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Computational Speedup")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/computational_speedup.pdf')

    plt.show()


def plot_efficiency(path, dataset, data):
    x = [4, 8, 12]  # cores
    y_articles = [data["ARTICLE4"]["scaled"]["efficiency"],
                  data["ARTICLE8"]["scaled"]["efficiency"],
                  data["ARTICLE12"]["scaled"]["efficiency"]]
    y_text = [data["TEXT4"]["scaled"]["efficiency"],
              data["TEXT8"]["scaled"]["efficiency"],
              data["TEXT12"]["scaled"]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Efficiency")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper right')

    fig.savefig(path + '/efficiency.pdf')

    plt.show()


def plot_runtime_text_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff
    y_text_runtime = [data["TEXT_1000_12"]["scaled"]["mean"], data["TEXT_2500_12"]["scaled"]["mean"],
                      data["TEXT_5000_12"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_runtime.pdf')

    plt.show()


def plot_application_speedup_text_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff

    y_text_application_speedup = [data["TEXT_1000_12"]["scaled"]["application_speedup"],
                                  data["TEXT_2500_12"]["scaled"]["application_speedup"],
                                  data["TEXT_5000_12"]["scaled"]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs")

    ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')
    # ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_speedup.pdf')

    plt.show()


def plot_computational_speedup_text_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff

    y_text_computational_speedup = [data["TEXT_1000_12"]["scaled"]["computational_speedup"],
                                    data["TEXT_2500_12"]["scaled"]["computational_speedup"],
                                    data["TEXT_5000_12"]["scaled"]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs")

    ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_comp.pdf')

    plt.show()


def plot_efficiency_speedup_text_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff

    y_text_efficiency = [data["TEXT_1000_12"]["scaled"]["efficiency"],
                         data["TEXT_2500_12"]["scaled"]["efficiency"],
                         data["TEXT_5000_12"]["scaled"]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs")

    ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper right')

    fig.savefig(path + '/text_cutoffs_efficiency.pdf')

    plt.show()


def plot_runtime_article_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff
    y_text_runtime = [data["ARTICLE_1000_12"]["scaled"]["mean"], data["ARTICLE_2500_12"]["scaled"]["mean"],
                      data["ARTICLE_5000_12"]["scaled"]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_runtime.pdf')

    plt.show()


def plot_application_speedup_article_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff

    y_text_application_speedup = [data["ARTICLE_1000_12"]["scaled"]["application_speedup"],
                                  data["ARTICLE_2500_12"]["scaled"]["application_speedup"],
                                  data["ARTICLE_5000_12"]["scaled"]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs")

    ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')
    # ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_speedup.pdf')

    plt.show()


def plot_computational_speedup_article_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff

    y_text_computational_speedup = [data["ARTICLE_1000_12"]["scaled"]["computational_speedup"],
                                    data["ARTICLE_2500_12"]["scaled"]["computational_speedup"],
                                    data["ARTICLE_5000_12"]["scaled"]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs")

    ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_comp.pdf')

    plt.show()


def plot_efficiency_speedup_article_cutoffs(path, dataset, data):
    x = [1000, 2500, 5000]  # cutoff

    y_text_efficiency = [data["ARTICLE_1000_12"]["scaled"]["efficiency"],
                         data["ARTICLE_2500_12"]["scaled"]["efficiency"],
                         data["ARTICLE_5000_12"]["scaled"]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs")

    ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_cutoffs_efficiency.pdf')

    plt.show()
