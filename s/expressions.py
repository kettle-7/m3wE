############
#   NOTE   #
############

# Throughout this file, boolean operators gain precedence over those that work
# on any data type. For example, NOT gains precendence over GREATER THAN.


def p_expression_sum(p):
    "expression : sum"
    p[0] = (' ', p[1])

def p_expression_not(p):
    "expression : NOT expression" # NOT expression instead of NOT sum means that
    p[0] = ('!', p[2])            # !a==b means a!=b rather than !(a==b).

def p_expression_eq(p):
    "expression : sum EQ sum"
    p[0] = ('==', p[1], p[3])

def p_expression_neq(p):
    "expression : sum NEQ sum"
    p[0] = ('!=', p[1], p[3])

def p_expression_gt(p):
    "expression : sum GT sum"
    p[0] = ('>', p[1],p[3])

def p_expression_lt(p):
    "expression : sum LT sum"
    p[0] = ('<', p[1], p[3])

def p_expression_gte(p):
    "expression : sum GTE sum"
    p[0] = ('>=', p[1], p[3])

def p_expression_lte(p):
    "expression : sum LTE sum"
    p[0] = ('<=', p[1], p[3])

def p_expression_and(p):
    "expression : expression AND expression" # a==b&&c means (a==b)&&c and not
    p[0] = ('&&', p[1], p[3])                # a==(b&&c).

def p_expression_or(p):
    "expression : expression OR expression" # Same applies here
    p[0] = ('||', p[1], p[3])

def p_expression_bor(p):       # However, bitwise operators do not gain
    "expression : sum BOR sum" # precedence, as I see no reason to use them with
    p[0] = ('|', p[1], p[3])   # boolean values.

def p_expression_band(p):
    "expression : sum BAND sum"
    p[0] = ('&', p[1], p[3])
