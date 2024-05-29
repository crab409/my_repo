import streamlit 
import myfunction

if 'login' not in streamlit.session_state:
    streamlit.session_state.login = False
login_tab, signup_tab = streamlit.tabs(["LOG IN","SIGN UP"])

with login_tab :
    streamlit.title("log in page")

    id_in = streamlit.text_input("Enter the your id")
    password_in = streamlit.text_input("Enter the your Password", )

    if streamlit.button("LOG IN") :
        if (myfunction.is_user(id_in, password=password_in)) :
            streamlit.session_state.login = True
            streamlit.success(f"{id_in}, It's nice to see you again!")

        else :
            streamlit.warning("Something is wroge! Try again!")

with signup_tab : 
    streamlit.title("SIGN IN")
    sign_id_in = streamlit.text_input("Enter the id")
    emali_in = streamlit.text_input("Enter the email")
    sign_password_in = streamlit.text_input("Enter the password") 
    password_check = streamlit.text_input("Enter the password again")


    if streamlit.button("SIGN UP") :
        if (sign_password_in==password_check) :
            if (myfunction.is_user(sign_id_in)) :
                pass 
        fun_result = myfunction.sign_up(id_in, sign_password_in, emali_in)

        if fun_result == 1 :
            streamlit.warning("It is already exist!")