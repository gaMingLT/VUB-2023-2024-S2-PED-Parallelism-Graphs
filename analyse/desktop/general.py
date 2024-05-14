import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

SOURCE = "scaled"


def plot_confidence_interval_for_articles(path, dataset, data):
    keys = ['SEQ', 'ARTICLE1', 'ARTICLE4', 'ARTICLE8', 'ARTICLE12']

    fig, ax = plt.subplots(layout='constrained')

    # plt.yticks(np.arange(len(keys)), keys)
    # y = np.arange(len(keys))
    #
    # x_upper = []
    # x_lower = []
    # x_mean = []
    # x_error = []
    #
    # for i, key in enumerate(keys):
    #     mean = data[key][SOURCE]['mean']
    #     lower_bound = data[key][SOURCE]['lower_bound']
    #     upper_bound = data[key][SOURCE]['upper_bound']
    #     margin_of_error = data[key][SOURCE]['margin_of_error']
    #
    #     x_error.append(margin_of_error)
    #     x_mean.append(mean)
    #     x_upper.append(upper_bound)
    #     x_lower.append(lower_bound)
    #
    # ax.barh(y, x_mean, xerr=x_error, ecolor='r', align='center', label='mean')

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
    x_keys = ['SEQ', 'TEXT1', 'TEXT4', 'TEXT8', 'TEXT12']

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
