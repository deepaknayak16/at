'''
re.compile('pattern')	#Compile a regular expression pattern provided as a string into a re.Pattern object.
re.search(pattern, str)	#Search for occurrences of the regex pattern inside the target string and return only the first match.
re.match(pattern, str)	#Try to match the regex pattern at the start of the string. It returns a match only if the pattern is located at the beginning of the string.
re.fullmatch(pattern, str)	#Match the regular expression pattern to the entire string from the first to the last character.
re.findall(pattern, str)	#Scans the regex pattern through the entire string and returns all matches.
re.finditer(pattern, str)	#Scans the regex pattern through the entire string and returns an iterator yielding match objects.
re.split(pattern, str)	#It breaks a string into a list of matches as per the given regular expression pattern.
re.sub(pattern, replacement, str)	#Replace one or more occurrences of a pattern in the string with a replacement.
re.subn(pattern, replacement, str)	#Same as re.sub(). The difference is it will return a tuple of two elements.
First, a new string after all replacement, and second the number of replacements it has made
--------------------------------------------------------------------------------------------------------
\A	Matches pattern only at the start of the string.
\Z	Matches pattern only at the end of the string.
\d	Matches to any digit. Short for character classes [0-9].
\D	Matches to any non-digit. short for [^0-9].
\s	Matches any whitespace character. short for character class [ \t\n\x0b\r\f].
\S	Matches any non-whitespace character. Short for [^ \t\n\x0b\r\f].
\w	Matches any alphanumeric character. Short for character class [a-zA-Z_0-9].
\W	Matches any non-alphanumeric character. Short for [^a-zA-Z_0-9]
\b	Matches the empty string, but only at the beginning or end of a word. Matches a word boundary where a word character is [a-zA-Z0-9_].
    For example, '\bJessa\b' matches 'Jessa', 'Jessa.', '(Jessa)', 'Jessa Emma Kelly' but not 'JessaKelly' or 'Jessa5'.
\B	Opposite of a \b. Matches the empty string, but only when it is not at the beginning or end of a word
------------------------------------------------------------------------------------------------------------
*	Match 0 or more repetitions of the preceding regex. For example, a* matches any string that contains zero or more occurrences of 'a'.
+	Match 1 or more repetitions of the preceding regex. For example, a+ matches any string that contains at least one a, i.e., a, aa, aaa, or any number of a's.
?	Match 0 or 1 repetition of the preceding regex. For example, a? matches any string that contains zero or one occurrence of a.
{2}	Matches only 2 copies of the preceding regex. For example, p{3} matches exactly three 'p' characters, but not four.
{2, 4}	Match 2 to 4 repetitions of the preceding regex. For example, a{2,4} matches any string that contains 3 to 5 'a' characters.
{3,}	Matches minimum 3 copies of the preceding regex. It will try to match as many repetitions as possible.
For example, p{3,} matches a minimum of three 'p' characters.
-------------------------------------------------------------------------------------------------------------
*	Match 0 or more repetitions of the preceding regex. For example, a* matches any string that contains zero or more occurrences of 'a'.
+	Match 1 or more repetitions of the preceding regex. For example, a+ matches any string that contains at least one a, i.e., a, aa, aaa, or any number of a's.
?	Match 0 or 1 repetition of the preceding regex. For example, a? matches any string that contains zero or one occurrence of a.
{2}	Matches only 2 copies of the preceding regex. For example, p{3} matches exactly three 'p' characters, but not four.
{2, 4}	Match 2 to 4 repetitions of the preceding regex. For example, a{2,4} matches any string that contains 3 to 5 'a' characters.
{3,}	Matches minimum 3 copies of the preceding regex. It will try to match as many repetitions as possible.
For example, p{3,} matches a minimum of three 'p' characters.
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Remover the Special Charecter from the string 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
intal = "123abcjw:, .@! eiw"
final = re.sub('[^A-Za-z0-9]+', '', intal)
final1 = ''.join(e for e in intal if e.isalnum())
final2 = re.sub(r'\W+','', intal)
print("1st execution", final)
print("2nd execution", final1)
print("3rd execution", final2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Romve the Space from the string ex. "ab cd 12 de" o/p "abcd12de"
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
str1 = "ab cd 12 ef"
print (re.sub(r"\s+", "", str1), sep='')
print (re.sub(r"^\s+", "", str1), sep='') 
print (re.sub(r"\s+$", "", str1), sep='')
print (re.sub(r"^\s+|\s+$", "", str1), sep='')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Find all the number O/p[12, 34, 56]
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input = "ab 12 { cd 34 } ef 563 deepak 3 find 10 job after 2023 "
In_patt2 = r"\d+" #'12', '34', '563', '3', '10', '2023']
In_patt = r"\b\d{2}\b" #['12', '34']
reg_pat = re.compile(In_patt)
reg_pat2 = re.compile(In_patt2)
q_result = reg_pat.findall(Input)
q_result2 = reg_pat2.findall(Input)
print(q_result)
print(q_result2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Find all the number O/p ['Python', 'pandas']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
str3= "Jessa loves Python and pandas"
patt3 = r"\w{6}"
result3 = re.search(patt3, str3)
print(result3) #<re.Match object; span=(12, 18), match='Python'>
print(result3.group()) #Python
print(re.findall(patt3, str3)) #['Python', 'pandas']

str1 = "Ema Deepak whwrer is a good bad 236"
string_pattern = r"\b\w{3}\b"
regex_pattern = re.compile(string_pattern)
print(type(regex_pattern)) #<class 're.Pattern'>
result = regex_pattern.findall(str1)
print(result) #['Ema', 'bad', '236']

s_result = re.match(r"\w{3}", str1)
print("onlymatch", s_result) #<re.Match object; span=(0, 3), match='Ema'>
print("group match", s_result.group()) #Ema
