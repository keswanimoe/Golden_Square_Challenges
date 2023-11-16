1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def improve_grammar(text):

<!-- Parameters: text: a string 

Returns: True or False

Side effects: no side effects, nothing is printed

    pass



3. Create Examples as Tests
Make a list of examples of what the function will take and return. -->

# EXAMPLE

Give a text and return True if condition is met
Condition: a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark

improve_grammar('This is a sentence') -> False
improve_grammar('This is a sentence.') -> True


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.improve_grammar import *

def test_improve_grammar_returns_false():
result = improve_grammar('This is a sentence')
assert result == False

def test_improve_grammar_returns_true():
result = improve_grammar('This is a sentence.')
assert result == True