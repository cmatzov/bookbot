def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        file_content = file.read()
    return file_content

def count_words(file_content: str) -> int:
    return len(file_content.split())

def create_list_of_chars(file_content: str) -> str:
    return ["".join(word).lower() for word in file_content]

def characters_count(char_list: str) -> dict[str, int]:
    recurrencies = {}
    for char in char_list:
        try:
            counter = recurrencies[char]
            counter += 1
            recurrencies[char] = counter
        except KeyError:
            recurrencies[char] = 1
    return recurrencies

def sort_list(recurrency: dict):
    return recurrency["count"]

def report(recurrencies: dict[str, int]) -> list[dict]:
    unsorted_list = [{"char": char, "count": count} for char, count in recurrencies.items()]
    unsorted_list.sort(reverse=True, key=sort_list)
    return unsorted_list

def print_report(unsorted_list: list[dict]):
    for char_count in unsorted_list:
        key = char_count["char"]
        value = char_count["count"]
        if key.isalpha():
            symbol_recurrency = f"{key}: {value}"
            print(symbol_recurrency)