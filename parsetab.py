
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLASE COMA DIGITO ID LLAVEAPERTURA LLAVECIERRE MODIFICADORACCESO NOMBRECLASE PARENTECISAPERTURA PARENTESISCIERRE PUBLIC PUNTOCOMA TIPODATOS : PUBLIC CLASE NCLASE LLAVEA CUERPOCLASE LLAVECNCLASE : NOMBRECLASECUERPOCLASE : VARIABLE PCOMA\n    | LISTACUERPO RESTOMETODO PARENTESISC LLAVEA LLAVECLISTACUERPO : MODIFICARACCESO TIPODATO ID PARENTESISARESTOMETODO : TIPODATO ID LISTAPARAMETRO\n    | emptyVARIABLE : TIPODATO IDPARAMETRO : TIPODATO IDLISTAPARAMETRO : COMA PARAMETRO LISTAPARAMETRO\n    | emptyMODIFICARACCESO : MODIFICADORACCESOLLAVEA : LLAVEAPERTURALLAVEC : LLAVECIERREPARENTESISA : PARENTECISAPERTURAPARENTESISC : PARENTESISCIERREPCOMA : PUNTOCOMAempty :'
    
_lr_action_items = {'PUBLIC':([0,],[2,]),'$end':([1,14,15,],[0,-1,-14,]),'CLASE':([2,],[3,]),'NOMBRECLASE':([3,],[5,]),'LLAVEAPERTURA':([4,5,23,24,],[7,-2,7,-16,]),'TIPODATO':([6,7,10,12,13,29,31,32,],[11,-13,19,22,-12,35,-5,-15,]),'MODIFICADORACCESO':([6,7,],[13,-13,]),'LLAVECIERRE':([7,8,15,16,17,27,33,],[-13,15,-14,-3,-17,15,-4,]),'PUNTOCOMA':([9,21,],[17,-8,]),'PARENTESISCIERRE':([10,18,20,25,28,30,31,32,34,36,37,],[-18,24,-7,-18,-6,-11,-5,-15,-18,-10,-9,]),'ID':([11,19,22,35,],[21,25,26,37,]),'COMA':([25,34,37,],[29,29,-9,]),'PARENTECISAPERTURA':([26,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'NCLASE':([3,],[4,]),'LLAVEA':([4,23,],[6,27,]),'CUERPOCLASE':([6,],[8,]),'VARIABLE':([6,],[9,]),'LISTACUERPO':([6,],[10,]),'MODIFICARACCESO':([6,],[12,]),'LLAVEC':([8,27,],[14,33,]),'PCOMA':([9,],[16,]),'RESTOMETODO':([10,],[18,]),'empty':([10,25,34,],[20,30,30,]),'PARENTESISC':([18,],[23,]),'LISTAPARAMETRO':([25,34,],[28,36,]),'PARENTESISA':([26,],[31,]),'PARAMETRO':([29,],[34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> PUBLIC CLASE NCLASE LLAVEA CUERPOCLASE LLAVEC','S',6,'p_S','analizadorSintactico.py',15),
  ('NCLASE -> NOMBRECLASE','NCLASE',1,'p_NCLASE','analizadorSintactico.py',20),
  ('CUERPOCLASE -> VARIABLE PCOMA','CUERPOCLASE',2,'p_CUERPOCLASE','analizadorSintactico.py',25),
  ('CUERPOCLASE -> LISTACUERPO RESTOMETODO PARENTESISC LLAVEA LLAVEC','CUERPOCLASE',5,'p_CUERPOCLASE','analizadorSintactico.py',26),
  ('LISTACUERPO -> MODIFICARACCESO TIPODATO ID PARENTESISA','LISTACUERPO',4,'p_LISTACUERPO','analizadorSintactico.py',35),
  ('RESTOMETODO -> TIPODATO ID LISTAPARAMETRO','RESTOMETODO',3,'p_RESTOMETODO','analizadorSintactico.py',40),
  ('RESTOMETODO -> empty','RESTOMETODO',1,'p_RESTOMETODO','analizadorSintactico.py',41),
  ('VARIABLE -> TIPODATO ID','VARIABLE',2,'p_VARIABLE','analizadorSintactico.py',46),
  ('PARAMETRO -> TIPODATO ID','PARAMETRO',2,'p_PARAMETRO','analizadorSintactico.py',50),
  ('LISTAPARAMETRO -> COMA PARAMETRO LISTAPARAMETRO','LISTAPARAMETRO',3,'p_LISTAPARAMETRO','analizadorSintactico.py',55),
  ('LISTAPARAMETRO -> empty','LISTAPARAMETRO',1,'p_LISTAPARAMETRO','analizadorSintactico.py',56),
  ('MODIFICARACCESO -> MODIFICADORACCESO','MODIFICARACCESO',1,'p_MODIFICARACCESO','analizadorSintactico.py',61),
  ('LLAVEA -> LLAVEAPERTURA','LLAVEA',1,'p_LLAVEA','analizadorSintactico.py',66),
  ('LLAVEC -> LLAVECIERRE','LLAVEC',1,'p_LLAVEC','analizadorSintactico.py',71),
  ('PARENTESISA -> PARENTECISAPERTURA','PARENTESISA',1,'p_PARENTESISA','analizadorSintactico.py',78),
  ('PARENTESISC -> PARENTESISCIERRE','PARENTESISC',1,'p_PARENTESISC','analizadorSintactico.py',82),
  ('PCOMA -> PUNTOCOMA','PCOMA',1,'p_PCOMA','analizadorSintactico.py',87),
  ('empty -> <empty>','empty',0,'p_empty','analizadorSintactico.py',92),
]
