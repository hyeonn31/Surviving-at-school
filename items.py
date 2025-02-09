
# class milk:         # 우유
#     def __init__(self):
#         self.name = "우유"
#         self.anti = -10


# class bandage:      # 붕대
#     def __init__(self):
#         self.name = "붕대"
#         self.heal = 5


# class choco_donut:  # 초코도넛
#     def __init__(self):
#         self.name = "초코 도넛"
#         self.heal = 10


# class strawberry_donut:  # 딸기도넛
#     def __init__(self):
#         self.name = "딸기 도넛"
#         self.heal = 15




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 전체 설명




# 아이템 클래스를 위에 만들긴 했지만 구현을 못함.
# 그래서 차선책으로 아래에 리스트의 인덱스의 값을 이용해서 인벤토리와 아이템 사용기능 구현
# 버튼을 입력받아 1을 누르면 0번 인덱스값을 1만큼 차감시켜 인벤토리에 있는 아이템의 갯수 차감
# 만약 n번 인덱스의 값이 0이라면, 더이상 사용할 아이템이 없다는 메시지를 출력하는 기능 구현
 




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



inven = [2,2,2,2]        # 차례대로 우유 2개, 붕대 1개, 초코 1개, 딸기 1개(시작할 때 부터 아이템 소지한상태로 시작)

def using_item(player1):
    
    print("에잇..! 일단 도망쳐서 필요한걸 사용하자!\n")
    
    print("가방에 분명 쓸만한게 있을거야..!")
    print("=================    인벤토리    =================\n\n")
    print("1. 우유 : 현재 감염수치를 10만큼 회복합니다.")                           
    print(f"현재 보유 갯수 : {inven[0]}개\n")
    print("2. 붕대 : 체력을 5만큼 회복합니다.")
    print(f"현재 보유 갯수 : {inven[1]}개\n")
    print("3. 초코 도넛 : 체력을 10만큼 회복합니다.")
    print(f"현재 보유 갯수 : {inven[2]}개\n")
    print("4. 딸기 도넛 : 체력을 15만큼 회복합니다.")
    print(f"현재 보유 갯수 : {inven[3]}개\n\n")
    print("==================================================\n")

    print("무엇을 사용하시겠습니까??")
    use = int(input())              # 1,2,3,4중 하나 입력받음
    
    print("\n\n\n")
    if use == 1:
        if inven[0] > 0:                # 우유 갯수가 0보다 클때 사용가능
            player1.infection += -10    # 플레이어 감염수치를 10만큼 줄여줌
            print("우유를 사용하여 감염수치를 10 회복했습니다.\n")
            print("플레이어 체력 : ", player1.hp)
            print(f"플레이어 감염수치 : {player1.infection}%\n\n\n")
            inven[0] -= 1               # 한번 사용하면 인덱스 0번 값을 1만큼 차감 = 아이템(우유) 1개 소비함
        elif inven[0] <= 0:             # 우유가 없을떄 사용 불가 메시지 
            print("더 이상 사용할 우유가 없어!\n\n")
    
    elif use == 2:
        if inven[1] > 0:
            player1.hp += 5
            print("붕대를 사용하여 체력을 5 회복했습니다.\n")
            print("플레이어 체력 : ", player1.hp)
            print(f"플레이어 감염수치 : {player1.infection}%\n\n\n")
            inven[1] -= 1
        elif inven[1] <= 0:
            print("더 이상 사용할 붕대가 없어!\n\n")    

    elif use == 3:
        if inven[2] > 0:
            player1.hp += 10
            print("초코 도넛을 사용하여 체력을 10 회복했습니다.\n")
            print("플레이어 체력 : ", player1.hp)
            print(f"플레이어 감염수치 : {player1.infection}%\n\n\n")
            inven[2] -= 1
        elif inven[2] <= 0:
            print("더 이상 사용할 초코 도넛이 없어!\n\n")  

    elif use == 4:
        if inven[3] > 0:
            player1.hp += 15
            print("딸기 도넛을 사용하여 체력을 15 회복했습니다.\n")
            print("플레이어 체력 : ", player1.hp)
            print(f"플레이어 감염수치 : {player1.infection}%\n\n\n")
            inven[3] -= 1
        elif inven[3] <= 0:
            print("더 이상 사용할 딸기 도넛이 없어!\n\n")

    
            
            

