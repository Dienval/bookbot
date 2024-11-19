def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        word_count = len(words)
        print(word_count)

main()

def char_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        char_dict = {}
        words = file_contents.split()
        
        for l in words:

            low_l = l.lower()
            for split_char in low_l:
                if split_char in char_dict:
                    char_dict[split_char] += 1
                else:
                    print(f"{split_char} first instance - adding to dictionary")
                    char_dict[split_char] = 1
                    
        print(f"{char_dict}")

char_count()

        