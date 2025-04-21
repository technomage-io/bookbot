def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    print (file_contents)
    count = num_words()
    print(f"{count} words found in the document")
    return file_contents


def get_book_text(path):
      with open(path) as f:
        return f.read()

def num_words():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = (len)(file_contents.split())
           
    return (num_words)

main()