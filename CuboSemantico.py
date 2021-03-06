# LOS TIPOS DE DATO QUE SE USARAN SON INT, FLOAT, CHAR y el manejo de ARRAYS
# Utilizaré un diccionario como estructura para determinar el tipo de resultado que se espera entre 2 operandos
#
# Sintaxis:
#   (operando1, operando2, operador) : tipoEsperado

class CuboSemantico:
    def __init__(self):

        self.CuboSemantico = {

            #INT con INT
            ('int', 'int', '+') : 'int',
            ('int', 'int', '-') : 'int',
            ('int', 'int', '*') : 'int',
            ('int', 'int', '/') : 'int',
            ('int', 'int', '=') : 'int',
            ('int', 'int', '==') : 'bool',
            ('int', 'int', '>') : 'bool',
            ('int', 'int', '<') : 'bool',
            ('int', 'int', '<=') : 'bool',
            ('int', 'int', '>=') : 'bool',
            ('int', 'int', '!=') : 'bool',
            ('int', 'int', '||') : 'error',
            ('int', 'int', '&&') : 'error',

            #INT con FLOAT
            ('int', 'float', '+') : 'float',
            ('int', 'float', '-') : 'float',
            ('int', 'float', '*') : 'float',
            ('int', 'float', '/') : 'float',
            ('int', 'float', '=') : 'int',
            ('int', 'float', '==') : 'bool',
            ('int', 'float', '>') : 'bool',
            ('int', 'float', '<') : 'bool',
            ('int', 'float', '<=') : 'bool',
            ('int', 'float', '>=') : 'bool',
            ('int', 'float', '!=') : 'bool',
            ('int', 'float', '||') : 'error',
            ('int', 'float', '&&') : 'error',

            #INT CON CHAR
            ('int', 'char', '+') : 'error',
            ('int', 'char', '-') : 'error',
            ('int', 'char', '*') : 'error',
            ('int', 'char', '/') : 'error',
            ('int', 'char', '=') : 'error',
            ('int', 'char', '==') : 'error',
            ('int', 'char', '>') : 'error',
            ('int', 'char', '<') : 'error',
            ('int', 'char', '<=') : 'error',
            ('int', 'char', '>=') : 'error',
            ('int', 'char', '!=') : 'error',
            ('int', 'char', '||') : 'error',
            ('int', 'char', '&&') : 'error',

            #INT con ARRAY
            ('int', 'array', '+') : 'error',
            ('int', 'array', '-') : 'error',
            ('int', 'array', '*') : 'error',
            ('int', 'array', '/') : 'error',
            ('int', 'array', '=') : 'error',
            ('int', 'array', '==') : 'error',
            ('int', 'array', '>') : 'error',
            ('int', 'array', '<') : 'error',
            ('int', 'array', '<=') : 'error',
            ('int', 'array', '>=') : 'error',
            ('int', 'array', '!=') : 'error',
            ('int', 'array', '||') : 'error',
            ('int', 'array', '&&') : 'error',

            #FLOAT con INT
            ('float', 'int', '+') : 'float',
            ('float', 'int', '-') : 'float',
            ('float', 'int', '*') : 'float',
            ('float', 'int', '/') : 'float',
            ('float', 'int', '=') : 'float',
            ('float', 'int', '==') : 'bool',
            ('float', 'int', '>') : 'bool',
            ('float', 'int', '<') : 'bool',
            ('float', 'int', '<=') : 'bool',
            ('float', 'int', '>=') : 'bool',
            ('float', 'int', '!=') : 'bool',
            ('float', 'int', '||') : 'error',
            ('float', 'int', '&&') : 'error',

            #FLOAT con FLOAT
            ('float', 'float', '+') : 'float',
            ('float', 'float', '-') : 'float',
            ('float', 'float', '*') : 'float',
            ('float', 'float', '/') : 'float',
            ('float', 'float', '=') : 'float',
            ('float', 'float', '==') : 'bool',
            ('float', 'float', '>') : 'bool',
            ('float', 'float', '<') : 'bool',
            ('float', 'float', '<=') : 'bool',
            ('float', 'float', '>=') : 'bool',
            ('float', 'float', '!=') : 'bool',
            ('float', 'float', '||') : 'error',
            ('float', 'float', '&&') : 'error',

            #FLOAT con CHAR
            ('float', 'char', '+') : 'error',
            ('float', 'char', '-') : 'error',
            ('float', 'char', '*') : 'error',
            ('float', 'char', '/') : 'error',
            ('float', 'char', '=') : 'error', 
            ('float', 'char', '==') : 'error',
            ('float', 'char', '<') : 'error',
            ('float', 'char', '>') : 'error',
            ('float', 'char', '<=') : 'error',
            ('float', 'char', '>=') : 'error',
            ('float', 'char', '!=') : 'error',
            ('float', 'char', '|') : 'error',
            ('float', 'char', '&') : 'error',

            #FLOAT con ARRAY
            ('float', 'array', '+') : 'error',
            ('float', 'array', '-') : 'error',
            ('float', 'array', '*') : 'error',
            ('float', 'array', '/') : 'error',
            ('float', 'array', '=') : 'error', 
            ('float', 'array', '==') : 'error',
            ('float', 'array', '<') : 'error',
            ('float', 'array', '>') : 'error',
            ('float', 'array', '<=') : 'error',
            ('float', 'array', '>=') : 'error',
            ('float', 'array', '!=') : 'error',
            ('float', 'array', '|') : 'error',
            ('float', 'array', '&') : 'error',

            #CHAR con INT
            ('char', 'int', '+') : 'error',
            ('char', 'int', '-') : 'error',
            ('char', 'int', '*') : 'error',
            ('char', 'int', '/') : 'error',
            ('char', 'int', '=') : 'error', 
            ('char', 'int', '==') : 'error',
            ('char', 'int', '<') : 'error',
            ('char', 'int', '>') : 'error',
            ('char', 'int', '<=') : 'error',
            ('char', 'int', '>=') : 'error',
            ('char', 'int', '!=') : 'error',
            ('char', 'int', '|') : 'error',
            ('char', 'int', '&') : 'error',

            #CHAR con FLOAT
            ('char', 'float', '+') : 'error',
            ('char', 'float', '-') : 'error',
            ('char', 'float', '*') : 'error',
            ('char', 'float', '/') : 'error',
            ('char', 'float', '=') : 'error', 
            ('char', 'float', '==') : 'error',
            ('char', 'float', '<') : 'error',
            ('char', 'float', '>') : 'error',
            ('char', 'float', '<=') : 'error',
            ('char', 'float', '>=') : 'error',
            ('char', 'float', '!=') : 'error',
            ('char', 'float', '|') : 'error',
            ('char', 'float', '&') : 'error',

            #CHAR con CHAR
            ('char', 'char', '+') : 'error',
            ('char', 'char', '-') : 'error',
            ('char', 'char', '*') : 'error',
            ('char', 'char', '/') : 'error',
            ('char', 'char', '=') : 'char', 
            ('char', 'char', '==') : 'bool',
            ('char', 'char', '<') : 'error',
            ('char', 'char', '>') : 'error',
            ('char', 'char', '<=') : 'error',
            ('char', 'char', '>=') : 'error',
            ('char', 'char', '!=') : 'bool',
            ('char', 'char', '|') : 'error',
            ('char', 'char', '&') : 'error',

            #CHAR con ARRAY
            ('char', 'array', '+') : 'error',
            ('char', 'array', '-') : 'error',
            ('char', 'array', '*') : 'error',
            ('char', 'array', '/') : 'error',
            ('char', 'array', '=') : 'error', 
            ('char', 'array', '==') : 'error',
            ('char', 'array', '<') : 'error',
            ('char', 'array', '>') : 'error',
            ('char', 'array', '<=') : 'error',
            ('char', 'array', '>=') : 'error',
            ('char', 'array', '!=') : 'error',
            ('char', 'array', '|') : 'error',
            ('char', 'array', '&') : 'error',

            #ARRAY con INT
            ('array', 'int', '+') : 'error',
            ('array', 'int', '-') : 'error',
            ('array', 'int', '*') : 'error',
            ('array', 'int', '/') : 'error',
            ('array', 'int', '=') : 'error', 
            ('array', 'int', '==') : 'error',
            ('array', 'int', '<') : 'error',
            ('array', 'int', '>') : 'error',
            ('array', 'int', '<=') : 'error',
            ('array', 'int', '>=') : 'error',
            ('array', 'int', '!=') : 'error',
            ('array', 'int', '|') : 'error',
            ('array', 'int', '&') : 'error',

            #ARRAY con FLOAT
            ('array', 'float', '+') : 'error',
            ('array', 'float', '-') : 'error',
            ('array', 'float', '*') : 'error',
            ('array', 'float', '/') : 'error',
            ('array', 'float', '=') : 'error', 
            ('array', 'float', '==') : 'error',
            ('array', 'float', '<') : 'error',
            ('array', 'float', '>') : 'error',
            ('array', 'float', '<=') : 'error',
            ('array', 'float', '>=') : 'error',
            ('array', 'float', '!=') : 'error',
            ('array', 'float', '|') : 'error',
            ('array', 'float', '&') : 'error',

            #ARRAY con CHAR
            ('array', 'char', '+') : 'error',
            ('array', 'char', '-') : 'error',
            ('array', 'char', '*') : 'error',
            ('array', 'char', '/') : 'error',
            ('array', 'char', '=') : 'error', 
            ('array', 'char', '==') : 'error',
            ('array', 'char', '<') : 'error',
            ('array', 'char', '>') : 'error',
            ('array', 'char', '<=') : 'error',
            ('array', 'char', '>=') : 'error',
            ('array', 'char', '!=') : 'error',
            ('array', 'char', '|') : 'error',
            ('array', 'char', '&') : 'error',

            #ARRAY con STRING
            ('array', 'string', '+') : 'error',
            ('array', 'string', '-') : 'error',
            ('array', 'string', '*') : 'error',
            ('array', 'string', '/') : 'error',
            ('array', 'string', '=') : 'error', 
            ('array', 'string', '==') : 'error',
            ('array', 'string', '<') : 'error',
            ('array', 'string', '>') : 'error',
            ('array', 'string', '<=') : 'error',
            ('array', 'string', '>=') : 'error',
            ('array', 'string', '!=') : 'error',
            ('array', 'string', '|') : 'error',
            ('array', 'string', '&') : 'error',

            #ARRAY con ARRAY
            ('array', 'array', '+') : 'error',
            ('array', 'array', '-') : 'error',
            ('array', 'array', '*') : 'error',
            ('array', 'array', '/') : 'error',
            ('array', 'array', '=') : 'array', 
            ('array', 'array', '==') : 'error',
            ('array', 'array', '<') : 'error',
            ('array', 'array', '>') : 'error',
            ('array', 'array', '<=') : 'error',
            ('array', 'array', '>=') : 'error',
            ('array', 'array', '!=') : 'error',
            ('array', 'array', '|') : 'error',
            ('array', 'array', '&') : 'error',

            #READS
            ('read', 'int', '') : 'int',
            ('read', 'float', '') : 'float',
            ('read', 'char', '') : 'error',
            ('read', 'string', '') : 'error',
            ('read', 'array', '') : 'char',

            #WRITES
            ('write', 'int', '') : 'string',
            ('write', 'float', '') : 'string',
            ('write', 'char', '') : 'string',
            ('write', 'string', '') : 'string',
            ('write', 'array', '') : 'error',

            #RETORNOS
            ('retorna', 'int', '') : 'int',
            ('retorna', 'float', '') : 'float',
            ('retorna', 'char', '') : 'char',
            ('retorna', 'string', '') : 'string',
            ('retorna', 'array', '') : 'array'
        }

# Funcion que busca en el diccionario el tipo de resultado esperado
def getType(self, op1, op2, operador):
    return self.CuboSemantico[op1, op2, operador]