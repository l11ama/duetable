from duetable.abc_utils import generate_sequence_from_abc
from duetable.transformations import FixedRangeTransformer, ApproachNotesTransformer


def test_range_transform():
    abc_seq = """
    X: 1
    T: ABC Music
    M: 4/4
    L: 1/8
    |:CDcF  GABc | c_dd gabc':|
    """
    transform = FixedRangeTransformer(2, 4)
    seq = generate_sequence_from_abc(abc_seq)
    print(seq)
    res = transform.transform(seq)
    print(res)

def test_approach_transform():
    abc_seq = """
    X: 1
    T: ABC Music
    M: 4/4
    L: 1/8
    |:CDcF  GABc | c_dd gabc':|
    """
    transform = ApproachNotesTransformer()
    seq = generate_sequence_from_abc(abc_seq)
    print(seq)
    res = transform.transform(seq)
    print(res)
