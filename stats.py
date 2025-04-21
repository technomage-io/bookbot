def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    n = 1
    lower_text = text.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char] = char_counts[char] +1
        else:
            char_counts[char] = 1

        
    return char_counts