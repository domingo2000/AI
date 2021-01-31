import random
import re


def index_all_regex(pattern, string):
    return [(m.start(0), m.end(0)) for m in re.finditer(pattern, string)]


def replace_string(string, start, stop, replacement):
    a = ""
    a += string[:start]
    a += replacement
    a += string[stop:]
    return a


def sequence(lenght):
    letters = ["A", "B", "C", "E"]
    seq = ""
    for _ in range(lenght):
        seq += random.choice(letters)
    return seq


def expand_seq(sequence):
    """
    Given a sequence return all the possible sequence using the equalities.
    Note: Ex = x is implemented using regular expressions with re library, so EEE
    has only 1 expanding
    """
    expanded_seqs = []
    """
    # FORM WITH REGEX
    # First Cases with no special regex
    eq_dict = {"AC": "E", "AB" : "BC", "BB": "E"}
    for pattern, replacement in eq_dict.items():
        pattern = re.compile(pattern)
        for start, stop in index_all_regex(pattern, sequence):
            new_seq = replace_string(sequence, start, stop, replacement)
            expanded_seqs.append(new_seq)
    # Case E. sequence
    pattern = re.compile("E.")
    for start, stop, replacement in \
            [(m.start(0), m.end(0), m.group()[1]) for m in re.finditer(pattern, sequence)]:
        new_seq = replace_string(sequence, start, stop, replacement)
        expanded_seqs.append(new_seq)
    return expanded_seqs
    """
    # Forma propia
    start = 0
    stop = 2
    while stop <= len(sequence):
        block = sequence[start: stop]
        if block == "AB":
            expanded_seqs.append(replace_string(sequence, start, stop, "BC"))
        elif block == "AC":
            expanded_seqs.append(replace_string(sequence, start, stop, "E"))
        elif block == "BB":
            expanded_seqs.append(replace_string(sequence, start, stop, "E"))
        elif block[0] == "E":
            expanded_seqs.append(replace_string(sequence, start, stop, block[1]))
        start += 1
        stop += 1
    return expanded_seqs


def is_goal(sequence):
    if sequence == "E":
        return True
    else:
        return False


def sequence_creator(lenght):
    seq = "E"
    new_seq = random.choice(["EE", "AB", "AC"])
    while len(new_seq) < lenght:
        n = len(new_seq)
        start = random.randint(0, n - 2)
        stop = start + 2
        block = new_seq[start:stop]
        a = new_seq
        if block[0] == "E":
            new_seq = new_seq[:start] + random.choice(["EE", "BB", "AC"]) + new_seq[stop - 1:]
            type = 0
        elif block[1] == "E":
            new_seq = new_seq[:start + 1] + random.choice(["BB", "AC"]) + new_seq[stop:]
            type = 1
        elif block == "BC":
            new_seq = new_seq[:start] + "AB" + new_seq[stop:]
            type = 2
        else:
            a = new_seq
            new_seq = new_seq[:start] + f"E{block[0]}" + new_seq[stop - 1:]
            type = 3
    return new_seq


if __name__ == "__main__":
    seq = sequence(100)
    print(sequence_creator(30))