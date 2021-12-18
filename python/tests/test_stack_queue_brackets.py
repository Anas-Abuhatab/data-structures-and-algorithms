from stack_queue_brackets.stack_queue_brackets import validate_brackets



def test_validate_brackets():
    actual = validate_brackets("[{}[jgvuyv0]((*()))]")
    expected = True
    assert actual == expected