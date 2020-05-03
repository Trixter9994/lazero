import re


def windowConv(a, window_size):
    return [a[x: x + window_size] for x in range(len(a) - window_size)]


def windowEndMark(a, window_size):
    return [a[x * window_size: (x + 1) * window_size] for x in range(len(a) // window_size)]


def phraseStartMark(a, start_phrase):
    return re.findall(r'{}.+'.format(re.escape(start_phrase)), a)


def phraseEndMark(a, end_phrase):
    return re.findall(r'.+{}'.format(re.escape(end_phrase)), a)


def phraseSegment(a, start_phrase, end_phrase):
    return re.findall(r'{}.+{}'.format(re.escape(start_phrase, end_phrase)), a)


def setStartMark(a, start_phrase, sigma):
    assert sigma < 1 and sigma > 0
    len_phrase = len(start_phrase)
    a0, a1 = list(map(round, [len_phrase * sigma, len_phrase / sigma]))
    start_phrase = "".join(set(start_phrase))
    return re.findall(r'['+r'{}'.format(re.escape(start_phrase))+r']{'+r'{},{}'.format(str(a0), str(a1))+r'}.+', a)


def setEndMark(a, end_phrase, sigma):
    assert sigma < 1 and sigma > 0
    len_phrase = len(end_phrase)
    a0, a1 = list(map(round, [len_phrase * sigma, len_phrase / sigma]))
    end_phrase = "".join(set(end_phrase))
    return re.findall(r'.+[{}]'.format(re.escape(end_phrase))+r'{'+r'{},{}'.format(str(a0), str(a1))+r'}.+', a)


def setSegment(a, start_phrase, end_phrase, sigma):
    assert sigma < 1 and sigma > 0
    len_phrase = len(end_phrase)
    a0, a1 = list(map(round, [len_phrase * sigma, len_phrase / sigma]))
    len_phrase = len(start_phrase)
    a2, a3 = list(map(round, [len_phrase * sigma, len_phrase / sigma]))
    start_phrase = "".join(set(start_phrase))
    end_phrase = "".join(set(end_phrase))
    return re.findall(r'['+r'{}'.format(re.escape(start_phrase))+r']{'+r'{},{}'.format(str(a2), str(a3))+r'}'+r'.+[{}]'.format(re.escape(end_phrase))+r'{'+r'{},{}'.format(str(a0), str(a1))+r'}.+', a)
