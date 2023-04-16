class Transformer_SequenceModelling():
    """
    Class module for a squencer modelling transformer,
    also called DTransformer.
    Given a vocabulary V, let x_n \in V^* for n \in [N_data]
    be a dataset of sequences (imagined to be i.i.d.) from
    some distribution P over V^*. The goal is to learn an
    estimate \hat{P} of the distribution P(x).
    """
    def __init__(self):
        pass

class Transformer_Sequence2Sequence():
    """
    Class module for a squencer to sequence (seq2seq) transformer,
    also called EDTransfomer.
    Given a vocabulary V and an i.i.d. dataset of sequence pairs 
    (z_n, x_n) \sim P, where P is a distribution over V^* x V^*,
    learn an estimate of the conditional distribution P(x|z).
    """
    def __init__(self):
        pass

class Transformer_Classification():
    """
    Class module for a squencer to sequence (seq2seq) transformer,
    also called ETransfomer.
    Given a vocabulary V and a set of classes [N_c], let (x_n, c_n)
    \in V^* x [N_c] for n \in [N_data] be an i.i.d. dataset of 
    sequence-class pairs sampled from P(x, c). The goal is to learn 
    an estimate of the conditional distribution P(c|x)
    """
    def __init__(self):
        pass