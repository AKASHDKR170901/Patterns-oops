HOME_TEAM_WON=1
def tournamentwinner(competitions,results):
    currentbestteam=""
    scores={currentbestteam:0}
    for idx,competition in enumerate(competitions):
        result=results[idx]
        hometeam,awayteam=competition
        winningteam=hometeam if result==HOME_TEAM_WON else awayteam
        updatescores(winningteam,3,scores)
        if scores[winningteam]>scores[currentbestteam]:
            currentbestteam=winningteam
    return currentbestteam
def updatescores(team,points,scores):
    if team not in scores:
        scores[team]=0
    scores[team]+=points
