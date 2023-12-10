class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # High score should never be reset.
        #self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = 0

        # 比较文件中的最高分和现在的最高分
        save_high_score=self.read_high_score()
        if int(save_high_score)>self.high_score:
            self.high_score=int(save_high_score)
            
    def read_high_score(self):
        Note = open('./Projects/code/x.txt', mode='r')
        content = Note.read()
        print(content)
        Note.close()
        return content



