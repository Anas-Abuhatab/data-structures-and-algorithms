from .hash_tables import Hashtable

def repeat_word(text: str) -> str:
    valid_chars = "abcdefghijklmnopqrstuvwxyz "
    words = "".join([x for x in text.lower() if x in valid_chars])
    hashy = Hashtable()
    for word in words.split():
        if hashy.contains(word):
            return word
        hashy.add(word, "word")

    return "no duplicate words found"