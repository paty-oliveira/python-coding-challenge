"""
Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear
in the glass based on their density. (Lower density floats to the top)

The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O','O','O','O']
 ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
 ['H', 'H', 'O', 'O']         ['H','H','H','H']
 ]                           ]

The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.
"""

DENSITY_CHART = {
    "H": 1.36,
    "W": 1.00,
    "A": 0.87,
    "O": 0.80
}


def separate_liquids(glass: list):
    if not glass:
        return []

    layer_size = len(glass[0])
    liquids_ordered_by_density = sorted([liquid for layer in glass for liquid in layer], key=lambda l: DENSITY_CHART[l])

    return [liquids_ordered_by_density[i:i + layer_size] for i in range(0, len(liquids_ordered_by_density), layer_size)]

