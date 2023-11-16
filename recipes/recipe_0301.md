1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def reading_time(text):

<!-- Parameters: text: a string containing text user wants to estimate reading time

Returns: a string 'The estimated reading time is: ' followed by an estimated reading time as a float
Assumptions: user can read 200 words per minute

Side effects: print of the result -->

    pass



3. Create Examples as Tests
Make a list of examples of what the function will take and return. -->

# EXAMPLE

Give a text and return esimated reading time

reading_time('text') -> 'The estimated reading time is 1 minute'


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.reading_time import *

def test_reading_time_returns_one():
result = reading_time(text)
assert result == 'The estimated reading time is 1 minute'

def test_reading_time_returns_twentytwo():
result = reading_time(text)
assert result == 'The estimated reading time is 22 minutes'
