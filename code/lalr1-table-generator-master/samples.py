from parsing.grammar import *


def get_sample_1():
    
    return Grammar([
        NonTerminal('program', [
            "'program' 'IDENTIFIER' '(' identifier-list ')' ';'"
        ]),
        NonTerminal('identifier-list', [
            "'IDENTIFIER'","identifier-list ',' 'IDENTIFIER'"
        ]),
        NonTerminal('declarations', [
            "'var' declaration-list", "''"
        ]),
        NonTerminal('declaration-list', [
            "identifier-list ':' type ';'", "declaration-list identifier-list ':' type ';'"
        ]),
        NonTerminal('type', [
            "standard-type", "array-type"
        ]),
        NonTerminal('standard-type', [
            "'integer'", "'real'"
        ]),
        NonTerminal('array-type',[
            "'array' '[' 'CONSTANT' '..' 'CONSTANT' ']' 'of' standard-type"
        ]),
        NonTerminal('subprogram-declarations',[
            "subprogram-declarations subprogram-declaration","''"
        ]),
        NonTerminal('subprogram-declaration',[
            "subprogram-head declarations compound-statement"
        ]),
        NonTerminal('subprogram-head',[
            "'function' 'IDENTIFIER' arguments ':' 'result' standard-type ';'", "'procedure' 'IDENTIFIER' arguments ';'"
        ]),
        NonTerminal('arguments',[
            "'(' parameter-list ')'","''"
        ]),
        NonTerminal('parameter-list',[
            "identifier-list ':' type","parameter-list ':' identifier-list ':' type"
        ]),
        NonTerminal('compound-statement',[
            "'begin' statement-list 'end'"
        ]),
        NonTerminal('statement-list',[
            "statement","statement-list ';' statement"
        ]),
        NonTerminal('fucntion-reference',[
            "'IDENTIFIER'","'IDENTIFIER' '(' expression-list ')'"
        ]),
        NonTerminal('factor',[
            "variable","'CONSTANT'","'(' expression ')'","function-reference","'not' factor"
        ]),
        NonTerminal('expression',[
            "simple-expression","simple-expression '=' simple-expression",
            "simple-expression '<>' simple-expression","simple-expression '<' simple-expression","simple-expression '<=' simple-expression","simple-expression '>=' simple-expression",
            "simple-expression '>' simple-expression"
        ]),
        NonTerminal('simple-expression',[
            "term","sign term","simple-expression '+' term","simple-expression '-' term","simple-expression 'or' term","function-reference","'not' factor"
        ]),
        NonTerminal('term',[
            "factor","term 'mod' factor","term 'and' factor","term '*' factor","term '/' factor","term 'div' factor"
        ]),
        NonTerminal('sign',[
            "'+'","'-'"
        ]),
        NonTerminal('statement', [
            "elementary-statement " , "'if' expression 'then' restricted-statement 'else' statement " , "'if' expression 'then' statement " , "'while' expression 'do' statement "
        ]),

        NonTerminal('restricted-statement', [
            "elementary-statement " , "'if' expression 'then' restricted-statement 'else' restricted-statement"  ," 'while' expression 'do' restricted-statement "
        ]),

        NonTerminal('elementary-statement', [
            " variable ':=' expression"  , " procedure-statement " , " compound-statement"
        ]),

        NonTerminal('variable', [
            " 'IDENTIFIER' " , " 'IDENTIFIER'  '(' expression-list ')' "
        ]),

        NonTerminal('expression-list', [
           "expression" , "expression-list ',' expression "
        ])
    ])


