import os.path
import matplotlib.pyplot as plt

SOURCE = "original"


def print_overhead(path, dataset, data):
    print("Overhead {}".format(dataset))
    print("Text: " + str(data["TEXT1"]["original"]['overhead']))
    print("ARTICLE1: " + str(data["ARTICLE1"]["original"]["overhead"]))


def plot_articles(data):
    x = [1, 4, 8, 12]  # cores
    y = [data["ARTICLE1"][SOURCE]["mean"], data["ARTICLE4"][SOURCE]["mean"], data["ARTICLE8"][SOURCE]["mean"],
         data["ARTICLE12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title("Article Statistics")

    ax.plot(x, y, '-o', label='Articles')
    ax.legend(loc='upper left')

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    fig.savefig('desktop/graphs/articles.svg')

    plt.show()


def plot_text(data):
    x = [1, 4, 8, 12]  # cores
    y = [data["TEXT1"][SOURCE]["mean"], data["TEXT4"][SOURCE]["mean"], data["TEXT8"][SOURCE]["mean"],
         data["TEXT12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title("Text Statistics")

    ax.plot(x, y, '-o', label='Text')
    ax.legend(loc='upper left')

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    fig.savefig('desktop/graphs/text.svg')

    plt.show()


def plot_articles_and_text(path, dataset,  data):
    x = [1, 4, 8, 12]  # cores
    SOURCE = "scaled"
    y_articles = [data["ARTICLE1"][SOURCE]["mean"], data["ARTICLE4"][SOURCE]["mean"],
                  data["ARTICLE8"][SOURCE]["mean"], data["ARTICLE12"][SOURCE]["mean"]]
    y_text = [data["TEXT1"][SOURCE]["mean"], data["TEXT4"][SOURCE]["mean"],
              data["TEXT8"][SOURCE]["mean"], data["TEXT12"][SOURCE]["mean"]]

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
    x = [1, 4, 8, 12]  # cores
    y_articles = [data["ARTICLE1"][SOURCE]["application_speedup"], data["ARTICLE4"][SOURCE]["application_speedup"],
                  data["ARTICLE8"][SOURCE]["application_speedup"], data["ARTICLE12"][SOURCE]["application_speedup"]]
    y_text = [data["TEXT1"][SOURCE]["application_speedup"], data["TEXT4"][SOURCE]["application_speedup"],
              data["TEXT8"][SOURCE]["application_speedup"], data["TEXT12"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Application Speedup")
    ax.set_xlabel("Workers")

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper left')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


def plot_computational_speedup(path, dataset,  data):
    x = [4, 8, 12]  # cores
    y_articles = [data["ARTICLE4"][SOURCE]["computational_speedup"],
                  data["ARTICLE8"][SOURCE]["computational_speedup"],
                  data["ARTICLE12"][SOURCE]["computational_speedup"]]
    y_text = [data["TEXT4"][SOURCE]["computational_speedup"],
              data["TEXT8"][SOURCE]["computational_speedup"],
              data["TEXT12"][SOURCE]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Computational Speedup")
    ax.set_xlabel("Workers")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper left')

    fig.savefig(path + '/computational_speedup.svg')

    plt.show()


def plot_efficiency(path, dataset, data):
    x = [4, 8, 12]  # cores
    y_articles = [data["ARTICLE4"][SOURCE]["efficiency"],
                  data["ARTICLE8"][SOURCE]["efficiency"],
                  data["ARTICLE12"][SOURCE]["efficiency"]]
    y_text = [data["TEXT4"][SOURCE]["efficiency"],
              data["TEXT8"][SOURCE]["efficiency"],
              data["TEXT12"][SOURCE]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Efficiency")
    ax.set_xlabel("Workers")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='upper left')

    fig.savefig(path + '/efficiency.svg')

    plt.show()


def plot_runtime_text_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff
    y_text_runtime = [data["TEXT_500_12"][SOURCE]["mean"], data["TEXT_750_12"][SOURCE]["mean"],
                        data["TEXT_1000_12"][SOURCE]["mean"], data["TEXT_2500_12"][SOURCE]["mean"],
                      data["TEXT_5000_12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_runtime.svg')

    plt.show()


def plot_application_speedup_text_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_application_speedup = [data["TEXT_500_12"][SOURCE]["application_speedup"], data["TEXT_750_12"][SOURCE]["application_speedup"],
                                    data["TEXT_1000_12"][SOURCE]["application_speedup"],
                                  data["TEXT_2500_12"][SOURCE]["application_speedup"],
                                  data["TEXT_5000_12"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')
    # ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_speedup.svg')

    plt.show()


def plot_computational_speedup_text_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_computational_speedup = [
        data["TEXT_500_12"][SOURCE]["computational_speedup"], data["TEXT_750_12"][SOURCE]["computational_speedup"],
        data["TEXT_1000_12"][SOURCE]["computational_speedup"],
                                    data["TEXT_2500_12"][SOURCE]["computational_speedup"],
                                    data["TEXT_5000_12"][SOURCE]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_comp.svg')

    plt.show()


def plot_efficiency_speedup_text_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_efficiency = [

        data["TEXT_500_12"][SOURCE]["efficiency"], data["TEXT_750_12"][SOURCE]["efficiency"],
        data["TEXT_1000_12"][SOURCE]["efficiency"],
                         data["TEXT_2500_12"][SOURCE]["efficiency"],
                         data["TEXT_5000_12"][SOURCE]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
    ax.set_xlabel("Characters Sequential")

    ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper left')

    fig.savefig(path + '/text_cutoffs_efficiency.svg')

    plt.show()


def plot_runtime_article_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff
    y_text_runtime = [
        data["ARTICLE_500_12"][SOURCE]["mean"], data["ARTICLE_750_12"][SOURCE]["mean"],
        data["ARTICLE_1000_12"][SOURCE]["mean"], data["ARTICLE_2500_12"][SOURCE]["mean"],
                      data["ARTICLE_5000_12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_runtime.svg')

    plt.show()


def plot_application_speedup_article_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_application_speedup = [

        data["ARTICLE_500_12"][SOURCE]["application_speedup"], data["ARTICLE_750_12"][SOURCE]["application_speedup"],
        data["ARTICLE_1000_12"][SOURCE]["application_speedup"],
                                  data["ARTICLE_2500_12"][SOURCE]["application_speedup"],
                                  data["ARTICLE_5000_12"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')
    # ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_speedup.svg')

    plt.show()


def plot_computational_speedup_article_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_computational_speedup = [
        data["ARTICLE_500_12"][SOURCE]["computational_speedup"], data["ARTICLE_750_12"][SOURCE]["computational_speedup"],
        data["ARTICLE_1000_12"][SOURCE]["computational_speedup"],
                                    data["ARTICLE_2500_12"][SOURCE]["computational_speedup"],
                                    data["ARTICLE_5000_12"][SOURCE]["computational_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_comp.svg')

    plt.show()


def plot_efficiency_speedup_article_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_efficiency = [
        data["ARTICLE_500_12"][SOURCE]["efficiency"], data["ARTICLE_750_12"][SOURCE]["efficiency"],
        data["ARTICLE_1000_12"][SOURCE]["efficiency"],
                         data["ARTICLE_2500_12"][SOURCE]["efficiency"],
                         data["ARTICLE_5000_12"][SOURCE]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
    ax.set_xlabel("Articles Sequential")

    ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_efficiency.svg')

    plt.show()


def plot_application_speedup_combined(path, datasets, dataset_values):
    x = [1, 4, 8, 12]  # cores

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_articles = [data["ARTICLE1"][SOURCE]["application_speedup"], data["ARTICLE4"][SOURCE]["application_speedup"],
                      data["ARTICLE8"][SOURCE]["application_speedup"], data["ARTICLE12"][SOURCE]["application_speedup"]]
        y_text = [data["TEXT1"][SOURCE]["application_speedup"], data["TEXT4"][SOURCE]["application_speedup"],
                  data["TEXT8"][SOURCE]["application_speedup"], data["TEXT12"][SOURCE]["application_speedup"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Combined" + " - Application Speedup")
    ax.set_xlabel("Workers")

    if not os.path.exists("desktop/graphs"):
        os.mkdir("desktop/graphs")

    ax.legend(loc='upper left')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


def plot_computational_speedup_combined(path, datasets, dataset_values):
    x = [4, 8, 12]  # cores

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_articles = [data["ARTICLE4"][SOURCE]["computational_speedup"],
                      data["ARTICLE8"][SOURCE]["computational_speedup"],
                      data["ARTICLE12"][SOURCE]["computational_speedup"]]

        y_text = [data["TEXT4"][SOURCE]["computational_speedup"],
                  data["TEXT8"][SOURCE]["computational_speedup"],
                  data["TEXT12"][SOURCE]["computational_speedup"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Combined" + " - Computational Speedup")
    ax.set_xlabel("Workers")

    ax.legend(loc='upper left')

    fig.savefig(path + '/computational_speedup.svg')

    plt.show()


def plot_articles_and_text_combined(path, datasets, dataset_values):
    x = [1, 4, 8, 12]  # cores
    SOURCE = "scaled"

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_articles = [data["ARTICLE1"][SOURCE]["mean"], data["ARTICLE4"][SOURCE]["mean"],
                      data["ARTICLE8"][SOURCE]["mean"], data["ARTICLE12"][SOURCE]["mean"]]

        y_text = [data["TEXT1"][SOURCE]["mean"], data["TEXT4"][SOURCE]["mean"],
                  data["TEXT8"][SOURCE]["mean"], data["TEXT12"][SOURCE]["mean"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Combined" + " - Articles & Text")
    ax.set_xlabel("Workers")
    ax.set_ylabel("Milliseconds")

    ax.legend(loc='upper right')

    fig.savefig(path + '/article_and_text.svg')

    plt.show()


def plot_tresholds_article_and_text(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    SOURCE = "scaled"
    fig, ax = plt.subplots()

    # for dataset in dataset_values:
    #     data = datasets[dataset]

    y_text = [data["TEXT_500_12"][SOURCE]["mean"], data["TEXT_750_12"][SOURCE]["mean"],
              data["TEXT_1000_12"][SOURCE]["mean"], data["TEXT_2500_12"][SOURCE]["mean"],
              data["TEXT_5000_12"][SOURCE]["mean"]]

    y_articles = [
        data["ARTICLE_500_12"][SOURCE]["mean"], data["ARTICLE_750_12"][SOURCE]["mean"],
        data["ARTICLE_1000_12"][SOURCE]["mean"], data["ARTICLE_2500_12"][SOURCE]["mean"],
        data["ARTICLE_5000_12"][SOURCE]["mean"]]

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.set_title(dataset.upper() + " - Article & Text Cutoffs")
    ax.set_xlabel("Text & Articles Sequentially")
    ax.set_ylabel("Milliseconds")

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_runtime.svg')

    plt.show()




# def plot_tresholds_articles_combined(path, datasets, dataset_values):
#     x = [500, 750, 1000, 2500, 5000]  # cutoff
#     SOURCE = "scaled"
#     fig, ax = plt.subplots()
#
#     for dataset in dataset_values:
#         data = datasets[dataset]
#
#         y_articles = [
#             data["ARTICLE_500_12"][SOURCE]["mean"], data["ARTICLE_750_12"][SOURCE]["mean"],
#             data["ARTICLE_1000_12"][SOURCE]["mean"], data["ARTICLE_2500_12"][SOURCE]["mean"],
#             data["ARTICLE_5000_12"][SOURCE]["mean"]]
#
#         ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
#
#     ax.set_title("Combined" + " - Articles")
#     ax.set_xlabel("Articles Sequential")
#     ax.set_ylabel("Milliseconds")
#
#     ax.legend(loc='center left')
#
#     fig.savefig(path + '/article_cutoffs_runtime.svg')
#
#     plt.show()
#
#
# def plot_tresholds_text_combined(path, datasets, dataset_values):
#     x = [500, 750, 1000, 2500, 5000]  # cutoff
#
#     SOURCE = "scaled"
#     fig, ax = plt.subplots()
#
#     for dataset in dataset_values:
#         data = datasets[dataset]
#
#         y_text = [data["TEXT_500_12"][SOURCE]["mean"], data["TEXT_750_12"][SOURCE]["mean"],
#                           data["TEXT_1000_12"][SOURCE]["mean"], data["TEXT_2500_12"][SOURCE]["mean"],
#                           data["TEXT_5000_12"][SOURCE]["mean"]]
#
#         ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())
#
#     ax.set_title("Combined" + " - Text")
#     ax.set_xlabel("Characters Sequentially")
#     ax.set_ylabel("Milliseconds")
#
#     ax.legend(loc='center left')
#
#     fig.savefig(path + '/text_cutoffs_runtime.svg')
#
#     plt.show()


def plot_amdahls_law_articles(path, dataset, data):
    x = [4, 8, 12]  # cores

    fig, ax = plt.subplots()

    y_min = [data["ARTICLE4"][SOURCE]["application_speedup"], data["ARTICLE8"][SOURCE]["application_speedup"], data["ARTICLE12"][SOURCE]["application_speedup"]]
    y_750 = [data["ARTICLE_750_4"][SOURCE]["application_speedup"], data["ARTICLE_750_8"][SOURCE]["application_speedup"], data["ARTICLE_750_12"][SOURCE]["application_speedup"]]

    ax.plot(x, y_min, '-o', label='Article Min')
    ax.plot(x, y_750, '-o', label='Article 750')

    ax.set_title(dataset.upper() + " - Application Speedup")
    ax.set_xlabel("Workers")

    ax.legend(loc='upper left')

    fig.savefig(path + '/amdahls_law_article.svg')

    plt.show()


def plot_amdahls_law_text(path, dataset, data):
    x = [4, 8, 12]  # cores

    fig, ax = plt.subplots()

    y_min = [data["TEXT4"][SOURCE]["application_speedup"], data["TEXT8"][SOURCE]["application_speedup"], data["TEXT12"][SOURCE]["application_speedup"]]
    y_750 = [data["TEXT_2500_4"][SOURCE]["application_speedup"], data["TEXT_2500_8"][SOURCE]["application_speedup"], data["TEXT_2500_12"][SOURCE]["application_speedup"]]

    ax.plot(x, y_min, '-o', label='Text Min')
    ax.plot(x, y_750, '-o', label='Text 750')

    ax.set_title(dataset.upper() + " - Application Speedup")
    ax.set_xlabel("Workers")

    ax.legend(loc='upper left')

    fig.savefig(path + '/amdahls_law_text.svg')

    plt.show()