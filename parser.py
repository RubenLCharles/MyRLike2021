import ply.yacc as yacc
from lexer import tokens

# PRECEDENCIA DE OPERADORES
precedencia = {
    ('nonassoc', 'SEMIC'),
    ('right', 'ASSIGN'),
    ('left', 'NE_LOG'),
    ('nonassoc', 'LT_LOG','LTE_LOG','GTE_LOG','GTE_LOG'),
    ('left', 'PLUS_OP','MINUS_OP'),
    ('left', 'MULT_OP', 'DIV_OP'),
    ('left', 'LPAREN','RPAREN'),
    ('left', 'LBRACK', 'RBRACK'),
    ('left', 'LCURLY', 'RCURLY')
}

# INICIO
def p_program(p):
    'program : PROGRAM ID SEMIC dec_var_gob def_funciones main'

# VARIABLES Y TIPOS
def p_dec_var_gob(p):
    '''
    dec_var_gob : VARS tipos COLON lista_ids SEMIC dec_var_aux
                | empty
    '''

def p_dec_var_aux(p):
    '''
    dec_var_aux : tipos COLON lista_ids SEMIC dec_var_aux
                | empty
    '''

def p_lista_ids(p):
    '''
    lista_ids : id lista_aux lista_aux_b
    '''

def p_lista_aux(p):
    '''
    lista_aux : LBRACKET CTE_INT RBRACKET
              | empty
    ''' 

def p_lista_aux_b(p):
    '''
    lista_aux_b : COMMA lista_ids
                | empty
    '''

def p_tipos(p):
    '''
    tipos   : INT
            : FLOAT
            : CHAR
    '''

# DEFINICION DE FUNCIONES
def p_def_funciones(p):
    '''
    def_funciones : FUNCTION tipos_func ID LPAREN parametros RPAREN SEMIC dec_var_loc bloque
    '''

def p_dec_var_loc(p):
    '''
    dec_var_loc : VARS tipos COLON ID dec_var_loc_aux SEMIC 
                | empty
    '''

def p_dec_var_loc_aux(p):
    '''
    dec_var_loc_aux : COMMA ID dec_var_loc_aux
                    | empty
    '''

def p_tipos_func(p):
    '''
    tipos_func : INT
               | FLOAT
               | CHAR
               | VOID
    '''
