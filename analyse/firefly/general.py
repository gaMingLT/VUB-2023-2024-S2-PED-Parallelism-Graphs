import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

SOURCE = "scaled"


def plot_confidence_interval_text_between(path, dataset, data):
    keys = ['SEQ', 'TEXT1', 'TEXT32', 'TEXT64', 'TEXT128']

    fig, ax = plt.subplots(layout='constrained')

    plt.xticks(np.arange(len(keys)), keys)
    x = np.arange(len(keys))

    y_upper = []
    y_lower = []
    y_mean = []

    for i, key in enumerate(keys):
        mean = data[key][SOURCE]['mean']
        lower_bound = data[key][SOURCE]['lower_bound']
        upper_bound = data[key][SOURCE]['upper_bound']

        y_mean.append(mean)
        y_upper.append(upper_bound)
        y_lower.append(lower_bound)

    ax.plot(x, y_mean, '--o')
    ax.fill_between(x, y_lower, y_upper, alpha=0.2)

    ax.set_title(dataset.upper() + " - Confidence Intervals")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Confidence Interval")

    ax.legend(loc='best')

    fig.savefig(path + '/confidence_interval_text_inbetween.svg')

    plt.show()


def plot_confidence_interval_for_articles_between(path, dataset, data):
    keys = ['SEQ', 'ARTICLE1', 'ARTICLE32', 'ARTICLE64', 'ARTICLE128']

    fig, ax = plt.subplots(layout='constrained')

    plt.xticks(np.arange(len(keys)), keys)
    x = np.arange(len(keys))

    y_upper = []
    y_lower = []
    y_mean = []

    for i, key in enumerate(keys):
        mean = data[key][SOURCE]['mean']
        lower_bound = data[key][SOURCE]['lower_bound']
        upper_bound = data[key][SOURCE]['upper_bound']

        y_mean.append(mean)
        y_upper.append(upper_bound)
        y_lower.append(lower_bound)

    ax.plot(x, y_mean, '--o')
    ax.fill_between(x, y_lower, y_upper, alpha=0.2)

    ax.set_title(dataset.upper() + " - Confidence Intervals")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Confidence Interval")

    ax.legend(loc='best')

    fig.savefig(path + '/confidence_interval_articles_inbetween.svg')

    plt.show()



def plot_confidence_interval_for_articles(path, dataset, data):
    x_keys = ['SEQ', 'ARTICLE1', 'ARTICLE32', 'ARTICLE64', 'ARTICLE128']

    fig, ax = plt.subplots(layout='constrained')
    plt.xticks(np.arange(len(x_keys)), x_keys)
    x = np.arange(len(x_keys))

    y_upper = []
    y_lower = []
    y_mean = []

    for i, key in enumerate(x_keys):
        mean = data[key][SOURCE]['mean']
        lower_bound = data[key][SOURCE]['lower_bound']
        upper_bound = data[key][SOURCE]['upper_bound']

        y_mean.append(mean)
        y_upper.append(upper_bound)
        y_lower.append(lower_bound)

    ax.bar(x-0.15, y_lower, width=0.1, color='b', align='center', label='lower')
    ax.bar(x, y_mean, width=0.1, color='g', align='center', label="mean")
    ax.bar(x+0.15, y_upper, width=0.1, color='r', align='center', label='upper')

    ax.set_title(dataset.upper() + " - Confidence Intervals")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Confidence Interval")

    ax.legend(loc='best')

    fig.savefig(path + '/confidence_interval_articles.svg')

    plt.show()


def plot_confidence_interval_for_text(path, dataset, data):
    x_keys = ['SEQ', 'TEXT1', 'TEXT32', 'TEXT64', 'TEXT128']

    fig, ax = plt.subplots(layout='constrained')
    plt.xticks(np.arange(len(x_keys)), x_keys)
    x = np.arange(len(x_keys))

    y_upper = []
    y_lower = []
    y_mean = []

    for i, key in enumerate(x_keys):
        mean = data[key][SOURCE]['mean']
        lower_bound = data[key][SOURCE]['lower_bound']
        upper_bound = data[key][SOURCE]['upper_bound']

        y_mean.append(mean)
        y_upper.append(upper_bound)
        y_lower.append(lower_bound)

    ax.bar(x-0.15, y_lower, width=0.1, color='b', align='center', label='lower')
    ax.bar(x, y_mean, width=0.1, color='g', align='center', label="mean")
    ax.bar(x+0.15, y_upper, width=0.1, color='r', align='center', label='upper')

    ax.set_title(dataset.upper() + " - Confidence Intervals")
    ax.set_xlabel("Categories")
    ax.set_ylabel("Confidence Interval")

    ax.legend(loc='best')

    fig.savefig(path + '/confidence_interval_text.svg')

    plt.show()

