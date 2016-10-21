"""
Problem:

    The function 'matcher' should take two strings as inputs.
    If they are:
      
      * Exactly the same, it should print "Exact match"
      * The same word but different case, it should print "Partial match"
    
    Otherwise, print "No match"


Tests:

    >>> matcher("Boom", "Boom")
    Exact match
    >>> matcher("Shake", "shake")
    Partial match
    >>> matcher("The", "room")
    No match
    >>> matcher("tick", "Tick")
    Partial match
    >>> matcher("boom", ".")
    No match

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def matcher(word1, word2):

    s = word1
    t = word2

    if s == t:
        print("Exact match")

    elif s.title() == t or s == t.title() :
        print("Partial match")

    else:
        print("No match")
        

