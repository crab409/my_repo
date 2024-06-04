def is_user(id_in, password="sign_up") :
    if (id_in=="admin") :
        return True
    f = open("user_info.txt", "r") 
    lines = f.readlines()
    lines.reverse()
    for line in lines : 
        user_info = line.strip().split(',')
        id_info = user_info[0]
        password_info = user_info[1]
        if (id_in==id_info) :
            if (password==password_info) :
                f.close()
                return True
    f.close()    
    return False

def sign_up(id_in, password, email) :
    id_in = id_in.strip() 
    password = password.strip()
    email = email.strip()
    f = open("user_info.txt", 'a') 
    data = f"{id_in},{password},{email}\n"
    f.write(data)
    f.close()

answer1 = '''문제 1번 "변수의 설명에 대해 옳은것은?"

정답 : 2 or 4

1.변수명에 '.'를 사용할 수 있다.
오답) python의 변수명에는 _(언더바)를 제외한 특수문자는 사용을 불가능하다.

2.변수명에 한글을 사용할 수 있다.
정답) python 3버전부터 한국어를 포함한 모든 유니코드 내의 문자가 변수명으로 선언 가능하다.

3.변수명은 숫자로 시작할 수 있다.
오답) 변수명은 숫자로 시작할 수 없다.

4.예약어는 변수명으로 사용할 수 없다.
정답) 변수명으로 try, except, if, for와 같은 예약어는 사용할 수 없다.

5.변수의 길이는 제한되어있다.
오답) 변수명의 길이는 제한되어 있지 않다.
'''

answer2 = '''문제 2번 "다음 연산 코드 중 옳은 것은?"

정답 : 2 

1. '동'+'아'+'고등학교' != '동아고등학교'
오답) 문자열 더하기 연산은 문자열을 이어 붙힌다. 

2. 'algorithm' * 2 == 'algorithmalgorithm' 
정답) 문자열 곱하기 연산은 문자열을 해당 정수만큼 반복한다.

3. '10'/'2' == '5' 
오답) 해당 항목은 정수의 나누기가 아닌 문자열의 나누기이다. 문자열은 나눌 수 없다.

4. 29 // 5 != 5 
오답) //는 정수형 나누기 연산자로써 몱을 구하는 연산자이다. 따라서 29 // 5 는 29를 5로 나눈 몱으로써 5와 같다.

5. 7 ** 2 == 14
오답) ** 연산자는 거듭제곱의 연산자이다. 따라서 7 ** 2 는 7의 제곱인 49이다.
'''