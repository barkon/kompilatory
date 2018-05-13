import sys
import ply.yacc as yacc
import MParser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    MParser = MParser.MParser()
    parser = yacc.yacc(module=MParser)
    text = file.read()
    ast = parser.parse(text, lexer=MParser.scanner)

