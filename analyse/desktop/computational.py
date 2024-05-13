import matplotlib.pyplot as plt


SOURCE = "original"


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
    ax.set_ylabel("Computational Speedup")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/computational_speedup.svg')

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
    ax.set_ylabel("Computational Speedup")

    ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')

    ax.legend(loc='best')

    fig.savefig(path + '/text_cutoffs_comp.svg')

    plt.show()


def plot_articles_and_text_computational_combined(path, datasets, dataset_values):
    x = [500, 750, 1000, 2500, 5000]  # cutoff
    SOURCE = "original"

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_text = [data["TEXT_500_12"][SOURCE]["computational_speedup"], data["TEXT_750_12"][SOURCE]["computational_speedup"],
                  data["TEXT_1000_12"][SOURCE]["computational_speedup"], data["TEXT_2500_12"][SOURCE]["computational_speedup"],
                  data["TEXT_5000_12"][SOURCE]["computational_speedup"]]

        y_articles = [
            data["ARTICLE_500_12"][SOURCE]["computational_speedup"], data["ARTICLE_750_12"][SOURCE]["computational_speedup"],
            data["ARTICLE_1000_12"][SOURCE]["computational_speedup"], data["ARTICLE_2500_12"][SOURCE]["computational_speedup"],
            data["ARTICLE_5000_12"][SOURCE]["computational_speedup"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Article & Text Cutoffs")
    ax.set_xlabel("Text & Articles Sequentially")
    ax.set_ylabel("Computational Speedup")

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_comp.svg')

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
    ax.set_ylabel("Computational Speedup")

    ax.legend(loc='best')

    fig.savefig(path + '/computational_speedup.svg')

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
    ax.set_ylabel("Computational Speedup")

    ax.plot(x, y_text_computational_speedup, '-o', label='Computational Speedup')

    ax.legend(loc='best')

    fig.savefig(path + '/article_cutoffs_comp.svg')

    plt.show()