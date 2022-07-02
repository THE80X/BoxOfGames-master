import json
from datetime import datetime
import vk_api
import pyrebase
import os
import time
import sqlite3

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token, group_token, name_by_id, vk_admin_permission


vk_session = vk_api.VkApi(token=main_token)
longpoll = VkBotLongPoll(vk_session, group_token)

# longpoll = VkLongPoll(vk_session)
# цифирки отвечают за id группы

con = {
    "apiKey": "AIzaSyBlYQaKQbbVCKnSYjovcE5YjbNNB2e9eic",
    "authDomain": "roleplaychecker.firebaseapp.com",
    "databaseURL": "https://roleplaychecker-default-rtdb.firebaseio.com",
    "projectId": "roleplaychecker",
    "storageBucket": "roleplaychecker.appspot.com",
    "messagingSenderId": "366565363251",
    "appId": "1:366565363251:web:dabd05d9a4db73ed2e9d46",
    "measurementId": "G-2EZM6Q1BT0"
}
firebase = pyrebase.initialize_app(con)
database = firebase.database()

spec_symbol = '"'

counter_messages = 0


def make_camp(msg, msg_id_sender, id, hero_name):
    sender(id, hero_name + " разбил лагерь")


def take_a_rest(msg, msg_id_sender, id, hero_name):
    sender(id, hero_name + " отдыхает")


def using_item(msg, msg_id_sender, id, hero_name, item_name, item_target):
    s = ''
    hero_name_for_check = (hero_name.replace(' ', '')).lower()
    item_target_for_check = (item_target.replace(' ', '')).lower()
    counter_comma = item_target.count(',')
    if (hero_name_for_check != item_target_for_check):
        if counter_comma == 0:
            sender(id, hero_name + " использует " + item_name + " на" + item_target)
        else:
            for i in range(counter_comma + 1):
                person_target = item_target.split(',')
                if person_target[i][0:1] == ' ':
                    person_target[i] = person_target[i][1:]
                    print(person_target[i])
                    if counter_comma > i:
                        if person_target[i] == hero_name:
                            s = s + "на себе,"
                        else:
                            s = s + " на " + person_target[i] + ','
                    else:
                        if person_target[i] == hero_name:
                            s = s + "на себе"
                        else:
                            s = s + " на " + person_target[i]
            sender(id, hero_name + " использует " + item_name + ' ' + s)
    if (hero_name_for_check == item_target_for_check):
        sender(id, hero_name + " использует " + item_name + " на себе")


# абилити надо будет тоже обязательно поправить

def using_ability(msg, msg_id_sender, id, hero_name, ability_name, ability_target):
    hero_name_for_check = (hero_name.replace(' ', '')).lower()
    ability_target_for_check = (ability_target.replace(' ', '')).lower()

    if (hero_name_for_check != ability_target_for_check):
        sender(id, hero_name + " использует " + ability_name + " на" + ability_target)

    if (hero_name_for_check == ability_target_for_check):
        sender(id, hero_name + " использует " + ability_name + " на себе")


def end_of_the_journey(msg, msg_id_sender, id, hero_name, target):
    hero_name_for_check = (hero_name.replace(' ', '')).lower()
    target_for_check = (target.replace(' ', '')).lower()

    if (hero_name_for_check != target_for_check):
        sender(id, hero_name + " закончил путешествие " + target + ". " + '"' + "Cпи спокойно друг мой" + '"')

    if (hero_name_for_check == target_for_check):
        sender(id,
               hero_name + " закончил своё путешествие. " + spec_symbol + "Конец неминуем, и ты отдохнёшь" + spec_symbol)


def add_item_in_inventory(msg, msg_id_sender, id, hero_name, target, list_of_items):
    print(hero_name)
    print(target)
    hero_name_for_check = (hero_name.replace(' ', '')).lower()
    target_for_check = (target.replace(' ', '')).lower()
    if (hero_name_for_check != target_for_check):
        s = ''
        counter_comma = list_of_items.count(',') + 1
        if list_of_items.count(',') != 0:
            items = list_of_items.split(',')
            for i in range(counter_comma):
                item = items[i].replace(' ', '')
                counter_dash = items[i].count('-')
                if counter_dash > 0:
                    dash_position = int(str(item).find('-'))
                    print("dash_position: " + str(dash_position))
                    print(str(item)[:dash_position])
                    if (str(item)[:dash_position]).isdigit():
                        amount = int(str(item)[:dash_position])
                        print("amount: " + str(amount))
                        item_name = str(items[i])[(str(items[i]).find('-')) + 1:]
                        if counter_comma >= i:
                            s = s + str(amount) + ' ' + item_name + '\n'
                        else:
                            s = s + str(amount) + ' ' + item_name
                else:
                    if counter_comma >= i:
                        s = s + str(items[i]) + '\n'
                    else:
                        s = s + str(items[i])

        if list_of_items.count(',') == 0:
            print(list_of_items.count(','))
            item = list_of_items.replace(' ', '')
            counter_dash = item.count('-')

            if counter_dash > 0:
                print("counter_dash: " + str(counter_dash))
                dash_position = int(str(item).find('-'))
                print("dash_position: " + str(dash_position))
                if str(item)[:dash_position].isdigit():
                    amount = int(str(item)[:(str(item).find('-'))])
                    item_name = str(list_of_items)[(str(list_of_items).find('-')) + 1:]
                    print(amount)
                    s = s + str(amount) + ' ' + item_name
                else:
                    sender(id, "У вас ошибка в колличестве предметов, исправьтесь!")
            else:
                s = s + str(item)
        sender(id, hero_name + " наградил " + target + " предеметами:" + '\n' + s)
    else:
        sender(id, "А зачем самому себе предметы передавать?")


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})
    counter_some = vk_session.method('messages.getHistory',
                                     {'count': 1, 'peer_id': '-' + group_token, 'group_id': group_token})
    print(counter_some)


def admin_check(vk_admin_permission, msg_id_sender):
    x = False
    for i in vk_admin_permission:
        # print(i)
        if int(i) == msg_id_sender:
            x = True
    # print(x)
    return x


def replacer(msg):
    msg = msg.replace('“', '"')
    msg = msg.replace('”', '"')
    msg = msg.replace('«', '"')
    msg = msg.replace('»', '"')
    msg = msg.replace('–', '-')
    return msg


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            msg = event.object.message['text']
            replacer(msg)
            msg_all_info = event.message
            msg_id = event.object.message['conversation_message_id']  # айдишник сообщения в чатах, где пребывает бот
            msg_id_sender = event.object.message['from_id']  # айдишник отправителя сообщений, где пребывает бот
            id = event.chat_id  # айдишник чата
            msg_time_send = datetime.now()
            user = vk_session.method('users.get', {'user_ids': msg_id_sender, 'name_case': 'nom'})
            msg_fullname_sender = user[0]['first_name'] + ' ' + user[0]['last_name']
            counter = msg.count('|')

            # data = {"Name": msg_fullname_sender}
            # database.push(data)
            data = {"Message": msg, "Data": str(msg_time_send), "Message_id": msg_id}
            """
                hero = {"NAME": hero_name,
                        "RACE": {
                            "POINTS":
                            {
                                "START_POINTS":{},
                                "FINISH_POINTS":{}
                            },
                            "START_RESISTANCES": {},
                            "START_PERMISSIONS": {},
                            "EQIUP_SLOT_START": {},
                        },
                        "PERSON_INFO":
                        {
                            "POINTS":{
                                "SUMMARY_POINTS":{},
                                "POINTS_BY_LVL":{}
                            },
                            "KNOWLEDGES":
                                {
                                "MAGIC_KNOWLEDGE":{},
                                "WEAPON KNOWLEDGE":{}
                                },
                            "BARS":
                                {
                                    "MAX_BARS": {},
                                    "NOW_BARS": {}
                                },
                            "STATUSES":{},
                            "RESISTANCES_NOW":{},
                            "EQUIP_SLOT":{
                                "EQUIP_SLOT_SUM": {},
                                "EQUIP_SLOT_NOW": {}
                            },
                            "PERSON_LVL":{}
                        },
                        "INVENTORY":
                            {"Things":
                                {
                                "POINTS_NEED_TO":
                                    {
                                    "POINTS_TO_USE_THING": {},
                                    "POINTS_TO_MAKE_THING": {}
                                    },
                                "POINTS_GIVES":
                                    {
                                    "GIVES_PASSIVE": {},
                                    "GIVES_ACTIVE": {}
                                    },
                                "GIVE_RESISTANCES_THING":
                                    {
                                    "PASSIVE_RESISTANCE_THING": {},
                                    "ACTIVE_RESISTANCE_THING": {}
                                    },
                                "ACCESS_USE_TO":
                                    {
                                    "MAGIC_USE_TO": {},
                                    "WEAPON_USE_TO": {}
                                    },
                                "GIVE_PERMISSIONS":
                                    {
                                    "MAGIC_ACTIVE_GIVES": {},
                                    "MAGIC_PASSIVE_GIVES": {},
                                    "WEAPON_ACTIVE_GIVES": {},
                                    "WEAPON_PASSIVE_GIVES": {}
                                    },
                                "MAX_BARS":
                                    {
                                    "ACTIVE_MAX_BARS":{},
                                    "PASSIVE_MAX_BARS":{}
                                    },
                                "NOW_BARS":
                                    {
                                    "ACTIVE_NOW_BARS":{},
                                    "PASSIVE_NOW_BARS":{}
                                    },
                                "EQUIP_SLOT_GIVES":
                                    {
                                    "EQUIP_SLOT_ACTIVE":{},
                                    "EQUIP_SLOT_PASSIVE":{}
                                    },
                                "EQUIP_SLOT_USE_TO":{},
                                "THING_STATUSES":{},
                                "DAMAGE_TYPE":
                                    {
                                    "DAMAGE_ACTIVE":{},
                                    "DAMAGE_PASSIVE":{}
                                    },
                                "COST":{},
                                "ITEM_NEED_TO":
                                    {
                                    "ACTIVE":{},
                                    "PASSIVE":{}
                                    }
                                },
                            "Consumables":
                                {
                                "NEED_TO_MAKE_ITEM":
                                    {
                                    "POINTS_TO_MAKE_ITEM":{},
                                    "KNOWLEDGE_TO_MAKE_ITEM":{}
                                    },
                                "GIVES_ACTIVE":{},
                                "ACTIVE_RESISTANCE":{},
                                "MAGIC_ACTIVE_GIVES":{},
                                "WEAPON_ACTIVE_GIVES":{},
                                "ACTIVE_MAX_BARS":{},
                                "ACTIVE_NOW_BARS":{},
                                "CONSUMABLE_STATUSES":{},
                                "DAMAGE_ACTIVE":{},
                                "COST":{},
                                "ACTIVE":{}
                                },
                            "Coins":{}
                            },
                        "SPELLS_ABILITIES":
                            {
                            "POINTS_TO_USE_SPELLS_ABILITIES":{},
                            "GIVES_SPELLS_ABILITIES":{},
                            "ACTIVE_RESISTANCE_SPELLS_ABILITIES":{},
                            "USE_TO":
                                {
                                "MAGIC_USE_TO":{},
                                "WEAPON_USE_TO":{}
                                },
                            "BARS":
                                {
                                "MAX_BARS":{},
                                "NOW_BARS":{}
                                },
                            "STATUSES":{},
                            "DAMAGE_TYPE":{},
                            "ANOTHER_REQUEST":{},
                            "LIFE_STATUS":{}
                            }
                        }
                """
            if not database.child("Players").child(msg_fullname_sender).child("id").shallow().get().val():
                database.child("Players").child(msg_fullname_sender).set({"id": msg_id_sender})
            database.child("Players").child(msg_fullname_sender).child('chats').child(name_by_id[id]).push(data)

            print('\n' + "сообщение: " + msg)
            print("кол-во палок: " + str(counter))
            print("кол-во черток: " + str(msg.count(spec_symbol)))
            print("кол-во обращений к людям: " + str(msg.count("[")))
            print("id сообщения: " + str(msg_id))
            print("id беседы: " + str(id))
            print("Название беседы: " + str(name_by_id[id]))
            print("id собеседника: " + str(msg_id_sender))
            print("имя и фамилия собеседника: " + str(msg_fullname_sender))
            print("Время отправки сообщения: " + str(msg_time_send))

            if id == 3:
                if msg.count('|') >= 2:
                    massive = msg.split('|')
                    person_name = massive[1]
                    if os.path.exists("персонажи/посты/" + person_name.lower() + ".rtf"):
                        f = open("персонажи/посты/" + person_name.lower() + ".rtf", 'r')
                        text_old = f.read()
                        f.close()
                        f = open("персонажи/посты/" + person_name.lower() + ".rtf", 'w')
                        print("Старое текст: " + text_old)
                        f.write(text_old + msg + '\n')
                        f.close()
                    else:
                        vk_session.method('messages.delete',
                                          {'spam': 0, 'delete_for_all': 1, 'peer_id': 2000000000 + id, 'cmids': msg_id})
                else:
                    vk_session.method('messages.delete',
                                      {'spam': 0, 'delete_for_all': 1, 'peer_id': 2000000000 + id, 'cmids': msg_id})

            if id == 1:
                if ((msg.count('|') - msg.count("["))) == 4:
                    massive = msg.split("|")
                    if massive[0] == "!Имя ":
                        name_old = massive[1].lower()
                        name_new = massive[3].lower()
                        if os.path.exists("персонажи/посты/" + name_old + ".rtf"):
                            f = open("персонажи/посты/" + name_old + ".rtf")
                            Owner_line = f.readline()
                            Owner_data = Owner_line.split("|")
                            Owner = Owner_data[1]
                            print("Владелец: " + Owner)
                            f.close()
                            if (int(Owner) == int(msg_id_sender)):
                                f_old = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Посты", name_old + ".rtf")
                                f_new = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Посты", name_new + ".rtf")
                                os.rename(f_old, f_new)
                                f_old = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Владельцы", name_old + ".rtf")
                                f_new = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Владельцы", name_new + ".rtf")
                                os.rename(f_old, f_new)
                                f_old = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Инвентарь", name_old + ".rtf")
                                f_new = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Инвентарь", name_new + ".rtf")
                                os.rename(f_old, f_new)
                                f_old = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Статистики", name_old + ".rtf")
                                f_new = os.path.join("D:\\Pythonchick\\Bot\\Персонажи\\Статистики", name_new + ".rtf")
                                os.rename(f_old, f_new)
                                sender(id, "Имя персонажа было успешно изменено")
                            else:
                                sender(id, "У вас нет такого персонажа")
                        else:
                            sender(id, "Нет такого персонажа")
                            print("Старое имя: " + name_old)

                # if (((msg.count('|') - msg.count("["))) == 2) | msg.count(spec_symbol) == 0:
                if (((msg.count('|') - msg.count("["))) == 2):
                    massive = msg.split("|")
                    print(massive[0])
                    print(massive[1])
                    # Бан
                    if ((massive[0] == "!Смерть ") or (massive[0] == "!Казнь ")):
                        if admin_check(vk_admin_permission, msg_id_sender):
                            # print("ВРЕМЯ УБИВАТЬ!")
                            # vk_session.method('messages.delete', {'spam': 0, 'delete_for_all': 1, 'peer_id': 2000000000 + id, 'cmids': msg_id})
                            sender(id, "Казнил " + massive[1])
                    # Создание персонажа в списках
                    if ((massive[0] == "!Создать ") or (massive[0] == "!создать ")):
                        if admin_check(vk_admin_permission, msg_id_sender):
                            massive[1] = massive[1].lower()
                            print("создаётся " + str(massive[1]))
                            my_file = open("Персонажи/Посты/" + str(massive[1]) + ".txt", "w+")
                            my_file.close()
                            my_file = open("Персонажи/Инвентарь/" + str(massive[1]) + ".txt", "w+")
                            my_file.write("|Артефакты|" + "\n\n" + "|Расходники|")
                            my_file.close()
                            my_file = open("Персонажи/Владельцы/" + str(massive[1]) + ".txt", "w+")
                            my_file.write("|Владельцы|" + str(massive[2]) + "\n" + "|Совладельцы|" + str(massive[2]))
                            my_file.close()
                            my_file = open("Персонажи/Статистики/" + str(massive[1]) + ".txt", "w+")
                            my_file.write(
                                "НРИ СТАТУС|0" + "\n" + "Статистики|SP|MP|IP|PP|AP|FP|LP|CP|BP" + "\n" + "Здоровье|0" + "\n" + "Рассудок|0" + "\n" + "Стамина|0" + "\n" + "Мана|0" + "\n" + "Локация|" + "\n" + "Статус боя|0" + "\n" + "Репутация|0")
                            my_file.close()
                    # то что ниже потом перенести в перечень команд на ролевой

                if ((msg.count('|') - msg.count("["))) == 3:
                    massive = msg.split("|")
                    if (massive[0] == "!Добавить " or massive[0] == "!добавить ") & (str(massive[1]).lower() != '') & (
                            str(massive[2]).lower() != ''):
                        hero_name = massive[1]
                        race_name = massive[2]
                        with open("Races/" + race_name.lower() + ".json", "r", encoding='utf-8') as json_file:
                            a = json.load(json_file)
                            print(a["RACE_NAME"])
                            health = round(
                                (25 * (int(a["POINTS"]["START_POINTS"]["SP_START"]) * 0.2 +
                                       int(a["POINTS"]["START_POINTS"]["IP_START"]) * 0.2 +
                                       int(a["POINTS"]["START_POINTS"]["PP_START"]) * 0.5 +
                                       int(a["POINTS"]["START_POINTS"]["AP_START"]) * 0.4 +
                                       int(a["POINTS"]["START_POINTS"]["BT_START"]) * 0.4 +
                                       int(a["PERMISSIONS"]["BLEED_ACCESS_START"]) * 0.1 +
                                       int(a["PERMISSIONS"]["NATURE_ACCESS_START"]) * 0.1 +
                                       int(a["PERMISSIONS"][
                                               "MENTAL_ACCESS_START"]) * 0.1) ** 1.5), 0)
                            mind_health = round(
                                (10 * (int(a["POINTS"]["START_POINTS"]["IP_START"]) * 0.4 +
                                       int(a["POINTS"]["START_POINTS"]["FP_START"]) * 0.3 +
                                       int(a["POINTS"]["START_POINTS"]["BT_START"]) * 0.5 +
                                       int(a["PERMISSIONS"]["MENTAL_ACCESS_START"]) * 0.1 -
                                       abs((int(a["PERMISSIONS"]["HOLY_ACCESS_START"]) -
                                            int(a["PERMISSIONS"][
                                                    "CURSE_ACCESS_START"])) * 0.1)) ** 1.2), 0)
                            stamina = round(
                                (15 * (int(a["POINTS"]["START_POINTS"]["SP_START"]) * 0.5 +
                                       int(a["POINTS"]["START_POINTS"]["MP_START"]) * 0.4 +
                                       int(a["POINTS"]["START_POINTS"]["PP_START"]) * 0.2 +
                                       int(a["POINTS"]["START_POINTS"]["AP_START"]) * 0.4 +
                                       int(a["PERMISSIONS"]["BLEED_ACCESS_START"]) * 0.1
                                       ) ** 1.2), 0)
                            weight = round(
                                (5 * (int(a["POINTS"]["START_POINTS"]["SP_START"]) * 0.4 +
                                      int(a["POINTS"]["START_POINTS"]["PP_START"]) * 0.5 +
                                      int(a["POINTS"]["START_POINTS"]["AP_START"]) * 0.2
                                      ) ** 1.05), 0)
                            mana = round(
                                (15 * (int(a["POINTS"]["START_POINTS"]["MP_START"]) * 0.5 +
                                       int(a["POINTS"]["START_POINTS"]["IP_START"]) * 0.4 +
                                       int(a["POINTS"]["START_POINTS"]["FP_START"]) * 0.2 +
                                       int(a["PERMISSIONS"]["MENTAL_ACCESS_START"]) * 0.1 +
                                       abs((int(a["PERMISSIONS"]["HOLY_ACCESS_START"]) -
                                            int(a["PERMISSIONS"][
                                                    "CURSE_ACCESS_START"])) * 0.1)) ** 1.2), 0)
                            hunger = round(
                                (5 * (int(a["POINTS"]["START_POINTS"]["PP_START"]) * 0.3 +
                                      int(a["POINTS"]["START_POINTS"]["AP_START"]) * 0.3 +
                                      int(a["POINTS"]["START_POINTS"]["SP_START"]) * 0.3
                                      ) ** 1.05), 0)
                            intoxication = round(
                                (5 * (int(a["POINTS"]["START_POINTS"]["PP_START"]) * 0.7 +
                                      int(a["POINTS"]["START_POINTS"]["AP_START"]) * 0.1 +
                                      int(a["POINTS"]["START_POINTS"]["SP_START"]) * 0.1 +
                                      int(a["PERMISSIONS"]["BLEED_ACCESS_START"]) * 0.1
                                      ) ** 1.05), 0)
                            print("\n"+"Полоски персонажа:")
                            print("Начальная максимальная полоса здоровья: " + str(health))
                            print("Начальная максимальная полоса ментального здоровья: " + str(mind_health))
                            print("Начальная максимальная полоса выносливости: " + str(stamina))
                            print("Начальное максимальное значение переносимого веса: " + str(weight))
                            print("Начальная максимальная полоса маны: " + str(mana))
                            print("Начальная максимальная полоса полноты желудка: " + str(hunger))
                            print("Начальная максимальная полоса незаражённости организма: " + str(intoxication))

                            fire_res_now = (
                                    int(a["PERMISSIONS"]["FIRE_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["FIRE_RES_START"]))
                            water_res_now = (
                                    int(a["PERMISSIONS"]["WATER_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["WATER_RES_START"]))
                            wind_res_now = (
                                    int(a["PERMISSIONS"]["WIND_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["WIND_RES_START"]))
                            dirt_res_now = (
                                    int(a["PERMISSIONS"]["DIRT_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["DIRT_RES_START"]))
                            lightning_res_now = (
                                    int(a["PERMISSIONS"]["LIGHTNING_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["LIGHTNING_RES_START"]))
                            holy_res_now = (
                                    int(a["PERMISSIONS"]["HOLY_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["HOLY_RES_START"]))
                            curse_res_now = (
                                    int(a["PERMISSIONS"]["CURSE_ACCESS_START"]) * 5 +
                                    int(a["RESISTANCES"]["CURSE_RES_START"]))
                            crush_res_now = int(a["RESISTANCES"]["CRUSH_RES_START"])
                            cut_res_now = int(a["RESISTANCES"]["CUT_RES_START"])
                            stab_res_now = int(a["RESISTANCES"]["STAB_RES_START"])

                            print("\n"+"Нынешние значения сопративления: ")
                            print("Сопративление к огненному урону: " + str(fire_res_now))
                            print("Сопративление к водному урону: " + str(water_res_now))
                            print("Сопративление к воздушному урону: " + str(wind_res_now))
                            print("Сопративление к земляному урону: " + str(dirt_res_now))
                            print("Сопративление к электрическому урону: " + str(lightning_res_now))
                            print("Сопративление к светлому урону: " + str(holy_res_now))
                            print("Сопративление к тёмному урону: " + str(curse_res_now))
                            print("Сопративление к дробящему урону: " + str(crush_res_now))
                            print("Сопративление к режущему урону: " + str(cut_res_now))
                            print("Сопративление к протыкающему урону: " + str(stab_res_now))
                            hero = {
                                "RACE": a,
                                "PERSON_INFO":
                                    {
                                        "POINTS_BY_LVL":
                                            {
                                                "SP_BY_LVL": 0,
                                                "MP_BY_LVL": 0,
                                                "IP_BY_LVL": 0,
                                                "PP_BY_LVL": 0,
                                                "AP_BY_LVL": 0,
                                                "FP_BY_LVL": 0,
                                                "LP_BY_LVL": 0,
                                                "CP_BY_LVL": 0,
                                                "BP_BY_LVL": 0
                                            },
                                        "KNOWLEDGES":
                                            {
                                                "FIRE_ACCESS_BY_LVL": 0,
                                                "WATER_ACCESS_BY_LVL": 0,
                                                "WIND_ACCESS_BY_LVL": 0,
                                                "DIRT_ACCESS_BY_LVL": 0,
                                                "LIGHTNING_ACCESS_BY_LVL": 0,
                                                "HOLY_ACCESS_BY_LVL": 0,
                                                "CURSE_ACCESS_BY_LVL": 0,
                                                "BLEED_ACCESS_BY_LVL": 0,
                                                "NATURE_ACCESS_BY_LVL": 0,
                                                "MENTAL_ACCESS_BY_LVL": 0,
                                                "TWOHANDED_ACCESS_BY_LVL": 0,
                                                "POLEARM_ACCESS_BY_LVL": 0,
                                                "ONEHANDED_ACCESS_BY_LVL": 0,
                                                "STABBING_ACCESS_BY_LVL": 0,
                                                "CUTTING_ACCESS_BY_LVL": 0,
                                                "CRUSHING_ACCESS_BY_LVL": 0,
                                                "SMALL_ARMS_ACCESS_BY_LVL": 0,
                                                "SHIELDS_ACCESS_BY_LVL": 0,
                                            },
                                        "BARS":
                                            {
                                                "MAX_BARS":
                                                    {
                                                        "HEALTH_MAX": health,
                                                        "MIND_HEALTH_MAX": mind_health,
                                                        "STAMINA_MAX": stamina,
                                                        "WEIGHT_MAX": weight,
                                                        "MANA_MAX": mana,
                                                        "HUNGER_MAX": hunger,
                                                        "INTOXICATION_MAX": intoxication
                                                    },
                                                "NOW_BARS":
                                                    {
                                                        "HEALTH_NOW": health,
                                                        "MIND_HEALTH_NOW": mind_health,
                                                        "STAMINA_NOW": stamina,
                                                        "WEIGHT_NOW": weight,
                                                        "MANA_NOW": mana,
                                                        "HUNGER_NOW": hunger,
                                                        "INTOXICATION_NOW": intoxication
                                                    }
                                            },
                                        "STATUSES":
                                            {
                                                "LIFE_STATUS": 1,
                                                "LOCATION_X": 0,
                                                "LOCATION_Y": 0,
                                                "LOCATION_Z": 0,
                                                "FIGHT_STATUS": 0,
                                                "REP_STATUS": 0
                                            },
                                        "RESISTANCES_NOW":
                                            {
                                                "FIRE_RES_NOW": fire_res_now,
                                                "WATER_RES_NOW": water_res_now,
                                                "WIND_RES_NOW": wind_res_now,
                                                "DIRT_RES_NOW": dirt_res_now,
                                                "LIGHTNING_RES_NOW": lightning_res_now,
                                                "HOLY_RES_NOW": holy_res_now,
                                                "CURSE_RES_NOW": curse_res_now,
                                                "CRUSH_RES_NOW": crush_res_now,
                                                "CUT_RES_NOW": cut_res_now,
                                                "STAB_RES_NOW": stab_res_now

                                            },
                                        "EQUIP_SLOT":
                                            {
                                                "EQUIP_SLOT_SUM_IS_FREE":
                                                    {
                                                        "HELMET_STATUS_SUM": int(a["EQUIPMENT"]["HELMET_STATUS_START"]),
                                                        "CHEST_STATUS_SUM": int(a["EQUIPMENT"]["CHEST_STATUS_START"]),
                                                        "SHOES_STATUS_SUM": int(a["EQUIPMENT"]["SHOES_STATUS_START"]),
                                                        "GLOVES_STATUS_SUM": int(a["EQUIPMENT"]["GLOVES_STATUS_START"]),
                                                        "ITEM_SLOT_SUM": int(a["EQUIPMENT"]["ITEM_SLOT_START"])
                                                    },
                                                "EQUIP_SLOT_NOW":
                                                    {
                                                        "HELMET_STATUS_NOW": 0,
                                                        "CHEST_STATUS_NOW": 0,
                                                        "SHOES_STATUS_NOW": 0,
                                                        "GLOVES_STATUS_NOW": 0,
                                                        "ITEM_SLOT_NOW": 0
                                                    }
                                            },
                                        "PERSON_LVL":
                                            {
                                                "LVL": 0,
                                                "EXP_NOW": 0,
                                                "EXP_TO_LVL": 55
                                            }
                                    },

                                "INVENTORY":
                                    {
                                        "THINGS":
                                            {
                                                "POINTS_NEED_TO":
                                                    {
                                                        "POINTS_TO_USE_THING": {},
                                                        "POINTS_TO_MAKE_THING": {}
                                                    },
                                                "POINTS_GIVES":
                                                    {
                                                        "GIVES_PASSIVE": {},
                                                        "GIVES_ACTIVE": {}
                                                    },
                                                "GIVE_RESISTANCES_THING":
                                                    {
                                                        "PASSIVE_RESISTANCE_THING": {},
                                                        "ACTIVE_RESISTANCE_THING": {}
                                                    },
                                                "ACCESS_USE_TO":
                                                    {
                                                        "MAGIC_USE_TO": {},
                                                        "WEAPON_USE_TO": {}
                                                    },
                                                "GIVE_PERMISSIONS":
                                                    {
                                                        "MAGIC_ACTIVE_GIVES": {},
                                                        "MAGIC_PASSIVE_GIVES": {},
                                                        "WEAPON_ACTIVE_GIVES": {},
                                                        "WEAPON_PASSIVE_GIVES": {}
                                                    },
                                                "MAX_BARS":
                                                    {
                                                        "ACTIVE_MAX_BARS": {},
                                                        "PASSIVE_MAX_BARS": {}
                                                    },
                                                "NOW_BARS":
                                                    {
                                                        "ACTIVE_NOW_BARS": {},
                                                        "PASSIVE_NOW_BARS": {}
                                                    },
                                                "EQUIP_SLOT_GIVES":
                                                    {
                                                        "EQUIP_SLOT_ACTIVE": {},
                                                        "EQUIP_SLOT_PASSIVE": {}
                                                    },
                                                "EQUIP_SLOT_USE_TO": {},
                                                "THING_STATUSES": {},
                                                "DAMAGE_TYPE":
                                                    {
                                                        "DAMAGE_ACTIVE": {},
                                                        "DAMAGE_PASSIVE": {}
                                                    },
                                                "COST": {},
                                                "ITEM_NEED_TO":
                                                    {
                                                        "ACTIVE": {},
                                                        "PASSIVE": {}
                                                    }
                                            },
                                        "CONSUMABLES":
                                            {
                                                "NEED_TO_MAKE_ITEM":
                                                    {
                                                        "POINTS_TO_MAKE_ITEM": {},
                                                        "KNOWLEDGE_TO_MAKE_ITEM": {}
                                                    },
                                                "GIVES_ACTIVE": {},
                                                "ACTIVE_RESISTANCE": {},
                                                "MAGIC_ACTIVE_GIVES": {},
                                                "WEAPON_ACTIVE_GIVES": {},
                                                "ACTIVE_MAX_BARS": {},
                                                "ACTIVE_NOW_BARS": {},
                                                "CONSUMABLE_STATUSES": {},
                                                "DAMAGE_ACTIVE": {},
                                                "COST": {},
                                                "ACTIVE": {}
                                            },
                                        "COINS": {}
                                    },

                                "SPELLS_ABILITIES":
                                    {
                                        "POINTS_TO_USE_SPELLS_ABILITIES": {},
                                        "GIVES_SPELLS_ABILITIES": {},
                                        "ACTIVE_RESISTANCE_SPELLS_ABILITIES": {},
                                        "USE_TO":
                                            {
                                                "MAGIC_USE_TO": {},
                                                "WEAPON_USE_TO": {}
                                            },
                                        "BARS":
                                            {
                                                "MAX_BARS": {},
                                                "NOW_BARS": {}
                                            },
                                        "STATUSES": {},
                                        "DAMAGE_TYPE": {},
                                        "ANOTHER_REQUEST": {},
                                        "LIFE_STATUS": {}
                                    }
                            }
                            database.child("Players").child(msg_fullname_sender).child("Hero").child(hero_name).set(
                                hero)
                            database.child("Heroes").child(hero_name).set(hero)

                if (msg.count('|') - msg.count("[")) == 4:
                    massive = msg.split('|')
                    if ((str(massive[3]) == "Разбить лагерь") or (str(massive[3]) == "разбить лагерь")):
                        hero_name = massive[1]
                        make_camp(msg, msg_id_sender, id, hero_name)
                    if ((str(massive[3]) == "отдыхать") or (str(massive[3]) == "Отдыхать")):
                        hero_name = massive[1]
                        take_a_rest(msg, msg_id_sender, id, hero_name)

                if (msg.count('|') - msg.count("[")) == 4:
                    massive = msg.split('|')
                    action = str(massive[3])[0:massive[3].find(' ', 0)]
                    action = action.strip(' ')
                    print(action)
                    if action == "Использовать" or action == "использовать":
                        hero_name = massive[1]
                        item_name = action[1]
                        item_target = action[2]

                        using_item(msg, msg_id_sender, id, hero_name, item_name, item_target)
                    if action == "Умение" or action == "умение":
                        db = sqlite3.connect('db/database.db')

                        hero_name = massive[1]
                        ability_name = str(massive[3])[massive[3].find('"', 0) + 1:massive[3].rfind('"', 0)]
                        ability_target = str(massive[3])[massive[3].rfind('"', 0) + 1:]

                        db.close()
                        using_ability(msg, msg_id_sender, id, hero_name, ability_name, ability_target)
                    if action == "Закопать" or action == "закопать":
                        hero_name = massive[1]
                        target = str(massive[3])[massive[3].find(' ', 0) + 1:]

                        end_of_the_journey(msg, msg_id_sender, id, hero_name, target)
                    if action == "Отдать" or action == "отдать":
                        hero_name = massive[1]
                        target = str(massive[3])[massive[3].find(' ', 0) + 1:massive[3].find('"', 0)]
                        target = target.strip(' ')
                        print(target)
                        list_of_items = str(massive[3])[massive[3].find('"', 0) + 1:massive[3].rfind('"', 0)]
                        print(list_of_items)

                        add_item_in_inventory(msg, msg_id_sender, id, hero_name, target, list_of_items)
                    # if action == "Переместиться" or action == "переместиться":
