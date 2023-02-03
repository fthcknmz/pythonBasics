# A RegEx, or Regular Expression, is a sequance of characters that forms a search pattern.
# RegEx can be used to check if a tring contains the specific search pattern.
import re # Python built-in package re, can be used to work with RegEx

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print()
"""
The re module offers a set of functions that allows us to search a string for a match:

findall	returns a list containing all matches
search	returns a Match object if there is a match anywhere in the string
split	returns a list where the string has been split at each match
sub	    replaces one or many matches with a string

"""
"""
Metacharacters are characters with a special meaning:
    
Character	 Description	                                                                 Example
[]	         A set of characters	                                                        "[a-m]"	
\            Signals a special sequence (can also be used to escape special characters)    	"\d"	
.	         Any character (except newline character)                                     	"he..o"	
^	         Starts with	                                                                "^hello"	
$	         Ends with	                                                                    "world$"	
*	         Zero or more occurrences	                                                    "aix*"	
+          	One or more occurrences	                                                        "aix+"	
{}	        Exactly the specified number of occurrences	                                    "al{2}"	
|	        Either or	                                                                    "falls|stays"	
()	        Capture and group

"""
"""
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	                                                                                                                             Example
\A	        Returns a match if the specified characters are at the beginning of the string	                                                        "\AThe"	
\b       	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	                                                     r"\bain"  r"ain\b"	
\B      	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	                                                     r"\Bain"  r"ain\B"	
\d	        Returns a match where the string contains digits (numbers from 0-9)	                                                                    "\d"	
\D      	Returns a match where the string DOES NOT contain digits	                                                                            "\D"	
\s      	Returns a match where the string contains a white space character	                                                                    "\s"	
\S	        Returns a match where the string DOES NOT contain a white space character	                                                            "\S"	
\w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	        Returns a match where the string DOES NOT contain any word characters	                                                                "\W"	
\Z	        Returns a match if the specified characters are at the end of the string	                                                            "Spain\Z"

"""
"""

A set is a set of characters inside a pair of square brackets [] with a special meaning:
    
Set	            Description
[arn]       	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	        Returns a match for any lower case character, alphabetically between a and n	
[^arn]	        Returns a match for any character EXCEPT a, r, and n	
[0123]	        Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	        Returns a match for any digit between 0 and 9	
[0-5][0-9]	    Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	   Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

"""

# findall() function returns a list containing all matches
txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x)
print()
# search() function returns a match object if there is a match
x = re.search("\s", txt)
print("The first white-space character is located in positon:",x.start())
print()
# split function returns a list where the string has been split at each match.
x = re.split("\s",txt)
print(x)
x = re.split("\s",txt, 1) #you can control the number of occurences by specifying maxsplit parameter
print(x)
print()
# max() function replaces the matches with the text of your choice
x = re.sub("\s","9",txt)
print(x)
x = re.sub("\s","9",txt,1) #you can control the number of replacements by specifiyng the count parameter
print(x)