
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN CLOSE_H2 CLOSE_H3 CLOSE_LI CLOSE_P CLOSE_UL CONTENT END OPEN_H2 OPEN_H3 OPEN_LI OPEN_P OPEN_ULstart : tableskiptag : CONTENT skiptag\n               | emptytable : BEGIN skiptag CLOSE_H2 content datadata : skiptag OPEN_H2 CONTENT content CLOSE_H2 content data            \n            | END\n            | skiptagcontent : CONTENT content\n               | emptyempty :'
    
_lr_action_items = {'BEGIN':([0,],[3,]),'$end':([1,2,5,6,7,8,9,10,11,12,13,14,15,19,20,21,],[0,-1,-10,-3,-10,-2,-10,-10,-9,-7,-4,-6,-8,-10,-10,-5,]),'CONTENT':([3,5,7,9,10,11,15,16,17,19,20,],[5,5,10,5,10,-9,-8,17,10,10,5,]),'CLOSE_H2':([3,4,5,6,8,10,11,15,17,18,],[-10,7,-10,-3,-2,-10,-9,-8,-10,19,]),'OPEN_H2':([5,6,7,8,9,10,11,12,15,19,20,],[-10,-3,-10,-2,-10,-10,-9,16,-8,-10,-10,]),'END':([7,9,10,11,15,19,20,],[-10,14,-10,-9,-8,-10,14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'table':([0,],[2,]),'skiptag':([3,5,9,20,],[4,8,12,12,]),'empty':([3,5,7,9,10,17,19,20,],[6,6,11,6,11,11,11,6,]),'content':([7,10,17,19,],[9,15,18,20,]),'data':([9,20,],[13,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> table','start',1,'p_start','M2_4_Australia.py',61),
  ('skiptag -> CONTENT skiptag','skiptag',2,'p_skiptag','M2_4_Australia.py',68),
  ('skiptag -> empty','skiptag',1,'p_skiptag','M2_4_Australia.py',69),
  ('table -> BEGIN skiptag CLOSE_H2 content data','table',5,'p_table','M2_4_Australia.py',73),
  ('data -> skiptag OPEN_H2 CONTENT content CLOSE_H2 content data','data',7,'p_data','M2_4_Australia.py',87),
  ('data -> END','data',1,'p_data','M2_4_Australia.py',88),
  ('data -> skiptag','data',1,'p_data','M2_4_Australia.py',89),
  ('content -> CONTENT content','content',2,'p_content','M2_4_Australia.py',100),
  ('content -> empty','content',1,'p_content','M2_4_Australia.py',101),
  ('empty -> <empty>','empty',0,'p_empty','M2_4_Australia.py',110),
]
