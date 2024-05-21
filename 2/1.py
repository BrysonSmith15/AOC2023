#!/usr/bin/python3

def is_valid(game: str) -> bool:
    if game:
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
            if not (vals.get('red') <= 12 and
                    vals.get('green') <= 13 and
                    vals.get('blue') <= 14):
                return False
        return True
    return False


def main():
    out = 0
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        for idx, line in enumerate(contents):
            if is_valid(line):
                out += idx + 1
                print(line)

    print(out)


if __name__ == '__main__':
    main()
