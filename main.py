def main(): 
    book_path = "books/frankenstein.txt"
    text = read_book(book_path) 
    word_count = num_words(text)
    characters = character_count(text)
    sorted_list = chars_to_sorted_list(characters)
    
    print(f"{word_count} are in this book")

    print()

    for item in sorted_list: 
        print(f"The character '{item['char']}' was found this many times: {item['num']}")

def read_book(book_path):
    with open(book_path) as f: 
        return f.read() 


def num_words(text): 
    counter = 0 
    words = text.split() 
    return len(words)
    
def character_count(text):
    characters = {}
    text_lowered = text.lower() 
    for c in text_lowered: 
        if c.isalpha(): 
            if c not in characters: 
                characters[c] = 1
            else: 
                characters[c]+= 1

    return characters

def sort_on(d):
    return d["num"]

def chars_to_sorted_list(characters):
    list = []
    for c in characters: 
        list.append({"char": c, "num": characters[c]})
    
    list.sort(reverse=True, key=sort_on) 
    return list



main()