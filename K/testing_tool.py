import argparse
import subprocess
import sys
import traceback
import string
import os

def write(p, line):
    assert p.poll() is None, 'Program terminated early'
    print('<{}'.format(line), flush=True)
    p.stdin.write('{}\n'.format(line))
    p.stdin.flush()


def read(p):
    assert p.poll() is None, 'Program terminated early'
    line = p.stdout.readline().strip()
    assert line != '', 'Read empty line or closed output pipe. Make sure that your program started successfully.'
    print('>%s' % line, flush=True)
    return line


parser = argparse.ArgumentParser(description='Testing tool for treasure hunt')
parser.add_argument(
    "-r", "--row",
    type=int,
    default=1,
    help="Number of rows (default: 1)"
)
parser.add_argument(
    "-c", "--col",
    type=int,
    default=2,
    help="Number of columns (default: 2)"
)
parser.add_argument('program', nargs='+', help='Your solution')

args = parser.parse_args()
guesses = 0

with subprocess.Popen(" ".join(args.program), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                          universal_newlines=True) as p:
    try:
        while True:
            guess = read(p).strip()
            kind, row, col = guess.split()
            row = int(row)
            col = int(col)

            if kind == '!':
                assert p.stdout.readline() == '', 'Printed extra data after making final guess'
                assert p.wait() == 0, 'Did not exit cleanly after finishing'
                if (row, col) == (args.row, args.col):
                    sys.stdout.write ("You guessed it!\n")
                    os._exit(0)
                else:
                    sys.stdout.write (f"You guessed wrong, the treasure is at {args.row} {args.col}.\n")
                    os._exit(1)
                break
            elif kind == '?':
                guesses += 1
                if 0 <= row - args.row <= 1 and 0 <= col - args.col <= 1:
                    write(p, '1')
                else:
                    write(p, '0')

            if guesses > 5:
                sys.stdout.write('Program used too many guesses\n')
                p.kill()
                break
    except:
        p.kill()
        p.wait()
        traceback.print_exc()
    finally:
        sys.stdout.flush()
        sys.stdout.write('Program guessed too often or gave wrong output\n')
        sys.stderr.flush()
        sys.stdout.flush()
        sys.exit(1)