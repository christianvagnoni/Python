def calcola_media_mobile(numeri, n):

    media_mobili = []

    # Elementi lista
    for i in range(len(numeri)):
    
        ultimi_n = numeri[max(0, i - n + 1):i + 1]

        media = sum(ultimi_n) / len(ultimi_n)

        media_mobili.append(media)

        
    return media_mobili
        
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
result = calcola_media_mobile(numeri, n)
print("Le medie mobili sono:", result)


    









