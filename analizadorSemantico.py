import matplotlib.pyplot as plt
import datetime as date


nombreClase = []
atributo = []
metodo = []

def digramaUML():
    print("AQUI SE GENERARA EL DIAGRAMA DE CLASES")

    diagrama = plt.subplot(1,1,1)
    diagrama.axis('tight')
    diagrama.axis('off')

    table = [[nombreClase[0]]]
    table.append([atributo[0]])
    table.append([metodo[0]])
    colors = [['#66CFFF'],['#82fffb'],['#c0fffd']]
   
    table = diagrama.table(cellText = table, cellColours= colors, loc = 'center', cellLoc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1,3)

    tiempo = str(date.datetime.now()).replace(':','_')
    tiempo = tiempo.replace('-','_')
    tiempo = tiempo.replace(' ','__')
    print(tiempo[:19])

    plt.tight_layout()
    plt.savefig('./diagramaClase/'+nombreClase[0]+'_'+tiempo[:19])
    plt.show()