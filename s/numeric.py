###############################
#        NUMERIC RULES        #
#   Rules for +, -, * and /   #
###############################

def p_sum_term(p):
    "sum : term"
    p[0] = (' ', p[1])

def p_sum_minus(p):
    "sum : sum HYPHEN sum"
    p[0] = ('-', p[1], p[3])

def p_sum_plus(p):
    "sum : sum PLUS sum"
    p[0] = ('+', p[1], p[3])

def p_term_factor(p):
    "term : factor"
    p[0] = (' ', p[1])

def p_term_times(p):
    "term : term STAR term"
    p[0] = ('*', p[1], p[3])

def p_term_divide(p):
    "term : term SLASH term"
    p[0] = ('/', p[1], p[3])

def p_factor_number(p):
    "factor : NUMBER"
    p[0] = ('I', p[1])

def p_factor_decimal(p):
    "factor : NUMBER DOT NUMBER"
    p[0] = ('F', float(str(p[1]) + "." + str(p[3])))

def p_factor_expression(p):
    "factor : LBRACKET expression RBRACKET"
    p[0] = ('E', p[2])

def p_factor_negative(p):
    "factor : HYPHEN NUMBER"
    p[0] = ('I', 0 - int(p[2]))

def p_factor_ndecimal(p):
    "factor : HYPHEN NUMBER DOT NUMBER"
    p[0] = ('F', 0 - float(str(p[2]) + "." + str(p[4])))

def p_factor_fn(p):
    "factor : ID list"
    p[0] = ('C', p[1], p[2])

def p_factor_id(p):
    "factor : ID"
    p[0] = ('V', p[1])

def p_factor_list(p):
    "factor : list"
    p[0] = ('L', p[1])

def p_factor_attr(p):
    "factor : expression DOT ID"
    p[0] = ('A', p[1], p[3])

def p_factor_exp(p):
    "factor : expression CARET NUMBER"
    p[0] = ('^', p[1], p[3])

def p_factor_true(p):
    "factor : TRUE"
    p[0] = ('B', True)

def p_factor_false(p):
    "factor : FALSE"
    p[0] = ('B', False)

def p_factor_string(p):
    "factor : STRING"
    p[0] = ('S', p[1][1:-1])

# This one might need to be commented out at some point
# - Yep, it's a naughty one.
#def p_elist(p):
#    "list : cpart"
#    p[0] = ('L', p[1])

def p_clist(p):
    "list : LBRACKET cpart RBRACKET"
    p[0] = ('L', p[2])

def p_list(p):
    "list : LSQ cpart RSQ"
    p[0] = ('L', p[2])

def p_cpart_empty(p):
    "cpart : "
    p[0] = []

def p_cpart_une(p):
    "cpart : expression"
    p[0] = [p[1]]

def p_cpart_mult(p):
    "cpart : cpart COMMA cpart"
    p[0] = p[1] + p[3]
