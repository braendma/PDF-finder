import PyPDF2
import os 

#Definition der Suchmaschine
def PathWalker():
    # Hier eigene Pfade hinterlegen, die genutzt werden sollen
    path1 = 'YOUR\\USER\\PATH\\FOR\\SEARCHING\\HERE'
    path2 = 'YOUR\\USER\\PATH\\FOR\\SEARCHING\\HERE'
    path3 = 'YOUR\\USER\\PATH\\FOR\\SEARCHING\\HERE'
    docs = []
    type = '.pdf'
    
    select = int(input('Welcher Pfad soll gewählt werden? (1: OneDrive, 2: Ordner "Digitalisierung", 3: Y-Laufwerk): '))
    if select == 2:
        path = path2
    elif select == 1:
        path = path1
    elif select == 3:
        path = path3
    
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            if type in name:
                docs.append(os.path.join(root, name))
    return docs
        #for name in directories:
            #print(os.path.join(root, name))

def pdfReader():
    try:
        file = open(document, 'rb')
        fileReader = PyPDF2.PdfFileReader(file, strict = False)
        seiten = fileReader.numPages

        full = "".join((fileReader.getPage(i)).extractText() for i in range (0, seiten))
        full = str.lower(full)
        file.close()

        if suchbegriffe == 1:
            if stichwort in full:
                return document
            else:
                pass
            
        elif suchbegriffe == 2:
            if stichwort[0] and stichwort[1] in full:
                return document
            else:
                pass
        
    except:
        return ('Dokument konnte nicht geöffnet werden' + ': ' + document)

#Ausführen der Suche
pfad = PathWalker()

stichwort = []
stichwort.append(str.lower(input('Nach welchem Stichwort willst du suchen? Stichwort 1: ')))
stichwort.append(str.lower(input('Nach welchem Stichwort willst du suchen? Stichwort 2: ')))

if stichwort[1] == '':
    suchbegriffe = 1
    stichwort = str(stichwort[0])
else:
    suchbegriffe = 2

print('\nSuche läuft für:', stichwort, 'Begriffe:', suchbegriffe)

print('\n\nSuchergebnisse: \n\n')
for document in pfad:
    if pdfReader() == None:
        continue
    else:
        print(pdfReader())
        print('\n')
