from socialrecon import reconinput
from webvuln import Webvuln
cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m' 
def Main(a):
    if(a==1):
        reconinput()
    elif(a==2):
        Webvuln()
        

if __name__=="__main__":
    print(cyan+"""
    
 _   __         _____      _       _   
| | / /        |  _  |    (_)     | |  
| |/ /  __  __ | | | | ___ _ _ __ | |_ 
|    \  \ \/ / | | | |/ __| | '_ \| __|
| |\  \  >  <  \ \_/ /\__ \ | | | | |_ 
\_| \_/ /_/\_\  \___/ |___/_|_| |_|\__|
                                     
                                     


    """)
    print(Y+"                           Created By : Karan Kumar")
    print(Y+"                           Github profile: https://github.com/Karannkx")
    print(green+"""
                Available Modules 
           
           1.Information gathering,
           2.Web vulnerability scanning,
    """) 
    print(Y+"Note : In Information gathering type 'tools' to find tools.")
    print(Y+"Note : In Web vulnerability scanning type 'help' to find tools.")
    a=int(input("Module >> "))
    Main(a)
    