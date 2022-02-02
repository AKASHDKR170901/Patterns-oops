def classPhotos(redShirtHeights,blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    shirtcolourinfirstrow='red' if redShirtHeights[0]<blueShirtHeights[0] else 'blue'
    for idx in range(len(redShirtHeights)):
        redShirtHeight=redShirtHeights[idx]
        blueShirtHeight=blueShirtHeights[idx]
        if shirtcolourinfirstrow=='red':
            if redShirtHeight>=blueShirtHeight:
                return False
        else:
            if blueShirtHeight>=redShirtHeight:
                return False
    return True


