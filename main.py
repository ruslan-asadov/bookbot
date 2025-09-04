from stats import get_num_words
from stats import get_num_chars
from stats import sorted_dict
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    fp = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}")
    print("----------- Word Count ----------")
    ct = get_num_words(fp)
    print(f'Found {ct} total words')
    print("--------- Character Count -------")
    charcount = get_num_chars(fp)
    newdict = sorted_dict(charcount)
    for idict in newdict:
        print(f'{idict["char"]}: {idict["num"]}')

main()