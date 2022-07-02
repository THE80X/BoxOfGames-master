# coding=utf-8
import json
import os.path

path_to_file = "Things/THING.json"
id_permission_equip_to = ""
id_permission_use_to = ""
id_gives_equip_to = ""
id_gives_use_to = ""
spec_symbol = r'"'
x = 1


def race_start_points():
    print("\n Введите начальные очки расы: ")
    print("Стамина")
    sp_start = input()
    print("Колдовство")
    mp_start = input()
    print("Интелект")
    ip_start = input()
    print("Сила")
    pp_start = input()
    print("Ловкость")
    ap_start = input()
    print("Вера")
    fp_start = input()
    print("Удача")
    lp_start = input()
    print("Харизма")
    cp_start = input()
    print("Рассудок")
    bp_start = input()
    return {"SP_START": sp_start,
            "MP_START": mp_start,
            "IP_START": ip_start,
            "PP_START": pp_start,
            "AP_START": ap_start,
            "FP_START": fp_start,
            "LP_START": lp_start,
            "CP_START": cp_start,
            "BP_START": bp_start
            }


def race_max_points():
    print("\n Введите  конечные очки расы: ")
    print("Стамина")
    sp_max = input()
    print("Колдовство")
    mp_max = input()
    print("Интелект")
    ip_max = input()
    print("Сила")
    pp_max = input()
    print("Ловкость")
    ap_max = input()
    print("Вера")
    fp_max = input()
    print("Удача")
    lp_max = input()
    print("Харизма")
    cp_max = input()
    print("Рассудок")
    bp_max = input()
    return {"SP_MAX": sp_max,
            "MP_MAX": mp_max,
            "IP_MAX": ip_max,
            "PP_MAX": pp_max,
            "AP_MAX": ap_max,
            "FP_MAX": fp_max,
            "LP_MAX": lp_max,
            "CP_MAX": cp_max,
            "BP_MAX": bp_max
            }


def race_resistances():
    print("\n Введите стартовые сопративления расы к различным типам урона: ")
    print("Сопративление к огню")
    fire_res_start = input()
    print("Сопративление к воде")
    water_res_start = input()
    print("Сопративление к воздху")
    wind_res_start = input()
    print("Сопративление к земле")
    dirt_res_start = input()
    print("Сопративление к молниям")
    lightning_res_start = input()
    print("Сопративление к свету")
    holy_res_start = input()
    print("Сопративление ко тьме")
    curse_res_start = input()
    print("Сопративление к протыканию")
    cut_res_start = input()
    print("Сопративление к порезам")
    stab_res_start = input()
    print("Сопративление к дроблению")
    crush_res_start = input()
    return {"FIRE_RES_START": fire_res_start,
            "WATER_RES_START": water_res_start,
            "WIND_RES_START": wind_res_start,
            "DIRT_RES_START": dirt_res_start,
            "LIGHTNING_RES_START": lightning_res_start,
            "HOLY_RES_START": holy_res_start,
            "CURSE_RES_START": curse_res_start,
            "CUT_RES_START": cut_res_start,
            "STAB_RES_START": stab_res_start,
            "CRUSH_RES_START": crush_res_start,
            }


def race_permissions():
    print("\n Введите стартовые очки умений: ")
    print("Пирокинектика")
    fire_access_start = input()
    print("Гидрософистика")
    water_access_start = input()
    print("Аэрософистика")
    wind_access_start = input()
    print("Геомантия")
    dirt_access_start = input()
    print("Киловактика")
    lightning_access_start = input()
    print("Элафриситка")
    holy_access_start = input()
    print("Катифристика")
    curse_access_start = input()
    print("Гематомантия")
    bleed_access_start = input()
    print("Ботаника")
    nature_access_start = input()
    print("Псифистика")
    mental_access_start = input()
    print("Владение навыками Колющего оружия")
    twohanded_access_start = input()
    print("Владение навыками Режущего оружия")
    polearm_access_start = input()
    print("Владение навыками Дробящего оружия")
    onehanded_access_start = input()
    print("Владение навыками Двуручного оружия")
    stabbing_access_start = input()
    print("Владение навыками Древкового оружия")
    cutting_access_start = input()
    print("Владение навыками Одноручного оружия")
    crushing_access_start = input()
    print("Владение навыками Стрелкового оружия")
    small_arms_access_start = input()
    print("Владение навыками щитов")
    shields_access_start = input()
    return {'FIRE_ACCESS_START': fire_access_start,
            'WATER_ACCESS_START': water_access_start,
            'WIND_ACCESS_START': wind_access_start,
            'DIRT_ACCESS_START': dirt_access_start,
            'LIGHTNING_ACCESS_START': lightning_access_start,
            'HOLY_ACCESS_START': holy_access_start,
            'CURSE_ACCESS_START': curse_access_start,
            'BLEED_ACCESS_START': bleed_access_start,
            'NATURE_ACCESS_START': nature_access_start,
            'MENTAL_ACCESS_START': mental_access_start,
            'TWOHANDED_ACCESS_START': twohanded_access_start,
            'POLEARM_ACCESS_START': polearm_access_start,
            'ONEHANDED_ACCESS_START': onehanded_access_start,
            'STABBING_ACCESS_START': stabbing_access_start,
            'CUTTING_ACCESS_START': cutting_access_start,
            'CRUSHING_ACCESS_START': crushing_access_start,
            'SMALL_ARMS_ACCESS_START': small_arms_access_start,
            'SHIELDS_ACCESS_START': shields_access_start}


def race_equipment():
    print("\n Введите стартовые очки экипировки: ")
    print("Шлем")
    helmet_status_start = input()
    print("Нагрудник")
    chest_status_start = input()
    print("Ботинки")
    shoes_status_start = input()
    print("Наручи")
    gloves_status_start = input()
    print("Предметы экипировки")
    item_slot_start = input()
    return {'HELMET_STATUS_START': helmet_status_start,
            'CHEST_STATUS_START': chest_status_start,
            'SHOES_STATUS_START': shoes_status_start,
            'GLOVES_STATUS_START': gloves_status_start,
            'ITEM_SLOT_START': item_slot_start}


def raceCreate():
    check_file = os.path.exists('Races')
    if check_file:
        print("Введите название расы")
        race_name = input()
        race_name.lower()
        if os.path.exists('Races/' + race_name):
            print("Данная раса уже существует")
            raceCreate()
        else:

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер расы. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_race = str(input())
            id_race.replace(" ", "")
            if (id_race == "") or (
                    str(data["RACES_BUILDER"]["RACE"].keys()).count(id_race) == 0):
                id_race = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер набора минимальных очков. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_now_points = str(input())
            id_now_points.replace(" ", "")
            if (id_now_points == "") or (
                    str(data["RACES_BUILDER"]["NOW_POINTS"].keys()).count(id_now_points) == 0):
                id_now_points = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                start_points = race_start_points()
            else:
                start_points = data["RACES_BUILDER"]["NOW_POINTS"][id_now_points]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер набора максимальных очков. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_max_points = str(input())
            id_max_points.replace(" ", "")
            if (id_max_points == "") or (
                    str(data["RACES_BUILDER"]["MAX_POINTS"].keys()).count(id_max_points) == 0):
                id_max_points = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                max_points = race_max_points()
            else:
                max_points = data["RACES_BUILDER"]["MAX_POINTS"][id_max_points]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер набора сопративлений. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_res = str(input())
            id_res.replace(" ", "")
            if (id_res == "") or (
                    str(data["RACES_BUILDER"]["RESISTANCES"].keys()).count(id_res) == 0):
                id_res = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                resistances = race_resistances()
            else:
                resistances = data["RACES_BUILDER"]["RESISTANCES"][id_res]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер набора разрешений. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_permissions = str(input())
            id_permissions.replace(" ", "")
            if (id_permissions == "") or (
                    str(data["RACES_BUILDER"]["PERMISSIONS"].keys()).count(id_permissions) == 0):
                id_permissions = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                permission = race_permissions()
            else:
                permission = data["RACES_BUILDER"]["PERMISSIONS"][id_permissions]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер набора экипировки. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_equipment = str(input())
            id_equipment.replace(" ", "")
            if (id_equipment == "") or (
                    str(data["RACES_BUILDER"]["EQUIPMENT"].keys()).count(id_equipment) == 0):
                id_equipment = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                equipment = race_equipment()
            else:
                equipment = data["RACES_BUILDER"]["EQUIPMENT"][id_equipment]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            race = {
                'RACE_NAME': race_name,
                'LIST_OF_IDS': [id_race, id_now_points, id_max_points, id_res, id_permissions, id_equipment],
                'POINTS':
                    {
                        'START_POINTS': start_points,
                        'MAX_POINTS': max_points
                    },
                'RESISTANCES': resistances,
                'PERMISSIONS': permission,
                'EQUIPMENT': equipment
            }

            with open(path_to_file, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            with open(path_to_file, "w", encoding="utf-8") as json_file:
                print(data)
                data["RACES_BUILDER"]["RACE"][id_race] = race
                data["RACES_BUILDER"]["NOW_POINTS"][id_now_points] = start_points
                data["RACES_BUILDER"]["MAX_POINTS"][id_max_points] = max_points
                data["RACES_BUILDER"]["RESISTANCES"][id_res] = resistances
                data["RACES_BUILDER"]["PERMISSIONS"][id_permissions] = permission
                data["RACES_BUILDER"]["EQUIPMENT"][id_equipment] = equipment
                print(data)
                json.dump(data, json_file, indent=4, ensure_ascii=False)
                json_file.close()


def nothingGiver(stroka):
    stroka.replace(" ", "")
    if stroka.lower() == "none" or stroka.lower() == "null" or stroka.lower() == "":
        stroka = None
        return stroka


def requirements_equip_to():
    global id_permission_equip_to

    print("\n" + "Введите требования для экипировки артефакта связанные с очками: ")
    print("Стамина")
    sp_equip_to = str(input())
    nothingGiver(sp_equip_to)
    print("Колдовство")
    mp_equip_to = str(input())
    nothingGiver(mp_equip_to)
    print("Интелект")
    ip_equip_to = str(input())
    nothingGiver(ip_equip_to)
    print("Сила")
    pp_equip_to = str(input())
    nothingGiver(pp_equip_to)
    print("Ловкость")
    ap_equip_to = str(input())
    nothingGiver(ap_equip_to)
    print("Вера")
    fp_equip_to = str(input())
    nothingGiver(fp_equip_to)
    print("Удача")
    lp_equip_to = str(input())
    nothingGiver(lp_equip_to)
    print("Харизма")
    cp_equip_to = str(input())
    nothingGiver(cp_equip_to)
    print("Рассудок")
    bp_equip_to = str(input())
    nothingGiver(bp_equip_to)

    print("\n" + "Введите требования для экипировки артефакта связанные с очками умений: ")
    print("Пирокинектика")
    fire_access_equip_to_thing = str(input())
    nothingGiver(fire_access_equip_to_thing)
    print("Гидрософистика")
    water_access_equip_to_thing = str(input())
    nothingGiver(water_access_equip_to_thing)
    print("Аэрософистика")
    wind_access_equip_to_thing = str(input())
    nothingGiver(wind_access_equip_to_thing)
    print("Геомантия")
    dirt_access_equip_to_thing = str(input())
    nothingGiver(dirt_access_equip_to_thing)
    print("Киловактика")
    lightning_access_equip_to_thing = str(input())
    nothingGiver(lightning_access_equip_to_thing)
    print("Элафриситка")
    holy_access_equip_to_thing = str(input())
    nothingGiver(holy_access_equip_to_thing)
    print("Катифристика")
    curse_access_equip_to_thing = str(input())
    nothingGiver(curse_access_equip_to_thing)
    print("Гематомантия")
    bleed_access_equip_to_thing = str(input())
    nothingGiver(bleed_access_equip_to_thing)
    print("Ботаника")
    nature_access_equip_to_thing = str(input())
    nothingGiver(nature_access_equip_to_thing)
    print("Псифистика")
    mental_access_equip_to_thing = str(input())
    nothingGiver(mental_access_equip_to_thing)
    print("Владение навыками Колющего оружия")
    twohanded_access_equip_to_thing = str(input())
    nothingGiver(twohanded_access_equip_to_thing)
    print("Владение навыками Режущего оружия")
    polearm_access_equip_to_thing = str(input())
    nothingGiver(polearm_access_equip_to_thing)
    print("Владение навыками Дробящего оружия")
    onehanded_access_equip_to_thing = str(input())
    nothingGiver(onehanded_access_equip_to_thing)
    print("Владение навыками Двуручного оружия")
    stabbing_access_equip_to_thing = str(input())
    nothingGiver(stabbing_access_equip_to_thing)
    print("Владение навыками Древкового оружия")
    cutting_access_equip_to_thing = str(input())
    nothingGiver(cutting_access_equip_to_thing)
    print("Владение навыками Одноручного оружия")
    crushing_access_equip_to_thing = str(input())
    nothingGiver(crushing_access_equip_to_thing)
    print("Владение навыками Стрелкового оружия")
    small_arms_access_equip_to_thing = str(input())
    nothingGiver(small_arms_access_equip_to_thing)
    print("Владение навыками щитов")
    shields_access_equip_to_thing = str(input())
    nothingGiver(shields_access_equip_to_thing)

    print("\n" + "Введите очки экипировки, занимаемые артефактом: ")
    print("Шлем")
    helmet_status_equip_to_thing = str(input())
    nothingGiver(helmet_status_equip_to_thing)
    print("Нагрудник")
    chest_status_equip_to_thing = str(input())
    nothingGiver(chest_status_equip_to_thing)
    print("Ботинки")
    shoes_status_equip_to_thing = str(input())
    nothingGiver(shoes_status_equip_to_thing)
    print("Наручи")
    gloves_status_equip_to_thing = str(input())
    nothingGiver(gloves_status_equip_to_thing)
    print("Предметы экипировки")
    item_slot_equip_to_thing = str(input())
    nothingGiver(item_slot_equip_to_thing)
    return {
        "SP_EQUIP_TO": sp_equip_to,
        "MP_EQUIP_TO": mp_equip_to,
        "IP_EQUIP_TO": ip_equip_to,
        "PP_EQUIP_TO": pp_equip_to,
        "AP_EQUIP_TO": ap_equip_to,
        "FP_EQUIP_TO": fp_equip_to,
        "LP_EQUIP_TO": lp_equip_to,
        "CP_EQUIP_TO": cp_equip_to,
        "BP_EQUIP_TO": bp_equip_to,
        "FIRE_ACCESS_EQUIP_TO_THING": fire_access_equip_to_thing,
        "WATER_ACCESS_EQUIP_TO_THING": water_access_equip_to_thing,
        "WIND_ACCESS_EQUIP_TO_THING": wind_access_equip_to_thing,
        "DIRT_ACCESS_EQUIP_TO_THING": dirt_access_equip_to_thing,
        "LIGHTNING_ACCESS_EQUIP_TO_THING": lightning_access_equip_to_thing,
        "HOLY_ACCESS_EQUIP_TO_THING": holy_access_equip_to_thing,
        "CURSE_ACCESS_EQUIP_TO_THING": curse_access_equip_to_thing,
        "BLEED_ACCESS_EQUIP_TO_THING": bleed_access_equip_to_thing,
        "NATURE_ACCESS_EQUIP_TO_THING": nature_access_equip_to_thing,
        "MENTAL_ACCESS_EQUIP_TO_THING": mental_access_equip_to_thing,
        "TWOHANDED_ACCESS_EQUIP_TO_THING": twohanded_access_equip_to_thing,
        "POLEARM_ACCESS_EQUIP_TO_THING": polearm_access_equip_to_thing,
        "ONEHANDED_ACCESS_EQUIP_TO_THING": onehanded_access_equip_to_thing,
        "STABBING_ACCESS_EQUIP_TO_THING": stabbing_access_equip_to_thing,
        "CUTTING_ACCESS_EQUIP_TO_THING": cutting_access_equip_to_thing,
        "CRUSHING_ACCESS_EQUIP_TO_THING": crushing_access_equip_to_thing,
        "SMALL_ARMS_ACCESS_EQUIP_TO_THING": small_arms_access_equip_to_thing,
        "SHIELDS_ACCESS_EQUIP_TO_THING": shields_access_equip_to_thing,
        "HELMET_STATUS_EQUIP_TO_THING": helmet_status_equip_to_thing,
        "CHEST_STATUS_EQUIP_TO_THING": chest_status_equip_to_thing,
        "SHOES_STATUS_EQUIP_TO_THING": shoes_status_equip_to_thing,
        "GLOVES_STATUS_EQUIP_TO_THING": gloves_status_equip_to_thing,
        "ITEM_SLOT_EQUIP_TO_THING": item_slot_equip_to_thing,
    }


def requirements_use_to():
    global id_permission_use_to
    print("Введите число вводимых требований")
    i = input()
    if i == "":
        i = 0
    i = int(i)
    z = 0
    list_of_requirements = []
    for z in range(i):
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            counter = int(data["number"])
            smth_idk = len(str(counter))
            number = '0' * (16 - smth_idk) + str(counter)
            print("\n" + "Введите номер требования для использования артефакта.[" + str(
                z) + "] (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                  " Если вы ничего не введёте, он будет использован по умолчанию)")
            permission = str(input())
            permission.replace(" ", '')
            if permission == "":
                permission = number
                counter = counter + 1
            list_of_requirements.append(permission)
            smth_idk = len(str(counter))
            number = '0' * (16 - smth_idk) + str(counter)
            fuck_it = {'number': number}
            with open(path_to_file, "w", encoding="utf-8") as file_1:
                json.dump(fuck_it, file_1, indent=4, ensure_ascii=False)
    print("Введите число необходимых требований для использования особенностей:")
    amount_of_requirements = input()
    if amount_of_requirements == "":
        amount_of_requirements = 0
    return {
        "LIST_OF_REQUIREMENTS": list_of_requirements,
        "AMOUNT_OF_REQUIREMENTS": amount_of_requirements
    }


def thing_give_able_to_equip():
    global idk
    global id_gives_equip_to

    print("\n" + "Введите получаемые очки за экипировку артефакта: ")
    print("Стамина")
    sp_gives_equip_to = str(input())
    nothingGiver(sp_gives_equip_to)
    print("Колдовство")
    mp_gives_equip_to = str(input())
    nothingGiver(mp_gives_equip_to)
    print("Интелект")
    ip_gives_equip_to = str(input())
    nothingGiver(ip_gives_equip_to)
    print("Сила")
    pp_gives_equip_to = str(input())
    nothingGiver(pp_gives_equip_to)
    print("Ловкость")
    ap_gives_equip_to = str(input())
    nothingGiver(ap_gives_equip_to)
    print("Вера")
    fp_gives_equip_to = str(input())
    nothingGiver(fp_gives_equip_to)
    print("Удача")
    lp_gives_equip_to = str(input())
    nothingGiver(lp_gives_equip_to)
    print("Харизма")
    cp_gives_equip_to = str(input())
    nothingGiver(cp_gives_equip_to)
    print("Рассудок")
    bp_gives_equip_to = str(input())
    nothingGiver(bp_gives_equip_to)

    print("\n" + "Введите получаемые сопративления к различным типам урона за экипировку артефакта: ")
    print("Сопративление к огню")
    fire_res_gives_equip_to = str(input())
    nothingGiver(fire_res_gives_equip_to)
    print("Сопративление к воде")
    water_res_gives_equip_to = str(input())
    nothingGiver(water_res_gives_equip_to)
    print("Сопративление к воздху")
    wind_res_gives_equip_to = str(input())
    nothingGiver(wind_res_gives_equip_to)
    print("Сопративление к земле")
    dirt_res_gives_equip_to = str(input())
    nothingGiver(dirt_res_gives_equip_to)
    print("Сопративление к молниям")
    lightning_res_gives_equip_to = str(input())
    nothingGiver(lightning_res_gives_equip_to)
    print("Сопративление к свету")
    holy_res_gives_equip_to = str(input())
    nothingGiver(holy_res_gives_equip_to)
    print("Сопративление ко тьме")
    curse_res_gives_equip_to = str(input())
    nothingGiver(curse_res_gives_equip_to)
    print("Сопративление к протыканию")
    cut_res_gives_equip_to = str(input())
    nothingGiver(cut_res_gives_equip_to)
    print("Сопративление к порезам")
    stab_res_gives_equip_to = str(input())
    nothingGiver(stab_res_gives_equip_to)
    print("Сопративление к дроблению")
    crush_res_gives_equip_to = str(input())
    nothingGiver(crush_res_gives_equip_to)

    print("\n" + "Введите получаемые очки урона за экипировку артефакта: ")
    print("Дробящий урон")
    crush_damage_gives_equip_to = str(input())
    nothingGiver(crush_damage_gives_equip_to)
    print("Разрубающий урон")
    cut_damage_gives_equip_to = str(input())
    nothingGiver(cut_damage_gives_equip_to)
    print("Колющий урон")
    stab_damage_gives_equip_to = str(input())
    nothingGiver(stab_damage_gives_equip_to)

    print("\n" + "Введите получаемые очки экипировки, занимаемые артефактом: ")
    print("Шлем")
    helmet_status_gives_equip_to_thing = str(input())
    nothingGiver(helmet_status_gives_equip_to_thing)
    print("Нагрудник")
    chest_status_gives_equip_to_thing = str(input())
    nothingGiver(chest_status_gives_equip_to_thing)
    print("Ботинки")
    shoes_status_gives_equip_to_thing = str(input())
    nothingGiver(shoes_status_gives_equip_to_thing)
    print("Наручи")
    gloves_status_gives_equip_to_thing = str(input())
    nothingGiver(gloves_status_gives_equip_to_thing)
    print("Предметы экипировки")
    item_slot_gives_equip_to_thing = str(input())
    nothingGiver(item_slot_gives_equip_to_thing)

    print("\n" + "Введите колличество дающих разрешений, дающего артефактом при экипировке: ")
    i = input()
    if i == "":
        i = 0
    i = int(i)
    z = 0
    list_of_permissions_equip_to = []
    for z in range(i):
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            counter = int(data["number"])
            smth_idk = len(str(counter))
            number = '0' * (16 - smth_idk) + str(counter)
            print("\n" + "Введите номер разрешения.[" + str(
                z) + "] (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                  " Если вы ничего не введёте, он будет использован по умолчанию)")
            permission = str(input())
            permission.replace(" ", '')
            if permission == "":
                permission = number
                counter = counter + 1
            list_of_permissions_equip_to.append(permission)
            smth_idk = len(str(counter))
            number = '0' * (16 - smth_idk) + str(counter)
            data["number"] = number
            with open(path_to_file, "w", encoding="utf-8") as file_1:
                json.dump(data, file_1, indent=4, ensure_ascii=False)
    return {
        "SP_GIVES": sp_gives_equip_to,
        "MP_GIVES": mp_gives_equip_to,
        "IP_GIVES": ip_gives_equip_to,
        "PP_GIVES": pp_gives_equip_to,
        "AP_GIVES": ap_gives_equip_to,
        "FP_GIVES": fp_gives_equip_to,
        "LP_GIVES": lp_gives_equip_to,
        "CP_GIVES": cp_gives_equip_to,
        "BP_GIVES": bp_gives_equip_to,
        "FIRE_RES_GIVE_THING": fire_res_gives_equip_to,
        "WATER_RES_GIVE_THING": water_res_gives_equip_to,
        "WIND_RES_GIVE_THING": wind_res_gives_equip_to,
        "DIRT_RES_GIVE_THING": dirt_res_gives_equip_to,
        "LIGHTNING_RES_GIVE_THING": lightning_res_gives_equip_to,
        "HOLY_RES_GIVE_THING": holy_res_gives_equip_to,
        "CURSE_RES_GIVE_THING": curse_res_gives_equip_to,
        "CRUSH_RES_GIVE_THING": crush_res_gives_equip_to,
        "CUT_RES_GIVE_THING": cut_res_gives_equip_to,
        "STAB_RES_GIVE_THING": stab_res_gives_equip_to,
        "FIRE_DAMAGE_GIVES_THING": "",
        "WATER_DAMAGE_GIVES_THING": "",
        "WIND_DAMAGE_GIVES_THING": "",
        "DIRT_DAMAGE_GIVES_THING": "",
        "LIGHTNING_DAMAGE_GIVES_THING": "",
        "HOLY_DAMAGE_GIVES_THING": "",
        "CURSE_DAMAGE_GIVES_THING": "",
        "CRUSH_DAMAGE_GIVES_THING": crush_damage_gives_equip_to,
        "CUT_DAMAGE_GIVES_THING": cut_damage_gives_equip_to,
        "STAB_DAMAGE_GIVES_THING": stab_damage_gives_equip_to,
        "CLEAR_DAMAGE_GIVES_THING": "",
        "FIRE_ACCESS_GIVES_THING":  "",
        "WATER_ACCESS_GIVES_THING": "",
        "WIND_ACCESS_GIVES_THING": "",
        "DIRT_ACCESS_GIVES_THING": "",
        "LIGHTNING_ACCESS_GIVES_THING": "",
        "HOLY_ACCESS_GIVES_THING": "",
        "CURSE_ACCESS_GIVES_THING": "",
        "BLEED_ACCESS_GIVES_THING": "",
        "NATURE_ACCESS_GIVES_THING": "",
        "MENTAL_ACCESS_GIVES_THING": "",
        "TWOHANDED_ACCESS_GIVES_THING": "",
        "POLEARM_ACCESS_GIVES_THING": "",
        "ONEHANDED_ACCESS_GIVES_THING": "",
        "STABBING_ACCESS_GIVES_THING": "",
        "CUTTING_ACCESS_GIVES_THING": "",
        "CRUSHING_ACCESS_GIVES_THING": "",
        "SMALL_ARMS_ACCESS_GIVES_THING": "",
        "SHIELDS_ACCESS_GIVES_THING": "",
        "HEALTH_MAX_GIVES_THING": "",
        "MIND_MAX_GIVES_THING": "",
        "STAMINA_MAX_GIVES_THING": "",
        "MANA_MAX_GIVES_THING": "",
        "HUNGER_MAX_GIVES_THING": "",
        "INTOXICATION_MAX_GIVES_THING": "",
        "HELMET_STATUS_GIVES_THING": helmet_status_gives_equip_to_thing,
        "CHEST_STATUS_GIVES_THING": chest_status_gives_equip_to_thing,
        "SHOES_STATUS_GIVES_THING": shoes_status_gives_equip_to_thing,
        "GLOVES_STATUS_GIVES_THING": gloves_status_gives_equip_to_thing,
        "ITEM_SLOT_GIVES_THING": item_slot_gives_equip_to_thing,
        "LIST_PERMISSION_GIVES": list_of_permissions_equip_to
    }


def thing_give_able_to_use():
    global idk
    global id_gives_use_to

    print("\n" + "Введите получаемые очки за экипировку и использование артефакта: ")
    print("Стамина")
    sp_gives_use_to = str(input())
    nothingGiver(sp_gives_use_to)
    print("Колдовство")
    mp_gives_use_to = str(input())
    nothingGiver(mp_gives_use_to)
    print("Интелект")
    ip_gives_use_to = str(input())
    nothingGiver(ip_gives_use_to)
    print("Сила")
    pp_gives_use_to = str(input())
    nothingGiver(pp_gives_use_to)
    print("Ловкость")
    ap_gives_use_to = str(input())
    nothingGiver(ap_gives_use_to)
    print("Вера")
    fp_gives_use_to = str(input())
    nothingGiver(fp_gives_use_to)
    print("Удача")
    lp_gives_use_to = str(input())
    nothingGiver(lp_gives_use_to)
    print("Харизма")
    cp_gives_use_to = str(input())
    nothingGiver(cp_gives_use_to)
    print("Рассудок")
    bp_gives_use_to = str(input())
    nothingGiver(bp_gives_use_to)

    print(
        "\n" + "Введите получаемые сопративления к различным типам урона за экипировку и использование артефакта: ")
    print("Сопративление к огню")
    fire_res_gives_use_to = str(input())
    nothingGiver(fire_res_gives_use_to)
    print("Сопративление к воде")
    water_res_gives_use_to = str(input())
    nothingGiver(water_res_gives_use_to)
    print("Сопративление к воздху")
    wind_res_gives_use_to = str(input())
    nothingGiver(wind_res_gives_use_to)
    print("Сопративление к земле")
    dirt_res_gives_use_to = str(input())
    nothingGiver(dirt_res_gives_use_to)
    print("Сопративление к молниям")
    lightning_res_gives_use_to = str(input())
    nothingGiver(lightning_res_gives_use_to)
    print("Сопративление к свету")
    holy_res_gives_use_to = str(input())
    nothingGiver(holy_res_gives_use_to)
    print("Сопративление ко тьме")
    curse_res_gives_use_to = str(input())
    nothingGiver(curse_res_gives_use_to)
    print("Сопративление к протыканию")
    cut_res_gives_use_to = str(input())
    nothingGiver(cut_res_gives_use_to)
    print("Сопративление к порезам")
    stab_res_gives_use_to = str(input())
    nothingGiver(stab_res_gives_use_to)
    print("Сопративление к дроблению")
    crush_res_gives_use_to = str(input())
    nothingGiver(crush_res_gives_use_to)

    print("\n" + "Введите получаемые очки урона за экипировку и использоваение артефакта: ")
    print("Огненный урон")
    fire_damage_gives_use_to = str(input())
    nothingGiver(fire_damage_gives_use_to)
    print("Водяной урон")
    water_damage_gives_use_to = str(input())
    nothingGiver(water_damage_gives_use_to)
    print("Воздушный урон")
    wind_damage_gives_use_to = str(input())
    nothingGiver(wind_damage_gives_use_to)
    print("Земляной урон")
    dirt_damage_gives_use_to = str(input())
    nothingGiver(dirt_damage_gives_use_to)
    print("Электрический урон")
    lightning_damage_gives_use_to = str(input())
    nothingGiver(lightning_damage_gives_use_to)
    print("Светлый урон")
    holy_damage_gives_use_to = str(input())
    nothingGiver(holy_damage_gives_use_to)
    print("Тёмный урон")
    curse_damage_gives_use_to = str(input())
    nothingGiver(curse_damage_gives_use_to)
    print("Дробящий урон")
    crush_damage_gives_use_to = str(input())
    nothingGiver(crush_damage_gives_use_to)
    print("Разрубающий урон")
    cut_damage_gives_use_to = str(input())
    nothingGiver(cut_damage_gives_use_to)
    print("Колющий урон")
    stab_damage_gives_use_to = str(input())
    nothingGiver(stab_damage_gives_use_to)
    print("Чистый урон")
    clear_damage_gives_use_to = str(input())
    nothingGiver(clear_damage_gives_use_to)

    print("\n" + "Введите получаемые очки умений за экипировку и использоваение артефакта: ")
    print("Пирокинектика")
    fire_access_gives_use_to_thing = str(input())
    nothingGiver(fire_access_gives_use_to_thing)
    print("Гидрософистика")
    water_access_gives_use_to_thing = str(input())
    nothingGiver(water_access_gives_use_to_thing)
    print("Аэрософистика")
    wind_access_gives_use_to_thing = str(input())
    nothingGiver(wind_access_gives_use_to_thing)
    print("Геомантия")
    dirt_access_gives_use_to_thing = str(input())
    nothingGiver(dirt_access_gives_use_to_thing)
    print("Киловактика")
    lightning_access_gives_use_to_thing = str(input())
    nothingGiver(lightning_access_gives_use_to_thing)
    print("Элафриситка")
    holy_access_gives_use_to_thing = str(input())
    nothingGiver(holy_access_gives_use_to_thing)
    print("Катифристика")
    curse_access_gives_use_to_thing = str(input())
    nothingGiver(curse_access_gives_use_to_thing)
    print("Гематомантия")
    bleed_access_gives_use_to_thing = str(input())
    nothingGiver(bleed_access_gives_use_to_thing)
    print("Ботаника")
    nature_access_gives_use_to_thing = str(input())
    nothingGiver(nature_access_gives_use_to_thing)
    print("Псифистика")
    mental_access_gives_use_to_thing = str(input())
    nothingGiver(mental_access_gives_use_to_thing)
    print("Владение навыками Колющего оружия")
    twohanded_access_gives_use_to_thing = str(input())
    nothingGiver(twohanded_access_gives_use_to_thing)
    print("Владение навыками Режущего оружия")
    polearm_access_gives_use_to_thing = str(input())
    nothingGiver(polearm_access_gives_use_to_thing)
    print("Владение навыками Дробящего оружия")
    onehanded_access_gives_use_to_thing = str(input())
    nothingGiver(onehanded_access_gives_use_to_thing)
    print("Владение навыками Двуручного оружия")
    stabbing_access_gives_use_to_thing = str(input())
    nothingGiver(stabbing_access_gives_use_to_thing)
    print("Владение навыками Древкового оружия")
    cutting_access_gives_use_to_thing = str(input())
    nothingGiver(cutting_access_gives_use_to_thing)
    print("Владение навыками Одноручного оружия")
    crushing_access_gives_use_to_thing = str(input())
    nothingGiver(crushing_access_gives_use_to_thing)
    print("Владение навыками Стрелкового оружия")
    small_arms_access_gives_use_to_thing = str(input())
    nothingGiver(small_arms_access_gives_use_to_thing)
    print("Владение навыками щитов")
    shields_access_gives_use_to_thing = str(input())
    nothingGiver(shields_access_gives_use_to_thing)

    print("\n" + "Введите получаемые полоски за экипировку и использование предмета: ")
    print("Полоска здоровья")
    health_max_gives_use_to_thing = str(input())
    nothingGiver(health_max_gives_use_to_thing)
    print("Полоска ментального здоровья")
    mind_max_gives_use_to_thing = str(input())
    nothingGiver(mind_max_gives_use_to_thing)
    print("Полоска выносливости")
    stamina_max_gives_use_to_thing = str(input())
    nothingGiver(stamina_max_gives_use_to_thing)
    print("Полоска маны")
    mana_max_gives_use_to_thing = str(input())
    nothingGiver(mana_max_gives_use_to_thing)
    print("Полоска голода")
    hunger_max_gives_use_to_thing = str(input())
    nothingGiver(hunger_max_gives_use_to_thing)
    print("Полоска интоксикации")
    intoxication_max_gives_use_to_thing = str(input())
    nothingGiver(intoxication_max_gives_use_to_thing)

    print("\n" + "Введите получаемые очки экипировки и использования, занимаемые артефактом: ")
    print("Шлем")
    helmet_status_gives_use_to_thing = str(input())
    nothingGiver(helmet_status_gives_use_to_thing)
    print("Нагрудник")
    chest_status_gives_use_to_thing = str(input())
    nothingGiver(chest_status_gives_use_to_thing)
    print("Ботинки")
    shoes_status_gives_use_to_thing = str(input())
    nothingGiver(shoes_status_gives_use_to_thing)
    print("Наручи")
    gloves_status_gives_use_to_thing = str(input())
    nothingGiver(gloves_status_gives_use_to_thing)
    print("Предметы экипировки")
    item_slot_gives_use_to_thing = str(input())
    nothingGiver(item_slot_gives_use_to_thing)

    print("\n" + "Введите колличество дающих разрешений, дающего артефактом при экипировке и использовании: ")
    i = input()
    if i == "":
        i = 0
    i = int(i)
    z = 0
    list_of_permissions_use_to = []
    for z in range(i):
        with open(path_to_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            counter = int(data["number"])
            smth_idk = len(str(counter))
            number = '0' * (16 - smth_idk) + str(counter)
            print("\n" + "Введите номер разрешения.[" + str(
                z) + "] (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                  " Если вы ничего не введёте, он будет использован по умолчанию)")
            permission = str(input())
            permission.replace(" ", '')
            if permission == "":
                permission = number
                counter = counter + 1
            list_of_permissions_use_to.append(permission)
            smth_idk = len(str(counter))
            number = '0' * (16 - smth_idk) + str(counter)
            data["number"] = number
            with open(path_to_file, "w", encoding="utf-8") as file_1:
                json.dump(data, file_1, indent=4, ensure_ascii=False)
    return {
        "SP_GIVES": sp_gives_use_to,
        "MP_GIVES": mp_gives_use_to,
        "IP_GIVES": ip_gives_use_to,
        "PP_GIVES": pp_gives_use_to,
        "AP_GIVES": ap_gives_use_to,
        "FP_GIVES": fp_gives_use_to,
        "LP_GIVES": lp_gives_use_to,
        "CP_GIVES": cp_gives_use_to,
        "BP_GIVES": bp_gives_use_to,
        "FIRE_RES_GIVE_THING": fire_res_gives_use_to,
        "WATER_RES_GIVE_THING": water_res_gives_use_to,
        "WIND_RES_GIVE_THING": wind_res_gives_use_to,
        "DIRT_RES_GIVE_THING": dirt_res_gives_use_to,
        "LIGHTNING_RES_GIVE_THING": lightning_res_gives_use_to,
        "HOLY_RES_GIVE_THING": holy_res_gives_use_to,
        "CURSE_RES_GIVE_THING": curse_res_gives_use_to,
        "CRUSH_RES_GIVE_THING": crush_res_gives_use_to,
        "CUT_RES_GIVE_THING": cut_res_gives_use_to,
        "STAB_RES_GIVE_THING": stab_res_gives_use_to,
        "FIRE_DAMAGE_GIVES_THING": fire_damage_gives_use_to,
        "WATER_DAMAGE_GIVES_THING": water_damage_gives_use_to,
        "WIND_DAMAGE_GIVES_THING": wind_damage_gives_use_to,
        "DIRT_DAMAGE_GIVES_THING": dirt_damage_gives_use_to,
        "LIGHTNING_DAMAGE_GIVES_THING": lightning_damage_gives_use_to,
        "HOLY_DAMAGE_GIVES_THING": holy_damage_gives_use_to,
        "CURSE_DAMAGE_GIVES_THING": curse_damage_gives_use_to,
        "CRUSH_DAMAGE_GIVES_THING": crush_damage_gives_use_to,
        "CUT_DAMAGE_GIVES_THING": cut_damage_gives_use_to,
        "STAB_DAMAGE_GIVES_THING": stab_damage_gives_use_to,
        "CLEAR_DAMAGE_GIVES_THING": clear_damage_gives_use_to,
        "FIRE_ACCESS_GIVES_THING": fire_access_gives_use_to_thing,
        "WATER_ACCESS_GIVES_THING": water_access_gives_use_to_thing,
        "WIND_ACCESS_GIVES_THING": wind_access_gives_use_to_thing,
        "DIRT_ACCESS_GIVES_THING": dirt_access_gives_use_to_thing,
        "LIGHTNING_ACCESS_GIVES_THING": lightning_access_gives_use_to_thing,
        "HOLY_ACCESS_GIVES_THING": holy_access_gives_use_to_thing,
        "CURSE_ACCESS_GIVES_THING": curse_access_gives_use_to_thing,
        "BLEED_ACCESS_GIVES_THING": bleed_access_gives_use_to_thing,
        "NATURE_ACCESS_GIVES_THING": nature_access_gives_use_to_thing,
        "MENTAL_ACCESS_GIVES_THING": mental_access_gives_use_to_thing,
        "TWOHANDED_ACCESS_GIVES_THING": twohanded_access_gives_use_to_thing,
        "POLEARM_ACCESS_GIVES_THING": polearm_access_gives_use_to_thing,
        "ONEHANDED_ACCESS_GIVES_THING": onehanded_access_gives_use_to_thing,
        "STABBING_ACCESS_GIVES_THING": stabbing_access_gives_use_to_thing,
        "CUTTING_ACCESS_GIVES_THING": cutting_access_gives_use_to_thing,
        "CRUSHING_ACCESS_GIVES_THING": crushing_access_gives_use_to_thing,
        "SMALL_ARMS_ACCESS_GIVES_THING": small_arms_access_gives_use_to_thing,
        "SHIELDS_ACCESS_GIVES_THING": shields_access_gives_use_to_thing,
        "HEALTH_MAX_GIVES_THING": health_max_gives_use_to_thing,
        "MIND_MAX_GIVES_THING": mind_max_gives_use_to_thing,
        "STAMINA_MAX_GIVES_THING": stamina_max_gives_use_to_thing,
        "MANA_MAX_GIVES_THING": mana_max_gives_use_to_thing,
        "HUNGER_MAX_GIVES_THING": hunger_max_gives_use_to_thing,
        "INTOXICATION_MAX_GIVES_THING": intoxication_max_gives_use_to_thing,
        "HELMET_STATUS_GIVES_THING": helmet_status_gives_use_to_thing,
        "CHEST_STATUS_GIVES_THING": chest_status_gives_use_to_thing,
        "SHOES_STATUS_GIVES_THING": shoes_status_gives_use_to_thing,
        "GLOVES_STATUS_GIVES_THING": gloves_status_gives_use_to_thing,
        "ITEM_SLOT_GIVES_THING": item_slot_gives_use_to_thing,
        "LIST_PERMISSION_GIVES": list_of_permissions_use_to
    }


def thingCreate():
    global id_permission_equip_to, id_permission_use_to, id_gives_equip_to, id_gives_use_to
    check_file = os.path.exists('Things')
    if check_file:
        print("Введите название артефакта")
        thing_name = input()
        thing_name.lower()
        thing_name.replace(" ", '_')
        if os.path.exists('Things/' + thing_name):
            print("Данный артефакт уже существует")
            thingCreate()
        else:
            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер предмета. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_thing = str(input())
            id_thing.replace(" ", "")
            if id_thing == "":
                id_thing = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                with open(path_to_file, "w", encoding="utf-8") as file:
                    json.dump(data, file,indent=4, ensure_ascii=False)
                    file.close()

            print("\n" + "Введите прочность артефакта: нынешнюю и максимальную ")
            durability_now = str(input())
            nothingGiver(durability_now)
            print(durability_now)
            durability_max = str(input())
            nothingGiver(durability_max)
            print("Ввердите вес артефакта: ")
            weight = str(input())
            nothingGiver(weight)
            print("Введите стоимость купли и продажи артефакта: ")
            cost_thing_buy = str(input())
            nothingGiver(cost_thing_buy)
            cost_thing_sell = str(input())
            nothingGiver(cost_thing_sell)

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер требования для экипировки артефакта. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_permission_equip_to = str(input())
            id_permission_equip_to.replace(" ", "")
            if (id_permission_equip_to == "") or (
                    str(data["THING_BUILDER"]["EQUIP_TO"].keys()).count(id_permission_equip_to) == 0):
                id_permission_equip_to = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                equip_to = requirements_equip_to()
            else:
                equip_to = data["THING_BUILDER"]["EQUIP_TO"][id_permission_equip_to]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            print("\n" + "ЭТАП ТРЕБОВАНИЯ ДЛЯ ЭКИПИРОВКИ ПРОЙДЕН")

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер требования для экипировки и использования артефакта. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_permission_use_to = str(input())
            id_permission_use_to.replace(" ", "")
            if (id_permission_use_to == "") or (
                    str(data["THING_BUILDER"]["USE_TO"].keys()).count(id_permission_use_to) == 0):
                id_permission_use_to = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                use_to = requirements_use_to()
            else:
                use_to = data["THING_BUILDER"]["USE_TO"][id_permission_use_to]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            print("\n" + "ЭТАП ТРЕБОВАНИЯ ДЛЯ ИСПОЛЬЗОВАНИЯ ПРОЙДЕН")

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер награды за экипировку артефакта. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_gives_equip_to = str(input())
            id_gives_equip_to.replace(" ", "")
            if (id_gives_equip_to == "") or (
                    str(data["THING_BUILDER"]["ABLE_TO_EQUIP"].keys()).count(id_gives_equip_to) == 0):
                id_gives_equip_to = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                able_to_equip = thing_give_able_to_equip()
            else:
                able_to_equip = data["THING_BUILDER"]["ABLE_TO_EQUIP"][id_gives_equip_to]
            with open(path_to_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            print("\n" + "ЭТАП НАГРАДЫ ЗА ЭКИПИРОВКУ ПРОЙДЕН")

            with open(path_to_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                counter = int(data["number"])
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
            print(
                "\n" + "Введите номер награды за экипировку артефакта. (Авотматически сгенерированный ключ имеет номер: " + number + "." + "\n" +
                " Если вы ничего не введёте, он будет использован по умолчанию)")
            id_gives_use_to = str(input())
            id_gives_use_to.replace(" ", "")
            if (id_gives_use_to == "") or (
                    str(data["THING_BUILDER"]["ABLE_TO_USE"].keys()).count(id_gives_use_to) == 0):
                id_gives_use_to = number
                counter = counter + 1
                smth_idk = len(str(counter))
                number = '0' * (16 - smth_idk) + str(counter)
                data["number"] = number
                able_to_use = thing_give_able_to_use()
            else:
                able_to_use = data["THING_BUILDER"]["ABLE_TO_USE"][id_gives_use_to]
            with open("Things/THING.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.close()

            print("\n" + "ЭТАП НАГРАДЫ ЗА ИСПОЛЬЗОВАНИЕ ПРОЙДЕН")

            thing = {
                'THING_NAME': thing_name,
                'THING_STATUSES':
                    {
                        'ARTEFACT_WEARED_THING': 0,
                        'COSTS_THING_BUY': cost_thing_buy,
                        'COSTS_THING_SELL': cost_thing_sell,
                        'COST_PER_REPUTATION': 0,
                        'DURABILITY_MAX': durability_max,
                        'DURABILITY_NOW': durability_now,
                        'WEIGHT_GIVES': weight,
                        'LIST_OF_IDS': [id_thing, id_permission_equip_to, id_permission_use_to, id_gives_equip_to,
                                        id_gives_use_to]
                    },
                'REQUIREMENTS':
                    {
                        'EQUIP_TO': equip_to,
                        'USE_TO': use_to
                    },
                'THING_GIVE':
                    {
                        'ABLE_TO_EQUIP': able_to_equip,
                        'ABLE_TO_USE': able_to_use
                    }
            }

            things = {"THING_BUILDER": {"THING": {id_thing: thing}}}
            with open(path_to_file, "r", encoding="utf-8") as json_file:
                file_content = json_file.read().strip()
                json_file.close()
                if not file_content:
                    with open(path_to_file, "w", encoding="utf-8") as json_file:
                        json.dump({}, json_file, ensure_ascii=False)
                else:
                    with open(path_to_file, "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)
                print(str(data.keys()))
                print(str(data.keys()).count("THING"))
            if str(data.keys()).count("THING") == 0:
                with open(path_to_file, "w", encoding="utf-8") as json_file:
                    json.dump(things, json_file, indent=4, ensure_ascii=False)
                    print("ФАЙЛ ПУСТОЙ, ПРИКОЛИСЬ!")
            else:
                with open(path_to_file, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                with open(path_to_file, "w", encoding="utf-8") as json_file:
                    print(data)
                    data["THING_BUILDER"]["THING"][id_thing] = thing
                    data["THING_BUILDER"]["EQUIP_TO"][id_permission_equip_to] = equip_to
                    data["THING_BUILDER"]["USE_TO"][id_permission_use_to] = use_to
                    data["THING_BUILDER"]["ABLE_TO_EQUIP"][id_gives_equip_to] = able_to_equip
                    data["THING_BUILDER"]["ABLE_TO_USE"][id_gives_use_to] = able_to_use
                    print(data)
                    json.dump(data, json_file, indent=4, ensure_ascii=False)
                    json_file.close()


def abillitiesCreate():
    print("Пока здесь ничего")


def maker_starter():
    global x
    while x != 0:
        print(
            "что вы хотите сделать?" + "\n" + "Чтобы добавить расу введите 1. " + "\n" + "Чтобы добавить артефакт введите 2.")
        x = int(input())
        if x == 1:
            raceCreate()
        if x == 2:
            thingCreate()
        if x == 3:
            abillitiesCreate()
        if x != 1 and x != 2:
            print("Неверная команда, попробуйте ещё раз.")
            maker_starter()


maker_starter()
