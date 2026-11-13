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

## How they were made

- Reference: a full-game blueprint (6-max, 100 bb cash, 5 % rake capped at 4.5 bb) holding all 1,755 flops; its flop
  decisions were within 0.17 % of the pot of exact solves on average in our measurements.
- Each flop is described by its strategies on three training lines (action frequencies and range EV), its suit
  structure and whether it is paired. Flops that play alike are grouped (weighted k-medoids, weight = how often the
  flop is dealt); each group's most central flop enters the subset with the group's combined weight.

## Limits

- Chosen and measured on one game: 6-max cash at 100 bb. Other stack depths, tournaments and multiway pots are not
  measured yet.
- The figures describe aggregated reports (frequencies and EV summed over flops), not how well one flop's strategy
  stands in for another flop.

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use, share and adapt them, also in commercial tools, with
credit: *"Flop subsets by PulseGTO — https://pulsegto.com/flop-subsets"*.

Made by [PulseGTO](https://pulsegto.com), a solver for No-Limit Hold'em and Pot-Limit Omaha.
