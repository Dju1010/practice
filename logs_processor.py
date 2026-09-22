import re
from collections import Counter

PATTERN = re.compile(r"\[(INFO|WARNING|ERROR|DEBUG)\]")


def read_log(path):
    with open(path, encoding="utf-8") as f:
        return f.readlines()


def count_slow(lines, levels):
    result = {}
    for lvl in levels:
        count = 0
        for line in lines:
            if f"[{lvl}]" in line:
                count += 1
        result[lvl] = count
    return result


def count_fast(lines):
    counter = Counter()
    for line in lines:
        m = PATTERN.search(line)
        if m:
            counter[m.group(1)] += 1
    return dict(counter)


def main():
    lines = read_log("app.log")
    levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

    print("Строк:", len(lines))
    print("Медленный:", count_slow(lines, levels))
    print("Быстрый:", count_fast(lines))


if __name__ == "__main__":
    main()