#!/usr/bin/python3

def min_cubes_power(game: str) -> int:
    if game:
        r = 0
        g = 0
        b = 0
        subsets = game.split(': ')[1].split('; ')
        for subset in subsets:
            shows = subset.split(' ')
            for idx, val in enumerate(shows):
                if val[-1] == ',':
                    shows[idx] = val[:-1]
            vals = {shows[i + 1]: int(shows[i])
                    for i in range(0, len(shows), 2)}
            for key in ['red', 'green', 'blue']:
                if not vals.get(key):
                    vals[key] = 0
            if vals['red'] > r:
                r = vals['red']
            if vals['green'] > g:
                g = vals['green']
            if vals['blue'] > b:
                b = vals['blue']
        return r * g * b
    return 0


def main():
    out = 0
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        for idx, line in enumerate(contents):
            out += min_cubes_power(line)

    print(out)


if __name__ == '__main__':
    main()
