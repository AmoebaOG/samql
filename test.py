#!/usr/bin/env python
import subprocess
import sys

def main():
    run_case('all-columns')
    run_case('all-spelled-out-columns')
    run_case('single-column')
    run_case('few-columns')
    run_case('duplicate-columns')
    run_case('reordered-columns')
    run_case('single-filter')
    run_case('greater_than-filter')
    run_case('less_than-filter')
    run_case('equals-filter')
    run_case('contains-filter')
    run_case('all-filters')
    run_case('a-few-columns-and-a-filter')
    run_case('no-results')

    print('All tests passed!')

def run_case(name):
    expected_exitcode = int(read_file(f'cases/{name}/exitcode'))
    expected_stdout = read_file(f'cases/{name}/stdout')
    expected_stderr = read_file(f'cases/{name}/stderr')

    query = read_file(f'cases/{name}/query')
    actual = run_query(query)

    if expected_exitcode != actual.returncode:
        print(f'Test case {name} failed!', file=sys.stderr)
        print(f'Expected exitcode\n----\n{expected_exitcode}\n----\n\nActual exitcode\n----\n{actual.returncode}\n----', file=sys.stderr)
        exit(1)

    if expected_stdout != actual.stdout:
        print(f'Test case {name} failed!', file=sys.stderr)
        print(f'Expected stdout\n----\n{expected_stdout}\n----\n\nActual stdout\n----\n{actual.stdout}\n----', file=sys.stderr)
        exit(1)

    if expected_stderr != actual.stderr:
        print(f'Test case {name} failed!', file=sys.stderr)
        print(f'Expected stderr\n----\n{expected_stderr}\n----\n\nActual stderr\n----\n{actual.stderr}\n----', file=sys.stderr)
        exit(1)

def run_query(query):
    return subprocess.run(['python', 'samql.py', query], capture_output=True, encoding='utf-8')

def read_file(path):
    with open(path) as file:
        return file.read()

if __name__ == '__main__':
    main()
