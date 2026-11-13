"""Rebuild canonical_flops_1755.csv from scratch: every Hold'em flop and the strategically distinct ones.

Hold'em has 22,100 flops (52 choose 3). Two flops play the same when one turns into the other by renaming suits
(clubs <-> spades and so on), so the flops fall into 1,755 classes. This prints each class once, with its weight:
how many of the 22,100 flops belong to it (4, 12 or 24). The weights add up to 22,100.

    python canonical_flops.py > canonical_flops_1755.csv

No dependencies beyond the Python standard library (3.8+).

How a class is found: for every flop, all 24 renamings of the four suits are tried and the smallest
(rank, suit) tuple wins; flops with the same winner are one class. The name printed for a class is its first flop
in deck order, written high card first (e.g. AdTd6c).
"""
import itertools
import sys

RANKS, SUITS = '23456789TJQKA', 'cdhs'


def canonical_flops():
    deck = [r + s for r in RANKS for s in SUITS]
    classes = {}
    for flop in itertools.combinations(deck, 3):
        key = min(tuple(sorted((RANKS.index(c[0]), perm[SUITS.index(c[1])]) for c in flop))
                  for perm in itertools.permutations(range(4)))
        cls = classes.setdefault(key, [None, 0])
        cls[1] += 1
        if cls[0] is None:
            cls[0] = ''.join(sorted(flop, key=lambda c: (-RANKS.index(c[0]), c[1])))
    out = [tuple(v) for v in classes.values()]
    assert len(out) == 1755 and sum(w for _, w in out) == 22100
    return sorted(out, key=lambda x: (-x[1], x[0]))


if __name__ == '__main__':
    sys.stdout.reconfigure(newline='\n')   # the same bytes as the CSV in this repository, on Windows too
    w = sys.stdout
    w.write('flop,weight\n')
    for flop, weight in canonical_flops():
        w.write(f'{flop},{weight}\n')
