
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFXnonassocELSEleft,right=PLUSASSIGNMINUSASSIGNMULASSIGNDIVASSIGNleftEQNEQleft><LESSEQMOREEQleft+-left*/nonassocUMINUSleftDOTPLUSDOTMINUSleftDOTMULDOTDIV' ( ) * + , - / : ; < = > BREAK CONTINUE DIVASSIGN DOTDIV DOTMINUS DOTMUL DOTPLUS ELSE EQ EYE FLOAT FOR ID IF INT LESSEQ MINUSASSIGN MOREEQ MULASSIGN NEQ ONES PLUSASSIGN PRINT RETURN STRING WHILE ZEROS [ ] { }program : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction\n                        | instructioninstruction : if_else_instr\n                       | while_instr\n                       | for_instr\n                       | break_instr\n                       | continue_instr\n                       | return_instr\n                       | print_instr\n                       | instr_block\n                       | assignment ';'if_else_instr : IF '(' expression ')' instruction %prec IFX \n                         | IF '(' expression ')' instruction ELSE instruction\n                         | IF '(' error ')' instruction  %prec IFX\n                         | IF '(' error ')' instruction ELSE instruction while_instr : WHILE '(' expression ')' instruction\n                       | WHILE '(' error ')' instruction for_instr : FOR for_init instructionfor_init : ID '=' expression ':' expressionbreak_instr : BREAK ';'continue_instr : CONTINUE ';'return_instr : RETURN expression ';'print_instr : PRINT print_vars ';'\n                       | PRINT error ';'print_vars : print_vars ',' print_var\n                      | print_varprint_var : STRING\n                     | expression instr_block : '{' instructions '}'number : INTnumber : FLOATlvalue : ID\n                  | ID '[' INT ']'\n                  | ID '[' INT ',' INT ']'assignment : lvalue assign_op expressionassign_op : '='\n                     | PLUSASSIGN\n                     | MINUSASSIGN\n                     | MULASSIGN\n                     | DIVASSIGNexpression : number\n                      | lvalue\n                      | matrix_init\n                      | '(' expression ')'\n                      | '-' expression %prec UMINUS\n                      | expression '\\''expression : expression '<' expression\n                      | expression '>' expression\n                      | expression EQ expression\n                      | expression NEQ expression\n                      | expression LESSEQ expression\n                      | expression MOREEQ expressionexpression : expression '+' expression\n                      | expression '-' expression\n                      | expression '*' expression\n                      | expression '/' expressionexpression : expression DOTPLUS expression\n                      | expression DOTMINUS expression\n                      | expression DOTMUL expression\n                      | expression DOTDIV expressionmatrix_init : eye\n                       | ones\n                       | zeros\n                       | '[' matrix_rows ']'\n                       | '[' scopes ']'eye : EYE '(' INT ')' ones : ONES '(' INT ')' zeros : ZEROS '(' INT ')' matrix_rows : matrix_rows ';' row_elems\n                       | row_elems row_elems : row_elems ',' number\n                     | number scopes : scope\n                | scopes ';' scope scope : INT ':' INT\n                | number ':' number ':' number"
    
_lr_action_items = {'IF':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[9,-12,-35,-5,-11,-13,9,-7,-8,-9,-6,9,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,9,-23,-4,9,-26,-48,-27,-49,-32,-21,-25,-36,9,9,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,9,9,-17,-15,-69,-70,-71,-20,-19,-37,9,9,-22,-18,-16,]),'FOR':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[20,-12,-35,-5,-11,-13,20,-7,-8,-9,-6,20,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,20,-23,-4,20,-26,-48,-27,-49,-32,-21,-25,-36,20,20,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,20,20,-17,-15,-69,-70,-71,-20,-19,-37,20,20,-22,-18,-16,]),'<':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,77,77,77,77,-48,-49,77,77,-36,-47,-68,-67,-63,-61,-50,77,-55,-59,-54,-51,77,-60,-58,-56,-57,-62,77,-69,-70,-71,-37,77,]),'MINUSASSIGN':([2,16,100,148,],[-35,49,-36,-37,]),'/':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,80,80,80,80,-48,-49,80,80,-36,-47,-68,-67,-63,-61,80,80,80,-59,80,80,80,-60,-58,80,80,-62,80,-69,-70,-71,-37,80,]),'ZEROS':([10,23,27,31,33,49,50,51,52,53,54,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[46,46,46,46,46,-41,-42,-39,-40,46,-43,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'>':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,82,82,82,82,-48,-49,82,82,-36,-47,-68,-67,-63,-61,-50,82,-55,-59,-54,-51,82,-60,-58,-56,-57,-62,82,-69,-70,-71,-37,82,]),'$end':([0,1,3,4,5,8,12,14,15,17,18,19,21,25,26,48,55,64,68,92,95,98,133,134,146,147,153,154,],[-3,-12,-5,-1,-11,-13,-7,-8,-9,-6,-2,0,-10,-24,-14,-23,-4,-26,-27,-32,-21,-25,-17,-15,-20,-19,-18,-16,]),'PRINT':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[10,-12,-35,-5,-11,-13,10,-7,-8,-9,-6,10,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,10,-23,-4,10,-26,-48,-27,-49,-32,-21,-25,-36,10,10,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,10,10,-17,-15,-69,-70,-71,-20,-19,-37,10,10,-22,-18,-16,]),"'":([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,84,84,84,84,-48,-49,84,84,-36,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,84,-69,-70,-71,-37,84,]),'(':([9,10,22,23,27,31,33,35,45,46,49,50,51,52,53,54,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[27,31,58,31,31,31,31,67,90,91,-41,-42,-39,-40,31,-43,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'INT':([10,23,24,27,31,33,38,49,50,51,52,53,54,58,63,67,75,76,77,78,79,80,81,82,83,85,86,87,88,89,90,91,94,99,106,108,109,111,112,145,151,],[32,32,60,32,32,32,73,-41,-42,-39,-40,32,-43,32,32,105,32,32,32,32,32,32,32,32,32,32,32,32,32,32,127,128,32,132,73,32,32,141,32,32,32,]),'NEQ':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,83,83,83,83,-48,-49,83,83,-36,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,83,-69,-70,-71,-37,83,]),'+':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,87,87,87,87,-48,-49,87,87,-36,-47,-68,-67,-63,-61,87,87,87,-59,87,87,87,-60,-58,-56,-57,-62,87,-69,-70,-71,-37,87,]),'-':([2,10,23,27,29,31,32,33,34,36,39,40,41,42,43,49,50,51,52,53,54,58,59,62,63,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,94,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,145,148,152,],[-35,33,33,33,-65,33,-33,33,-44,-46,-34,-66,-45,-64,88,-41,-42,-39,-40,33,-43,33,88,88,33,88,-48,33,33,33,33,33,33,33,33,33,-49,33,33,33,33,33,88,33,88,-36,-47,-68,-67,-63,-61,88,88,88,-59,88,88,88,-60,-58,-56,-57,-62,88,-69,-70,-71,33,-37,88,]),'=':([2,16,56,100,148,],[-35,51,94,-36,-37,]),'error':([10,27,58,],[37,61,96,]),'EQ':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,78,78,78,78,-48,-49,78,78,-36,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,78,-69,-70,-71,-37,78,]),'MOREEQ':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,79,79,79,79,-48,-49,79,79,-36,-47,-68,-67,-63,-61,-50,79,-55,-59,-54,-51,79,-60,-58,-56,-57,-62,79,-69,-70,-71,-37,79,]),';':([2,6,7,13,28,29,30,32,34,36,37,39,40,41,42,43,44,59,66,69,70,71,72,73,74,84,93,100,103,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,135,136,138,139,140,141,143,144,148,155,],[-35,25,26,48,-29,-65,64,-33,-44,-46,68,-34,-66,-45,-64,-31,-30,98,-48,106,-76,-73,109,-33,-75,-49,-38,-36,-28,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,-69,-77,-74,-72,-75,-78,-70,-71,-37,-79,]),'RETURN':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[23,-12,-35,-5,-11,-13,23,-7,-8,-9,-6,23,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,23,-23,-4,23,-26,-48,-27,-49,-32,-21,-25,-36,23,23,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,23,23,-17,-15,-69,-70,-71,-20,-19,-37,23,23,-22,-18,-16,]),'WHILE':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[22,-12,-35,-5,-11,-13,22,-7,-8,-9,-6,22,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,22,-23,-4,22,-26,-48,-27,-49,-32,-21,-25,-36,22,22,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,22,22,-17,-15,-69,-70,-71,-20,-19,-37,22,22,-22,-18,-16,]),':':([2,29,32,34,36,39,40,41,42,66,73,74,84,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,137,142,143,144,148,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,-48,111,112,-49,-36,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,145,-69,112,151,-70,-71,-37,]),'BREAK':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[13,-12,-35,-5,-11,-13,13,-7,-8,-9,-6,13,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,13,-23,-4,13,-26,-48,-27,-49,-32,-21,-25,-36,13,13,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,13,13,-17,-15,-69,-70,-71,-20,-19,-37,13,13,-22,-18,-16,]),',':([2,28,29,30,32,34,36,39,40,41,42,43,44,60,66,71,73,74,84,100,103,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,135,138,139,140,143,144,148,],[-35,-29,-65,63,-33,-44,-46,-34,-66,-45,-64,-31,-30,99,-48,108,-33,-75,-49,-36,-28,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,-69,-74,108,-75,-70,-71,-37,]),'CONTINUE':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[6,-12,-35,-5,-11,-13,6,-7,-8,-9,-6,6,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,6,-23,-4,6,-26,-48,-27,-49,-32,-21,-25,-36,6,6,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,6,6,-17,-15,-69,-70,-71,-20,-19,-37,6,6,-22,-18,-16,]),'PLUSASSIGN':([2,16,100,148,],[-35,52,-36,-37,]),')':([2,29,32,34,36,39,40,41,42,61,62,65,66,84,96,97,100,104,105,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,135,143,144,148,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,101,102,104,-48,-49,130,131,-36,-47,135,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,143,144,-69,-70,-71,-37,]),'LESSEQ':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,81,81,81,81,-48,-49,81,81,-36,-47,-68,-67,-63,-61,-50,81,-55,-59,-54,-51,81,-60,-58,-56,-57,-62,81,-69,-70,-71,-37,81,]),'}':([1,3,5,8,12,14,15,17,21,25,26,47,48,55,64,68,92,95,98,133,134,146,147,153,154,],[-12,-5,-11,-13,-7,-8,-9,-6,-10,-24,-14,92,-23,-4,-26,-27,-32,-21,-25,-17,-15,-20,-19,-18,-16,]),'*':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,86,86,86,86,-48,-49,86,86,-36,-47,-68,-67,-63,-61,86,86,86,-59,86,86,86,-60,-58,86,86,-62,86,-69,-70,-71,-37,86,]),'DIVASSIGN':([2,16,100,148,],[-35,54,-36,-37,]),'{':([0,1,2,3,5,8,11,12,14,15,17,18,21,25,26,29,32,34,36,39,40,41,42,47,48,55,57,64,66,68,84,92,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,146,147,148,149,150,152,153,154,],[11,-12,-35,-5,-11,-13,11,-7,-8,-9,-6,11,-10,-24,-14,-65,-33,-44,-46,-34,-66,-45,-64,11,-23,-4,11,-26,-48,-27,-49,-32,-21,-25,-36,11,11,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,11,11,-17,-15,-69,-70,-71,-20,-19,-37,11,11,-22,-18,-16,]),'FLOAT':([10,23,27,31,33,38,49,50,51,52,53,54,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,106,108,109,112,145,151,],[39,39,39,39,39,39,-41,-42,-39,-40,39,-43,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'EYE':([10,23,27,31,33,49,50,51,52,53,54,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[35,35,35,35,35,-41,-42,-39,-40,35,-43,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'ONES':([10,23,27,31,33,49,50,51,52,53,54,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[45,45,45,45,45,-41,-42,-39,-40,45,-43,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'[':([2,10,23,27,31,33,49,50,51,52,53,54,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[24,38,38,38,38,38,-41,-42,-39,-40,38,-43,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'MULASSIGN':([2,16,100,148,],[-35,50,-36,-37,]),'DOTMINUS':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,76,76,76,76,76,-49,76,76,-36,-47,-68,-67,-63,-61,76,76,76,76,76,76,76,-60,76,76,76,-62,76,-69,-70,-71,-37,76,]),'DOTDIV':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,75,75,75,75,75,-49,75,75,-36,-47,-68,-67,-63,75,75,75,75,75,75,75,75,75,75,75,75,-62,75,-69,-70,-71,-37,75,]),'ID':([0,1,2,3,5,8,10,11,12,14,15,17,18,20,21,23,25,26,27,29,31,32,33,34,36,39,40,41,42,47,48,49,50,51,52,53,54,55,57,58,63,64,66,68,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,94,95,98,100,101,102,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,130,131,133,134,135,143,144,145,146,147,148,149,150,152,153,154,],[2,-12,-35,-5,-11,-13,2,2,-7,-8,-9,-6,2,56,-10,2,-24,-14,2,-65,2,-33,2,-44,-46,-34,-66,-45,-64,2,-23,-41,-42,-39,-40,2,-43,-4,2,2,2,-26,-48,-27,2,2,2,2,2,2,2,2,2,-49,2,2,2,2,2,-32,2,-21,-25,-36,2,2,-47,-68,-67,-63,-61,-50,-52,-55,-59,-54,-51,-53,-60,-58,-56,-57,-62,2,2,-17,-15,-69,-70,-71,2,-20,-19,-37,2,2,-22,-18,-16,]),'DOTMUL':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,89,89,89,89,89,-49,89,89,-36,-47,-68,-67,-63,89,89,89,89,89,89,89,89,89,89,89,89,-62,89,-69,-70,-71,-37,89,]),'STRING':([10,63,],[44,44,]),'DOTPLUS':([2,29,32,34,36,39,40,41,42,43,59,62,65,66,84,93,97,100,104,107,110,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,135,143,144,148,152,],[-35,-65,-33,-44,-46,-34,-66,-45,-64,85,85,85,85,85,-49,85,85,-36,-47,-68,-67,-63,-61,85,85,85,85,85,85,85,-60,85,85,85,-62,85,-69,-70,-71,-37,85,]),'ELSE':([1,5,8,12,14,15,17,21,25,26,48,64,68,92,95,98,133,134,146,147,153,154,],[-12,-11,-13,-7,-8,-9,-6,-10,-24,-14,-23,-26,-27,-32,-21,-25,149,150,-20,-19,-18,-16,]),']':([32,39,60,69,70,71,72,73,74,132,136,138,139,140,141,155,],[-33,-34,100,107,-76,-73,110,-33,-75,148,-77,-74,-72,-75,-78,-79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'print_instr':([0,11,18,47,57,101,102,130,131,149,150,],[1,1,1,1,1,1,1,1,1,1,1,]),'number':([10,23,27,31,33,38,53,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,106,108,109,112,145,151,],[34,34,34,34,34,74,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,137,138,140,142,34,155,]),'instruction':([0,11,18,47,57,101,102,130,131,149,150,],[3,3,55,55,95,133,134,146,147,153,154,]),'instructions_opt':([0,],[4,]),'return_instr':([0,11,18,47,57,101,102,130,131,149,150,],[5,5,5,5,5,5,5,5,5,5,5,]),'assign_op':([16,],[53,]),'assignment':([0,11,18,47,57,101,102,130,131,149,150,],[7,7,7,7,7,7,7,7,7,7,7,]),'ones':([10,23,27,31,33,53,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'print_vars':([10,],[30,]),'instr_block':([0,11,18,47,57,101,102,130,131,149,150,],[8,8,8,8,8,8,8,8,8,8,8,]),'matrix_init':([10,23,27,31,33,53,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'row_elems':([38,109,],[71,139,]),'print_var':([10,63,],[28,103,]),'for_init':([20,],[57,]),'while_instr':([0,11,18,47,57,101,102,130,131,149,150,],[12,12,12,12,12,12,12,12,12,12,12,]),'break_instr':([0,11,18,47,57,101,102,130,131,149,150,],[15,15,15,15,15,15,15,15,15,15,15,]),'scopes':([38,],[69,]),'scope':([38,106,],[70,136,]),'zeros':([10,23,27,31,33,53,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'lvalue':([0,10,11,18,23,27,31,33,47,53,57,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,101,102,130,131,145,149,150,],[16,41,16,16,41,41,41,41,16,41,16,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,16,16,16,16,41,16,16,]),'if_else_instr':([0,11,18,47,57,101,102,130,131,149,150,],[17,17,17,17,17,17,17,17,17,17,17,]),'instructions':([0,11,],[18,47,]),'program':([0,],[19,]),'expression':([10,23,27,31,33,53,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[43,59,62,65,66,93,97,43,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,152,]),'matrix_rows':([38,],[72,]),'continue_instr':([0,11,18,47,57,101,102,130,131,149,150,],[21,21,21,21,21,21,21,21,21,21,21,]),'for_instr':([0,11,18,47,57,101,102,130,131,149,150,],[14,14,14,14,14,14,14,14,14,14,14,]),'eye':([10,23,27,31,33,53,58,63,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,145,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','MParser.py',38),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','MParser.py',43),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','MParser.py',47),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','MParser.py',51),
  ('instructions -> instruction','instructions',1,'p_instructions','MParser.py',52),
  ('instruction -> if_else_instr','instruction',1,'p_instruction','MParser.py',61),
  ('instruction -> while_instr','instruction',1,'p_instruction','MParser.py',62),
  ('instruction -> for_instr','instruction',1,'p_instruction','MParser.py',63),
  ('instruction -> break_instr','instruction',1,'p_instruction','MParser.py',64),
  ('instruction -> continue_instr','instruction',1,'p_instruction','MParser.py',65),
  ('instruction -> return_instr','instruction',1,'p_instruction','MParser.py',66),
  ('instruction -> print_instr','instruction',1,'p_instruction','MParser.py',67),
  ('instruction -> instr_block','instruction',1,'p_instruction','MParser.py',68),
  ('instruction -> assignment ;','instruction',2,'p_instruction','MParser.py',69),
  ('if_else_instr -> IF ( expression ) instruction','if_else_instr',5,'p_if_else_inst','MParser.py',73),
  ('if_else_instr -> IF ( expression ) instruction ELSE instruction','if_else_instr',7,'p_if_else_inst','MParser.py',74),
  ('if_else_instr -> IF ( error ) instruction','if_else_instr',5,'p_if_else_inst','MParser.py',75),
  ('if_else_instr -> IF ( error ) instruction ELSE instruction','if_else_instr',7,'p_if_else_inst','MParser.py',76),
  ('while_instr -> WHILE ( expression ) instruction','while_instr',5,'p_while_inst','MParser.py',81),
  ('while_instr -> WHILE ( error ) instruction','while_instr',5,'p_while_inst','MParser.py',82),
  ('for_instr -> FOR for_init instruction','for_instr',3,'p_for_inst','MParser.py',86),
  ('for_init -> ID = expression : expression','for_init',5,'p_for_init','MParser.py',90),
  ('break_instr -> BREAK ;','break_instr',2,'p_break_inst','MParser.py',94),
  ('continue_instr -> CONTINUE ;','continue_instr',2,'p_continue_inst','MParser.py',98),
  ('return_instr -> RETURN expression ;','return_instr',3,'p_return_instr','MParser.py',102),
  ('print_instr -> PRINT print_vars ;','print_instr',3,'p_print_instr','MParser.py',106),
  ('print_instr -> PRINT error ;','print_instr',3,'p_print_instr','MParser.py',107),
  ('print_vars -> print_vars , print_var','print_vars',3,'p_print_vars','MParser.py',111),
  ('print_vars -> print_var','print_vars',1,'p_print_vars','MParser.py',112),
  ('print_var -> STRING','print_var',1,'p_print_var','MParser.py',121),
  ('print_var -> expression','print_var',1,'p_print_var','MParser.py',122),
  ('instr_block -> { instructions }','instr_block',3,'p_complex_instr','MParser.py',126),
  ('number -> INT','number',1,'p_number_int','MParser.py',130),
  ('number -> FLOAT','number',1,'p_number_float','MParser.py',134),
  ('lvalue -> ID','lvalue',1,'p_lvalue','MParser.py',138),
  ('lvalue -> ID [ INT ]','lvalue',4,'p_lvalue','MParser.py',139),
  ('lvalue -> ID [ INT , INT ]','lvalue',6,'p_lvalue','MParser.py',140),
  ('assignment -> lvalue assign_op expression','assignment',3,'p_assignment','MParser.py',147),
  ('assign_op -> =','assign_op',1,'p_assign_op','MParser.py',151),
  ('assign_op -> PLUSASSIGN','assign_op',1,'p_assign_op','MParser.py',152),
  ('assign_op -> MINUSASSIGN','assign_op',1,'p_assign_op','MParser.py',153),
  ('assign_op -> MULASSIGN','assign_op',1,'p_assign_op','MParser.py',154),
  ('assign_op -> DIVASSIGN','assign_op',1,'p_assign_op','MParser.py',155),
  ('expression -> number','expression',1,'p_expression','MParser.py',159),
  ('expression -> lvalue','expression',1,'p_expression','MParser.py',160),
  ('expression -> matrix_init','expression',1,'p_expression','MParser.py',161),
  ('expression -> ( expression )','expression',3,'p_expression','MParser.py',162),
  ('expression -> - expression','expression',2,'p_expression','MParser.py',163),
  ("expression -> expression '",'expression',2,'p_expression','MParser.py',164),
  ('expression -> expression < expression','expression',3,'p_rel_op','MParser.py',173),
  ('expression -> expression > expression','expression',3,'p_rel_op','MParser.py',174),
  ('expression -> expression EQ expression','expression',3,'p_rel_op','MParser.py',175),
  ('expression -> expression NEQ expression','expression',3,'p_rel_op','MParser.py',176),
  ('expression -> expression LESSEQ expression','expression',3,'p_rel_op','MParser.py',177),
  ('expression -> expression MOREEQ expression','expression',3,'p_rel_op','MParser.py',178),
  ('expression -> expression + expression','expression',3,'p_num_op','MParser.py',182),
  ('expression -> expression - expression','expression',3,'p_num_op','MParser.py',183),
  ('expression -> expression * expression','expression',3,'p_num_op','MParser.py',184),
  ('expression -> expression / expression','expression',3,'p_num_op','MParser.py',185),
  ('expression -> expression DOTPLUS expression','expression',3,'p_dot_op','MParser.py',189),
  ('expression -> expression DOTMINUS expression','expression',3,'p_dot_op','MParser.py',190),
  ('expression -> expression DOTMUL expression','expression',3,'p_dot_op','MParser.py',191),
  ('expression -> expression DOTDIV expression','expression',3,'p_dot_op','MParser.py',192),
  ('matrix_init -> eye','matrix_init',1,'p_matrix_init','MParser.py',196),
  ('matrix_init -> ones','matrix_init',1,'p_matrix_init','MParser.py',197),
  ('matrix_init -> zeros','matrix_init',1,'p_matrix_init','MParser.py',198),
  ('matrix_init -> [ matrix_rows ]','matrix_init',3,'p_matrix_init','MParser.py',199),
  ('matrix_init -> [ scopes ]','matrix_init',3,'p_matrix_init','MParser.py',200),
  ('eye -> EYE ( INT )','eye',4,'p_eye','MParser.py',204),
  ('ones -> ONES ( INT )','ones',4,'p_ones','MParser.py',208),
  ('zeros -> ZEROS ( INT )','zeros',4,'p_zeros','MParser.py',212),
  ('matrix_rows -> matrix_rows ; row_elems','matrix_rows',3,'p_matrix_rows','MParser.py',216),
  ('matrix_rows -> row_elems','matrix_rows',1,'p_matrix_rows','MParser.py',217),
  ('row_elems -> row_elems , number','row_elems',3,'p_row_elems','MParser.py',226),
  ('row_elems -> number','row_elems',1,'p_row_elems','MParser.py',227),
  ('scopes -> scope','scopes',1,'p_scopes','MParser.py',236),
  ('scopes -> scopes ; scope','scopes',3,'p_scopes','MParser.py',237),
  ('scope -> INT : INT','scope',3,'p_scope','MParser.py',247),
  ('scope -> number : number : number','scope',5,'p_scope','MParser.py',248),
]