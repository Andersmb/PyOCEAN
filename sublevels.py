import math
from matplotlib import pyplot as plt
import pandas as pd


def a2r(a):
    return a * 2 * math.pi / 360


def plot(data, person):
    labels = ['Int', 'Ope',
              'Ind', 'Ord',
              'Ent', 'Ass',
              'Com', 'Pol',
              'Vol', 'Wit']
    angles = [i * 360 / len(labels) for i in range(len(labels))]
    radians = [a * 2 * math.pi / 360 for a in angles]

    fig, ax = plt.subplots(dpi=150, figsize=(5, 5), subplot_kw={'projection': 'polar'})
    ax.set_thetagrids(angles, labels, fontsize=20)
    ax.set_yticklabels([])
    ax.set_rlim(0, 100)
    ax.set_facecolor('#1f1f1f')
    ax.set_title(person.upper(), fontsize=20)

    ax.plot(radians+[radians[0]], data+[data[0]], marker='.', mfc='orange', mec='black', color='black')
    ax.fill(radians+[radians[0]], data+[data[0]], color='orange', alpha=0.5)

    ax.grid(True, ls=':', lw=0.75)
    plt.tight_layout()
    plt.savefig('figs_sublevels/'+person+'.png', facecolor='white')


if __name__ == '__main__':
    data = pd.read_csv('sublevels.csv')
    persons = ['anders', 'heidi', 'eirik', 'anette', 'daniel', 'lisbeth', 'jostein']
    for person in persons:
        print(person)
        plot(data[person].tolist(), person)

