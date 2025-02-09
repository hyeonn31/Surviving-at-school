import random
from player import player
import enemy
import time
import items
import ending
import picture


# 이미지 삽입





def play():
    

    time.sleep(1)
    player1 = player()
    player1.playerName()

    picture.ground()

    print("체육 교수님 : 자~ 오늘 야구수업은 여기 까지 하는걸로 하고 다음주엔 이론수업으로 강의실에서 봅시다~!\n")
    time.sleep(1.5)
    print(str(player1.name1)+", 학생들 : 수고하셨습니다~!!\"\n")
    time.sleep(1.5)
    print(str(player1.name1)+" : 하.. 평소에 운동좀 할걸.. 꼴이 말이 아니네… 좀비도 아니고\n")
    time.sleep(1.5)
    print(str(player1.name1)+" : 드디어 길고 길던 월요일이 끝이다.. 빨리 집가서 쉬어야지~\n")
    time.sleep(1.5)
    print("(운동장에서 교문을 향해 내려 가는 주인공)\n")
    time.sleep(1.5)
    print("(그 순간 저 멀리 중생관에서 걸음걸이가 이상한 사람들이 떼지어 뛰어내려온다...)\n")
    time.sleep(1.5)
    print(str(player1.name1)+" : 뭐지..? 이시간에 원래 중생관에 사람들이 이렇게 많았나..? 오늘 하체하는 날인가?? 다들 걸음걸이도 좀 이상하네.....\n")
    time.sleep(1.5)
    print("(그 순간 갑자기 사이렌이 울리고, 방송이 나온다.)\n")
    time.sleep(1.5)
    print("??? : 성결대학교 학생들에게 알립니다!! 지금 안양에 좀비사태가 일어났습니다!!!\n")
    time.sleep(1.5)
    print("??? : 학교에 있는 학생들은 지금 당장 성결관 옥상으로 대피하여 구조를 기다려 주시기 바랍니다!!\n")
    time.sleep(1.5)
    print(str(player1.name1)+" : 이게 뭔소리야.. 할로윈 이벤트인가..?\n")
    time.sleep(1.5)
    print("(그들이 가까이 오니 정말로 상태가 이상했다. 악취가 흐르고 몸은 피에 덮혀있으며....)\n")
    time.sleep(1.5)
    print("(...마치 영화 속 좀비같았다.)\n")
    time.sleep(1.5)
    print("(\'"+str(player1.name1)+"\'은 방금 나온 안내방송에 따라 황급히 가까운 성결관으로 도망친다.)\n")
    time.sleep(1.5)
    print("(열심히 뛰어 성결관에 도착한 \'"+str(player1.name1)+"\', 그러나 성결관도 좀비가 가득 차 안전하진 않아 보인다...)\n")
    time.sleep(1.5)
    print(str(player1.name1)+" : 아이씨...교문도 막혀있고.. 살아남을 수 있는 길은 여기밖에 없는데.. \n")
    time.sleep(1.5)
    print("아 몰라!! 어떻게든 되겠지!!!!\n")
    time.sleep(1.5)
    print("(가방에 들어있던 야구배트를 꺼내들고 심호흡을 하며 성결관 옥상을 향한 여정이 시작된다..)\n")
    time.sleep(3)
    print("")
    print("")
    time.sleep(3)


    print("======================     게임 방법     =====================")
    time.sleep(2)
    print("1층부터 4층까지, 각 층마다 좀비 2마리가 랜덤으로 생성됩니다.")
    print("좀비를 처치하여 4층으로 올라간 후, ")
    print("보스 좀비를 처치하면 게임에서 승리합니다.")
    print("")
    time.sleep(2)
    print("<플레이어 스펙>")
    print("체력 : 100")
    print("공격력 : 30")
    print("방어력 : 5")
    print("감염수치 : 0%")
    print("")
    time.sleep(2)
    print("좀비를 마주친 후,")
    print("1입력 - 공격")
    print("2입력 - 도망가서 아이템 사용")
    print("    1 입력 - 우유 사용(현재 감염수치에서 10만큼 회복)")
    print("    2 입력 - 붕대 사용(체력 5회복)")
    print("    3 입력 - 초코도넛 사용(체력 10 회복)")
    print("    4 입력 - 딸기도넛 사용(체력 10 회복)")
    print("")
    print("============================================================")
    print("\n\n\n\n\n\n\n\n\n\n")

    time.sleep(2)
    print("==================     [ENTER를 눌러 게임 시작]     ==================")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    gamestart = input()
    if gamestart == "":
        print("")
        print("["+str(player1.name1)+"님이 모험을 떠납니다!]") # test
    # else:
    #     print("")
    #     print("["+str(player1.name1)+"님이 모험을 떠납니다!]")

    time.sleep(2)    
        
    level(player1)



def level(player1):
    global cnt          # 글로벌 변수 cnt 
    cnt = 0             # cnt = 0으로 시작. 좀비 한마리를 잡을때마다 cnt += 1
    global stage          # 1스테이지부터 시작
    stage = 1

    while True:

        # print(cnt)

        if cnt == 2:        # 좀비를 두마리 잡았을 때,      
            stage = 2       # 스테이지 2     

        elif cnt == 4:      # 두마리 더 잡았을 때
            stage = 3       # 스테이지 3
            
        elif cnt == 6:      # 두마리 더
            stage = 4       # 스테이지 4

        elif cnt == 8:      # 두마리 더 
            stage = "<< Boss Stage >> 4"    # 보스 스테이지

        elif cnt == 9:
            break           # 보스전 깬 다음 반복 종료
        

        

        print(f"================     {stage}층     =================\n") # f-string으로 스테이지 출력
        if cnt < 8:
            monster(player1)
        elif cnt == 8:
            boss(player1)                  
        


def monster(player1):
    monster_list = enemy.monster_list
    chose_monster = random.choice(monster_list) 
    global cnt     
    global stage
    
    print(chose_monster.name+"가 나타났다.")        # chose_monster의 이름 출력
    print("어떻게 하시겠습니까?")                                          
    while (chose_monster.monster_hp>0):          # while문으로 조건은 좀비 체력이 0보다 크면
        print("1. 싸운다. \n2. 도망쳐서 아이템 사용.\n")    
        a = int(input())
        if a == 1:              # 1을 선택하면 attack()으로 이어짐
            print()
            attack(player1, chose_monster)
            
        elif a==2:              # 2를 선택하면 좀비와 싸우지 않았으므로 
            print()
            items.using_item(player1)   # 아이템을 사용하기 위해 items.py의 using_item으로 이동
                    
        
            break
    

# 보스전 제작 함 ^^

def boss(player1):              # 보스전 따로 만듦
    boss_zombie_list = enemy.boss_zombie_list       # 일반 몹들 가져오는 방식이랑 같음
    boss_zombie = random.choice(boss_zombie_list)
    global cnt
    
    
    print(boss_zombie.name+"가 나타났다.")
    print("어떻게 하시겠습니까?")
    while (boss_zombie.monster_hp>0):
        print("1. 싸운다. \n2. 도망쳐서 아이템 사용.\n")    
        a = int(input())
        if a == 1:              # 1을 선택하면 attack()으로 이어짐
            print()
            boss_attack(player1, boss_zombie)
            
        elif a==2:              # 2를 선택하면 좀비와 싸우지 않았으므로 
            cnt -= 1            # cnt -= 1 해줌 => 도망가면 결국 cnt는 오르지 않음
            print()
            items.using_item(player1)   # 아이템을 사용하기 위해 items.py의 using_item으로 이동

            break
                    








     

def attack(player1, chose_monster):
            
    global cnt
    chose_monster.monster_hp -= player1.attack
    print("몬스터에게"+str(player1.attack)+"의 피해를 주었습니다.")
    print("남은 몬스터의 체력:", chose_monster.monster_hp)
    if chose_monster.monster_hp <= 0:
        enemy.monster_list.remove(chose_monster)
        
        cnt += 1

        print("\n\n\n해치웠다!\n\n\n")
        if cnt == 2:
            print("다 해치웠나..?\n")              # 층 올라갈때마다 스토리 추가
            print("[Enter를 눌러 다음층으로 올라가자.]")
            a = input()
            if a == "":
                print("2층엔 없겠지..?")
                time.sleep(1)
                print("(좀비가 바글바글 하다.)")

                picture.first_zomb()        # 사진

                time.sleep(1)
                print("젠장...")
                print("")
                print("")
                time.sleep(2)
        
        elif cnt == 4:     
            print("이번엔 정말 없을거야..\n")
            print("[Enter를 눌러 다음층으로 올라가자.]")       
            a = input()
            if a == "":
                print("제발.. 없어라...")
                time.sleep(1)
                print("(좀비가 바글바글 하다.)")

                picture.second_zomb()       # 사진 2

                time.sleep(1)
                print("이런 씹...")
                print("")
                print("")
                time.sleep(2)

        elif cnt == 6:      
            print("이번엔 정말 정말 정~!말! 없을거야 아니? 없어야해.\n")
            print("[Enter를 눌러 다음층으로 올라가자.]")       
            a = input()
            if a == "":
                time.sleep(1)
                print("(좀비가 바글바글 하다.)")

                picture.third_zomb()        #사진

                time.sleep(1)
                print("제에발 그만해...")
                print("")
                print("")
                time.sleep(2)

        elif cnt == 8:          
            print("이젠 정말 끝이야.. 여기가 마지막 층이잖아..!!\n")
            print("[Enter를 눌러 계속]")       
            a = input()
            if a == "":
                print("빨리 옥상에 올라가서 구조를 기다리자..!")
                time.sleep(2)
                print("(그 순간, 저 멀리서 지금까지와는 다른 어마어마한 크기의 좀비가 달려온다.)")
                
                picture.last_zomb()
                
                time.sleep(2)
                print("어..? 어....? 어?!?!?!?!")
                time.sleep(2)
                print("이게 뭔.. 하..")
                print("")
                print("")
                time.sleep(2)

        

        

              
            
    else:
        real_damage = chose_monster.damage - player1.defense
        player1.hp -= (real_damage)
        player1.infection += chose_monster.virus
        print()
        print("몬스터에게"+str(real_damage)+"의 피해를 입었습니다.")
        print("현재 체력 :", player1.hp)
        print(f"현재 감염율 : {player1.infection}%\n") #f-string 입력 방식 사용

        
        if player1.hp <= 0:
            player.chack(player1)       # hp가 0이 되었을 때 사망하는 기능 player에서 구현
            exit()                      # 게임 오버가 되면 게임 종료
        elif player1.infection >=100:
            player.infec(player1)       # 감염수치가 100이 되었을 때 사망하는 기능 player에서 구현
            exit()                      # 게임 오버가 되면 게임 종료
        


        
        
         # using item자리   
        
            


def boss_attack(player1, boss_zombie):              #   보스전 
    global cnt
            
    boss_zombie.monster_hp -= player1.attack
    print("몬스터에게"+str(player1.attack)+"의 피해를 주었습니다.")
    print("남은 몬스터의 체력:", boss_zombie.monster_hp)
    if boss_zombie.monster_hp <= 0:
        enemy.boss_zombie_list.remove(boss_zombie)
        
        cnt += 1

        print("\n\n\n보스를 해치웠다!\n\n\n")
        ending.happy_end()
      
            
    else:
        real_damage = boss_zombie.damage - player1.defense
        player1.hp -= (real_damage)
        player1.infection += boss_zombie.virus
        print()
        print("몬스터에게"+str(real_damage)+"의 피해를 입었습니다.")
        print("현재 체력 :", player1.hp)
        print(f"현재 감염율 : {player1.infection}%\n") #f-string 입력 방식 사용

        
        if player1.hp <= 0:
            player.chack(player1)       # hp가 0이 되었을 때 사망하는 기능 player에서 구현
            exit()                      # 게임 오버가 되면 게임 종료
        elif player1.infection >=100:
            player.infec(player1)       # 감염수치가 100이 되었을 때 사망하는 기능 player에서 구현
            exit()                      # 게임 오버가 되면 게임 종료
        







play()