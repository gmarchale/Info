class Coureur:
    
    def __init__(self,nom,score):
        self.__nom = nom
        self.__meilleurscore = score
        
    def get_nom(self):
        return self.__nom
        
    def get_score(self):
        return self.__meilleurscore
        
    def set_score(self,new):
        if new > self.__meilleurscore:
            self.__meilleurscore = new
    
    def __eq__(self,other):
        return self.score == other.score
        
    def __le__(self,other):
        return self.score <= other.score
        
    def __he__(self,other):
        return self.score >= other.score
        
    def __lt__(self,other):
        return self.score < other.score
        
    def __ht__(self,other):
        return self.score > other.score
        
    def __repr__(self):
        return self.__nom
        
    def __str__(self):
        return "|{0:<15}|{1:^10}|".format(self.nom,self.score)
            
    nom = property(get_nom)
    score = property(get_score,set_score)

class Classement:
    
    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        self.__resultats = []
        self.__size = 0
        
    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__size
    
    def add(self,*c):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        """
        for r in c:
            self.__resultats.append(r)
            self.__resultats = sorted(self.__resultats)
            self.__resultats.reverse()
            self.__size += 1
        
    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return c.score

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        """
        try:
            return self.__resultats.index(c)
        except ValueError:
            return -1
        

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        self.__resultats.remove(c)
        

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        txt = "="*33+"\n"
        for i in range(len(self.__resultats)):
            txt += "| {0:>2} {1}".format(i+1,self.__resultats[i])+"\n"
        txt += "="*33+"\n"
        return txt
        
a = Classement()
c1 = Coureur("Jhon",20)
c2 = Coureur("David",100)
c3 = Coureur("Raimon",50)
c4 = Coureur("Will",50)
c5 = Coureur("Marc",63)
for i in ["AADEL" ,
"AADI" ,
"AARON" ,
"AARONE" ,
"ZIZ ",
"AB" ,
"DEL",
"ABAS" ,
"BASS" ,
"ABASSE" ,
"ABBAS" ,
"ABBES" ,
"ABD" ,
"ABD-ALLAH" ,
"ABD-EL" ,
"ABDALA"]:
    a.add(Coureur(str(i),50))
print(a)


