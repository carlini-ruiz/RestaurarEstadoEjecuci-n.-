import pickle


ListMeses = ["1", "2", "3", "4"]

ArchivoBinario = open("ArchivoLista","wb")
pickle.dump(ListMeses , ArchivoBinario)
ArchivoBinario.close()

Archivo2 = open("ArchivoLista" , "rb" )

Lista2 = pickle.load(Archivo2)

print(Lista2)