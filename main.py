import sys
from stats import get_book_text
from stats import get_num_words
from stats import count_characters
from stats import sort_character_counts


def main():
    print (sys.argv)
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
       book_path = sys.argv[1]
       
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_character_counts(char_counts)

    #print(f"{num_words} words found in the document")
    #print(f"{char_counts}")

    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words") 
    print ("--------- Character Count -------")
    
    for entry in sorted_chars:
        print(f"{entry['character']}: {entry['count']}")

    print ("============= END ===============")

main()