try:
    if '1'!=1:
        raise 'someError'
    else:
        print('someError not occurred')
except 'someError':
    print('someError occurred')

