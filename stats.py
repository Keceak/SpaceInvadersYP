class Stats():

    def __init__(self): #инициализирует статистику
        self.reset_stats()
        self.run_game = True
        with open('BestScore.txt', 'r') as f:
            self.best_score = int(f.readline())

    def reset_stats(self): #статистика изменяемая во время игры
         self.guns_left = 2
         self.score = 0


