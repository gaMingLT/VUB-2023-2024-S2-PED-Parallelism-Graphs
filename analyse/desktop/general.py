import matplotlib.pyplot as plt
import seaborn as sns


SOURCE = "scaled"


def plot_confidence_interval_for_keys(path, dataset, data):
    y_keys = ['SEQ', 'ARTICLE1', 'ARTICLE4', 'ARTICLE8', 'ARTICLE12']
    horizontal_line_width = 0.25
    color = '#2187bb'

    fig, ax = plt.subplots()
    plt.xticks(range(0, len(y_keys)), y_keys)
    # plt.yticks(range(0, len(y_keys)), y_keys)

    # intervals = []
    # for key in y_keys:
    #     intervals.append((data[key][SOURCE]['lower_bound'], data[key][SOURCE]['upper_bound'], data[key][SOURCE]['mean']))

    for x, (key) in enumerate(y_keys):
        lower_bound = data[key][SOURCE]['lower_bound']
        upper_bound = data[key][SOURCE]['upper_bound']
        mean = data[key][SOURCE]['mean']

        # print(x, key, lower_bound, upper_bound, mean)

        # plt.plot((lower_bound, upper_bound), (y, y), 'ro-', color='orange')

        left = x - horizontal_line_width / 2
        right = x + horizontal_line_width / 2
        plt.plot([x, x], [upper_bound, lower_bound], color=color)
        plt.plot([left, right], [upper_bound, upper_bound], color=color)
        plt.plot([left, right], [lower_bound, lower_bound], color=color)
        plt.plot(x, mean, 'o', color='#f44336')

    ax.set_title(dataset.upper() + " - Confidence Intervals Categories")
    ax.set_xlabel("Categories")

    ax.legend(loc='best')

    fig.savefig(path + '/confidence_interval.svg')

    plt.show()
