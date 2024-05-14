import matplotlib.pyplot as plt

SOURCE = "scaled"

X_LABEL_ARTICLES = "# articles"
X_LABEL_CHARACTERS = "# characters"
X_LABEL_BOTH = "# articles & characters"
X_LABEL_WORKERS = "# workers"
Y_LABEL_SECONDS = "Seconds"


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
    ax.set_xlabel(X_LABEL_WORKERS)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text.svg')

    plt.show()


def plot_runtime_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["mean"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel(X_LABEL_CHARACTERS)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='best')

    fig.savefig(path + '/text_cutoffs_runtime.svg')

    plt.show()


def plot_runtime_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs

    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["mean"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel(X_LABEL_ARTICLES)
    ax.set_ylabel(Y_LABEL_SECONDS)

    ax.plot(x, y_text_runtime, '-o', label='Runtime')

    ax.legend(loc='best')

    fig.savefig(path + '/article_cutoffs_runtime.svg')

    plt.show()