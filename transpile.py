from argparse import ArgumentParser
import re

def homogenise_functions(code):
    special_functions = re.findall(r'(?:\w+{.*}){2,}', code)
    for s in special_functions:
        args = ', '.join(re.findall(r'{(.?)}', s))

        function_name = re.sub(r'({.?})', '_', s)
        code = code.replace(s, f'{function_name}({args})')

    return code


def transpile(code):
    code = homogenise_functions(code)
    code = code.replace('{', '(').replace('}', ')')
    return code


if __name__=='__main__':
    parser = ArgumentParser('Tokenising arguments')
    parser.add_argument('filepath')
    args = parser.parse_args()

    with open(args.filepath, 'r') as f:
        code = f.read()

    print("Transpiling...")
    transpiled_code = transpile(code)
    for idx, line in enumerate(transpiled_code.split('\n')):
        print(f'  {idx+1}.  {line}')

    with open(args.filepath.replace('.rdbl', '.py'), 'w') as f:
        f.write(transpiled_code)
