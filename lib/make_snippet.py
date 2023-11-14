# take a string and slice it 
# return [0, 5]
def make_snippet(sentence):
    slice = sentence.split()
    if len(slice) > 5:
        return ' '.join(slice[0:5]) + '...'
    else:
        return sentence
