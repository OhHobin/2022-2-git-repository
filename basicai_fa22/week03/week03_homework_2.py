import zipfile as z

x = input('어떤 작업을 하시겠습니까(압축 또는 해제): ')
file_name = input('파일 이름: ')

if x == '압축':
    user_zip = z.ZipFile(file_name, 'w', encoding = 'UTF-8')
    user_zip.write('test.zip')
    print('test.zip 파일로 압축되었습니다.')

else:
    user_zip = z.ZipFile(file_name, encoding = 'UTF-8').extractall()
    print('압축해제 되었습니다.')

user_zip.close()