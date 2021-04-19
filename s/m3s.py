#!/bin/python3

from os.path import dirname

import sys
import os

# Use Python Lex-YACC included in the parent folder
sys.path.append(dirname(dirname(__file__ )))
import ply.yacc as yacc
import ply.lex as lex

# We can't use argv directly, that interferes with some modules.
args = [*sys.argv]

del args[0]
files = []
for arg in args:
    files.append(arg)

if not len(files):
    print("Error: no source files specified.")
    sys.exit(5)

###################
#   LEX SECTION   #
###################

tokens = (
    'NUMBER',
    'STRING',
    'SEMI',
    #'PREPROCESSOR',
    'ID',
    'LSQ',
    'RSQ',
    'DOT',
    'HYPHEN',
    'INC', 'INC1',
    'DEC', 'DEC1',
    'PLUS',
    'STAR',
    'SLASH',
    'LBRACKET',
    'RBRACKET',
    'FN', 'LBRACE',
    'RBRACE', 'IF',
    'ELSE',
    'WHILE',
    'NEQ', 'NOT',
    'EQ', 'AND', 'OR',
    'GTE', 'LTE',
    'GT', 'LT',
    'BAND', 'BOR',
    'FOR', 'IN',
    'EQUALS',
    'COMMENT', 'LINECOMMENT',
    'COMMA',
    'CARET',
    'TRUE', 'FALSE'
)

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'fn': 'FN',
    'for': 'FOR',
    'true': 'TRUE',
    'false': 'FALSE'
}

t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_SEMI = r';'
t_LSQ = r'\['
t_RSQ = r'\]'
t_DOT = r'[.]'
t_HYPHEN = r'-'
t_INC = r'[+][=]'
t_INC1 = r'[+][+]'
t_DEC = r'[-][=]'
t_DEC1 = r'[-][-]'
t_PLUS = r'[+]'
t_STAR = r'[*]'
t_SLASH = '/'
t_LBRACKET = r'[(]'
t_RBRACKET = r'[)]'
t_LBRACE = r'[{]'
t_RBRACE = r'[}]'
t_NEQ = r'[!][=]'
t_NOT = '!'
t_EQ = r'\=\='
t_AND = r'&&'; t_OR = r'[|][|]'
t_GTE = r'[>][=]'; t_LTE = r'[<][=]'
t_GT = r'[>]'; t_LT = r'[<]'
t_BAND = r'&'; t_BOR = r'[|]'
t_EQUALS = r'[=]'
t_COMMA = ','
t_CARET = '\^'
t_ignore_LINECOMMENT = r'//.*\n'
# Preprocessor is commented out for now.
#t_PREPROCESSOR = r'#.*\n'

def t_COMMENT(t):
    r'/\*.*\*/'
    pass
    # No return value. Token discarded

#def t_LINECOMMENT(t):
#    r'//.*\n'
#    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Syntax Error: Unexpected character '%s' on line %s" % (t.value[0], t.lineno))
    sys.exit(2)

lexer = lex.lex()

######################
#                    #
#    YACC SECTION    #
#                    #
######################

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax Error: Invalid syntax on line %s - unexpected %s" % (p.lineno, p.value))
    else:
        print("Syntax Error: Unexpected End of File")
    sys.exit(2)

# Import the syntax declarations
from loops import *
from numeric import *
from statements import *
from expressions import *

# Build the parser
parser = yacc.yacc(start="statement")

for file in files:
    try:
        with open(file) as f:
            s = f.read()
    except FileNotFoundError:
        print("Error: Source file %s not found." % file)
        sys.exit(5)
    try:
        result = parser.parse(s)
    except KeyboardInterrupt:
        print()
        continue
    print(result)
