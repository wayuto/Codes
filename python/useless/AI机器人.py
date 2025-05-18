import os
from datetime import datetime
import winsound
import time

print('我是WYT·AI机器人')
time.sleep(0.1)
print('我除聊天外还有多种功能,你可以输入help来查看')
time.sleep(1)
print('小W: 你叫什么?')
time.sleep(0.3)
name = input('XXX: ')


def chuang():
    mz = input('文件名: ')
    ly = input('拓展名: ')
    with open('{}.{}'.format(mz, ly), mode='r') as w:
        w.read()


def guan():
    os.system('shutdown -s -t 0')


def nz():
    now = datetime.now()
    al_time = input("请输入闹钟时间(示例:08:00:00 am): ")
    al_ho = al_time[0:2]
    al_mi = al_time[3:5]
    al_se = al_time[6:8]
    al_pe = al_time[9:11].upper()
    print('设置成功, 将在{}叫您'.format(al_time))

    while True:
        now = datetime.now()
        cu_ho = now.strftime("%I")
        cu_mi = now.strftime("%M")
        cu_se = now.strftime("%S")
        cu_pe = now.strftime("%p")
        print("\r当前时间: {}".format(now), end='')

        if al_pe == cu_pe:
            if al_ho == cu_ho:
                if al_mi == cu_mi:
                    if al_se == cu_se:
                        winsound.Beep(500, 300000)
                        break


def jsq():
    if 0 == 0:
        while True:
            s1 = float(input('请输入第一个数字(quit退出): '))
            sf = input('请输入运算符(quit退出): ')
            s2 = float(input('请输入第二个数字(quit退出): '))
            if sf == '+':
                print('答案等于: {}'.format(s1 + s2))
            s1 = float(input('请输入第一个数字(quit退出): '))
            sf = input('请输入运算符(quit退出): ')
            s2 = float(input('请输入第二个数字(quit退出): '))
            if sf == '*':
                print('答案等于: {}'.format(s1 * s2))
            s1 = float(input('请输入第一个数字(quit退出): '))
            sf = input('请输入运算符(quit退出): ')
            s2 = float(input('请输入第二个数字(quit退出): '))
            if sf == '/':
                print('答案等于: {}'.format(s1 / s2))
            s1 = float(input('请输入第一个数字(quit退出): '))
            sf = input('请输入运算符(quit退出): ')
            s2 = float(input('请输入第二个数字(quit退出): '))
            if sf == '-':
                print('答案等于: {}'.format(s1 - s2))
            if s1 or sf or s1 == 'quit':
                break


def cmd():
    while True:
        oss = input('cmd: ')
        os.system('{}'.format(oss))
        if oss == quit:
            break


while True:
    wenhao = input('{}: '.format(name))
    if wenhao == 'gn':
        gn = input('功能: ')
        if gn == '1':
            jsq()
        if gn == '2':
            chuang()

        if gn == '3':
            nz()

        if gn == '4':
            cmd()

        if gn == '5':
            guan()



    time.sleep(0.1)
    print('小O: ' + wenhao.strip('吗？').strip('?').strip('？').strip('吗?'))
    if wenhao == '拜拜' or wenhao == '再见':
        break
    if wenhao == 'help':
        print(
            '    1 ---计算器\n    2 ---创建文件\n    3 ---闹钟\n    4 ---cmd模式\n    5 ---关机\n    6 ---退出\n    gn ---功能模式\n(以上功能quit退出)\n更多功能开发ing~')
