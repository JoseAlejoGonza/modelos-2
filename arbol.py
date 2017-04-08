class Nodo_nario():
    def __init__ (self, valor, hijos=[]):
        self.valor=valor
        self.hijos=hijos
        
def ver_hijos(Nodo):
    print Nodo.valor
    [ver_hijos(x) for x in Nodo.hijos]

#buscar nodo
def b_nod(Nodo, palabra):
    if Nodo.valor == palabra:
        return ver_hijos(Nodo)
    else:
        return [b_nod(x,palabra) for x in Nodo.hijos]

n=Nodo_nario('',[Nodo_nario('d',[Nodo_nario('da',[Nodo_nario('dal',[Nodo_nario('dali',[])])
                                 ,Nodo_nario('dan',[Nodo_nario('dana',[Nodo_nario('danar',[]),Nodo_nario('danad',[Nodo_nario('danado',[])])])])])
                ,Nodo_nario('de',[Nodo_nario('det',[Nodo_nario('deta',[Nodo_nario('detal',[Nodo_nario('detall',[Nodo_nario('detalle',[])])])])]),
                                  Nodo_nario('dej',[Nodo_nario('deja',[Nodo_nario('dejar',[])])])])
                ,Nodo_nario('di',[Nodo_nario('dia',[Nodo_nario('dias',[])]),
                                  Nodo_nario('div',[Nodo_nario('divid',[Nodo_nario('dividi',[Nodo_nario('dividir',[]),Nodo_nario('dividid',[Nodo_nario('dividido',[])])])])]),
                                  Nodo_nario('dio',[Nodo_nario('dios',[Nodo_nario('dioso',[]),Nodo_nario('diosa',[])]),Nodo_nario('diod',[Nodo_nario('diodo',[])])])])
                ,Nodo_nario('do',[Nodo_nario('dob',[Nodo_nario('dobl',[Nodo_nario('dobla',[]),Nodo_nario('doble',[])])]),
                                  Nodo_nario('dor',[Nodo_nario('dori',[Nodo_nario('doria',[])]),
                                                    Nodo_nario('dora',[Nodo_nario('dorar',[]),Nodo_nario('doral',[])])])])
                ,Nodo_nario('du',[Nodo_nario('dul',[Nodo_nario('dulc',[Nodo_nario('dulce',[])])]),
                                  Nodo_nario('due',[Nodo_nario('duen',[Nodo_nario('dueno',[]),Nodo_nario('duena',[])]),
                                                    Nodo_nario('duen',[Nodo_nario('duende',[])])])])])
                ,Nodo_nario('l',[Nodo_nario('la',[Nodo_nario('laz',[Nodo_nario('lazo',[])])
                                 ,Nodo_nario('lau',[Nodo_nario('laur',[Nodo_nario('laura',[]),Nodo_nario('laur',[Nodo_nario('lauri',[])])])])])
                ,Nodo_nario('le',[Nodo_nario('let',[Nodo_nario('leti',[Nodo_nario('1etic',[Nodo_nario('letici',[Nodo_nario('leticia',[])])])])]),
                                  Nodo_nario('leo',[Nodo_nario('leon',[Nodo_nario('leona',[])])])])
                ,Nodo_nario('li',[Nodo_nario('lia',[Nodo_nario('liar',[])]),
                                  Nodo_nario('lis',[Nodo_nario('lisa',[Nodo_nario('lisan',[Nodo_nario('lisand',[]),Nodo_nario('lisandr',[Nodo_nario('lisandra',[])])])])]),
                                  Nodo_nario('lic',[Nodo_nario('lican',[Nodo_nario('licant',[]),Nodo_nario('licantr',[])]),Nodo_nario('licantro',[Nodo_nario('licantropo',[])])])])
                ,Nodo_nario('lo',[Nodo_nario('lor',[Nodo_nario('lore',[Nodo_nario('loren',[]),Nodo_nario('lorena',[])])]),
                                  Nodo_nario('los',[Nodo_nario('los',[Nodo_nario('losa',[])]),
                                                    Nodo_nario('los',[Nodo_nario('lose',[]),Nodo_nario('loser',[])])])])
                ,Nodo_nario('lu',[Nodo_nario('lul',[Nodo_nario('lulu',[])]),
                                  Nodo_nario('luc',[Nodo_nario('luci',[Nodo_nario('lucia',[]),Nodo_nario('1lucian',[])]),
                                                    Nodo_nario('luci',[Nodo_nario('lucia',[])])])])])
                ,Nodo_nario('s',[Nodo_nario('sa',[Nodo_nario('sab',[Nodo_nario('sabo',[])])
                                 ,Nodo_nario('sab',[Nodo_nario('saba',[Nodo_nario('sabado',[]),Nodo_nario('saba',[Nodo_nario('sabana',[])])])])])
                ,Nodo_nario('se',[Nodo_nario('sep',[Nodo_nario('sept',[Nodo_nario('septi',[Nodo_nario('septim',[Nodo_nario('septimo',[])])])])]),
                                  Nodo_nario('ser',[Nodo_nario('serpi',[Nodo_nario('serpiente',[])])])])
                ,Nodo_nario('si',[Nodo_nario('sia',[Nodo_nario('sian',[])]),
                                  Nodo_nario('sit',[Nodo_nario('sita',[Nodo_nario('sitac',[Nodo_nario('sitaci',[]),Nodo_nario('sitacio',[Nodo_nario('sitacion',[])])])])]),
                                  Nodo_nario('sil',[Nodo_nario('silb',[Nodo_nario('silba',[]),Nodo_nario('silbat',[])]),Nodo_nario('silbato',[Nodo_nario('silbatos',[])])])])
                ,Nodo_nario('so',[Nodo_nario('sol',[Nodo_nario('soli',[Nodo_nario('solit',[]),Nodo_nario('solito',[])])]),
                                  Nodo_nario('sor',[Nodo_nario('sora',[Nodo_nario('soraka',[])]),
                                                    Nodo_nario('sora',[Nodo_nario('soray',[]),Nodo_nario('soraya',[])])])])
                ,Nodo_nario('su',[Nodo_nario('sug',[Nodo_nario('sugar',[])]),
                                  Nodo_nario('sue',[Nodo_nario('suegr',[Nodo_nario('suegra',[]),Nodo_nario('suegras',[])]),
                                                    Nodo_nario('suegr',[Nodo_nario('suegro',[])])])])])])

cadena = raw_input("Introduce una cadena de texto:")
b_nod(n,cadena)

