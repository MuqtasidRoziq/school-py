from time import sleep

# notif awal masuk
def welcome():
    print('------------------------')
    print('---- SELAMAT DATANG ----')
    print('---------- DI ----------')
    print('-- SMA AL NIKMAT RIAU --')
    print('------------------------')  

# perintah keluar 
def exit():
    print('program akan dihentikan dalam')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    print('program berhenti')
    exit()
        
if __name__ == '__main__':
    welcome()
    exit()       
    
     