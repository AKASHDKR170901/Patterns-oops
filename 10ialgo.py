def minimumWaitingTime(queries):
    queries.sort()
    totalwaitingtime=0
    for idx,duration in enumerate(queries):
        queriesleft=len(queries)-(idx+1)
        totalwaitingtime+=duration*queriesleft
    return totalwaitingtime