import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType #чтение сообытий происходящих в сообществе и тип события
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0

class Bot:
    def __init__(self):
        self.vk_session = vk_api.VkApi(token="") # связь с сообществом
        self.long_poll = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api() #получаем способ взаимодействия с программой ВК
    
    def start(self):
        self.wait_message()

    def wait_message(self):
        global a1
        global a2
        global a3
        global a4
        global a5
        for event in self.long_poll.listen(): #слушаем что происходит в сообществе и ждем реакций
            if event.type  == VkEventType.MESSAGE_NEW and event.to_me:
                print("2")
                if 'привет' in event.message.lower():
                   text = 'Привет, друг! Я бот для определение профориентации. \n Для начала работы напиши <<начать>>. \n '
                   self.send_message(event.user_id, text)
                if 'начать' in event.message.lower():
                    text = 'Тест содержит 35 вопросов и в конце выводятся результаты к какой сфере у вас больше склонность. \n Для начала прохождения теста нажмите кнопку <<пройти тест>>.'
                    idea_keyboard = VkKeyboard(one_time=True)  # создание кнопок
                    idea_keyboard.add_button("пройти тест", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, idea_keyboard.get_keyboard())
                
                if 'пройти тест' in event.message.lower():
                    text = 'Я хочу обслуживать людей \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_1 = VkKeyboard(one_time=True)
                    a1_1.add_button("0-a1", color=VkKeyboardColor.PRIMARY)
                    a1_1.add_line()
                    a1_1.add_button("1-a1", color=VkKeyboardColor.PRIMARY)
                    a1_1.add_line()
                    a1_1.add_button("2-a1", color=VkKeyboardColor.PRIMARY)
                    a1_1.add_line()
                    a1_1.add_button("3-a1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_1.get_keyboard())
                #1
                if '0-a1' in event.message.lower():
                    a1 = a1+0
                    text = 'Я хочу заниматься лечением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_2 = VkKeyboard(one_time=True)
                    a1_2.add_button("0-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("1-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("2-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("2-a2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_2.get_keyboard())
                if '1-a1' in event.message.lower():
                    a1 = a1+1
                    text = 'Я хочу заниматься лечением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_2 = VkKeyboard(one_time=True)
                    a1_2.add_button("0-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("1-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("2-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("3-a2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_2.get_keyboard())
                if '2-a1' in event.message.lower():
                    a1 = a1+2
                    text = 'Я хочу заниматься лечением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_2 = VkKeyboard(one_time=True)
                    a1_2.add_button("0-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("1-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("2-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("3-a2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_2.get_keyboard())
                if '3-a1' in event.message.lower():
                    a1 = a1+3
                    text = 'Я хочу заниматься лечением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_2 = VkKeyboard(one_time=True)
                    a1_2.add_button("0-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("1-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("2-a2", color=VkKeyboardColor.PRIMARY)
                    a1_2.add_line()
                    a1_2.add_button("3-a2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_2.get_keyboard())

                #2
                if '0-a2' in event.message.lower():
                    a1 = a1+0
                    text = 'Я хочу обучать или воспитывать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_3 = VkKeyboard(one_time=True)
                    a1_3.add_button("0-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("1-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("2-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("3-a3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_3.get_keyboard())
                if '1-a2' in event.message.lower():
                    a1 = a1+1
                    text = 'Я хочу обучать или воспитывать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_3 = VkKeyboard(one_time=True)
                    a1_3.add_button("0-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("1-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("2-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("3-a3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_3.get_keyboard())
                if '2-a2' in event.message.lower():
                    a1 = a1+2
                    text = 'Я хочу обучать или воспитывать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_3 = VkKeyboard(one_time=True)
                    a1_3.add_button("0-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("1-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("2-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("3-a3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_3.get_keyboard())
                if '3-a2' in event.message.lower():
                    a1 = a1+3
                    text = 'Я хочу обучать или воспитывать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_3 = VkKeyboard(one_time=True)
                    a1_3.add_button("0-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("1-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("2-a3", color=VkKeyboardColor.PRIMARY)
                    a1_3.add_line()
                    a1_3.add_button("3-a3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_3.get_keyboard())

                #3
                if '0-a3' in event.message.lower():
                    a1 = a1+0
                    text = 'Я хочу защищать права и безопасность \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_4 = VkKeyboard(one_time=True)
                    a1_4.add_button("0-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("1-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("2-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("3-a4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_4.get_keyboard())
                if '1-a3' in event.message.lower():
                    a1 = a1+1
                    text = 'Я хочу защищать права и безопасность \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_4 = VkKeyboard(one_time=True)
                    a1_4.add_button("0-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("1-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("2-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("3-a4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_4.get_keyboard())
                if '2-a3' in event.message.lower():
                    a1 = a1+2
                    text = 'Я хочу защищать права и безопасность \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_4 = VkKeyboard(one_time=True)
                    a1_4.add_button("0-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("1-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("2-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("3-a4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_4.get_keyboard())
                if '3-a3' in event.message.lower():
                    a1 = a1+3
                    text = 'Я хочу защищать права и безопасность \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_4 = VkKeyboard(one_time=True)
                    a1_4.add_button("0-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("1-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("2-a4", color=VkKeyboardColor.PRIMARY)
                    a1_4.add_line()
                    a1_4.add_button("3-a4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_4.get_keyboard())

                #4
                if '0-a4' in event.message.lower():
                    a1 = a1+0
                    text = 'Я хочу управлять людьми \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_5 = VkKeyboard(one_time=True)
                    a1_5.add_button("0-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("1-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("2-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("3-a5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_5.get_keyboard())
                if '1-a4' in event.message.lower():
                    a1 = a1+1
                    text = 'Я хочу управлять людьми \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_5 = VkKeyboard(one_time=True)
                    a1_5.add_button("0-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("1-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("2-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("3-a5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_5.get_keyboard())
                if '2-a4' in event.message.lower():
                    a1 = a1+2
                    text = 'Я хочу управлять людьми \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_5 = VkKeyboard(one_time=True)
                    a1_5.add_button("0-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("1-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("2-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("3-a5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_5.get_keyboard())
                if '3-a4' in event.message.lower():
                    a1 = a1+3
                    text = 'Я хочу управлять людьми \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a1_5 = VkKeyboard(one_time=True)
                    a1_5.add_button("0-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("1-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("2-a5", color=VkKeyboardColor.PRIMARY)
                    a1_5.add_line()
                    a1_5.add_button("3-a5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a1_5.get_keyboard())

                #5
                if '0-a5' in event.message.lower():
                    a1 = a1+0
                    text = 'Я хочу управлять машинами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_6 = VkKeyboard(one_time=True)
                    a2_6.add_button("0-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("1-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("2-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("3-b1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_6.get_keyboard())
                if '1-a5' in event.message.lower():
                    a1 = a1+1
                    text = 'Я хочу управлять машинами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_6 = VkKeyboard(one_time=True)
                    a2_6.add_button("0-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("1-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("2-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("3-b2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_6.get_keyboard())
                if '2-a5' in event.message.lower():
                    a1 = a1+2
                    text = 'Я хочу управлять машинами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_6 = VkKeyboard(one_time=True)
                    a2_6.add_button("0-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("1-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("2-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("3-b1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_6.get_keyboard())
                if '3-a5' in event.message.lower():
                    a1 = a1+3
                    text = 'Я хочу управлять машинами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_6 = VkKeyboard(one_time=True)
                    a2_6.add_button("0-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("1-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("2-b1", color=VkKeyboardColor.PRIMARY)
                    a2_6.add_line()
                    a2_6.add_button("3-b1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_6.get_keyboard())
                #6
                if '0-b1' in event.message.lower():
                    a2 = a2+0
                    text = 'Я хочу ремонтировать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_7 = VkKeyboard(one_time=True)
                    a2_7.add_button("0-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("1-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("2-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("3-b2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_7.get_keyboard())
                if '1-b1' in event.message.lower():
                    a2 = a2+1
                    text = 'Я хочу ремонтировать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_7 = VkKeyboard(one_time=True)
                    a2_7.add_button("0-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("1-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("2-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("3-b2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_7.get_keyboard())
                if '2-b1' in event.message.lower():
                    a2 = a2+2
                    text = 'Я хочу ремонтировать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_7 = VkKeyboard(one_time=True)
                    a2_7.add_button("0-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("1-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("2-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("3-b2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_7.get_keyboard())
                if '3-b1' in event.message.lower():
                    a2 = a2+3
                    text = 'Я хочу ремонтировать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_7 = VkKeyboard(one_time=True)
                    a2_7.add_button("0-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("1-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("2-b2", color=VkKeyboardColor.PRIMARY)
                    a2_7.add_line()
                    a2_7.add_button("3-b2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_7.get_keyboard())
                #7
                if '0-b2' in event.message.lower():
                    a2 = a2+0
                    text = 'Я хочу собирать и налаживать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_8 = VkKeyboard(one_time=True)
                    a2_8.add_button("0-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("1-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("2-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("3-b3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_8.get_keyboard())
                if '1-b2' in event.message.lower():
                    a2 = a2+1
                    text = 'Я хочу собирать и налаживать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_8 = VkKeyboard(one_time=True)
                    a2_8.add_button("0-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("1-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("2-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("3-b3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_8.get_keyboard())
                if '2-b2' in event.message.lower():
                    a2 = a2+2
                    text = 'Я хочу собирать и налаживать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_8 = VkKeyboard(one_time=True)
                    a2_8.add_button("0-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("1-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("2-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("3-b3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_8.get_keyboard())
                if '3-b2' in event.message.lower():
                    a2 = a2+3
                    text = 'Я хочу собирать и налаживать оборудывание \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_8 = VkKeyboard(one_time=True)
                    a2_8.add_button("0-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("1-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("2-b3", color=VkKeyboardColor.PRIMARY)
                    a2_8.add_line()
                    a2_8.add_button("3-b3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_8.get_keyboard())
                #8
                if '0-b3' in event.message.lower():
                    a2 = a2+0
                    text = 'Я хочу обрабатывать материалы, изготавливать предметы и вещи \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_9 = VkKeyboard(one_time=True)
                    a2_9.add_button("0-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("1-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("2-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("3-b4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_9.get_keyboard())
                if '1-b3' in event.message.lower():
                    a2 = a2+1
                    text = 'Я хочу обрабатывать материалы, изготавливать предметы и вещи \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_9 = VkKeyboard(one_time=True)
                    a2_9.add_button("0-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("1-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("2-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("3-b4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_9.get_keyboard())
                if '2-b3' in event.message.lower():
                    a2 = a2+2
                    text = 'Я хочу обрабатывать материалы, изготавливать предметы и вещи \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_9 = VkKeyboard(one_time=True)
                    a2_9.add_button("0-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("1-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("2-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("3-b4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_9.get_keyboard())
                if '3-b3' in event.message.lower():
                    a2 = a2+3
                    text = 'Я хочу обрабатывать материалы, изготавливать предметы и вещи \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_9 = VkKeyboard(one_time=True)
                    a2_9.add_button("0-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("1-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("2-b4", color=VkKeyboardColor.PRIMARY)
                    a2_9.add_line()
                    a2_9.add_button("3-b4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_9.get_keyboard())
                #9
                if '0-b4' in event.message.lower():
                    a2 = a2+0
                    text = 'Я хочу заниматься строительством \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_10 = VkKeyboard(one_time=True)
                    a2_10.add_button("0-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("1-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("2-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("3-b5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_10.get_keyboard())
                if '1-b4' in event.message.lower():
                    a2 = a2+1
                    text = 'Я хочу заниматься строительством \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_10 = VkKeyboard(one_time=True)
                    a2_10.add_button("0-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("1-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("2-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("3-b5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_10.get_keyboard())
                if '2-b4' in event.message.lower():
                    a2 = a2+2
                    text = 'Я хочу заниматься строительством \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_10 = VkKeyboard(one_time=True)
                    a2_10.add_button("0-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("1-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("2-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("3-b5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_10.get_keyboard())
                if '3-b4' in event.message.lower():
                    a2 = a2+3
                    text = 'Я хочу заниматься строительством \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a2_10 = VkKeyboard(one_time=True)
                    a2_10.add_button("0-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("1-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("2-b5", color=VkKeyboardColor.PRIMARY)
                    a2_10.add_line()
                    a2_10.add_button("3-b5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a2_10.get_keyboard())
                #10
                if '0-b5' in event.message.lower():
                    a2 = a2+0
                    text = 'Я хочу редактировать тексты и таблицы \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_11 = VkKeyboard(one_time=True)
                    a3_11.add_button("0-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("1-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("2-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("3-c1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_11.get_keyboard())
                if '1-b5' in event.message.lower():
                    a2 = a2+1
                    text = 'Я хочу редактировать тексты и таблицы \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_11 = VkKeyboard(one_time=True)
                    a3_11.add_button("0-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("1-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("2-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("3-c1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_11.get_keyboard())
                if '2-b5' in event.message.lower():
                    a2 = a2+2
                    text = 'Я хочу редактировать тексты и таблицы \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_11 = VkKeyboard(one_time=True)
                    a3_11.add_button("0-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("1-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("2-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("3-c1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_11.get_keyboard())
                if '3-b5' in event.message.lower():
                    a2 = a2+3
                    text = 'Я хочу редактировать тексты и таблицы \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_11 = VkKeyboard(one_time=True)
                    a3_11.add_button("0-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("1-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("2-c1", color=VkKeyboardColor.PRIMARY)
                    a3_11.add_line()
                    a3_11.add_button("3-c1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_11.get_keyboard())
                #11
                if '0-c1' in event.message.lower():
                    a3 = a3+0
                    text = 'Я хочу производить расчеты и вычисления \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_12 = VkKeyboard(one_time=True)
                    a3_12.add_button("0-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("1-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("2-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("3-c2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_12.get_keyboard())
                if '1-c1' in event.message.lower():
                    a3 = a3+1
                    text = 'Я хочу производить расчеты и вычисления \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_12 = VkKeyboard(one_time=True)
                    a3_12.add_button("0-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("1-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("2-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("3-c2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_12.get_keyboard())
                if '2-c1' in event.message.lower():
                    a3 = a3+2
                    text = 'Я хочу производить расчеты и вычисления \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_12 = VkKeyboard(one_time=True)
                    a3_12.add_button("0-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("1-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("2-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("3-c2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_12.get_keyboard())
                if '3-c1' in event.message.lower():
                    a3 = a3+3
                    text = 'Я хочу производить расчеты и вычисления \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_12 = VkKeyboard(one_time=True)
                    a3_12.add_button("0-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("1-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("2-c2", color=VkKeyboardColor.PRIMARY)
                    a3_12.add_line()
                    a3_12.add_button("3-c2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_12.get_keyboard())
                #12
                if '0-c2' in event.message.lower():
                    a3 = a3+0
                    text = 'Я хочу обрабатывать информацию \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_13 = VkKeyboard(one_time=True)
                    a3_13.add_button("0-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("1-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("2-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("3-c3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_13.get_keyboard())
                if '1-c2' in event.message.lower():
                    a3 = a3+1
                    text = 'Я хочу обрабатывать информацию \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_13 = VkKeyboard(one_time=True)
                    a3_13.add_button("0-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("1-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("2-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("3-c3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_13.get_keyboard())
                if '2-c2' in event.message.lower():
                    a3 = a3+2
                    text = 'Я хочу обрабатывать информацию \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_13 = VkKeyboard(one_time=True)
                    a3_13.add_button("0-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("1-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("2-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("3-c3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_13.get_keyboard())
                if '3-c2' in event.message.lower():
                    a3 = a3+3
                    text = 'Я хочу обрабатывать информацию \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_13 = VkKeyboard(one_time=True)
                    a3_13.add_button("0-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("1-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("2-c3", color=VkKeyboardColor.PRIMARY)
                    a3_13.add_line()
                    a3_13.add_button("3-c3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_13.get_keyboard())
                #13
                if '0-c3' in event.message.lower():
                    a3 = a3+0
                    text = 'Я хочу работать с чертежами, картами и схемами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_14 = VkKeyboard(one_time=True)
                    a3_14.add_button("0-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("1-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("2-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("3-c4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_14.get_keyboard())
                if '1-c3' in event.message.lower():
                    a3 = a3+1
                    text = 'Я хочу работать с чертежами, картами и схемами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_14 = VkKeyboard(one_time=True)
                    a3_14.add_button("0-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("1-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("2-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("3-c4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_14.get_keyboard())
                if '2-c3' in event.message.lower():
                    a3 = a3+2
                    text = 'Я хочу работать с чертежами, картами и схемами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_14 = VkKeyboard(one_time=True)
                    a3_14.add_button("0-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("1-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("2-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("3-c4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_14.get_keyboard())
                if '3-c3' in event.message.lower():
                    a3 = a3+3
                    text = 'Я хочу работать с чертежами, картами и схемами \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_14 = VkKeyboard(one_time=True)
                    a3_14.add_button("0-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("1-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("2-c4", color=VkKeyboardColor.PRIMARY)
                    a3_14.add_line()
                    a3_14.add_button("3-c4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_14.get_keyboard())
                #14
                if '0-c4' in event.message.lower():
                    a3 = a3+0
                    text = 'Я хочу принимать и передавать сигналы и сообщения \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_15 = VkKeyboard(one_time=True)
                    a3_15.add_button("0-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("1-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("2-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("3-c5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_15.get_keyboard())
                if '1-c4' in event.message.lower():
                    a3 = a3+1
                    text = 'Я хочу принимать и передавать сигналы и сообщения \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_15 = VkKeyboard(one_time=True)
                    a3_15.add_button("0-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("1-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("2-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("3-c5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_15.get_keyboard())
                if '2-c4' in event.message.lower():
                    a3 = a3+2
                    text = 'Я хочу принимать и передавать сигналы и сообщения \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_15 = VkKeyboard(one_time=True)
                    a3_15.add_button("0-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("1-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("2-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("3-c5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_15.get_keyboard())
                if '3-c4' in event.message.lower():
                    a3 = a3+3
                    text = 'Я хочу принимать и передавать сигналы и сообщения \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a3_15 = VkKeyboard(one_time=True)
                    a3_15.add_button("0-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("1-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("2-c5", color=VkKeyboardColor.PRIMARY)
                    a3_15.add_line()
                    a3_15.add_button("3-c5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a3_15.get_keyboard())
                #15
                if '0-c5' in event.message.lower():
                    a3 = a3+0
                    text = 'Я хочу заниматься художественным оформлением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_16 = VkKeyboard(one_time=True)
                    a4_16.add_button("0-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("1-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("2-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("3-d1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_16.get_keyboard())
                if '1-c5' in event.message.lower():
                    a3 = a3+1
                    text = 'Я хочу заниматься художественным оформлением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_16 = VkKeyboard(one_time=True)
                    a4_16.add_button("0-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("1-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("2-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("3-d1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_16.get_keyboard())
                if '2-c5' in event.message.lower():
                    a3 = a3+2
                    text = 'Я хочу заниматься художественным оформлением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_16 = VkKeyboard(one_time=True)
                    a4_16.add_button("0-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("1-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("2-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("3-d1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_16.get_keyboard())
                if '3-c5' in event.message.lower():
                    a3 = a3+3
                    text = 'Я хочу заниматься художественным оформлением \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_16 = VkKeyboard(one_time=True)
                    a4_16.add_button("0-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("1-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("2-d1", color=VkKeyboardColor.PRIMARY)
                    a4_16.add_line()
                    a4_16.add_button("3-d1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_16.get_keyboard())
                #16
                if '0-d1' in event.message.lower():
                    a4 = a4+0
                    text = 'Я хочу рисовать, фотографировать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_17 = VkKeyboard(one_time=True)
                    a4_17.add_button("0-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("1-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("2-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("3-d2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_17.get_keyboard())
                if '1-d1' in event.message.lower():
                    a4 = a4+1
                    text = 'Я хочу рисовать, фотографировать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_17 = VkKeyboard(one_time=True)
                    a4_17.add_button("0-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("1-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("2-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("3-d2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_17.get_keyboard())
                if '2-d1' in event.message.lower():
                    a4 = a4+2
                    text = 'Я хочу рисовать, фотографировать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_17 = VkKeyboard(one_time=True)
                    a4_17.add_button("0-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("1-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("2-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("3-d2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_17.get_keyboard())
                if '3-d1' in event.message.lower():
                    a4 = a4+3
                    text = 'Я хочу рисовать, фотографировать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_17 = VkKeyboard(one_time=True)
                    a4_17.add_button("0-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("1-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("2-d2", color=VkKeyboardColor.PRIMARY)
                    a4_17.add_line()
                    a4_17.add_button("3-d2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_17.get_keyboard())
                #17
                if '0-d2' in event.message.lower():
                    a4 = a4+0
                    text = 'Я хочу создавать произведения искусства \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_18 = VkKeyboard(one_time=True)
                    a4_18.add_button("0-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("1-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("2-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("3-d3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_18.get_keyboard())
                if '1-d2' in event.message.lower():
                    a4 = a4+1
                    text = 'Я хочу создавать произведения искусства \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_18 = VkKeyboard(one_time=True)
                    a4_18.add_button("0-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("1-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("2-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("3-d3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_18.get_keyboard())
                if '2-d2' in event.message.lower():
                    a4 = a4+2
                    text = 'Я хочу создавать произведения искусства \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_18 = VkKeyboard(one_time=True)
                    a4_18.add_button("0-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("1-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("2-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("3-d3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_18.get_keyboard())
                if '3-d2' in event.message.lower():
                    a4 = a4+3
                    text = 'Я хочу создавать произведения искусства \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_18 = VkKeyboard(one_time=True)
                    a4_18.add_button("0-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("1-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("2-d3", color=VkKeyboardColor.PRIMARY)
                    a4_18.add_line()
                    a4_18.add_button("3-d3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_18.get_keyboard())
                #18
                if '0-d3' in event.message.lower():
                    a4 = a4+0
                    text = 'Я хочу выступать на сцене \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_19 = VkKeyboard(one_time=True)
                    a4_19.add_button("0-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("1-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("2-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("3-d4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_19.get_keyboard())
                if '1-d3' in event.message.lower():
                    a4 = a4+1
                    text = 'Я хочу выступать на сцене \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_19 = VkKeyboard(one_time=True)
                    a4_19.add_button("0-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("1-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("2-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("3-d4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_19.get_keyboard())
                if '2-d3' in event.message.lower():
                    a4 = a4+2
                    text = 'Я хочу выступать на сцене \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_19 = VkKeyboard(one_time=True)
                    a4_19.add_button("0-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("1-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("2-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("3-d4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_19.get_keyboard())
                if '3-d3' in event.message.lower():
                    a4 = a4+3
                    text = 'Я хочу выступать на сцене \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_19 = VkKeyboard(one_time=True)
                    a4_19.add_button("0-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("1-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("2-d4", color=VkKeyboardColor.PRIMARY)
                    a4_19.add_line()
                    a4_19.add_button("3-d4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_19.get_keyboard())
                #19
                if '0-d4' in event.message.lower():
                    a4 = a4+0
                    text = 'Я хочу шить, вышивать, вязать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_20 = VkKeyboard(one_time=True)
                    a4_20.add_button("0-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("1-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("2-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("3-d5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_20.get_keyboard())
                if '1-d4' in event.message.lower():
                    a4 = a4+1
                    text = 'Я хочу шить, вышивать, вязать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_20 = VkKeyboard(one_time=True)
                    a4_20.add_button("0-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("1-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("2-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("3-d5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_20.get_keyboard())
                if '2-d4' in event.message.lower():
                    a4 = a4+2
                    text = 'Я хочу шить, вышивать, вязать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_20 = VkKeyboard(one_time=True)
                    a4_20.add_button("0-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("1-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("2-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("3-d5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_20.get_keyboard())
                if '3-d4' in event.message.lower():
                    a4 = a4+3
                    text = 'Я хочу шить, вышивать, вязать \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a4_20 = VkKeyboard(one_time=True)
                    a4_20.add_button("0-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("1-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("2-d5", color=VkKeyboardColor.PRIMARY)
                    a4_20.add_line()
                    a4_20.add_button("3-d5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a4_20.get_keyboard())
                #20
                if '0-d5' in event.message.lower():
                    a4 = a4+0
                    text = 'Я хочу ухаживать за животными \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_21 = VkKeyboard(one_time=True)
                    a5_21.add_button("0-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("1-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("2-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("3-e1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_21.get_keyboard())
                if '1-d5' in event.message.lower():
                    a4 = a4+1
                    text = 'Я хочу ухаживать за животными \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_21 = VkKeyboard(one_time=True)
                    a5_21.add_button("0-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("1-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("2-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("3-e1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_21.get_keyboard())
                if '2-d5' in event.message.lower():
                    a4 = a4+2
                    text = 'Я хочу ухаживать за животными \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_21 = VkKeyboard(one_time=True)
                    a5_21.add_button("0-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("1-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("2-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("3-e1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_21.get_keyboard())
                if '3-d5' in event.message.lower():
                    a4 = a4+3
                    text = 'Я хочу ухаживать за животными \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_21 = VkKeyboard(one_time=True)
                    a5_21.add_button("0-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("1-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("2-e1", color=VkKeyboardColor.PRIMARY)
                    a5_21.add_line()
                    a5_21.add_button("3-e1", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_21.get_keyboard())
                #21
                if '0-e1' in event.message.lower():
                    a5 = a5+0
                    text = 'Я хочу разводить растения или животных \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_22 = VkKeyboard(one_time=True)
                    a5_22.add_button("0-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("1-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("2-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("3-e2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_22.get_keyboard())
                if '1-e1' in event.message.lower():
                    a5 = a5+1
                    text = 'Я хочу разводить растения или животных \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_22 = VkKeyboard(one_time=True)
                    a5_22.add_button("0-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("1-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("2-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("3-e2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_22.get_keyboard())
                if '2-e1' in event.message.lower():
                    a5 = a5+2
                    text = 'Я хочу разводить растения или животных \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_22 = VkKeyboard(one_time=True)
                    a5_22.add_button("0-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("1-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("2-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("3-e2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_22.get_keyboard())
                if '3-e1' in event.message.lower():
                    a5 = a5+3
                    text = 'Я хочу разводить растения или животных \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_22 = VkKeyboard(one_time=True)
                    a5_22.add_button("0-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("1-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("2-e2", color=VkKeyboardColor.PRIMARY)
                    a5_22.add_line()
                    a5_22.add_button("3-e2", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_22.get_keyboard())
                #22
                if '0-e2' in event.message.lower():
                    a5 = a5+0
                    text = 'Я хочу работать на открытом воздухе \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_23 = VkKeyboard(one_time=True)
                    a5_23.add_button("0-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("1-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("2-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("3-e3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_23.get_keyboard())
                if '1-e2' in event.message.lower():
                    a5 = a5+1
                    text = 'Я хочу работать на открытом воздухе \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_23 = VkKeyboard(one_time=True)
                    a5_23.add_button("0-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("1-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("2-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("3-e3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_23.get_keyboard())
                if '2-e2' in event.message.lower():
                    a5 = a5+2
                    text = 'Я хочу работать на открытом воздухе \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_23 = VkKeyboard(one_time=True)
                    a5_23.add_button("0-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("1-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("2-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("3-e3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_23.get_keyboard())
                if '3-e2' in event.message.lower():
                    a5 = a5+3
                    text = 'Я хочу работать на открытом воздухе \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_23 = VkKeyboard(one_time=True)
                    a5_23.add_button("0-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("1-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("2-e3", color=VkKeyboardColor.PRIMARY)
                    a5_23.add_line()
                    a5_23.add_button("3-e3", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_23.get_keyboard())
                #23
                if '0-e3' in event.message.lower():
                    a5 = a5+0
                    text = 'Я хочу ориентироваться в природных явлениях \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_24 = VkKeyboard(one_time=True)
                    a5_24.add_button("0-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("1-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("2-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("3-e4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_24.get_keyboard())
                if '1-e3' in event.message.lower():
                    a5 = a5+1
                    text = 'Я хочу ориентироваться в природных явлениях \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_24 = VkKeyboard(one_time=True)
                    a5_24.add_button("0-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("1-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("2-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("3-e4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_24.get_keyboard())
                if '2-e3' in event.message.lower():
                    a5 = a5+2
                    text = 'Я хочу ориентироваться в природных явлениях \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_24 = VkKeyboard(one_time=True)
                    a5_24.add_button("0-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("1-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("2-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("3-e4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_24.get_keyboard())
                if '3-e3' in event.message.lower():
                    a5 = a5+3
                    text = 'Я хочу ориентироваться в природных явлениях \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_24 = VkKeyboard(one_time=True)
                    a5_24.add_button("0-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("1-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("2-e4", color=VkKeyboardColor.PRIMARY)
                    a5_24.add_line()
                    a5_24.add_button("3-e4", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_24.get_keyboard())
                #24
                if '0-e4' in event.message.lower():
                    a5 = a5+0
                    text = 'Я хочу работать на земле \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_25 = VkKeyboard(one_time=True)
                    a5_25.add_button("0-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("1-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("2-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("3-e5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_25.get_keyboard())
                if '1-e4' in event.message.lower():
                    a5 = a5+1
                    text = 'Я хочу работать на земле \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_25 = VkKeyboard(one_time=True)
                    a5_25.add_button("0-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("1-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("2-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("3-e5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_25.get_keyboard())
                if '2-e4' in event.message.lower():
                    a5 = a5+2
                    text = 'Я хочу работать на земле \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_25 = VkKeyboard(one_time=True)
                    a5_25.add_button("0-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("1-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("2-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("3-e5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_25.get_keyboard())
                if '3-e4' in event.message.lower():
                    a5 = a5+3
                    text = 'Я хочу работать на земле \n 0 – вовсе нет, 1 – пожалуй, так, 2 – верно, 3 – совершенно верно'
                    a5_25 = VkKeyboard(one_time=True)
                    a5_25.add_button("0-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("1-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("2-e5", color=VkKeyboardColor.PRIMARY)
                    a5_25.add_line()
                    a5_25.add_button("3-e5", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a5_25.get_keyboard())
                #the and
                if '0-e5' in event.message.lower():
                    a7 = a7+0
                    text = 'вы прошли тест!!! \n чтобы завершить тест и просматреть результаты нажмите на кнопку <<завершить тест>>'
                    a7_100 = VkKeyboard(one_time=True)
                    a7_100.add_button("завершить тест", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a7_100.get_keyboard())
                if '1-e5' in event.message.lower():
                    a7 = a7+1
                    text = 'вы прошли тест!!! \n чтобы завершить тест и просматреть результаты нажмите на кнопку <<завершить тест>>'
                    a7_100 = VkKeyboard(one_time=True)
                    a7_100.add_button("завершить тест", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a7_100.get_keyboard())
                if '2-e5' in event.message.lower():
                    a7 = a7+2
                    text = 'вы прошли тест!!! \n чтобы завершить тест и просматреть результаты нажмите на кнопку <<завершить тест>>'
                    a7_100 = VkKeyboard(one_time=True)
                    a7_100.add_button("завершить тест", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a7_100.get_keyboard())
                if '3-e5' in event.message.lower():
                    a7 = a7+3
                    text = 'вы прошли тест!!! \n чтобы завершить тест и просмотреть результаты нажмите на кнопку <<завершить тест>>'
                    a7_100 = VkKeyboard(one_time=True)
                    a7_100.add_button("завершить тест", color=VkKeyboardColor.PRIMARY)
                    self.send_message(event.user_id, text, a7_100.get_keyboard())

                ###
                if 'завершить тест' in event.message.lower():
                    print(a1)
                    print(a2)
                    print(a3)
                    print(a4)
                    print(a5)
                    if a1 > a2 and a1 > a3 and a1 > a4 and a1 > a5 and a1 > a6 and a1 > a7:
                        text = "Вам больше подходит направление: Человек – человек. Эти профессии направлены на работу с людьми. К ним относятся: учителя, врачи, журналисты, парикмахеры и др."
                        self.send_message(event.user_id, text)
                    elif a2 > a1 and a2 > a3 and a2 > a4 and a2 > a5 and a2 > a6 and a2 > a7:
                        text = "Вам больше пожходит направление: Человек – техника. Представители данного типа профессий имеют непосредственное отношение к технике. Например, механики, технологи, инженеры, сантехники, мастера по ремонту стиральных машин и др."
                        self.send_message(event.user_id, text)
                    elif a3 > a1 and a3 > a2 and a3 > a4 and a3 > a5 and a3 > a6 and a3 > a7:
                        text = "Вам больше пожходит направление: Человек – информация. Речь идёт о людях, работающих со знаковыми системами (цифрами, кодами, буквами и прочими символами). В данную категорию входят программисты, бухгалтеры, финансисты, аналитики и др."
                        self.send_message(event.user_id, text)
                    elif a4 > a1 and a4 > a2 and a4 > a3 and a4 > a5 and a4 > a6 and a4 > a7:
                        text = "Вам больше пожходит направление: Человек – художественный образ. В эту группу входят различные творческие профессии, такие как художник, актёр, певец, композитор, режиссер и др."
                        self.send_message(event.user_id, text)
                    elif a5 > a1 and a5 > a2 and a5 > a3 and a5 > a4 and a5 > a6 and a5 > a7:
                        text = "Вам больше пожходит направление: Человек – природа. Здесь речь идёт о тех профессиях, представители которых связаны с природой. Это могут быть егеря, садовники, агрономы, экологи и др."
                        self.send_message(event.user_id, text)
                    
    def send_message(self,user_id, message, keyboard=None):
        print("1")
        if keyboard == None:
            keyboard = '{"buttons": [], "one_time": true}' #пустая клава кнопок нет
        self.vk.messages.send(peer_id=user_id,random_id = get_random_id(),keyboard = keyboard, message = message)

if '__main__'==__name__:
    bot = Bot()
    bot.start()
