class player():
    def __init__(self):
        self.hp = 100
        self.attack = 30
        self.defense = 5
        self.infection = 0
        self.victory = False

    def playerName(self):
        name = input("player 이름을 입력하세요 : ")
        self.name1 = name
        

    def chack(self):
        if self.hp <= 0:                    # hp가 0이 되었을 떄 게임오버 
            print() 
            print("game over...\n")
            print("좀비에게 맞아 죽었습니다.")
            # game over로 가는 코드
        
    def infec(self):
        if self.infection >= 100:           # 감염수치가 100이 되었을 때 게임 오버
            print("game over...\n")
            print("감염되어 좀비가 되었습니다.")
            # 감염수치 100으로 사망