#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task2-2')
def task():
	pass
	#------- пишите код здесь -----
r.sleep = 0
r.dn()
for i in range (5):
        r.dn()
        r.pt()
        r.rt()
        r.pt()
        r.up()
        r.pt()
        r.dn(2)
        r.pt()
        r.up()
        r.rt()
        r.pt()
        r.up()
        r.lt(2)
        if (i<4):
                r.rt(4)
#------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
