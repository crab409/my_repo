def is_user(id_in, password) :
    f = open("user_info.txt", "r") 
    lines = f.readlines()
    for line in lines : 
        id_info = (line.split(','))[0]
        password_info = (line.split(','))[1]
        if (id_in==id_info) :
            if (password==password_info) :
                return True 
    return False

def sign_up(id_in, password) :
    if (is_user(id_in, password)) :
        return 1
    else :
        try :
            f = open("user_info.txt", 'a')
            data = f"{id_in},{password}\n"
            f.write(data)
            return 0
        except :
            return -1