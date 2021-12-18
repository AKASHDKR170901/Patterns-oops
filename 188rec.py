class Movie:
    '''Movie class developed by durga for python demo purpose'''
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print('Movie name:',self.title)
        print('Hero name:', self.hero)
        print('Heroine name:', self.heroine)
list_of_movies=[]
while True:
    title=input('Enter movie name:')
    hero=input('Enter hero name:')
    heroine=input('Enter heroine name:')
m=Movie(title,hero,heroine)
list_of_movies.append(m)
print('Movie added to the list successfully')
option=input('Do you want to add one more movie?[yes|No]:')
if option=='no':
    break
print('All movies Information....')
print('#'*40)
for movie in list_of_movies:
    movie.info()
    print()
