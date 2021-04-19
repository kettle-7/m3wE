def p_statement_empty(p):
    "statement : "
    p[0] = []

def p_statement_expression(p):
    "statement : expression"
    p[0] = [("E", p[1])]

def p_statements(p):
    "statement : statement SEMI statement"
    p[0] = p[1] + p[3]

def p_statement_if(p):
    "statement : if"
    p[0] = [("I", p[1])]

def p_statement_while(p):
    "statement : while"
    p[0] = [("W", p[1])]

def p_statement_foreach(p):
    "statement : foreach"
    p[0] = [("f", p[1])]

def p_statement_for(p):
    "statement : for"
    p[0] = [("F", p[1])]

def p_statement_assignment(p):
    "statement : assignment"
    p[0] = [("A", p[1])]

def p_statement_fn(p):
    "statement : fn"
    p[0] = [("M", p[1])]
