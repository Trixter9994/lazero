""" Strip comments and docstrings from a file.
"""

import sys, token, tokenize, re

def do_file(fname):
    """ Run on just one file.

    """
    mod0=""
    source = open(fname)
    mod = open(fname[:-3] + "_strip.py", "w")

    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 0:   # Change to if 1 to see the tokens fly by.
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
                ))
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            mod0+=" " * (scol - last_col)
        if toktype == token.STRING and prev_toktype == token.INDENT:
            # Docstring
            mod0+=""
        elif toktype == tokenize.COMMENT:
            # Comment
            mod0+=""
        else:
            mod0+=ttext
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
    mod0=re.sub(r'[ \t]*\n',"\n",mod0,re.MULTILINE)
    while "\n\n" in mod0:
        mod0=mod0.replace("\n\n","\n")
    mod.write(mod0 if mod0[0]!= "\n" else mod0[1:])

if __name__ == '__main__':
    do_file(sys.argv[1])
