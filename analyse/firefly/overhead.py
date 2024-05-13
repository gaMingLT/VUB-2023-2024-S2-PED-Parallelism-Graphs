import matplotlib.pyplot as plt

SOURCE = "original"


def print_overhead(path, dataset, data):
    print("Overhead {}".format(dataset))
    print("Text: " + str(data["TEXT1"]["original"]['overhead']))
    print("ARTICLE1: " + str(data["ARTICLE1"]["original"]["overhead"]))


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