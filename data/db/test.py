from difflib import get_close_matches as matches

user_word=["test"]
sample_word=["tesst"]

for i in user_word:
    matched_word = matches(i,sample_word,n=1)

print(matched_word)
