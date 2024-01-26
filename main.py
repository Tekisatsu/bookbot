import re
def main():
      book = r'/home/iro/workspace/github.com/tekisatsu/bookbot/books/frankenstein.txt'

      def get_text(book):
            with open(book) as f:
                  return f.read()
      def get_letter_count(text):
            cleaned = re.sub(r"[^a-zA-Z]", "", text).lower()
            letters_dict = {}
            for letter in cleaned:
                  if letter not in letters_dict:
                        letters_dict[letter] = cleaned.count(letter)
            return letters_dict
      def get_report(counted_letters,text):
            amount_of_words = len(text.split())
            print(f'Report of the amount of words and letters')
            print(f'Total amount of words: {amount_of_words}')
            for i in sorted(counted_letters):
                  
                  print(f'Number of letter {i} is {counted_letters[i]}')
      text = get_text(book)
      counted_letters = get_letter_count(text)  
      get_report(counted_letters,text)


main()