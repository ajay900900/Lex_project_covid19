
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN CLOSE_H3 CONTENT END OPEN_H3start : tableskiptag : CONTENT skiptag\n               | emptytable : BEGIN skiptag data skiptag ENDheader : OPEN_H3 CONTENT content CLOSE_H3data : data header content\n            | header contentempty :content : CONTENT content\n               | empty'
    
_lr_action_items = {'BEGIN':([0,],[3,]),'$end':([1,2,17,],[0,-1,-4,]),'CONTENT':([3,5,7,8,9,12,13,14,15,16,18,19,21,],[5,5,5,14,16,14,-7,14,-10,14,-6,-9,-5,]),'OPEN_H3':([3,4,5,6,7,8,10,12,13,14,15,18,19,21,],[-8,9,-8,-3,9,-8,-2,-8,-7,-8,-10,-6,-9,-5,]),'END':([5,6,7,8,10,11,12,13,14,15,18,19,21,],[-8,-3,-8,-8,-2,17,-8,-7,-8,-10,-6,-9,-5,]),'CLOSE_H3':([14,15,16,19,20,],[-8,-10,-8,-9,21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'table':([0,],[2,]),'skiptag':([3,5,7,],[4,10,11,]),'empty':([3,5,7,8,12,14,16,],[6,6,6,15,15,15,15,]),'data':([4,],[7,]),'header':([4,7,],[8,12,]),'content':([8,12,14,16,],[13,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> table','start',1,'p_start','2_1.py',59),
  ('skiptag -> CONTENT skiptag','skiptag',2,'p_skiptag','2_1.py',64),
  ('skiptag -> empty','skiptag',1,'p_skiptag','2_1.py',65),
  ('table -> BEGIN skiptag data skiptag END','table',5,'p_table','2_1.py',69),
  ('header -> OPEN_H3 CONTENT content CLOSE_H3','header',4,'p_header','2_1.py',74),
  ('data -> data header content','data',3,'p_data','2_1.py',79),
  ('data -> header content','data',2,'p_data','2_1.py',80),
  ('empty -> <empty>','empty',0,'p_empty','2_1.py',95),
  ('content -> CONTENT content','content',2,'p_content','2_1.py',100),
  ('content -> empty','content',1,'p_content','2_1.py',101),
]
