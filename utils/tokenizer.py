import numpy as np
import re

from collections import Counter, defaultdict

##############
# BASE CLASS #
##############

class Tokenizer():
    """
    Tokenization refers to how a piece of text is represented as a 
    sequence of vocabulary.
    """
    def __init__(
        self: object, 
        representation: str
    ) -> None:
        """
        Initializes the tokenizer object.

        Inputs
        ------
        . representation : indicates the tokenizer type (character, 
          word, subword)

        Output
        ------
        . None
        """
        if representation == "character":
            self.tokenizer = character_level_tokenization
        elif representation == "word":
            self.tokenizer = word_level_tokenization
        elif representation == "subword":
            self.tokenizer = subword_level_tokenization
        else:
            raise Exception(f"Tokenizer ({representation}) not found")
  
#############
# FUNCTIONS #
#############

def character_level_tokenization(
        sequences: np.array
    ) -> dict:
    """
    CLT represents a sequence of vocabulary elements AS singular
    tokenS. CLT's "element" corresponds to a character.

    Inputs
    ------
        . sequences : set of sequences from which to build a unique 
        vocabulary
        
    Output
    ------
        . hash table of each vocabulary element to their token
    """
    corpus = list(map(str,np.unique(np.char.lower(sequences)).tolist()))
    vocabulary = {k:v.lower() for k,v in enumerate(corpus)}
    return vocabulary

def word_level_tokenization(
        sequences: np.array
    ) -> dict:
    """
    CLT represents a sequence of vocabulary elements as singular
    tokens. CLT's "element" corresponds to a word.

    Inputs
    ------
     . sequences : set of sequences from which to build a unique 
       vocabulary
     
    Output
    ------
     . hash table of each vocabulary element to their token
    """
    corpus = np.unique(np.char.lower(sequences)).tolist()
    vocabulary = {k:v.lower() for k,v in enumerate(corpus)}
    return vocabulary

def subword_level_tokenization(
        sequences: np.array
    ) -> dict:
    """
    CLT represents a sequence of vocabulary elements as singular
    tokens. CLT's "element" corresponds to a word segment.

    Process
    -------
     0) Retrieves the corpus of words/vocabulary
     1) Represent each word in the corpus as a string of space-separated
        character + an EoW token </w>
     2) Counts the character pairs in all the computed tokens
     3) Merge all occurences of the most frequent pairs and creates a new
        n-gram to add to then end vocabulary
     4) Repeat step 3 a given number of "merge" steps
     
    Inputs
    ------
     . sequences : set of sequences from which to build a unique 
       vocabulary
     
    Output
    ------
     . hash table of each vocabulary element to their token
    """
    corpus = sequences.flatten().tolist()

    # Separates each character in each word in the corpus + adds a
    # end of word marker </w>
    tokens = [" ".join(word.lower()) + " </w>" for word in corpus]

    # Counts the tokens' frequency in the corpus
    vocabulary = dict(Counter(tokens))

    # Declares the number of merges to try
    max_nb_merges = 50

    # Retrieves the pairs of consecutive symbols and counts them
    for _ in range(max_nb_merges):
        # defaultdict do not return an error (0 instead) is key miss
        pairs = defaultdict(int)
        for word, freq in vocabulary.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pairs[symbols[i], symbols[i+1]] += freq
        
        # early exit if no pairs found
        if not pairs:
            break

        # Finds best pair
        best = max(pairs, key=pairs.get)
        
        # Merges all occurences of the most frequent pair
        temp = {}
        bigram = re.escape(" ".join(best))
        parser = re.compile(r"(?<!\S)" + bigram + r"(?!\S)")
        for word in vocabulary:
            out = parser.sub("".join(best), word)
            print(word, best, out)
            temp[out] = vocabulary[word]
        vocabulary = temp
    return vocabulary

#########
# TESTS #
#########

def tokenizer_test() -> None:
    """
    Tests the different tokenizing functions.
    """
    sentence = "On the highest mountain, the delipendious and quickest " + \
    "brown fox jumps over the deliciously lazy dog"
    sentence = np.array(sentence.split())
    print(word_level_tokenization(sentence))
    print(character_level_tokenization(sentence))
    print(subword_level_tokenization(sentence))