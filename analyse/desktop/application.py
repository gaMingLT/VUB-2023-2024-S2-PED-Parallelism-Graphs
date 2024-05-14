import matplotlib.pyplot as plt

SOURCE = "original"


def plot_application_speedup(path, dataset, data):
    x = [1, 4, 8, 12]  # cores
    y_articles = [data["ARTICLE1"][SOURCE]["application_speedup"], data["ARTICLE4"][SOURCE]["application_speedup"],
                  data["ARTICLE8"][SOURCE]["application_speedup"], data["ARTICLE12"][SOURCE]["application_speedup"]]
    y_text = [data["TEXT1"][SOURCE]["application_speedup"], data["TEXT4"][SOURCE]["application_speedup"],
              data["TEXT8"][SOURCE]["application_speedup"], data["TEXT12"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Application Speedup")
    ax.set_xlabel("# workers")
    ax.set_ylabel("Application Speedup")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


def plot_application_speedup_text_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_application_speedup = [data["TEXT_500_12"][SOURCE]["application_speedup"],
                                  data["TEXT_750_12"][SOURCE]["application_speedup"],
                                  data["TEXT_1000_12"][SOURCE]["application_speedup"],
                                  data["TEXT_2500_12"][SOURCE]["application_speedup"],
                                  data["TEXT_5000_12"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
    ax.set_xlabel("# characters")
    ax.set_ylabel("Application Speedup")

    ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')

    ax.legend(loc='best')

    fig.savefig(path + '/text_cutoffs_speedup.svg')

    plt.show()


def plot_application_speedup_article_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    y_text_application_speedup = [
        data["ARTICLE_500_12"][SOURCE]["application_speedup"],
        data["ARTICLE_750_12"][SOURCE]["application_speedup"],
        data["ARTICLE_1000_12"][SOURCE]["application_speedup"],
        data["ARTICLE_2500_12"][SOURCE]["application_speedup"],
        data["ARTICLE_5000_12"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
    ax.set_xlabel("# articles")
    ax.set_xlabel("Application Speedup")

    ax.plot(x, y_text_application_speedup, '-o', label='Application Speedup')

    ax.legend(loc='best')

    fig.savefig(path + '/article_cutoffs_speedup.svg')

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

    ax.set_title("Articles & Text: Application Speedup")
    ax.set_xlabel("# workers")
    ax.set_ylabel("Application Speedup")

    ax.legend(loc='best')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


def plot_articles_and_text_application_combined(path, datasets, dataset_values):
    x = [500, 750, 1000, 2500, 5000]  # cutoff
    SOURCE = "original"

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_text = [data["TEXT_500_12"][SOURCE]["application_speedup"], data["TEXT_750_12"][SOURCE]["application_speedup"],
                  data["TEXT_1000_12"][SOURCE]["application_speedup"], data["TEXT_2500_12"][SOURCE]["application_speedup"],
                  data["TEXT_5000_12"][SOURCE]["application_speedup"]]

        y_articles = [
            data["ARTICLE_500_12"][SOURCE]["application_speedup"], data["ARTICLE_750_12"][SOURCE]["application_speedup"],
            data["ARTICLE_1000_12"][SOURCE]["application_speedup"], data["ARTICLE_2500_12"][SOURCE]["application_speedup"],
            data["ARTICLE_5000_12"][SOURCE]["application_speedup"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Articles & Text: Application Speedup - 12")
    ax.set_xlabel("# articles & # characters")
    ax.set_ylabel("Application Speedup")

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_app.svg')

    plt.show()
