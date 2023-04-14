from termcolor import colored
import os 

while True :

    ls = os.listdir(".")
    ls_index = 0
    for  item in ls :
        file_dir = ""
        if os.path.isdir("./"+item) :
            file_dir = colored(item,'green')
        else :
            file_dir = item
        print (colored(str(ls_index) +")  " , 'blue') + file_dir + "\n "
               +colored("---------------------------------------------------------------"
                         , 'red'))
        ls_index += 1

    print("\n ")
    print("what can i do for you\n")
    print("change dir :1 // make dir : 2 // delete dir or file : 3 // "+
          "\ncreate file : 4 // rename file or dir : 5\n")
    user_cmd = int(input("type and click enter : "))
    #cd
    if user_cmd == 1 :
        cd_cmd = input("number or just enter for privios dir :")
        if not cd_cmd :
            os.chdir("../")
        else :

            try:
                value = int(cd_cmd)
                os.chdir("./" +ls[value])
                print(os.getcwd())
            except ValueError:
                print("Invalid integer '%s', try again" % (cd_cmd,))
    #make dir
    if user_cmd == 2 :
        print("enter name of new dir , if you just enter we will name it new dir by default")
        cd_cmd = input("name new dir : ")
        if not cd_cmd :
            os.mkdir("new dir")
        else :
            os.mkdir(cd_cmd)
    #delete dir
    if user_cmd == 3 :
        cd_cmd = int(input("enter index of dir or file:"))
        if os.path.isdir("."+ ls[cd_cmd]):
            os.rmdir(ls[cd_cmd])
        else:
            os.remove(ls[cd_cmd])

        print("removed")
    #create file
    if user_cmd == 4 :
        cd_cmd = input("name file :")
        os.system('touch '+ cd_cmd)

    #rename file or dir
    if user_cmd == 5 :
        whichFile = int(input("rename which file or dir :"))
        newName = input("new name :")
        os.rename("./"+ls[whichFile],newName)
        

    
    os.system('clear')

