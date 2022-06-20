## wraps local cpplint to produce verbose output without code harness
import cpplint
import sys

def main():
    FILTERS=('cpplint --verbose=0 --linelength=100 --filter=-legal/copyright,-build/include_order,'
    '-build/c++11,-build/namespaces,-build/class,-build/include,-build/include_subdir,-readability/inheritance,'
    '-readability/function,-readability/casting,-readability/namespace,-readability/alt_tokens,'
    '-readability/braces,-readability/fn_size,-whitespace/comments,-whitespace/braces,-whitespace/empty_loop_body,'
    '-whitespace/indent,-whitespace/newline,-runtime/explicit,-runtime/arrays,-runtime/int,-runtime/references,'
    '-runtime/string,-runtime/operator,-runtime/printf').split(' ')

    result = False
    files = sys.argv[1:]
    for loopfile in files:
        newargs = FILTERS + [loopfile]
        sys.argv = newargs

        try:
            cpplint.main()
        except SystemExit as e:
            last_result = e.args[0]
            result = result or last_result
            if (last_result):
                write_code_lines(loopfile)
    sys.exit(result)

def write_code_lines(filename):
    with open(filename, 'r') as f:
        for linenum, line in enumerate(f, start=1):
            if '// by md-split' not in line:
                sys.stdout.write('%3d  %s' % (linenum, line))

if __name__ == '__main__':
  main()
