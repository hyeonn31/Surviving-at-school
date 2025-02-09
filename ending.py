import time
import picture


def happy_end():


    print("헉..헉.. 마지막 좀비는 우두머리였나..?")
    time.sleep(1)
    print("드디어... 헉.. 끝이야... 헉.. ")
    time.sleep(1)
    print("빨리 옥상으로 올라가서 구조를 기다리자!")
    print("[Enter를 눌러 옥상으로 올라가자.]\n")
    print("")
    a = input()
    if a == "":
        print("===============     옥상     ================")
        print("")

        picture.roof()      # 옥상 사진

        time.sleep(1)
       

        print("옥상으로 황급히 뛰어 올라가는 주인공")
        print("간발의 차이로 옥상문을 닫는데 성공한다.\n")
        time.sleep(1.5)

        print("나 : 휴… 5초만 늦었어도 끔찍했을거야.\n")
        time.sleep(1)
        print("다행히 옥상에 좀비는 없었다.\n")
        time.sleep(1)
        print("하지만 계속해서 두드리는 좀비들 때문에 언제 옥상 문이 부셔질지 모른다.")
        print("너무 무섭다.. \n")
        time.sleep(1)
        print("밤이 깊어졌지만 좀비들이 문을 부술 수 없게 주인공은 옥상의") 
        print("물건들로 문을 가로막으며 하루종일 잠에 들지 못했다.\n")
        time.sleep(1)

        picture.dawn()

        print("[다음날 새벽…]")
        time.sleep(3)
        print("헬기소리 : 두두두두ㅜ뚜두우ㅜ두ㅜ두두두\n\n")
        
        picture.resque()

        time.sleep(2)
        print("나 : 어 여기요!! 여기 사람있어요 살려주세요!!!!!\n")
        time.sleep(1)
        print("주인공은 황급히 옷을 벗어 깃발처럼 흔들었다.")
        time.sleep(2)
        print("구조헬기는 발견했다!\n\n")
        time.sleep(1.5)
        print("구조대 : 위치 확인했습니다. 조금만 더 버텨주세요 지금 내려갑니다!\n")
        time.sleep(1.5)
        print("나 : '제발..빨리.. 곧있으면 좀비가 문을 부술거야...!!'\n")

        picture.last_zomb()

        time.sleep(1)
        print("구조헬기가 밧줄을 내린 그 순간 문이 부숴지고 말았다.\n")
        time.sleep(1)
        print("간발의 차로 주인공은 밧줄을 잡았고, 헬기는 그 즉시 떠올랐다. \n")
        time.sleep(1)
        print("주인공은 무사히 구조되었다.")
        print("\n\n\n")
        print("~~~~~~~The End~~~~~~")
