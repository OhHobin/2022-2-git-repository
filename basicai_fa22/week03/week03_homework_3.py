from cryptography.fernet import Fernet

x = input('어떤 작업을 하시겠습니까?(enc or dec): ')
file_name = input('파일 이름: ')
xfile = open(file_name, 'r+', encoding='UTF-8')
xtr = ''
while True:
    xtr += xfile.readline()
    if not xtr:
        break

key = Fernet.generate_key()
fernet = Fernet(key)
if x == 'enc':
    enc = fernet.encrypt(xtr)
    xfile.write(enc)
    print('test.bin 파일로 암호화되었습니다.')
elif x == 'dec':
    dec = fernet.decrypt(xtr)
    xfile.write(dec)
    print('test.txt 파일로 복호화되었습니다.')

xfile.close()
yfile.close()