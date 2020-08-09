import difflib
def diff(a,b):
    thug=[a[i:i+n] for i, _, n in difflib.SequenceMatcher(None, a, b).get_matching_blocks() if n]
    return thug
