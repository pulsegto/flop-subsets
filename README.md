# Flop subsets for postflop solving, measured on all 1,755 distinct flops

Hold'em deals 22,100 different flops, but only **1,755** of them play differently once suits are swapped. This
repository has:

- **Subsets of 25, 49, 95 and 184 flops** for postflop solving and aggregated reports, chosen from full-game solver
  strategies and measured against all 1,755 flops, on lines the selection never saw.
- **All 1,755 canonical flops** with their deal weights (`canonical_flops_1755.csv`).

Free to use, share and ship in other tools. Details, charts and an interactive demo:
**https://pulsegto.com/flop-subsets**

## Files

| File | Format |
|---|---|
| `subsets/pulsegto_flops_N.txt` | one flop per line, weight after a colon: `Jc7d3c:516` |
| `subsets/pulsegto_flops_N.csv` | `flop,weight,percent` |
| `canonical_flops_1755.csv` | `flop,weight` for every strategically distinct flop |

Weights are deal counts: each file's weights add up to 22,100, the number of possible flops. A subset flop carries
the combined weight of the group of flops it stands for.

## Rebuild the 1,755 flops yourself

`canonical_flops.py` (Python 3.8+, standard library only) enumerates all 22,100 flops, groups the ones that differ
only by suit names (all 24 renamings of the four suits) and prints every class with its weight:

```
python canonical_flops.py > canonical_flops_1755.csv
```

The output is byte for byte the `canonical_flops_1755.csv` in this repository.

## How accurate they are

The aggregated report on a subset (how often the player to act checks, bets each size, folds, calls or raises, and
the range's EV) compared with the same report on all 1,755 flops, averaged over eight decisions on four test lines
that were not used to choose the subsets:

| Subset | Action frequencies (largest error) | Range EV | Inside texture groups |
|---|---|---|---|
| 25 flops | 1.11 pts | 0.30 % of the pot | 1.67 pts |
| 49 flops | 0.46 pts | 0.25 % of the pot | 1.00 pts |
| 95 flops | 0.25 pts | 0.24 % of the pot | 0.49 pts |
| 184 flops | 0.13 pts | 0.19 % of the pot | 0.27 pts |

## Other games

Each game has its own subsets, chosen and measured the same way on that game's blueprint (details and a checker for your
own lists: https://pulsegto.com/flop-subsets/plo, /tournaments, /short-deck). Every folder also holds
`measurement_*.csv`: every subset on every test decision.

### PLO (`plo/`)

From a PLO 6-max 100 bb cash blueprint, measured on PLO decisions; the last column is our Hold'em subset
of the same size measured on the same PLO decisions. Hold'em subsets are fine for PLO from about 95 flops; below that,
use the PLO ones.

| Subset | Action frequencies | Range EV | Inside texture groups | Hold'em subset, same size |
|---|---|---|---|---|
| 25 flops | 0.37 pts | 0.38 % of the pot | 0.95 pts | 1.12 pts |
| 49 flops | 0.28 pts | 0.16 % of the pot | 0.81 pts | 0.55 pts |
| 95 flops | 0.20 pts | 0.11 % of the pot | 0.52 pts | 0.27 pts |
| 184 flops | 0.13 pts | 0.07 % of the pot | 0.29 pts | 0.18 pts |

### Tournaments (`tournament-10bb/`, `tournament-20bb/`)

From 9-max tournament blueprints (chip EV) at 10 bb and 20 bb;
the last column is our 100 bb cash subset measured on the same tournament decisions.

**10 bb**

| Subset | Action frequencies | Range EV | Inside texture groups | Hold'em subset, same size |
|---|---|---|---|---|
| 25 flops | 1.37 pts | 1.07 % of the pot | 2.63 pts | 1.55 pts |
| 49 flops | 1.28 pts | 1.04 % of the pot | 1.64 pts | 0.49 pts |
| 95 flops | 0.64 pts | 0.28 % of the pot | 1.01 pts | 0.34 pts |
| 184 flops | 0.33 pts | 0.33 % of the pot | 0.55 pts | 0.27 pts |

**20 bb**

| Subset | Action frequencies | Range EV | Inside texture groups | Hold'em subset, same size |
|---|---|---|---|---|
| 25 flops | 0.63 pts | 0.25 % of the pot | 1.40 pts | 1.74 pts |
| 49 flops | 0.58 pts | 0.32 % of the pot | 1.03 pts | 0.51 pts |
| 95 flops | 0.24 pts | 0.22 % of the pot | 0.51 pts | 0.23 pts |
| 184 flops | 0.16 pts | 0.08 % of the pot | 0.28 pts | 0.12 pts |

### Short Deck (`short-deck/`)

36 cards (six to ace): 7,140 flops, 573 distinct; weights add up to 7,140. From a 3-handed Short
Deck blueprint (100 antes, every player antes 1 and the button 1 more, a straight beats three of a kind).

| Subset | Action frequencies | Range EV | Inside texture groups |
|---|---|---|---|
| 30 flops | 0.84 pts | 0.38 % of the pot | 1.81 pts |
| 60 flops | 0.52 pts | 0.14 % of the pot | 0.90 pts |
| 120 flops | 0.48 pts | 0.19 % of the pot | 0.64 pts |

## How they were made

- Reference: a full-game blueprint (6-max, 100 bb cash, 5 % rake capped at 4.5 bb) holding all 1,755 flops; its flop
  decisions were within 0.17 % of the pot of exact solves on average in our measurements.
- Each flop is described by its strategies on three training lines (action frequencies and range EV), its suit
  structure and whether it is paired. Flops that play alike are grouped (weighted k-medoids, weight = how often the
  flop is dealt); each group's most central flop enters the subset with the group's combined weight.

## Limits

- The Hold'em subsets are chosen and measured on 6-max cash at 100 bb; PLO, tournaments and Short Deck have their own
  (above). Deeper stacks and multiway pots are not measured yet.
- The figures describe aggregated reports (frequencies and EV summed over flops), not how well one flop's strategy
  stands in for another flop.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use, share and adapt them, also in commercial tools, with
credit: *"Flop subsets by PulseGTO — https://pulsegto.com/flop-subsets"*.

Made by [PulseGTO](https://pulsegto.com), a solver for No-Limit Hold'em, Pot-Limit Omaha and tournaments.
