
class person:
    def __init__(self, q,p,e):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = e
        self.key = str(self.n)+' '+str(self.e)

        # print(phi)
        obr_e = fev(self.e, self.phi)[1]
        self.d = obr_e % self.phi
        # print(self.n,' ',self.e)
        pass


    def shifr(self,m,key): #Чужой ключ шифрует
        keys = str(key).split(" ")
        nCH = int(keys[0])
        eCH = int(keys[1])
        x=[]
        for ch in m:
            dobx = (ord(ch)**eCH) % nCH
            x.append(dobx)
        return x

    def deshifr(self,x): #Свой ключ расшифровывает

        m = ''
        for num in x:
            dobm = (num**self.d) % self.n
            m+=chr(dobm)
        return m



def fev(A,B):   #Версия алгоритма Евклида для шифрования
    yx=[0,1]    #Базовый случай
    if A<B:     #Гарантировать, что А больше
        P=A
        A=B
        B=P
    ost=A%B     #Остаток и результат целочисленного деления
    res=A//B
    #print(A, ' ', B, ' ', ost, ' ', res)
    if(ost!=0): #Если остаток не равен нулю

        yxn=fev(B,ost)  #...То вызовем функцию от меньшего из чисел и остатка
        yx[0]=yxn[1]    #...А результат обработаем по формуле
        yx[1]=yxn[0]-(yxn[1]*res)

    #print(yx)
    return (yx)
