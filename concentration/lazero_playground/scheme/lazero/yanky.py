from common_words_ranker import ranky

with open("index.html") as f:
    f0 = f.read()
    m = ranky(f0, 0.5, 10)
    print(m)
