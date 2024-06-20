import re
import music21 as m21



SEPARATORS = ['|', '|]', '||', '[|', '|:', ':|', '::']
SEP_DICT = {}
for i, sep in enumerate(SEPARATORS, start=1):
    # E.g. ' | ': ' <1>'
    SEP_DICT[' ' + sep + ' '] = f' <{i}>'
NEWSEP = '<|>'


def sep2tok(row):
    for sep, tok in SEP_DICT.items():
        row = row.replace(sep, tok + '<=> ')
    return row


def tok2sep(bar):
    for sep, tok in SEP_DICT.items():
        bar = bar.replace(tok, sep)
    return bar


def spacing(row):
    for sep in SEPARATORS:

        def subfunc(match):
            symbol = [':', '|', ']']
            if match.group(1) is None:
                return f' {sep}'
            elif match.group(1) in symbol:
                return f' {sep}{match.group(1)}'
            else:
                return ' ' + sep + ' ' + match.group(1)

        pattern = r' ' + re.escape(sep) + r'(.{1})'
        row = re.sub(pattern, subfunc, row)
        row = row.replace('\n' + sep + '"', '\n ' + sep + ' "')  # B \n|"A -> B \n | "A
        row = row.replace(' ' + sep + '\n', ' ' + sep + ' \n')  # B |\n -> B | \n
    return row


def decode(piece, n_bars=2):
    dec_piece = ''
    idx = piece.find(' ' + NEWSEP + ' ')
    heads = piece[:idx]
    scores = piece[idx:]
    scores_lst = re.split(' <\|>', scores)

    all_bar_lst = []
    for bar in scores_lst:
        if bar == '':
            continue
        bar = sep2tok(bar)
        bar_lst = re.split('<=>', bar)
        bar_lst = list(map(tok2sep, bar_lst))
        if len(all_bar_lst) == 0:
            all_bar_lst = [[] for _ in range(len(bar_lst))]
        for i in range(len(bar_lst)):
            all_bar_lst[i].append(bar_lst[i])

    if len(all_bar_lst) > 1:
        # There might be the bar number like %30 at the end
        # which need to be specially handled.
        if len(all_bar_lst[0]) > len(all_bar_lst[1]):
            last_bar_lst = all_bar_lst[0][-1].split()
            all_bar_lst[0].pop()
            for i in range(len(all_bar_lst)):
                all_bar_lst[i].append(last_bar_lst[i])
                # Add the remaining symbols to the last row.
                if i == len(all_bar_lst) - 1:
                    for j in range(i + 1, len(last_bar_lst)):
                        all_bar_lst[i][-1] += ' ' + last_bar_lst[j]
        # Ensure the lengths are consistent.
        length = len(all_bar_lst[0])
        for lst in all_bar_lst[1:]:
            # assert len(lst) == length
            pass

    key_split = heads.split("|")
    assert len(key_split) > 0
    dec_piece += key_split[0]


    print(all_bar_lst)
    for i in range(len(all_bar_lst)):
        # if len(all_bar_lst) > 1:
        #     dec_piece += f'V:{i + 1}\n'
        dec_piece += ''.join(all_bar_lst[i][:n_bars])
        dec_piece += '\n'
    # Remove redundant spaces.
    dec_piece = re.sub(' {2,}', ' ', dec_piece)

    return dec_piece

def validate_abc(abc_string):
    abc_parser = m21.converter.parse(abc_string, format='abc')
    # Extract the first part and the first measure for validation
    # part = abc_parser.parts[0]
    # measure = part.measure(1)
    # time_signature = measure.getTimeSignatures()[0]
    # return validate_measure(measure, time_signature) # TODO: measure validation
    return True


# Function to validate a measure
def validate_measure(measure, time_signature):
    total_duration = sum(element.duration.quarterLength for element in measure.notesAndRests)
    expected_duration = time_signature.beatCount * (4 / time_signature.denominator)

    if total_duration == expected_duration:
        return True
    else:
        return False
