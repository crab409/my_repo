import streamlit 
import myfunction

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
                streamlit.warning(myfunction.answer1)

            if not streamlit.session_state.q2 :
                stremalit.wraning(myfunction.answer2)

                
        

else :
    streamlit.warning("먼저 로그인을 해주세요!")