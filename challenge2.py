# using comprehensions process the following string and record :-
# the length
# the number of digits
# the number of punctuation characters
# the unique letters
# a count of the unique letters

# hint - review pythons built-in methods, specifically the string methods

import string
import pprint

test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

digits = [n for n in test_str if n in string.digits]
dlen = len(digits)
punc = [p for p in test_str if p in string.punctuation]
plen = len(punc)
uniq = {l for l in test_str if l in string.ascii_letters}
ulen = len(uniq)

d = {
    "length": len(test_str),
    "digits_count": dlen,
    "punc_count": plen,
    "uniq_count": ulen,
    "uniq_char": uniq
}

print(test_str)
pprint.pprint(d)