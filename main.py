def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    print(f"Word count is: {get_word_count(text)}")
    list_letter_counts(get_letter_count(text))
    print("--- End report ---")  
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text): 
    words = text.split()
    return len(words)

def get_letter_count(text):
    dict = {}
    for char in text.lower():        
        if char in dict:
            dict[char] += 1            
        else:
            dict[char] = 1          
    return dict

def list_letter_counts(dict):   
    for i in sorted(list(dict.items())):
        if i[0].isalpha():
            print(f"The '{i[0]}' character was found {i[1]} times")        
    
main()
 