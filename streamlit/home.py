import streamlit 
import myfunction

if 'login' not in streamlit.session_state:
    streamlit.session_state.login = False

streamlit.title("log in page")

id_in = streamlit.text_input("Enter the id")
password_in = streamlit.text_input("Enter the Password")

if streamlit.button("LOG IN") :
    if (myfunction.is_user(id_in, password_in)) :
        streamlit.session_state.login = True
        streamlit.success(f"{id_in}, It's nice to see you again!")

    else :
        streamlit.warning("Something is wroge! Try again!")

if streamlit.button("SIGN UP") :
    fun_result = myfunction.sign_up(id_in, password_in)

    if fun_result == 1 :
        streamlit.warning("It is already exist!")