from stats import get_book_text, count_words, create_list_of_chars, characters_count, report, print_report

def main():
    file = "books/frankenstein.txt"
    file_content = get_book_text(file)
    char_list = create_list_of_chars(file_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_content)} total words")
    print("--------- Character Count -------")
    report_list = report(characters_count(char_list))
    print_report(report_list)
    print("============= END ===============")

if __name__ == "__main__":
    main()