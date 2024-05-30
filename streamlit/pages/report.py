import streamlit 

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
streamlit.title("정답 제출하기")

if 'login' not in streamlit.session_state :
    streamlit.session_state.login = False 
if 'score' not in streamlit.session_state :
    streamlit.session_state.score = 0 

if (streamlit.session_state.login) :
    if streamlit.button("성적 확인하기") :
        if 'q1' not in streamlit.session_state :
            streamlit.warning("1번 문제가 해결되지 않았습니다.")
        elif 'q2' not in streamlit.session_state :
            streamlit.warning("2번 문제가 해결되지 않았습니다.")
        else :

            streamlit.header(f"당신의 점수는 {streamlit.session_state.score}점입니다!")

            if not streamlit.session_state.q1 :
                streamlit.warning(answer1)

                
        

else :
    streamlit.warning("먼저 로그인을 해주세요!")