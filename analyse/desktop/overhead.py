import matplotlib.pyplot as plt

SOURCE = "original"


def print_overhead(path, dataset, data):
    print("Overhead {}".format(dataset))
    print("Text: " + str(data["TEXT1"]["original"]['overhead']))
    print("ARTICLE1: " + str(data["ARTICLE1"]["original"]["overhead"]))


def plot_thresholds_article_and_text_overhead(path, dataset, data):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    fig, ax = plt.subplots()

    y_text = [data["TEXT_500_12"][SOURCE]["overhead"], data["TEXT_750_12"][SOURCE]["overhead"],
              data["TEXT_1000_12"][SOURCE]["overhead"], data["TEXT_2500_12"][SOURCE]["overhead"],
              data["TEXT_5000_12"][SOURCE]["overhead"]]

    y_articles = [
        data["ARTICLE_500_12"][SOURCE]["overhead"], data["ARTICLE_750_12"][SOURCE]["overhead"],
        data["ARTICLE_1000_12"][SOURCE]["overhead"], data["ARTICLE_2500_12"][SOURCE]["overhead"],
        data["ARTICLE_5000_12"][SOURCE]["overhead"]]

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.set_title(dataset.upper() + " - Overhead")
    ax.set_xlabel("# articles & # characters")
    ax.set_ylabel("Overhead")

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_overhead.svg')

    plt.show()


def plot_thresholds_article_and_text_overhead_combined(path, datasets, dataset_values):
    x = [500, 750, 1000, 2500, 5000]  # cutoff

    fig, ax = plt.subplots()

    for dataset in dataset_values:
        data = datasets[dataset]

        y_text = [data["TEXT_500_12"][SOURCE]["overhead"], data["TEXT_750_12"][SOURCE]["overhead"],
                  data["TEXT_1000_12"][SOURCE]["overhead"], data["TEXT_2500_12"][SOURCE]["overhead"],
                  data["TEXT_5000_12"][SOURCE]["overhead"]]

        y_articles = [
            data["ARTICLE_500_12"][SOURCE]["overhead"], data["ARTICLE_750_12"][SOURCE]["overhead"],
            data["ARTICLE_1000_12"][SOURCE]["overhead"], data["ARTICLE_2500_12"][SOURCE]["overhead"],
            data["ARTICLE_5000_12"][SOURCE]["overhead"]]

        ax.plot(x, y_articles, '--o', label='Article - ' + dataset.upper())
        ax.plot(x, y_text, '-o', label='Text - ' + dataset.upper())

    ax.set_title("Article & Text Cutoffs - 12")
    ax.set_xlabel("# articles & # characters")
    ax.set_ylabel("Overhead")

    ax.legend(loc='best')

    fig.savefig(path + '/article_and_text_cutoffs_overhead.svg')

    plt.show()

