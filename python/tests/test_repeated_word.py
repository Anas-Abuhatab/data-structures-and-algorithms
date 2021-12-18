from hash_table.repeated_word import repeat_word

def test_string_one():
    actual = repeat_word("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected
def test_string_two():
    actual = repeat_word("It was the best of times, it was the worst of times, it was the age of wisdom")
    expected = "it"
    assert actual == expected

def test_string_three():
    actual = repeat_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs")
    expected = "summer"
    assert actual == expected