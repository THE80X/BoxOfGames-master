import os
import json

i = 0
n = 0
path = "F:\Pythonchick\BotVk\Races"

for root, dirs, files in os.walk(path):
    for file in files:
        if (file.endswith(".json")):
            i = i + 1
            print(os.path.join(root, file))
files_to_check = [0] * i

for root, dirs, files in os.walk(path):
    for file in files:
        if (file.endswith(".json")):
            files_to_check[n] = str(os.path.join(root, file)).replace('\\', '//').replace('//', '/').replace(
                'F:/Pythonchick/BotVk/', '')
            n = n + 1

for x in range(i):
    with open(files_to_check[x], "r") as json_file:
        a = json.load(json_file)
        print(files_to_check[x])
        print(int(a["POINTS"]["START_POINTS"]["SP_START"]) +
              int(a["POINTS"]["START_POINTS"]["MP_START"]) +
              int(a["POINTS"]["START_POINTS"]["IP_START"]) +
              int(a["POINTS"]["START_POINTS"]["PP_START"]) +
              int(a["POINTS"]["START_POINTS"]["AP_START"]) +
              int(a["POINTS"]["START_POINTS"]["FP_START"]) +
              int(a["POINTS"]["START_POINTS"]["LP_START"]) +
              int(a["POINTS"]["START_POINTS"]["CP_START"]) +
              int(a["POINTS"]["START_POINTS"]["BT_START"]) - 20)

        print(int(a["POINTS"]["MAX_POINTS"]["SP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["MP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["IP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["PP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["AP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["FP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["LP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["CP_MAX"]) +
              int(a["POINTS"]["MAX_POINTS"]["BT_MAX"]) - 20)

        print(int(a["RESISTANCES"]["FIRE_RES_START"]) +
              int(a["RESISTANCES"]["WATER_RES_START"]) +
              int(a["RESISTANCES"]["WIND_RES_START"]) +
              int(a["RESISTANCES"]["DIRT_RES_START"]) +
              int(a["RESISTANCES"]["LIGHTNING_RES_START"]) +
              int(a["RESISTANCES"]["HOLY_RES_START"]) +
              int(a["RESISTANCES"]["CURSE_RES_START"]) +
              int(a["RESISTANCES"]["CRUSH_RES_START"]) +
              int(a["RESISTANCES"]["CUT_RES_START"]) +
              int(a["RESISTANCES"]["STAB_RES_START"]))

        print(int(a["PERMISSIONS"]["FIRE_ACCESS_START"]) +
              int(a["PERMISSIONS"]["WATER_ACCESS_START"]) +
              int(a["PERMISSIONS"]["WIND_ACCESS_START"]) +
              int(a["PERMISSIONS"]["DIRT_ACCESS_START"]) +
              int(a["PERMISSIONS"]["LIGHTNING_ACCESS_START"]) +
              int(a["PERMISSIONS"]["HOLY_ACCESS_START"]) +
              int(a["PERMISSIONS"]["CURSE_ACCESS_START"]) +
              int(a["PERMISSIONS"]["BLEED_ACCESS_START"]) +
              int(a["PERMISSIONS"]["NATURE_ACCESS_START"]) +
              int(a["PERMISSIONS"]["MENTAL_ACCESS_START"]) +
              int(a["PERMISSIONS"]["TWOHANDED_ACCESS_START"]) +
              int(a["PERMISSIONS"]["POLEARM_ACCESS_START"]) +
              int(a["PERMISSIONS"]["ONEHANDED_ACCESS_START"]) +
              int(a["PERMISSIONS"]["STABBING_ACCESS_START"]) +
              int(a["PERMISSIONS"]["CUTTING_ACCESS_START"]) +
              int(a["PERMISSIONS"]["CRUSHING_ACCESS_START"]) +
              int(a["PERMISSIONS"]["SMALL_ARMS_ACCESS_START"]) +
              int(a["PERMISSIONS"]["SHIELDS_ACCESS_START"]))
