def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''

    acceptable_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "# Include a space at the end
    clean = word.lower()
    for i in clean:
        if i not in acceptable_char:
            clean = clean.replace(i,'')
    return clean
    

def test_letters(w1, w2):
    '''(str,str, list of str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''
    
    #sorted_w1 = ''.join(sorted(w1))
    #sorted_w2 = ''.join(sorted(w2))
    sorted_w1 = sorted(w1)
    sorted_w2 = sorted(w2)
    if sorted_w1 == sorted_w2:
        return True
    return False
    
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word() function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''
    
    s = s.split()
    new_list = []
    for i in s:
        ns = clean_word(i)
        if ns not in new_list:
            new_list.append(ns)
    sorted_list = sorted(new_list)
    return sorted_list


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function must call test_letters() function.
    The function returns a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    

    >>> word_anagrams("listen", wordbook)
    ['silent', 'enlist', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['care', 'acre']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
    
    new_list = []
    for i in wordbook:
        if test_letters(word,i) == True and i != word:
            new_list.append(i)
    sorted_list = sorted(new_list)
    return sorted_list
         

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''
    
    
    new_list = []
    for i in l:
        counter = 0
        for j in wordbook:
            if test_letters(i,j) == True and i != j  :
                counter = counter + 1
        new_list.append(counter)
    return new_list


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
 
    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'race', 'ear']
    '''
    
    new_list = []
    for i in range(0,len(anagcount)):
        if anagcount[i] == k :
            new_list.append(l[i])
    sorted_list = sorted(new_list)
    return sorted_list

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['listen', 'item']
    '''
    
    k = 0
    for i in anagcount:
        if i > k:
            k = i
    return k_anagram(l, anagcount, k)


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    k = 15
    for i in anagcount:
        if i < k:
            k = i
    return (k_anagram(l, anagcount, k))


                
    
##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

# when asking for k from the user assume that they will enter non-negative integer
if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")

  
    
    print(max_anagram(l, anagcount))
    print("")
    print("Here are their anagrams :")
    
    for i in max_anagram(l, anagcount):
        print("Anagrams of", i, "are:", word_anagrams(i, wordbook))
    
    print("")    
    print("Here are the words from your file that have no anagrams :")
    print(zero_anagram(l, anagcount))
    print("")

    print("Say you are interested if there is a word in your file that has exactly k anagrams")
    k = int(input("Enter an integer for k: "))
    print("Word(s) in your file with exactly " + str(k) + " anagram(s):")
    print(k_anagram(l, anagcount, k))
    

    
elif choice=='2':

    while True:

        flag = False
        
        while flag == False:
            word = input("Enter the letters that you have, one after another with no space: ")
            if " " in word:
                print("Error: You entered space(s).")
                flag = False
            else:
                flag = True

        word = clean_word(word)

        print("Would you like to form a word with: ")
        print("1. all these letters?")
        print("2. all but one of these letters?")

        flag2 = False

        while flag2 == False:
            sub_choice = input()
            if sub_choice == "1" or sub_choice == "2":
                flag2 = True
            elif sub_choice != "1" or sub_choice != "2":
                print("You must choose 1 or 2. Please try again.")
                print("Would you like to form a word with: ")
                print("1. all these letters?")
                print("2. all but one of these letters?")
                flag2 = False
            
        
        if int(sub_choice) == 1:
            
            if word_anagrams(word, wordbook) == []:
                print("There is no word comprised of exactly these letters.")
            else:
                print("Here are the word(s) comprised of exactly these letters:")
                print(word_anagrams(word, wordbook))
                
        elif int(sub_choice) == 2:
            print("The letters you gave us are: " + word)
            print("Let's see  what we can get if we ommit one of these letters.")
            
            for i in range(len(word)):
                word2 = word[:i]+word[i+1:]
                print("Without the letter in position", (i+1), "we have letters", word2)
                if word_anagrams(word2, wordbook) == [] :
                    print("There is no word comprised of letters:", word2)
                else:
                    print("Here are the words that are comprised of letters:", word2)
                    print(word_anagrams(word2, wordbook))
    
        
                       
                      
else:
    print("Good bye")


