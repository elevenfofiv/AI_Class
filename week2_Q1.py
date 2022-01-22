class Score():
    def __init__(self, mid:int, final:int):
        self.mid = mid
        self.final = final

score = Score(50, 75)
print((score.mid + score.final)/2)

