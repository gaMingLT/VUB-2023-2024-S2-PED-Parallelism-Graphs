import matplotlib.pyplot as plt


def plot_efficiency(path, dataset, data):
    x = [16, 32, 64, 128]  # cores
    SOURCE = "original"

    y_articles = [data["ARTICLE16"][SOURCE]["efficiency"],
                  data["ARTICLE32"][SOURCE]["efficiency"],
                  data["ARTICLE64"][SOURCE]["efficiency"],
                  data["ARTICLE128"][SOURCE]["efficiency"]]
    y_text = [data["TEXT16"][SOURCE]["efficiency"],
              data["TEXT32"][SOURCE]["efficiency"],
              data["TEXT64"][SOURCE]["efficiency"],
              data["TEXT128"][SOURCE]["efficiency"]]

    fig, ax = plt.subplots()
    ax.set_title(dataset.upper() + " - Efficiency")
    ax.set_xlabel("Workers")
    ax.set_xlabel("Efficiency")

    ax.plot(x, y_articles, '-o', label='Article')
    ax.plot(x, y_text, '-o', label='Text')

    ax.legend(loc='best')

    fig.savefig(path + '/efficiency.svg')

    plt.show()
