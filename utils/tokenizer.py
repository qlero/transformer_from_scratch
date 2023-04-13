import torch

def character_level_tokenization(
        sequences: torch.Tensor
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
    pass

def word_level_tokenization(
        sequences: torch.Tensor
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
    pass

def subword_level_tokenization(
        sequences: torch.Tensor
    ) -> dict:
    """
    CLT represents a sequence of vocabulary elements as singular
    tokens. CLT's "element" corresponds to a word segment.

    Inputs
    ------
     . sequences : set of sequences from which to build a unique 
       vocabulary
     
    Output
    ------
     . hash table of each vocabulary element to their token
    """
    pass
