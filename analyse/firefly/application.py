import matplotlib.pyplot as plt

SOURCE = "original"


def plot_application_speedup(path, dataset, data):
    x = [1, 16, 32, 64, 128]  # cores

    y_articles = [data["ARTICLE1"][SOURCE]["application_speedup"], data["ARTICLE16"][SOURCE]["application_speedup"],
                  data["ARTICLE32"][SOURCE]["application_speedup"], data["ARTICLE64"][SOURCE]["application_speedup"],
                  data["ARTICLE128"][SOURCE]["application_speedup"]]

    y_text = [data["TEXT1"][SOURCE]["application_speedup"], data["TEXT16"][SOURCE]["application_speedup"],
              data["TEXT32"][SOURCE]["application_speedup"], data["TEXT64"][SOURCE]["application_speedup"],
              data["TEXT128"][SOURCE]["application_speedup"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Application Speedup")
    ax.set_xlabel("# workers")
    ax.set_ylabel("Application Speedup")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/application_speedup.svg')

    plt.show()


def plot_application_speedup_article_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["application_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Article Cutoffs - " + str(workers))
    ax.set_xlabel("# articles")
    ax.set_ylabel("Application Speedup")

    ax.plot(x, y_text_runtime, '-o', label='Application')

    ax.legend(loc='best')

    fig.savefig(path + '/article_cutoffs_application_speedup.svg')

    plt.show()


def plot_application_speedup_text_cutoffs(path, dataset, data, cutoffs, keys, workers):
    x = cutoffs
    y_text_runtime = []
    for key in keys:
        y_text_runtime.append(data[key][SOURCE]["application_speedup"])

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Text Cutoffs - " + str(workers))
    ax.set_xlabel("# characters")
    ax.set_ylabel("Application Speedup")

    ax.plot(x, y_text_runtime, '-o', label='Application')

    ax.legend(loc='best')

    fig.savefig(path + '/text_cutoffs_application_speedup.svg')

    plt.show()