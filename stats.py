def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
     char_counts = {}
     for char in text.lower():  # Convert to lowercase for case-insensitive counting
         if char.isalpha():  # Only count letters
             char_counts[char] = char_counts.get(char, 0) + 1
     return char_counts

def get_book_text(path): 
    with open(path) as f:
        return f.read()
        
    
def sort_character_counts(char_counts):
    """Sorts character counts from greatest to least."""
    sorted_list = [{"character": char, "count": count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x["count"], reverse=True)  # Sort by count in descending order
    return sorted_list

