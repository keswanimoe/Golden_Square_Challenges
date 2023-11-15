def reading_time(text):
# Parameters: text: a string containing text user wants to estimate reading time

# Returns: a string 'The estimated reading time is: ' followed by an estimated reading time as a float
# Assumptions: user can read 200 words per minute

# Side effects: print of the result 
    slice = text.split()
    words = len(slice)
    time = words/200
    if time == 1.0:
        return f'The estimated reading time is {time} minute'
    else:
        return f'The estimated reading time is {time} minutes'