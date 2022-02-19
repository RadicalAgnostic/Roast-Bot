import requests
from bs4 import BeautifulSoup
import copy

url = "https://relatedwords.org/relatedto/fuck"
r = requests.get(url)

# print(r.content)

soup = BeautifulSoup(r.content, features="lxml")


    
words = soup.find_all("script")


# i = 0
# for word in words:
    
#     print(word)
#     i += 1
    
#     print(i)
    

# print(words[5])


big_word = words[5]

# print(big_word)

p_copy = copy.copy(words[5])

print(p_copy)
copy_list = []
copy_string = ""

for char in p_copy:
    
    for item in char:
    
        print(item)
        print("\n\n")
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
        
        print(222)
        
final_list = final_string.split(",")