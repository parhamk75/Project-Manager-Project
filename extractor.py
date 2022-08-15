
tmp_acc = 0

with open('PMP_LOG.txt', 'r') as log_file:
    for line in log_file.readlines():        
        tmp_acc += eval( line.split()[2])

print('sec ==> ', tmp_acc)        
print('min ==> ', tmp_acc/60)
print('hour ==> ', tmp_acc/3600)

tmp_in = input('Calculate Income? ([Y]/N)')

if tmp_in in ['y','Y','']:
    while(True):
        tmp_in = input('Enter the price per hours _> ')
        print('Income will be : ', (tmp_acc/3600)*float(tmp_in) )

        tmp_in = input('Exit? (Y/[N])')

        if tmp_in in ['y','Y']:
            break