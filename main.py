from libs import welcome, exit
from tools import teacher
from tools import student


def start():
    menus = int(input('silahkan pilih menu dibawah ini\n\n1. Data Guru\n2. Data Siswa\n3. Keluar\n\nSilahkan pilih: '                      ))
    while menus != 1 and menus != 2 and menus != 3:
        print('Input Invalid!! Tolong masukan dengan benar')
        menus = int(input('silahkan pilih menu dibawah ini\n\n1. Absensi Guru\n2. Absensi Siswa\n3. Keluar\n\nSilahkan pilih: '                      ))
    
    if menus == 1:
        teacher.start()
    elif menus == 2:
        student.start()    
    elif menus == 3:
        exit()    
        
        
def main():
    welcome()
    start()
    
if __name__ == '__main__':
    main()     