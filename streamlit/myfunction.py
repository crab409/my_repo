def is_user(id_in, password="sign_up") :
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
    f = open("user_info.txt", 'a') 
    data = f"{id_in},{password},{email}\n"
    f.write(data)
    f.close()