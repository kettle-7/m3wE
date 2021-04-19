def p_while(p):
    "while : WHILE expression LBRACE statement RBRACE"
    p[0] = (p[2], p[4])

def p_for(p):
    "for : FOR LBRACKET statement COMMA expression COMMA statement \
RBRACKET LBRACE statement RBRACE"
    p[0] = (p[3], p[5], p[7], p[10])

def p_foreach(p):
    "foreach : FOR ID IN expression LBRACE statement RBRACE"
    p[0] = (p[2], p[4], p[6])

# Ifs go here too :~)
def p_if(p):
    "if : IF expression LBRACE statement RBRACE"
    p[0] = (p[2], p[4], [])

def p_ifelse(p):
    "if : IF expression LBRACE statement RBRACE ELSE LBRACE statement RBRACE"
    p[0] = (p[2], p[4], [(('B', True), p[8])]) # Else at runtime is the same as
                                               # saying elif true.
def p_ifelif(p):
    "if : IF expression LBRACE statement RBRACE ELSE if"
    p[0] = (p[2], p[4], [(p[7][0], p[7][1])] + p[7][2])

def p_fn(p):
    "fn : FN ID list LBRACE statement RBRACE"
    p[0] = (p[2], p[3], p[5])

# No idea where to put this, so it's going here
def p_assignment(p):
    "assignment : ID EQUALS expression"
    p[0] = (p[1], p[3])
