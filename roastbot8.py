import requests
from bs4 import BeautifulSoup
import copy
import pygame as pg
import random
import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


pg.mixer.init()
pg.mixer.music.load("sound1.mp3")
pg.mixer.music.set_volume(1)


def playSound(sound = "random"):
    
    
    if sound == "random":
        
        r = random.randint(1,10)
        sound_file = "sound" + str(r) + ".mp3"
        

    else:
    
        
        sound_file = "sound" + str(sound) + ".mp3"
    
    pg.mixer.music.load(sound_file)
    pg.mixer.music.play()


def relatedWords(keyword):

    if " " in keyword:
    
        keyword_list = keyword.split(" ")
        keyword = str(keyword_list[0]) + "%20" + str(keyword_list[1])    




    url = "https://relatedwords.org/relatedto/" + str(keyword)
    r = requests.get(url)
    
    
    soup = BeautifulSoup(r.content, features="lxml")
    
    
    words = soup.find_all("script")
    

    p_copy = copy.copy(words[5])
    
    
    copy_string = ""
    
    for char in p_copy:
        
        for item in char:
        
            copy_string += str(item)
    
    copy_list = copy_string.split(":")
    
    related_words_string = ""
    
    for text in copy_list:
        
        if "score" in text and "wiki" not in text:
            
            
            related_words_string += str(text)
            
            
    related_words_list = related_words_string.split(",")
            
    final_string = ""
            
    for word in related_words_list:
        
        if "score" in word:
            
            new_word = str(word[7:])
            final_string= final_string + new_word + ","
            
    final_list = final_string.split(",")
    
    return final_list

# keyword = "tom cruise"
# result = relatedWords(keyword)

# print(result)







def tokenize(sentence):
    
    token=nltk.word_tokenize(sentence)
    tag=nltk.pos_tag(token)
    
    return tag






sentence = "I will ride your mom like a bike"



def sentenceDoctor(sentence, noun_replace = True, verb_replace = True):
    
    
    token=nltk.word_tokenize(sentence)  # splits the sentence into individual words
    tag=nltk.pos_tag(token)             # gives the word type
    
    ### tag is the variable that stores the sentence
    
    type_list = []  # list to collect the word type of each word
    noun_list = []   # format is [noun, word position in sentence] 
    verb_list = []   # format is [verb, word position in sentence] 
    
    
    ### Goes through sentence and makes a list of nouns and verbs ###
    
    i = 0
    for item in tag:
        
        type_list.append(item[1])
        
        if item[1] == "NN":
            
            noun_list.append([item[0], i])
        
        elif item[1] == "VB":
            
            verb_list.append([item[0], i])
            
        
        i += 1
        
        
        
        
        
    if len(noun_list) >= 2 and noun_replace == True:
        
        last_noun_position = noun_list[len(noun_list) - 1][1] # finds poisiton of last noun in original sentence
        word_to_replace = noun_list[len(noun_list) - 1][0]
        possible_replacements = relatedWords(word_to_replace)
        word_pool_size = 30
        
        if len(possible_replacements) < word_pool_size:
            upper_bound = len(possible_replacements)
            
        else:
            upper_bound = word_pool_size
            
        
        for i in range(1,100):
            
            r = random.randint(0, upper_bound)
            replacement_word = possible_replacements[r]
            replacement_word_type = nltk.word_tokenize(replacement_word)
            
            if replacement_word_type == "NN":
                break
            
        tag[last_noun_position] = (replacement_word, "NN")
        
        
        
        
        
    elif len(noun_list) == 1 and noun_replace == True:
        
        last_noun_position = noun_list[0][1]
        word_to_replace = noun_list[len(noun_list) - 1][0]
        possible_replacements = relatedWords(word_to_replace)
        word_pool_size = 30
        
        if len(possible_replacements) < word_pool_size:
            upper_bound = len(possible_replacements)
            
        else:
            upper_bound = word_pool_size
            
        
        for i in range(1,100):
            
            r = random.randint(0, upper_bound)
            replacement_word = possible_replacements[r]
            replacement_word_type = nltk.word_tokenize(replacement_word)
            
            if replacement_word_type == "NN":
                break
            
        tag[last_noun_position] = (replacement_word, "NN")
    
    
    
    
    
    if len(verb_list) >= 1 and verb_replace == True:
        
        first_verb_position = verb_list[0][1]
        word_to_replace = verb_list[0][0]
        possible_replacements = relatedWords(word_to_replace)
        word_pool_size = 30
        
        if len(possible_replacements) < word_pool_size: 
            upper_bound = len(possible_replacements)
            
        else:
            upper_bound = word_pool_size
            
        
        for i in range(1,100):
            
            r = random.randint(0, upper_bound)
            replacement_word = possible_replacements[r]
            replacement_word_type = nltk.word_tokenize(replacement_word)
            
            if replacement_word_type == "VB":
                break

        tag[first_verb_position] = (replacement_word, "NN")
    
    
    
    
    
    
    output_string = ""
    for item in tag:
        
        output_string += item[0] + " "
        
    print(output_string)
        
        
        
        
        
        
    return noun_list, verb_list, tag



output = sentenceDoctor(sentence)
        
        





