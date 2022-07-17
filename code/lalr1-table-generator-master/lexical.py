
from cv2 import sort


class lexical:
    def __init__(self,file,tokens) :
        self.tokens = tokens
        self.fileaddress = file
        self.input_token = []
    def getToken(self):
        buffer = open(self.fileaddress).read()
        cnt=0
        flg = True
        for i in range(len(buffer)): 
            for token in self.tokens:
                if token == 'IDENTIFIER':
                    if i-1<0:
                        k=i;
                        tmpstr=""
                        while (buffer[k].isalpha()):
                            tmpstr+=buffer[k]
                            k+=1
                            if k== len(buffer):
                                break;
                        if (tmpstr in self.tokens) != True:
                            self.input_token.append(("'"+token+"'",cnt))
                            cnt+=1    
                    else :
                        if buffer[i-1].isalpha()!=True:
                            k=i;
                            tmpstr=""
                            while (buffer[k].isalpha()):
                                tmpstr+=buffer[k]
                                k+=1
                                if k== len(buffer):
                                    break;
                            if (tmpstr in self.tokens) != True:
                                self.input_token.append(("'"+token+"'",cnt))
                                cnt+=1    
                            
                elif token != '':
                    k=i
                    tmpch=''
                    for char in token:
                        if (k<len(buffer)):
                            if (char != buffer[k]):
                                flg=False
                                break
                            k+=1
                            tmpch=char
                    if flg and (tmpch==token[-1]):
                        if buffer[k-1].isalpha():
                            if k<len(buffer):
                                if buffer[k].isalpha()!=True:
                                    if k-1-len(token)<0:
                                        self.input_token.append(("'"+token+"'",cnt))
                                        cnt+=1
                                    else:
                                        if buffer[k-1-len(token)].isalpha()!=True:
                                            self.input_token.append(("'"+token+"'",cnt))
                                            cnt+=1
                            else :
                                if k-1-len(token)<0:
                                    self.input_token.append(("'"+token+"'",cnt))
                                    cnt+=1
                                else:
                                    if buffer[k-1-len(token)].isalpha()!=True:
                                        self.input_token.append(("'"+token+"'",cnt))
                                        cnt+=1
                        else:
                            self.input_token.append(("'"+token+"'",cnt))
                            cnt+=1       
                    flg = True
                
                    
        self.input_token=sorted(self.input_token,key=self.__comp,reverse=False)
        return self.input_token
    def __comp(self,touple):
        
        x,y=touple
        return len(x)