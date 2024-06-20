from duetable.src.abc_utils import generate_sequence_from_abc

abc_seq = """
X: 1
T: ABC Music
M: 4/4
L: 1/8
|:CDEF  GABc | cdef gabc':|
"""

print(generate_sequence_from_abc(abc_seq))
