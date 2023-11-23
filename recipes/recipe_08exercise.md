design recipe for 08_test_drive_a_class_system exercise

## Unit Tests for Diary

``
Check that Diary may be instanstiated
``

    entry = Diary()
    isinstance(entry, Diary) => True

``
Initalises an empty list for diary entries
``

    entry = Diary()
    actual = entry.diary
    expected = []
    actual => expected

``
Returns an empty list when the all() method is initially applied to an instance (e.g before any entries have been added)
``

    entry = Diary()
    actual = entry.all()
    expected = []
    actual => expected

## Unit Tests for DiaryEntry2

``
Check that an instance object has been created 
``

    entry = DiaryEntry2('My Title', 'These are the contents')
    isinstance(entry, DiaryEntry2) => True


``
Initalises with title and contents a diary entry
``

    entry = DiaryEntry2('My Title', 'These are the contents')
    actual_title = entry.title
    actual_contents = entry.contents
    
    expected_title = 'My Title'
    expected_comtents = 'These are the contents'
    
    actual_title => expected_title
    actual_contents => expected_comtents


``
Returns the number of words in the contents 
``


    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.count_words()
    expected = 4
    
    assert actual => expected


``
Returns the integer 1 if a user can read 4 words per minute
``

    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.reading_time(4)
    expected = 1
    
    assert actual => expected

``
Returns a smaller chunk of contents epresenting a chunk of the contents that the user could read in the specified number of minutes so if a reader can read 3 words a minute and the contents is 4 words, return 3 words
``

    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.reading_chunk(3, 1)
    expected = 'These are the'
    assert actual == expected 

``
If called again, reading_chunk() should return the next chunk, skipping what has already been read
``

    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.reading_chunk(3, 1)
    expected = 'contents'
    assert actual == expected 

``
If contents if fully read, the next call should restart from the beginning
``

    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.reading_chunk(3, 1)
    expected = 'These are the'
    actual => expected

## Integration Tests 

``
Verify that add() adds an instance of DiaryEntry into the Diary list
``

    entries = Diary()
    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entries.add(entry)
    expected = [entry]
    actual => expected


``
Returns a list of instances of DiaryEntry which have been added into Diary
``

    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents')
    entry2 = DiaryEntry2('A Title', 'This is the contents')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.all()
    expected = [entry1, entry2]
    actual => expected

``
Returns an integer representing the total number of words in all diary entries
``

    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents')
    entry2 = DiaryEntry2('A Title', 'This is the contents')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.count_words()
    expected = 8
    actual => expected


``
For 2 entries, it should return the an estimate reading time in minutes if the user were to read all entries in the diary
``

    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents')
    entry2 = DiaryEntry2('A Title', 'This is the contents')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.reading_time(4)
    expected = 2
    actual => expected


``
For 2 seperate diary entries, return the instance of DiaryEntry representing the entry that is closest to, but not over, the length that the user could read in the minutes they have available given their reading speed.  If 1 diary entry is 10 words and another is 15 and I can read 13 words a minute, return the 10 word entry.
``


    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry2('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.find_best_entry_for_reading_time(13, 1)
    expected = entry
    actual => expected
