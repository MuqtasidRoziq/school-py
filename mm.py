
    # validasi nis
# while nis == '':
#     print('\nHarap isi bidang ini!!')
#     nis = int(input('Masukan nomer NIS: '))
nis = input('Masukan nomer NIS: ')    
while not nis.isdigit():
    print('\nHarap isi bidang ini dengan angka!!')
    nis = input('Masukan nomer NIS: ')
nis = int(nis)    