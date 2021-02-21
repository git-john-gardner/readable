import re
from argparse import ArgumentParser

_token_definitions = [
    ('comment', r'^#[^\n]*'),
    ('newline', r'\n'),
    ('indent', r'    '),
    ('maths', r'[\+\-\/\*<>]'),
    ('string-literal', r"^'[^']*'"),
    ('number-literal', r'\d+'),
    ('id', r'[\w~]+\??'),
    ('whitespace', r' +'),
    ('open-brace', r'{'),
    ('close-brace', r'}'),
    ('colon', r':'),
    ('other', r'\W')
]


def get_token_from(string):
    for token_type, pattern in _token_definitions:
        match = re.match(pattern, string)
        if match and match.span()[0] == 0 and match.span()[1] < len(string):
            return (token_type, string[:-1])


def tokenise(code):
    string, tokens = '', []
    for char in code+'\n':
        string += char
        token = get_token_from(string)
        if token:
            tokens.append(token)
            string = char
    return tokens


if __name__=='__main__':
    parser = ArgumentParser('Tokenising arguments')
    parser.add_argument('filepath')
    args = parser.parse_args()

    with open(args.filepath, 'r') as f:
        code = f.read()

    print("Tokenising:")
    for idx, line in enumerate(code.split('\n')):
        print(f"  {idx:>3}. {line}")

    print("Tokens:")
    for token in tokenise(code):
        print(f"   {token}")
