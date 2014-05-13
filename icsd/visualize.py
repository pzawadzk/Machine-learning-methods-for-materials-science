import json
import numpy as np
from collections import defaultdict
from pylab import *
from filterdb import *

def get_elements_statistics(d):
    elnum = defaultdict(int)
    els = defaultdict(int)
    for item in d.values():
        formula = item[0].replace("'",'').split()
        elnum[len(formula)] += 1

        for el in formula:
            for i in el:
                if i.isdigit():
                    el = el.replace(i, "")
            els[el] += 1

    return elnum, els

def plot_dict(a):
    X = np.arange(len(a))
    bar(X, a.values(), align="center", width=0.5)
    xticks(X, a.keys())
    ymax = max(a.values()) + 20
    ylim(0, ymax)
    show()


if __name__ == "__main__":
    d = json.load(open('icsd_notinDB.json', 'r'))
    elnum, els = get_elements_statistics(d)
    print elnum
    print els
#    d = filter_nel(d, 1)

    for el in els.keys():
        dnew = filter_elements(d, el)

        elnumnew, elsnew = get_elements_statistics(dnew)
        print el, elnumnew
#        plot_dict(elnumnew)