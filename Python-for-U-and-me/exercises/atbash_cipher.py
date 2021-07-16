# MIT Licensed
# https://github.com/exercism/python/blob/master/LICENSE
from string import ascii_lowercase as letters


atbash = dict(zip(letters, reversed(letters)))


def decode(sentence):
    """Return string of each character decoded.""" 
    return ''.join(atbash.get(s.lower(), '') for s in sentence)

def encode(sentence):
    """Decode each letter and group into 5-letter words."""
    clean = (char.lower() for char in sentence if char.isalpha() or char in '1234567890')
    deco = [atbash.get(s, s) for s in clean]
    sent = (deco[i:i + 5] for i in range(0, len(deco), 5) )
    return ' '.join(''.join(k) for k in sent)