def tandemBicycle(redShirtSpeeds,blueShirtSpeeds,fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)
    totalspeed=0
    for idx in range(len(redShirtSpeeds)):
        rider1=redShirtSpeeds[idx]
        rider2=blueShirtSpeeds[len(blueShirtSpeeds)-idx-1]
        totalspeed+=max(rider1,rider2)
    return totalspeed
def reverseArrayInPlace(array):
    i=0
    j=len(array)-1
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1