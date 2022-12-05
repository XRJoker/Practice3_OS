from threading import Thread
import hashlib
import time
import random
import keyboard

need_add = True
queue = []
need_to_stop = False
m_help = []
m_conditions = [0]

for _ in range(100):
    queue.append(random.randint(0, 100))


def adder_1():
    while (not (need_to_stop)):
        if ((len(queue) - len(m_help) < 80) or m_conditions[len(m_conditions) - 1] == 1):
            m_conditions.append(1)
            added_value = random.randint(0, 100)
            queue.append(added_value)
            st = 'added value by 1 adder is ' + str(added_value) + ' remined ' + str(len(queue) - len(m_help)) + '\n'
            print(st)
            time.sleep(0.5)
        if ((len(queue) - len(m_help) > 100)): m_conditions.append(0)


def adder_2():
    while (not (need_to_stop)):
        if (((len(queue) - len(m_help) < 80) or m_conditions[len(m_conditions) - 1] == 1)):
            m_conditions.append(1)
            need_add = True
            added_value = random.randint(0, 100)
            queue.append(added_value)
            st = 'added value by 2 adder is ' + str(added_value) + ' remined ' + str(len(queue) - len(m_help)) + '\n'
            print(st)
            time.sleep(0.5)
        if ((len(queue) - len(m_help) > 100)): m_conditions.append(0)


def adder_3():
    while (not (need_to_stop)):
        if (((len(queue) - len(m_help) < 80) or m_conditions[len(m_conditions) - 1] == 1)):
            m_conditions.append(1)
            need_add = True
            added_value = random.randint(0, 100)
            queue.append(added_value)
            st = 'added value by 3 adder is ' + str(added_value) + ' remined ' + str(len(queue) - len(m_help)) + '\n'
            print(st)
            time.sleep(0.5)
        if ((len(queue) - len(m_help) > 100)): m_conditions.append(0)


def consumer_1():
    if ((len(queue) - len(m_help)) > 0):
        while (not (need_to_stop)):
            time.sleep(0.5)
            collected_value = -1
            if len(queue) > 0:
                (m_help.append(1))
                collected_value = queue[len(m_help)]
            st = 'collected value by 1 consumer is ' + str(collected_value) + ' remined ' + str(
                len(queue) - len(m_help)) + '\n'
            print(st)


def consumer_2():
    if ((len(queue) - len(m_help)) > 0):

        while (not (need_to_stop)):
            time.sleep(0.5)
            collected_value = -1
            if len(queue) > 0:
                (m_help.append(1))
                collected_value = queue[len(m_help)]
            st = 'collected value by 2 consumer is ' + str(collected_value) + ' remined ' + str(
                len(queue) - len(m_help)) + '\n'
            print(st)


consumer1 = Thread(target=consumer_1, args=())
consumer2 = Thread(target=consumer_2, args=())

adder1 = Thread(target=adder_1, args=())
adder2 = Thread(target=adder_2, args=())
adder3 = Thread(target=adder_3, args=())
consumer1.start()
consumer2.start()

adder1.start()
adder2.start()
adder3.start()

keyboard.wait('q')

need_to_stop = True
