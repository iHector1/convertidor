'''Programa hehcho por HECTOR JOSUE GONZALEZ CORTES
SE TIENE QUE ENCONTRAR CUANTOS DIRECCIONAMIENTOS DE MEMORIA SE NECESITAN PARA UN TAMANO DE MEMORIA EN ESPECIFICO
'''
def welcome():
    print("Hola, Bienvenido a mi programa!")

def calculateUnids(memory):
    memorySplit=memory.split(' ')
    memory=float(memorySplit[0])
    memoryUnid=memorySplit[1]
    if memoryUnid=='MB':
        return memory*pow(2,20),1
    elif memoryUnid=='GB':
        return memory*pow(2,30),1
    elif memoryUnid=='kB':
        return memory*pow(2,10),1
    else:
        return memory,0
def calculateWords(words,type):
    wordsSplit=words.split(' ')
    words=float(wordsSplit[0])
    wordUnid=wordsSplit[1]
    if wordUnid=='bits' and type==1:
        return words/8
    elif wordUnid=='bytes' and type==0:
        return words*8
    else:
        return words

def calculateNodes(memory,words):
    cantUnids,unid=calculateUnids(memory)
    cantWords=calculateWords(words,unid)
    positions=cantUnids/cantWords
    print(positions)
    nodes=calculateX(positions)
    return nodes, cantUnids*cantWords

def calculateX(positions):
    x=1
    result=0
    while True:
        if result>=positions:
            break
        result=pow(2,x)
        print("x ",x)
        print("result ",result)
        print("Position ",positions)
        x+=1
    x-=1
    return x
def takeData():
    memory=input("Inserte la capacidad de la memoria (puede ser MB,GB,kB,bits separadas por espacios): ")
    words=input("Inserte las lineas de datos o palabras(separadas por espacios bytes,bits): ")
    cantNodes,cantColunms=calculateNodes(memory,words)
    print('Bits del direccionamiento 2^{}\n'.format(cantNodes))
    #print('Tamano de la palabra {:.0E}'.format(cantColunms))
def main():
    welcome()
    takeData()

main()
