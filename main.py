def return_txt(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(txt):
    words = txt.split()
    return len(words)


def count_letters(txt):
    res = {}
    file_contents = txt.lower()
    for c in file_contents:
        if not c.isalpha():
            continue
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


def gen_report(book_path):
    txt = return_txt(book_path)
    num_words = count_words(txt)
    txt_dict = count_letters(txt)
    txt_list = [(c, txt_dict[c]) for c in txt_dict]
    txt_list.sort()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print()
    for record in txt_list:
        print(f"The '{record[0]}' character was found {record[1]} times")
    print("--- End report ---")


def main():
    book_path = "./books/frankenstein.txt"
    gen_report(book_path)


if __name__ == "__main__":
    main()
