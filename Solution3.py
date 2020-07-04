sample_para = 'fried and this is fired and other word is gainly with anagram for laying with the next in the play listen me then go te the last word silent.'
li_of_words = sample_para.split()

li_of_anagrams = []

for word in li_of_words:
    for word2 in li_of_words:
        if word != word2 and (sorted(word) == sorted(word2)) :
            li_of_anagrams.append(word)

print(li_of_anagrams)        
