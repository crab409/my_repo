import streamlit 

if 'login' not in streamlit.session_state :
    streamlit.session_state.login = False 
if 'score' not in streamlit.session_state :
    streamlit.session_state.score = 0 

if streamlit.session_state.login :
    answer1 = "1. '동'+'아'+'고등학교' != '동아고등학교'"
    answer2 = "2. 'algorithm' * 2 == 'algorithmalgorithm'"
    answer3 = "3. '10'/'2' == '5'"
    answer4 = "4. 29 // 5 != 5"
    answer5 = "5. 7 ** 2 == 14"
    question = streamlit.radio("2.다음 연산 코드 중 옳은 것은?", 
                                 (answer1, answer2, answer3, answer4, answer5))
    
    if streamlit.button("submit") :
        if "q1" not in streamlit.session_state :
            if question == answer2 :
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