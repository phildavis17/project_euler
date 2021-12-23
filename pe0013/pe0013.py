# Project Euler
# Problem 013
# Philip Davis

from pathlib import Path


def parse_input(file_name: Path) -> list:
    with open(file_name) as raw_input:
        return [l.strip() for l in raw_input.readlines()]

_fn = Path(__file__).stem
problem_input = parse_input(Path(_fn + "_input.txt"))


columns = [list(map(int, c)) for c in list(zip(*problem_input))]
columns.reverse()
col_dict = {i: sum(c) for i, c in enumerate(columns)}


answer = ""
total = 0
for n in [sum(c) for c in columns]:
    total += n
    total = str(total)
    answer = total[-1] + answer
    total = int(total[:-1])

answer = str(total) + answer
print(answer[:10])
