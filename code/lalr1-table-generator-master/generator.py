from parsing import *
import samples
import numpy as np
import pandas as pd
from lexical import lexical

def get_grammar():
    return samples.get_sample_1()


def describe_grammar(gr):
    return '\n'.join([
        'Indexed grammar rules (%d in total):' % len(gr.productions),
        str(gr) + '\n',
        'Grammar non-terminals (%d in total):' % len(gr.nonterms),
        '\n'.join('\t' + str(s) for s in gr.nonterms) + '\n',
        'Grammar terminals (%d in total):' % len(gr.terminals),
        '\n'.join('\t' + str(s) for s in gr.terminals)
    ])


def describe_parsing_table(table):
    conflict_status = table.get_conflict_status()

    def conflict_status_str(state_id):
        has_sr_conflict = (conflict_status[state_id] == lalr_one.STATUS_SR_CONFLICT)
        status_str = ('shift-reduce' if has_sr_conflict else 'reduce-reduce')
        return 'State %d has a %s conflict' % (state_id, status_str)

    return ''.join([
        'PARSING TABLE SUMMARY\n',
        'Is the given grammar LALR(1)? %s\n' % ('Yes' if table.is_lalr_one() else 'No'),
        ''.join(conflict_status_str(sid) + '\n' for sid in range(table.n_states)
                if conflict_status[sid] != lalr_one.STATUS_OK) + '\n',
        table.stringify()
    ])
def comp(touple):
    x,y = touple
    return y

def main():
    
    gr = get_grammar()
    table = lalr_one.ParsingTable(gr)
    string = str(gr)
   
    with open('parsing-table' + '.txt', 'w') as textfile:
        textfile.write(describe_grammar(gr))
        textfile.write('\n\n')
        textfile.write(describe_parsing_table(table))
    table.save_to_csv('parsing-table' + '.csv')
    
    table_dict = {} 
    df=pd.read_csv('parsing-table' + '.csv')  
    df = df.astype(object).replace(np.nan, 'None')
   
    table_dict = df.to_dict()
    
    lexer = lexical("input.txt",['','(',')','*','+',"','",'-','..','/',':',':=',';','<','<=','<>','=','>','>=','CONSTANT','[',']','and','array','begin','div','do','else','end','function','if','integer','mod','not','of','or','procedure','program','real','result','then','var','while','IDENTIFIER'])
    
    buffer = lexer.getToken()
    buffer = sorted(buffer,key=comp)
    
    with open('token_table' + '.csv', 'w') as textfile:
        for x,y in buffer:
            textfile.write(str(y)+","+str(x)+'\n')
    buffer = [x for x,y in buffer]
    buffer.reverse()
    st = ['$end',0]
    while(buffer!=None):
        x = buffer.pop()
        st.append(x)           
        if (table_dict[st[-1]][st[-2]]!='None'):
            if(table_dict[st[-1]][st[-2]]=='a'):
                print('accept')
                return 0
            elif(table_dict[st[-1]][st[-2]][0]=='s'):
                st.append(int(table_dict[st[-1]][st[-2]][1:]))       
            elif(table_dict[st[-1]][st[-2]][0]=='r'):     
                j=-1;
                k=int(table_dict[st[-1]][st[-2]][1:])
                nonterminal=''
                terminal=''
                while(True):
                    r=np.asarray([gr.nonterm_offset.values()])==k
                    if(r) :
                        value=r[True] 
                        pos = gr.nonterm_offset.index(value)
                        key_list = list(gr.nonterm_offset.keys())[pos]
                        nonterminal = key_list.split('\'')[1]    
                        terminal=string.split("\n")[k].split("'")[-2] #k-1     
                        break;
                    k-=1
                    while((terminal==st[j])==False):
                        if j==-1:
                            sttmp=st.pop()
                        else:
                            st.pop()
                        j-=1
                    st.pop()
                    st.append(nonterminal)
                st.append(table_dict[st[-1]][st[-2]]) # goto 
                st.append(sttmp)
    print('error')
    return -1
if __name__ == "__main__":
    main()

