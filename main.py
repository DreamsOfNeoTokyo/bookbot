import sys
from stats import get_word_count, char_count, sort_list





def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
                return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    full_count = char_count(book_text)
    sorted_chars = sort_list(full_count)
    
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
        else:
            pass
    print("============= END ===============")






main()




