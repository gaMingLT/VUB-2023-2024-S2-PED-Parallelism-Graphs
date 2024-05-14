import matplotlib.pyplot as plt

SOURCE = "original"


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
    ax.set_xlabel("# workers")
    ax.set_ylabel("Efficiency")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/efficiency.svg')

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
    ax.set_xlabel("# articles")
    ax.set_ylabel("Efficiency")

    ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='best')

    fig.savefig(path + '/text_cutoffs_efficiency.svg')

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
    ax.set_xlabel("# articles")
    ax.set_ylabel("Efficiency")

    ax.plot(x, y_text_efficiency, '-o', label='Efficiency Speedup')

    ax.legend(loc='best')

    fig.savefig(path + '/article_cutoffs_efficiency.svg')

    plt.show()