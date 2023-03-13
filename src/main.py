import ast
import math
import matplotlib.pyplot as plt
import numpy as np

n = 52
conjecture = math.log2(n) - math.log2(4 if n & 1 == 0 else 16) / n


def data_dir(file_name: str):
    return f'C:\\Users\\Mark\\source\\repos\\Rust\\shuffle_stats\\{file_name}'


def to_list(mm_str: str):
    return ast.literal_eval(mm_str.replace('{', '[').replace('}', ']'))


def plot_shuffle(name: str, data_slice, label=None, legend=None):
    with open(data_dir(f'{name}_shuffle_data.txt'), 'r') as file:
        contents = file.read()
        data = to_list(contents)
        sub_len = len(data[0])

        xs = np.arange(1, 1 + sub_len)
        for index, sub in enumerate(data_slice(data)):
            ys = [x[0] for x in sub]
            plt.plot(xs, ys, label=label(index, sub) if label else None)

        plt.title(f'{name.capitalize()} Shuffle')
        plt.xlabel('Moves')
        plt.ylabel('Entropy')

        if legend:
            plt.legend(loc=legend)

        plt.xlim(1, sub_len)
        plt.ylim(0, 6)
        plt.plot(xs, np.repeat(conjecture, sub_len), 'k--')

        plt.show()


def plot_pile_shuffle():
    plot_shuffle(
        'pile',
        lambda data: data[1:],
        lambda index, sub: str(2 + index),
        'lower right'
    )


def plot_riffle_shuffle():
    plot_shuffle(
        'riffle',
        lambda data: data,
    )


def plot_weave_shuffle():
    labels = ['in', 'out']
    plot_shuffle(
        'weave',
        lambda data: data,
        lambda index, sub: labels[index],
        'right'
    )


def main():
    plot_pile_shuffle()
    plot_riffle_shuffle()
    plot_weave_shuffle()


if __name__ == '__main__':
    main()
