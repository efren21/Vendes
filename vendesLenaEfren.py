#EFRÉN LENA ROSELLÓ

#VECTORS
noms = []
preus = []
qVenudes = []

#ACUMULADORS
articleMesVenut = 0
qArticleMesVenut = 0
qArticleMesIngres = 0
articleMesIngres = 0
total = 0
opcio = 0

#BUCLE
while True:

    #CREACIÓ DEL MENÚ
    opcio = input("1. Introduir un article nou" +
                  "\n2. Fer una venda" +
                  "\n3. Mostrar informació" +
                  "\n4. Esborrar un article" +
                  "\n5. Esborrar tots els articles" +
                  "\n6. Eixir\n\n")
   
    #ACCIÓ A REALITZAR SEGONS EL NÚM DEL MENÚ QUE ES TRIE
    if opcio == "1":
        nom = input("Introdueix el nom del article: ")
        preu = input("Introdueix el preu del article: ")
        noms.append(nom)
        preus.append(float(preu))
        qVenudes.append(0)
    elif opcio == "2":
        nom = input("Introdueix el nom del article: ")
        existeixArticle = False
        for i in range(0, len(noms)):
            if noms[i] == nom:
                qVenuda = input("Quantitat venuda de " + nom + ": ")
                qVenudes[i] += int(qVenuda)
                existeixArticle = True
        if not existeixArticle:
            print("\nNo existeix el article " + nom + "\n")
    elif opcio == "3":
        print("\nNOM     QUANT   PREU   IMPORT")
        for i in range(0, len(noms)):
            importe = qVenudes[i]*preus[i]
            print(noms[i] + "     " + str(qVenudes[i]) +
                  "   "+str(preus[i])+"   "+str(importe))
            total = total + importe

            if qVenudes[i] > qArticleMesVenut:
                qArticleMesVenut = qVenudes[i]
                articleMesVenut = i

            if importe > qArticleMesIngres:
                qArticleMesIngres = importe
                articleMesIngres = i
        print("\n             TOTAL: " + str(total))
        print("\nArticle més venut: " + noms[articleMesVenut] +
              ", amb " + str(qVenudes[articleMesVenut]) + " unitats")
        print("Article amb més ingressos: " + noms[articleMesIngres] + " amb " + str(
            qVenudes[articleMesIngres]*preus[articleMesIngres]))
    elif opcio == "4":
        article = input("Article que es vol esborrar: ")
        existeixArticle = False
        for i in range(0, len(noms)):
            if article == noms[i]:
                articleEsborrat = i
                existeixArticle = True

        if not existeixArticle:
            print("Article no trobat")
        else:
            noms.pop(articleEsborrat)
            preus.pop(articleEsborrat)
            qVenudes.pop(articleEsborrat)
            print("Article esborrat")

    elif opcio == "5":
        noms.clear()
        preus.clear()
        qVenudes.clear()
    elif opcio == "6":
        resposta = input("Segur (s/n)?: ")
        if resposta == ("s"):
            break