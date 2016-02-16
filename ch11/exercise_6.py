# Write a program that asks the user to type in a sentence and then print 
# the sentence translated to pirate.

# Here's a table of English to Pirate translations:
# English         Pirate
# sir             matey
# hotel           fleabag inn
# student         swabbie
# boy             matey
# madam           proud beauty
# professor       foul blaggart
# restaurant      galley
# your            yer
# excuse          arr
# students        swabbies
# are             be
# lawyer          foul blaggart
# the             th'
# restroom        head
# my              me
# hello           avast
# is              be
# man             matey


eng_to_pirate = {
    "sir": "matey", "hotel": "fleabag inn", "student": "swabbie", 
    "boy": "matey", "madam": "proud beauty", "professor": "foul blaggart",
    "restaurant": "gallery", "your": "yer", "excuse": "arr", 
    "students": "swabbies", "are": "be", "lawyer": "foul blaggart",
    "the": "th'", "restroom": "head", "my": "me", "hello": "avast",
    "is": "be", "man": "matey"
}



def translate_eng_to_pirate(eng_sentence):
    pirate_sentence = eng_sentence
    for english, pirate in eng_to_pirate.items():
        pirate_sentence = pirate_sentence.replace(english, pirate)
    return pirate_sentence

sentence = raw_input("Please type in a sentence: ")
print translate_eng_to_pirate(sentence)

# print translate_eng_to_pirate("hello sir, I am in a hotel, because my student is a boy. \
#     And the professor is madam lawyer.  We meet at your restaurant.  Please excuse my \
#     students because they are here to use the restroom.  THank you my man.")