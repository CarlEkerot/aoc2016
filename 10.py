from collections import defaultdict
from functools import reduce
import re

input_pattern = re.compile(r'value (\d+) goes to (bot \d+)')
give_pattern = re.compile(r'(bot \d+) gives low to ((?:bot|output) (?:\d+)) '
                          'and high to ((?:bot|output) (?:\d+))')

inputs = []
nodes = defaultdict(lambda: {'chips': []})


def parse():
    with open('10.txt') as f:
        for l in f.readlines():
            if l.startswith('bot'):
                b, l, r = give_pattern.match(l).groups()
                nodes[b]['left'] = l
                nodes[b]['right'] = r
            else:
                inputs.append(input_pattern.match(l).groups())


def give(chip, to):
    b = nodes[to]
    chips = b['chips']
    chips.append(chip)
    if to.startswith('bot') and len(chips) == 2:
        chips.sort()
        give(chips[0], b['left'])
        give(chips[1], b['right'])


def process():
    for i in inputs:
        give(int(i[0]), i[1])

parse()
process()

print(next(filter(lambda b: nodes[b]['chips'] == [17, 61], nodes.keys())))
print(reduce(lambda a, b: a * b,
             sum([nodes['output %d' % i]['chips'] for i in range(3)], [])))
