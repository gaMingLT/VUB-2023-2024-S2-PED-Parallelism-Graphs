import matplotlib.pyplot as plt

SOURCE = "scaled"

X_LABEL_ARTICLES = "# articles"
X_LABEL_CHARACTERS = "# characters"
X_LABEL_BOTH = "# articles & characters"
X_LABEL_WORKERS = "# workers"
Y_LABEL_SECONDS = "Seconds"


def plot_articles_and_text(path, dataset,  data):
    x = [1, 4, 8, 12]  # cores

    y_articles = [data["ARTICLE1"][SOURCE]["mean"], data["ARTICLE4"][SOURCE]["mean"],
                  data["ARTICLE8"][SOURCE]["mean"], data["ARTICLE12"][SOURCE]["mean"]]
    y_text = [data["TEXT1"][SOURCE]["mean"], data["TEXT4"][SOURCE]["mean"],
              data["TEXT8"][SOURCE]["mean"], data["TEXT12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Articles & Text")
    ax.set_xlabel(X_LABEL_WORKERS)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text.svg')

    plt.show()


def plot_runtime_text_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff
    y_text_runtime = [data["TEXT_500_12"][SOURCE]["mean"], data["TEXT_750_12"][SOURCE]["mean"],
                      data["TEXT_1000_12"][SOURCE]["mean"], data["TEXT_2500_12"][SOURCE]["mean"],
                      data["TEXT_5000_12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - 12")
    ax.set_xlabel(X_LABEL_CHARACTERS)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='best')

    fig.savefig(path + '/text_cutoffs_runtime.svg')

    plt.show()


def plot_runtime_article_cutoffs(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff
    y_text_runtime = [
        data["ARTICLE_500_12"][SOURCE]["mean"], data["ARTICLE_750_12"][SOURCE]["mean"],
        data["ARTICLE_1000_12"][SOURCE]["mean"], data["ARTICLE_2500_12"][SOURCE]["mean"],
        data["ARTICLE_5000_12"][SOURCE]["mean"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - 12")
    ax.set_xlabel(X_LABEL_ARTICLES)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='upper left')

    fig.savefig(path + '/article_cutoffs_runtime.svg')

    plt.show()


def plot_articles_and_text_combined(path, datasets, dataset_values):
    x = [1, 4, 8, 12]  # cores

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_articles = [data["ARTICLE1"][SOURCE]["mean"], data["ARTICLE4"][SOURCE]["mean"],
                      data["ARTICLE8"][SOURCE]["mean"], data["ARTICLE12"][SOURCE]["mean"]]

        y_text = [data["TEXT1"][SOURCE]["mean"], data["TEXT4"][SOURCE]["mean"],
                  data["TEXT8"][SOURCE]["mean"], data["TEXT12"][SOURCE]["mean"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Runtime - Articles & Text")
    ax.set_xlabel(X_LABEL_WORKERS)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text.svg')

    plt.show()


def plot_thresholds_article_and_text_runtime(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    fig, ax = plt.subplots()

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
    ax.set_xlabel(X_LABEL_BOTH)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_runtime.svg')

    plt.show()