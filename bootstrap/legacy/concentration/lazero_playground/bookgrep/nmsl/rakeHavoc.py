from rake_nltk import Rake
def getShit(a):
  with open(a, "r") as f:
    return f.read()
    # shall we split?
r = Rake()
my_test = getShit("nmsl.log")
r.extract_keywords_from_text(my_test)
print(r.get_ranked_phrases())
print("==============================")
print(r.get_ranked_phrases_with_scores())
print("===========================")
print(r.stopwords) # these are english stopwords.
print("=============================")
print(r.get_word_degrees())
# fuck those people.