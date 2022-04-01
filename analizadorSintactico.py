import ply.yacc as yacc
from analizadorLexico import tokens

lista = []
errorSintactico = False




def p_S(p):
    # '''S : PUBLIC CLASS NCLASE LLAVEA CUERPOCLASE LLAVEC'''
    '''S : PUBLIC CLASE NCLASE LLAVEA CUERPOCLASE LLAVEC'''


def p_NCLASE(p):
    '''NCLASE : NOMBRECLASE'''


def p_CUERPOCLASE(p):
    # CUERPOCLASE → VARIABLE PCOMA | LISTACUERPO RESTOMETODO PARENTESISC  LLAVEA  LLAVEC
    '''CUERPOCLASE : VARIABLE PCOMA
    | LISTACUERPO RESTOMETODO PARENTESISC LLAVEA LLAVEC'''


def p_LISTACUERPO(p):
    #LISTACUERPO → MODIFICARACCESO  TIPODATO  ID  PARENTESISA
    '''LISTACUERPO : MODIFICARACCESO TIPODATO ID PARENTESISA'''


def p_RESTOMETODO(p):
    #RESTOMETODO → TIPODATO  ID  LISTAPARAMETRO | ε
    '''RESTOMETODO : TIPODATO ID LISTAPARAMETRO
    | empty'''


def p_VARIABLE(p):
    # VARIABLE →  TIPODATO  ID  RESTOVARIABLE
    '''VARIABLE : TIPODATO ID'''

def p_PARAMETRO(p):
    #PARAMETRO → TIPODATO ID | ε
    '''PARAMETRO : TIPODATO ID'''


def p_LISTAPARAMETRO(p):
    #LISTAPARAMETRO → COMA  PARAMETRO  LISTAPARAMETRO  | ε
    '''LISTAPARAMETRO : COMA PARAMETRO LISTAPARAMETRO
    | empty'''


def p_MODIFICARACCESO(p):
    '''MODIFICARACCESO : MODIFICADORACCESO'''



def p_LLAVEA(p):
    #{
    '''LLAVEA : LLAVEAPERTURA'''


def p_LLAVEC(p):
    #}
    '''LLAVEC : LLAVECIERRE'''




def p_PARENTESISA(p):
    #(
    '''PARENTESISA : PARENTECISAPERTURA'''

def p_PARENTESISC(p):
    #)
    '''PARENTESISC : PARENTESISCIERRE'''


def p_PCOMA(p):
    # ;
    '''PCOMA : PUNTOCOMA'''


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    global errorSintactico
    if p:
        estado = str(p.type), str(p.lineno), str(p.lexpos), str(p.value)
        print("Error De Sintaxis -> ", p.type, " Linea -> ", p.lineno, " Posicion -> ", p.lexpos, " Simbolo/s -> ",p.value)
        parser.errok()
        lista.append(estado)
        errorSintactico = True
    else:
        errorSintactico = True
        print("Error De Sintaxis")

parser = yacc.yacc()

def ejecucionAlgoritmo(texto):
    lista.clear()
    parser.parse(texto)

    return lista