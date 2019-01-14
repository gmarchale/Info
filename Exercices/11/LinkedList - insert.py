# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
def insert(self,s):
    suivant =self.first()
    if suivant is None:
        self.__head = self.Node(s,suivant)
    elif s < suivant.value():
        self.__head = self.Node(s,suivant)
    else :
        for i in range(self.size()-1):
            avant = suivant
            suivant = avant.next()
            if s < suivant.value():
                avant.set_next(self.Node(s,suivant))
                break
        avant = suivant
        suivant = avant.next()
        if suivant is None:
            avant.set_next(self.Node(s,None))
            
# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
def insert(self,s):
    previous = None
    current = self.__head
    
    if current is None:
        self.__head = self.Node(s, None)
        return
    
    while str(s) > str(current) and current is not None:
        previous = current
        current  = current.next()
        previous.set_next(self.Node(s, current))
