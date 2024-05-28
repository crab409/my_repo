import streamlit 

if 'login' not in streamlit.session_state :
    streamlit.session_state.login = False 
if 'score' not in streamlit.session_state :
    streamlit.session_state.score = 0 

if streamlit.session_state.login :
    answer1 = "1. 변수명에 '.'를 사용할 수 있다."
    answer2 = "변수명에 한글을 사용을 수 있다."
    answer3 = "변수명은 숫자로 시작할 수 있다."
    answer4 = "예약어는 변수명으로 사용할 수 없다!"
    answer5 = "변수명의 길이는 제한되어 있다."
    question = streamlit.radio("1.변수에 대한 설명으로 옳은것은 ?", 
                                 (answer1, answer2, answer3, answer4, answer5))
    
    if streamlit.button("submit") :
        if "q1" not in streamlit.session_state :
            if question == answer2 :
                streamlit.session_state.score += 2.6 
                streamlit.session_state.q1 = True
                streamlit.success("정답입니다!")
            elif (question == answer4) :
                streamlit.session_state.score += 2.6 
                streamlit.session_state.q1 = True
                streamlit.success("정답입니다!")
            else :
                streamlit.warning("오답입니다!")
                streamlit.session_state.q1 = False
        
        else : 
            streamlit.warning("이미 제출한 답은 변경할 수 없습니다.")

else : 
    streamlit.warning("먼저 로그인을 해주세요!")