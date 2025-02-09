

class miso:
    def __init__(self):
        self.name = "미소 좀비"
        self.damage = 10
        self.monster_hp = 60
        self.virus = 10

class boss:
    def __init__(self):
        self.name = "보스 좀비"
        self.damage = 60
        self.monster_hp = 30 #체력 수정
        self.virus = 15

class sankyung:
    def __init__(self):
        self.name = "산경 좀비"
        self.damage = 30
        self.monster_hp = 60
        self.virus = 10
        
class jungtoung:
    def __init__(self):
        self.name = "정통 좀비"
        self.damage = 40
        self.monster_hp = 30
        self.virus = 30

class comgong:
    def __init__(self):
        self.name = "컴공 좀비"
        self.damage = 40
        self.monster_hp = 30
        self.virus = 30

monster_list = []
for i in range(4):  # 몬스터 체력 0되면 리스트에서 삭제하는 방식으로 보완함
                    # 총 8 라운드지만 랜덤성을 위해 4마리씩 총 16마리 생성함
    monster_list.extend([miso(),sankyung(),comgong(),jungtoung()])

boss_zombie_list = [boss()]
