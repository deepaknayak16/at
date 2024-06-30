from collections import defaultdict  
  
def AnagramsTogether(words): 
    groupedWords = defaultdict(list) 
  
    # Put all anagram words together in a dictionary  
    # where key is sorted word 
    for word in words: 
        groupedWords["".join(sorted(word))].append(word) 
  
    # Print all anagrams together 
    for group in groupedWords.values(): 
        print(" ".join(group))       
  
  
if __name__ == "__main__":    
    arr =  ["cat", "dog", "tac", "god", "act"]   
    print(AnagramsTogether(arr))  


import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,7}\b'

def check(email):
    
    if (re.fullmatch(regex, email)):
        print ("valid Email")
    else:
        print("invalid")
        
if __name__ =='__main__':
    email = "ankitrai326@gmail.com"
    check(email)