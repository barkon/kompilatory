
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFXnonassocELSEleft,right=PLUSASSIGNMINUSASSIGNMULASSIGNDIVASSIGNleftEQNEQleft><LESSEQMOREEQleft+-left*/leftDOTPLUSDOTMINUSleftDOTMULDOTDIVleft:' ( ) * + , - / : ; < = > BREAK CONTINUE DIVASSIGN DOTDIV DOTMINUS DOTMUL DOTPLUS ELSE EQ EYE FLOAT FOR ID IF INT LESSEQ MINUSASSIGN MOREEQ MULASSIGN NEQ ONES PLUSASSIGN PRINT RETURN STRING WHILE ZEROS [ ] { }program : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction\n                        | instructioninstruction : if_else_instr\n                       | while_instr\n                       | for_instr\n                       | break_instr\n                       | continue_instr\n                       | return_instr\n                       | print_instr\n                       | instr_block\n                       | assignment ';'if_else_instr : IF '(' expression ')' instruction %prec IFX \n                         | IF '(' expression ')' instruction ELSE instruction\n                         | IF '(' error ')' instruction  %prec IFX\n                         | IF '(' error ')' instruction ELSE instruction while_instr : WHILE '(' expression ')' instruction\n                       | WHILE '(' error ')' instruction for_instr : FOR for_init instructionfor_init : ID '=' expression ':' expressionbreak_instr : BREAK ';'continue_instr : CONTINUE ';'return_instr : RETURN expression ';'print_instr : PRINT print_vars ';'\n                       | PRINT error ';'print_vars : print_vars ',' print_var\n                      | print_varprint_var : STRING\n                     | expression instr_block : '{' instructions '}'number : INTnumber : FLOATlvalue : ID\n                  | ID '[' INT ']'\n                  | ID '[' INT ',' INT ']'assignment : lvalue assign_op expressionassign_op : '='\n                     | PLUSASSIGN\n                     | MINUSASSIGN\n                     | MULASSIGN\n                     | DIVASSIGNexpression : number\n                      | lvalue\n                      | matrix_init\n                      | '(' expression ')'\n                      | '-' expression\n                      | expression '\\''\n                      | expression bin_op expressionbin_op : rel_op\n                  | num_op\n                  | dot_oprel_op : '<'\n                  | '>'\n                  | EQ\n                  | NEQ\n                  | LESSEQ\n                  | MOREEQnum_op : '+'\n                  | '-'\n                  | '*'\n                  | '/'dot_op : DOTPLUS\n                  | DOTMINUS\n                  | DOTMUL\n                  | DOTDIVmatrix_init : eye\n                       | ones\n                       | zeros\n                       | '[' matrix_rows ']'\n                       | '[' scopes ']'eye : EYE '(' INT ')' ones : ONES '(' INT ')' zeros : ZEROS '(' INT ')' matrix_rows : matrix_rows ';' row_elems\n                       | row_elems row_elems : row_elems ',' number\n                     | number scopes : scope\n                | scopes ';' scope scope : INT ':' INT\n                | number ':' number ':' number"
    
_lr_action_items = {'EYE':([5,6,35,36,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,123,],[27,27,27,27,27,-39,-41,-43,-40,-42,27,27,27,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,27,-59,-63,-65,-61,-56,-67,27,27,]),'NEQ':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,73,-45,-70,-46,-34,-68,-33,73,-49,73,-48,73,73,73,73,-72,-71,73,-47,-36,-73,-74,-75,73,-37,]),'}':([1,4,8,14,15,16,17,19,23,26,47,48,49,58,60,77,93,95,100,135,136,137,138,145,146,],[-9,-7,-11,-12,-10,-5,-6,-13,-8,-24,-23,-14,-4,100,-21,-25,-26,-27,-32,-19,-20,-15,-17,-16,-18,]),'DIVASSIGN':([11,13,117,141,],[-35,54,-36,-37,]),'<':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,74,-45,-70,-46,-34,-68,-33,74,-49,74,-48,74,74,74,74,-72,-71,74,-47,-36,-73,-74,-75,74,-37,]),'>':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,76,-45,-70,-46,-34,-68,-33,76,-49,76,-48,76,76,76,76,-72,-71,76,-47,-36,-73,-74,-75,76,-37,]),'$end':([0,1,4,8,10,12,14,15,16,17,19,20,23,26,47,48,49,60,77,93,95,100,135,136,137,138,145,146,],[-3,-9,-7,-11,-2,0,-12,-10,-5,-6,-13,-1,-8,-24,-23,-14,-4,-21,-25,-26,-27,-32,-19,-20,-15,-17,-16,-18,]),'DOTPLUS':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,78,-45,-70,-46,-34,-68,-33,78,-49,78,78,78,78,78,78,-72,-71,78,-47,-36,-73,-74,-75,78,-37,]),'PLUSASSIGN':([11,13,117,141,],[-35,55,-36,-37,]),'ZEROS':([5,6,35,36,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,123,],[31,31,31,31,31,-39,-41,-43,-40,-42,31,31,31,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,31,-59,-63,-65,-61,-56,-67,31,31,]),'+':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,80,-45,-70,-46,-34,-68,-33,80,-49,80,-48,80,80,80,80,-72,-71,80,-47,-36,-73,-74,-75,80,-37,]),'WHILE':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[18,-9,-7,-11,18,-35,-12,-10,-5,-6,-13,18,-8,18,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,18,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,18,18,18,18,-73,-74,-75,-19,-20,-15,-17,-22,-37,18,18,-16,-18,]),'(':([5,6,18,22,27,28,31,35,36,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,123,],[35,35,57,59,62,63,70,35,35,35,-39,-41,-43,-40,-42,35,35,35,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,35,-59,-63,-65,-61,-56,-67,35,35,]),'MOREEQ':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,84,-45,-70,-46,-34,-68,-33,84,-49,84,-48,84,84,84,84,-72,-71,84,-47,-36,-73,-74,-75,84,-37,]),'-':([5,6,11,30,32,33,34,35,36,37,38,39,40,41,43,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,97,98,101,103,107,109,114,115,117,123,124,125,133,139,141,],[36,36,-35,-69,-44,88,-45,36,36,-70,-46,-34,-68,-33,88,36,-39,-41,-43,-40,-42,36,36,36,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,36,-59,-63,-49,-65,-61,-56,-67,88,-48,36,88,88,88,88,-72,-71,88,-47,-36,36,-73,-74,-75,88,-37,]),'PRINT':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[6,-9,-7,-11,6,-35,-12,-10,-5,-6,-13,6,-8,6,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,6,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,6,6,6,6,-73,-74,-75,-19,-20,-15,-17,-22,-37,6,6,-16,-18,]),'MINUSASSIGN':([11,13,117,141,],[-35,53,-36,-37,]),'INT':([5,6,29,35,36,50,51,52,53,54,55,56,57,59,61,62,63,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,106,108,110,111,112,118,123,140,],[41,41,68,41,41,96,41,-39,-41,-43,-40,-42,41,41,41,104,105,113,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,41,-59,-63,-65,-61,-56,-67,41,68,41,41,131,41,134,41,41,]),'ELSE':([1,4,8,14,15,17,19,23,26,47,48,60,77,93,95,100,135,136,137,138,145,146,],[-9,-7,-11,-12,-10,-6,-13,-8,-24,-23,-14,-21,-25,-26,-27,-32,-19,-20,142,143,-16,-18,]),'error':([6,57,59,],[46,99,102,]),'{':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[21,-9,-7,-11,21,-35,-12,-10,-5,-6,-13,21,-8,21,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,21,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,21,21,21,21,-73,-74,-75,-19,-20,-15,-17,-22,-37,21,21,-16,-18,]),'ONES':([5,6,35,36,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,123,],[28,28,28,28,28,-39,-41,-43,-40,-42,28,28,28,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,28,-59,-63,-65,-61,-56,-67,28,28,]),',':([11,30,32,34,37,38,39,40,41,42,43,44,45,67,68,69,86,92,96,107,109,114,115,116,117,124,125,128,129,130,133,141,],[-35,-69,-44,-45,-70,-46,-34,-68,-33,94,-31,-30,-29,110,-33,-79,-49,-48,118,-72,-71,-50,-47,-28,-36,-73,-74,-79,110,-78,-75,-37,]),'FOR':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[2,-9,-7,-11,2,-35,-12,-10,-5,-6,-13,2,-8,2,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,2,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,2,2,2,2,-73,-74,-75,-19,-20,-15,-17,-22,-37,2,2,-16,-18,]),'CONTINUE':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[3,-9,-7,-11,3,-35,-12,-10,-5,-6,-13,3,-8,3,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,3,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,3,3,3,3,-73,-74,-75,-19,-20,-15,-17,-22,-37,3,3,-16,-18,]),'LESSEQ':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,75,-45,-70,-46,-34,-68,-33,75,-49,75,-48,75,75,75,75,-72,-71,75,-47,-36,-73,-74,-75,75,-37,]),'[':([5,6,11,35,36,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,123,],[29,29,50,29,29,29,-39,-41,-43,-40,-42,29,29,29,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,29,-59,-63,-65,-61,-56,-67,29,29,]),'BREAK':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[7,-9,-7,-11,7,-35,-12,-10,-5,-6,-13,7,-8,7,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,7,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,7,7,7,7,-73,-74,-75,-19,-20,-15,-17,-22,-37,7,7,-16,-18,]),'DOTMUL':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,79,-45,-70,-46,-34,-68,-33,79,-49,79,79,79,79,79,79,-72,-71,79,-47,-36,-73,-74,-75,79,-37,]),':':([11,30,32,34,37,38,39,40,41,68,69,86,92,103,107,109,114,115,117,124,125,127,132,133,141,],[-35,-69,-44,-45,-70,-46,-34,-68,-33,111,112,-49,-48,123,-72,-71,-50,-47,-36,-73,-74,112,140,-75,-37,]),'*':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,82,-45,-70,-46,-34,-68,-33,82,-49,82,82,82,82,82,82,-72,-71,82,-47,-36,-73,-74,-75,82,-37,]),';':([3,7,9,11,30,32,33,34,37,38,39,40,41,42,43,44,45,46,64,65,66,67,68,69,86,92,97,107,109,114,115,116,117,124,125,126,128,129,130,131,133,141,144,],[26,47,48,-35,-69,-44,77,-45,-70,-46,-34,-68,-33,93,-31,-30,-29,95,-80,106,108,-77,-33,-79,-49,-48,-38,-72,-71,-50,-47,-28,-36,-73,-74,-81,-79,-76,-78,-82,-75,-37,-83,]),'STRING':([6,94,],[44,44,]),'/':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,85,-45,-70,-46,-34,-68,-33,85,-49,85,85,85,85,85,85,-72,-71,85,-47,-36,-73,-74,-75,85,-37,]),'ID':([0,1,2,4,5,6,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,35,36,37,38,39,40,41,47,48,49,51,52,53,54,55,56,57,58,59,60,61,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,100,107,109,114,115,117,119,120,121,122,123,124,125,133,135,136,137,138,139,141,142,143,145,146,],[11,-9,25,-7,11,11,-11,11,-35,-12,-10,-5,-6,-13,11,-8,11,-24,-69,-44,-45,11,11,-70,-46,-34,-68,-33,-23,-14,-4,11,-39,-41,-43,-40,-42,11,11,11,-21,11,-52,-51,-57,-54,-58,-55,-25,-64,-66,-60,-53,-62,11,-59,-63,-49,-65,-61,-56,-67,-48,-26,11,-27,-32,-72,-71,-50,-47,-36,11,11,11,11,11,-73,-74,-75,-19,-20,-15,-17,-22,-37,11,11,-16,-18,]),"'":([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,86,-45,-70,-46,-34,-68,-33,86,-49,86,-48,86,86,86,86,-72,-71,86,-47,-36,-73,-74,-75,86,-37,]),'DOTMINUS':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,87,-45,-70,-46,-34,-68,-33,87,-49,87,87,87,87,87,87,-72,-71,87,-47,-36,-73,-74,-75,87,-37,]),'EQ':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,89,-45,-70,-46,-34,-68,-33,89,-49,89,-48,89,89,89,89,-72,-71,89,-47,-36,-73,-74,-75,89,-37,]),'RETURN':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[5,-9,-7,-11,5,-35,-12,-10,-5,-6,-13,5,-8,5,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,5,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,5,5,5,5,-73,-74,-75,-19,-20,-15,-17,-22,-37,5,5,-16,-18,]),'FLOAT':([5,6,29,35,36,51,52,53,54,55,56,57,59,61,71,72,73,74,75,76,78,79,80,81,82,83,84,85,87,88,89,90,94,106,108,110,112,123,140,],[39,39,39,39,39,39,-39,-41,-43,-40,-42,39,39,39,-52,-51,-57,-54,-58,-55,-64,-66,-60,-53,-62,39,-59,-63,-65,-61,-56,-67,39,39,39,39,39,39,39,]),'=':([11,13,25,117,141,],[-35,52,61,-36,-37,]),']':([39,41,64,65,66,67,68,69,96,126,128,129,130,131,134,144,],[-34,-33,-80,107,109,-77,-33,-79,117,-81,-79,-76,-78,-82,141,-83,]),')':([11,30,32,34,37,38,39,40,41,86,91,92,98,99,101,102,104,105,107,109,113,114,115,117,124,125,133,141,],[-35,-69,-44,-45,-70,-46,-34,-68,-33,-49,115,-48,119,120,121,122,124,125,-72,-71,133,-50,-47,-36,-73,-74,-75,-37,]),'IF':([0,1,4,8,10,11,14,15,16,17,19,21,23,24,26,30,32,34,37,38,39,40,41,47,48,49,58,60,77,86,92,93,95,100,107,109,114,115,117,119,120,121,122,124,125,133,135,136,137,138,139,141,142,143,145,146,],[22,-9,-7,-11,22,-35,-12,-10,-5,-6,-13,22,-8,22,-24,-69,-44,-45,-70,-46,-34,-68,-33,-23,-14,-4,22,-21,-25,-49,-48,-26,-27,-32,-72,-71,-50,-47,-36,22,22,22,22,-73,-74,-75,-19,-20,-15,-17,-22,-37,22,22,-16,-18,]),'MULASSIGN':([11,13,117,141,],[-35,56,-36,-37,]),'DOTDIV':([11,30,32,33,34,37,38,39,40,41,43,86,91,92,97,98,101,103,107,109,114,115,117,124,125,133,139,141,],[-35,-69,-44,90,-45,-70,-46,-34,-68,-33,90,-49,90,90,90,90,90,90,-72,-71,90,-47,-36,-73,-74,-75,90,-37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'print_vars':([6,],[42,]),'break_instr':([0,10,21,24,58,119,120,121,122,142,143,],[1,1,1,1,1,1,1,1,1,1,1,]),'while_instr':([0,10,21,24,58,119,120,121,122,142,143,],[4,4,4,4,4,4,4,4,4,4,4,]),'dot_op':([33,43,91,92,97,98,101,103,114,139,],[81,81,81,81,81,81,81,81,81,81,]),'scope':([29,106,],[64,126,]),'row_elems':([29,108,],[67,129,]),'ones':([5,6,35,36,51,57,59,61,83,94,123,],[30,30,30,30,30,30,30,30,30,30,30,]),'scopes':([29,],[65,]),'print_instr':([0,10,21,24,58,119,120,121,122,142,143,],[14,14,14,14,14,14,14,14,14,14,14,]),'return_instr':([0,10,21,24,58,119,120,121,122,142,143,],[8,8,8,8,8,8,8,8,8,8,8,]),'assignment':([0,10,21,24,58,119,120,121,122,142,143,],[9,9,9,9,9,9,9,9,9,9,9,]),'instructions':([0,21,],[10,58,]),'for_init':([2,],[24,]),'program':([0,],[12,]),'instruction':([0,10,21,24,58,119,120,121,122,142,143,],[16,49,16,60,49,135,136,137,138,145,146,]),'number':([5,6,29,35,36,51,57,59,61,83,94,106,108,110,112,123,140,],[32,32,69,32,32,32,32,32,32,32,32,127,128,130,132,32,144,]),'num_op':([33,43,91,92,97,98,101,103,114,139,],[71,71,71,71,71,71,71,71,71,71,]),'assign_op':([13,],[51,]),'expression':([5,6,35,36,51,57,59,61,83,94,123,],[33,43,91,92,97,98,101,103,114,43,139,]),'lvalue':([0,5,6,10,21,24,35,36,51,57,58,59,61,83,94,119,120,121,122,123,142,143,],[13,34,34,13,13,13,34,34,34,34,13,34,34,34,34,13,13,13,13,34,13,13,]),'continue_instr':([0,10,21,24,58,119,120,121,122,142,143,],[15,15,15,15,15,15,15,15,15,15,15,]),'matrix_rows':([29,],[66,]),'print_var':([6,94,],[45,116,]),'bin_op':([33,43,91,92,97,98,101,103,114,139,],[83,83,83,83,83,83,83,83,83,83,]),'zeros':([5,6,35,36,51,57,59,61,83,94,123,],[37,37,37,37,37,37,37,37,37,37,37,]),'matrix_init':([5,6,35,36,51,57,59,61,83,94,123,],[38,38,38,38,38,38,38,38,38,38,38,]),'for_instr':([0,10,21,24,58,119,120,121,122,142,143,],[23,23,23,23,23,23,23,23,23,23,23,]),'instr_block':([0,10,21,24,58,119,120,121,122,142,143,],[19,19,19,19,19,19,19,19,19,19,19,]),'instructions_opt':([0,],[20,]),'if_else_instr':([0,10,21,24,58,119,120,121,122,142,143,],[17,17,17,17,17,17,17,17,17,17,17,]),'eye':([5,6,35,36,51,57,59,61,83,94,123,],[40,40,40,40,40,40,40,40,40,40,40,]),'rel_op':([33,43,91,92,97,98,101,103,114,139,],[72,72,72,72,72,72,72,72,72,72,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','MParser.py',38),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','MParser.py',42),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','MParser.py',46),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','MParser.py',49),
  ('instructions -> instruction','instructions',1,'p_instructions','MParser.py',50),
  ('instruction -> if_else_instr','instruction',1,'p_instruction','MParser.py',59),
  ('instruction -> while_instr','instruction',1,'p_instruction','MParser.py',60),
  ('instruction -> for_instr','instruction',1,'p_instruction','MParser.py',61),
  ('instruction -> break_instr','instruction',1,'p_instruction','MParser.py',62),
  ('instruction -> continue_instr','instruction',1,'p_instruction','MParser.py',63),
  ('instruction -> return_instr','instruction',1,'p_instruction','MParser.py',64),
  ('instruction -> print_instr','instruction',1,'p_instruction','MParser.py',65),
  ('instruction -> instr_block','instruction',1,'p_instruction','MParser.py',66),
  ('instruction -> assignment ;','instruction',2,'p_instruction','MParser.py',67),
  ('if_else_instr -> IF ( expression ) instruction','if_else_instr',5,'p_if_else_inst','MParser.py',71),
  ('if_else_instr -> IF ( expression ) instruction ELSE instruction','if_else_instr',7,'p_if_else_inst','MParser.py',72),
  ('if_else_instr -> IF ( error ) instruction','if_else_instr',5,'p_if_else_inst','MParser.py',73),
  ('if_else_instr -> IF ( error ) instruction ELSE instruction','if_else_instr',7,'p_if_else_inst','MParser.py',74),
  ('while_instr -> WHILE ( expression ) instruction','while_instr',5,'p_while_inst','MParser.py',79),
  ('while_instr -> WHILE ( error ) instruction','while_instr',5,'p_while_inst','MParser.py',80),
  ('for_instr -> FOR for_init instruction','for_instr',3,'p_for_inst','MParser.py',84),
  ('for_init -> ID = expression : expression','for_init',5,'p_for_init','MParser.py',88),
  ('break_instr -> BREAK ;','break_instr',2,'p_break_inst','MParser.py',92),
  ('continue_instr -> CONTINUE ;','continue_instr',2,'p_continue_inst','MParser.py',96),
  ('return_instr -> RETURN expression ;','return_instr',3,'p_return_instr','MParser.py',100),
  ('print_instr -> PRINT print_vars ;','print_instr',3,'p_print_instr','MParser.py',104),
  ('print_instr -> PRINT error ;','print_instr',3,'p_print_instr','MParser.py',105),
  ('print_vars -> print_vars , print_var','print_vars',3,'p_print_vars','MParser.py',109),
  ('print_vars -> print_var','print_vars',1,'p_print_vars','MParser.py',110),
  ('print_var -> STRING','print_var',1,'p_print_var','MParser.py',119),
  ('print_var -> expression','print_var',1,'p_print_var','MParser.py',120),
  ('instr_block -> { instructions }','instr_block',3,'p_complex_instr','MParser.py',124),
  ('number -> INT','number',1,'p_number_int','MParser.py',128),
  ('number -> FLOAT','number',1,'p_number_float','MParser.py',132),
  ('lvalue -> ID','lvalue',1,'p_lvalue','MParser.py',136),
  ('lvalue -> ID [ INT ]','lvalue',4,'p_lvalue','MParser.py',137),
  ('lvalue -> ID [ INT , INT ]','lvalue',6,'p_lvalue','MParser.py',138),
  ('assignment -> lvalue assign_op expression','assignment',3,'p_assignment','MParser.py',145),
  ('assign_op -> =','assign_op',1,'p_assign_op','MParser.py',149),
  ('assign_op -> PLUSASSIGN','assign_op',1,'p_assign_op','MParser.py',150),
  ('assign_op -> MINUSASSIGN','assign_op',1,'p_assign_op','MParser.py',151),
  ('assign_op -> MULASSIGN','assign_op',1,'p_assign_op','MParser.py',152),
  ('assign_op -> DIVASSIGN','assign_op',1,'p_assign_op','MParser.py',153),
  ('expression -> number','expression',1,'p_expression','MParser.py',157),
  ('expression -> lvalue','expression',1,'p_expression','MParser.py',158),
  ('expression -> matrix_init','expression',1,'p_expression','MParser.py',159),
  ('expression -> ( expression )','expression',3,'p_expression','MParser.py',160),
  ('expression -> - expression','expression',2,'p_expression','MParser.py',161),
  ("expression -> expression '",'expression',2,'p_expression','MParser.py',162),
  ('expression -> expression bin_op expression','expression',3,'p_expression','MParser.py',163),
  ('bin_op -> rel_op','bin_op',1,'p_bin_op','MParser.py',172),
  ('bin_op -> num_op','bin_op',1,'p_bin_op','MParser.py',173),
  ('bin_op -> dot_op','bin_op',1,'p_bin_op','MParser.py',174),
  ('rel_op -> <','rel_op',1,'p_rel_op','MParser.py',178),
  ('rel_op -> >','rel_op',1,'p_rel_op','MParser.py',179),
  ('rel_op -> EQ','rel_op',1,'p_rel_op','MParser.py',180),
  ('rel_op -> NEQ','rel_op',1,'p_rel_op','MParser.py',181),
  ('rel_op -> LESSEQ','rel_op',1,'p_rel_op','MParser.py',182),
  ('rel_op -> MOREEQ','rel_op',1,'p_rel_op','MParser.py',183),
  ('num_op -> +','num_op',1,'p_num_op','MParser.py',187),
  ('num_op -> -','num_op',1,'p_num_op','MParser.py',188),
  ('num_op -> *','num_op',1,'p_num_op','MParser.py',189),
  ('num_op -> /','num_op',1,'p_num_op','MParser.py',190),
  ('dot_op -> DOTPLUS','dot_op',1,'p_dot_op','MParser.py',194),
  ('dot_op -> DOTMINUS','dot_op',1,'p_dot_op','MParser.py',195),
  ('dot_op -> DOTMUL','dot_op',1,'p_dot_op','MParser.py',196),
  ('dot_op -> DOTDIV','dot_op',1,'p_dot_op','MParser.py',197),
  ('matrix_init -> eye','matrix_init',1,'p_matrix_init','MParser.py',201),
  ('matrix_init -> ones','matrix_init',1,'p_matrix_init','MParser.py',202),
  ('matrix_init -> zeros','matrix_init',1,'p_matrix_init','MParser.py',203),
  ('matrix_init -> [ matrix_rows ]','matrix_init',3,'p_matrix_init','MParser.py',204),
  ('matrix_init -> [ scopes ]','matrix_init',3,'p_matrix_init','MParser.py',205),
  ('eye -> EYE ( INT )','eye',4,'p_eye','MParser.py',209),
  ('ones -> ONES ( INT )','ones',4,'p_ones','MParser.py',213),
  ('zeros -> ZEROS ( INT )','zeros',4,'p_zeros','MParser.py',217),
  ('matrix_rows -> matrix_rows ; row_elems','matrix_rows',3,'p_matrix_rows','MParser.py',221),
  ('matrix_rows -> row_elems','matrix_rows',1,'p_matrix_rows','MParser.py',222),
  ('row_elems -> row_elems , number','row_elems',3,'p_row_elems','MParser.py',231),
  ('row_elems -> number','row_elems',1,'p_row_elems','MParser.py',232),
  ('scopes -> scope','scopes',1,'p_scopes','MParser.py',241),
  ('scopes -> scopes ; scope','scopes',3,'p_scopes','MParser.py',242),
  ('scope -> INT : INT','scope',3,'p_scope','MParser.py',252),
  ('scope -> number : number : number','scope',5,'p_scope','MParser.py',253),
]
