import sys
from stats import get_book_text, count_words, create_list_of_chars, characters_count, report, print_report

def main():
    try:
        file = sys.argv[1]
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

    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == "__main__":
    main()