import json

path = "Things/THING.json"

with open(path, "r", encoding="utf-8") as file:
    data = json.load(file)
some_string = ((str(data["RACES_BUILDER"]["NOW_POINTS"].keys())).split("[")[1]).split("]")[0].replace("'", "").replace(" ", "")
massive_1 = some_string.split(",")
massive_2 = massive_1

for i in range(len(massive_1)):
    sp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["SP_START"])
    mp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["MP_START"])
    ip_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["IP_START"])
    pp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["PP_START"])
    ap_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["AP_START"])
    fp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["FP_START"])
    lp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["LP_START"])
    cp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["CP_START"])
    bp_start_now = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_1[i]]["BP_START"])
    for j in range(len(massive_2)):
        sp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["SP_START"])
        mp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["MP_START"])
        ip_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["IP_START"])
        pp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["PP_START"])
        ap_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["AP_START"])
        fp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["FP_START"])
        lp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["LP_START"])
        cp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["CP_START"])
        bp_start_updatable = int(data["RACES_BUILDER"]["NOW_POINTS"][massive_2[j]]["BP_START"])
        if i != j:
            if (sp_start_now == sp_start_updatable) and \
                    (mp_start_now == mp_start_updatable) and \
                    (ip_start_now == ip_start_updatable) and \
                    (pp_start_now == pp_start_updatable) and \
                    (ap_start_now == ap_start_updatable) and \
                    (fp_start_now == fp_start_updatable) and \
                    (lp_start_now == lp_start_updatable) and \
                    (cp_start_now == cp_start_updatable) and \
                    (bp_start_now == bp_start_updatable):
                print(massive_1[i] + " эквивалентен " + massive_2[j])

print(len(massive_1))


some_string = ((str(data["RACES_BUILDER"]["MAX_POINTS"].keys())).split("[")[1]).split("]")[0].replace("'", "").replace(" ", "")
massive_1 = some_string.split(",")
massive_2 = massive_1

for i in range(len(massive_1)):
    sp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["SP_MAX"])
    mp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["MP_MAX"])
    ip_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["IP_MAX"])
    pp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["PP_MAX"])
    ap_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["AP_MAX"])
    fp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["FP_MAX"])
    lp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["LP_MAX"])
    cp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["CP_MAX"])
    bp_max_now = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_1[i]]["BP_MAX"])
    """print("\nЗначения для поиска по сравнениям\n" +
          str(sp_max_now) + " " +
          str(mp_max_now) + " " +
          str(ip_max_now) + " " +
          str(pp_max_now) + " " +
          str(ap_max_now) + " " +
          str(fp_max_now) + " " +
          str(lp_max_now) + " " +
          str(cp_max_now) + " " +
          str(bp_max_now) + "\n"
          )"""
    for j in range(len(massive_2)):
        sp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["SP_MAX"])
        mp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["MP_MAX"])
        ip_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["IP_MAX"])
        pp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["PP_MAX"])
        ap_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["AP_MAX"])
        fp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["FP_MAX"])
        lp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["LP_MAX"])
        cp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["CP_MAX"])
        bp_max_updatable = int(data["RACES_BUILDER"]["MAX_POINTS"][massive_2[j]]["BP_MAX"])
        if i != j:
            """print(
                str(sp_max_updatable) + " " +
                str(mp_max_updatable) + " " +
                str(ip_max_updatable) + " " +
                str(pp_max_updatable) + " " +
                str(ap_max_updatable) + " " +
                str(fp_max_updatable) + " " +
                str(lp_max_updatable) + " " +
                str(cp_max_updatable) + " " +
                str(bp_max_updatable)
            )"""
            if (sp_max_now == sp_max_updatable) and \
                    (mp_max_now == mp_max_updatable) and \
                    (ip_max_now == ip_max_updatable) and \
                    (pp_max_now == pp_max_updatable) and \
                    (ap_max_now == ap_max_updatable) and \
                    (fp_max_now == fp_max_updatable) and \
                    (lp_max_now == lp_max_updatable) and \
                    (cp_max_now == cp_max_updatable) and \
                    (bp_max_now == bp_max_updatable):
                print(massive_1[i] + " эквивалентен " + massive_2[j])


some_string = ((str(data["RACES_BUILDER"]["RESISTANCES"].keys())).split("[")[1]).split("]")[0].replace("'", "").replace(" ", "")
massive_1 = some_string.split(",")
massive_2 = massive_1

for i in range(len(massive_1)):
    fire_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["FIRE_RES_START"])
    water_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["WATER_RES_START"])
    wind_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["WIND_RES_START"])
    dirt_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["DIRT_RES_START"])
    lightning_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["LIGHTNING_RES_START"])
    holy_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["HOLY_RES_START"])
    curse_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["CURSE_RES_START"])
    cut_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["CUT_RES_START"])
    stab_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["STAB_RES_START"])
    crush_res_now = int(data["RACES_BUILDER"]["RESISTANCES"][massive_1[i]]["CRUSH_RES_START"])
    for j in range(len(massive_2)):
        fire_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["FIRE_RES_START"])
        water_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["WATER_RES_START"])
        wind_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["WIND_RES_START"])
        dirt_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["DIRT_RES_START"])
        lightning_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["LIGHTNING_RES_START"])
        holy_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["HOLY_RES_START"])
        curse_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["CURSE_RES_START"])
        cut_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["CUT_RES_START"])
        stab_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["STAB_RES_START"])
        crush_res_updatable = int(data["RACES_BUILDER"]["RESISTANCES"][massive_2[j]]["CRUSH_RES_START"])
        if i != j:
            if (fire_res_now == fire_res_updatable) and \
                    (water_res_now == water_res_updatable) and \
                    (wind_res_now == wind_res_updatable) and \
                    (dirt_res_now == dirt_res_updatable) and \
                    (lightning_res_now == lightning_res_updatable) and \
                    (holy_res_now == holy_res_updatable) and \
                    (curse_res_now == curse_res_updatable) and \
                    (cut_res_now == cut_res_updatable) and \
                    (stab_res_now == stab_res_updatable) and \
                    (crush_res_now == crush_res_updatable):
                print(massive_1[i] + " эквивалентен " + massive_2[j])


some_string = ((str(data["RACES_BUILDER"]["PERMISSIONS"].keys())).split("[")[1]).split("]")[0].replace("'", "").replace(" ", "")
massive_1 = some_string.split(",")
massive_2 = massive_1

for i in range(len(massive_1)):
    fire_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["FIRE_ACCESS_START"])
    water_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["WATER_ACCESS_START"])
    wind_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["WIND_ACCESS_START"])
    dirt_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["DIRT_ACCESS_START"])
    lightning_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["LIGHTNING_ACCESS_START"])
    holy_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["HOLY_ACCESS_START"])
    curse_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["CURSE_ACCESS_START"])
    bleed_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["BLEED_ACCESS_START"])
    nature_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["NATURE_ACCESS_START"])
    mental_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["MENTAL_ACCESS_START"])
    twohanded_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["TWOHANDED_ACCESS_START"])
    polearm_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["POLEARM_ACCESS_START"])
    onehanded_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["ONEHANDED_ACCESS_START"])
    stab_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["STABBING_ACCESS_START"])
    cut_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["CUTTING_ACCESS_START"])
    crush_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["CRUSHING_ACCESS_START"])
    small_arms_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["SMALL_ARMS_ACCESS_START"])
    shields_access_now = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_1[i]]["SHIELDS_ACCESS_START"])
    print("\n Начальные значения")
    print(str(fire_access_now) + " " +
          str(water_access_now) + " " +
          str(wind_access_now) + " " +
          str(dirt_access_now) + " " +
          str(lightning_access_now) + " " +
          str(holy_access_now) + " " +
          str(curse_access_now) + " " +
          str(bleed_access_now) + " " +
          str(nature_access_now) + " " +
          str(mental_access_now) + " " +
          str(twohanded_access_now) + " " +
          str(polearm_access_now) + " " +
          str(onehanded_access_now) + " " +
          str(stab_access_now) + " " +
          str(cut_access_now) + " " +
          str(crush_access_now) + " " +
          str(small_arms_access_now) + " " +
          str(shields_access_now) + "\n"
          )
    for j in range(len(massive_2)):
        fire_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["FIRE_ACCESS_START"])
        water_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["WATER_ACCESS_START"])
        wind_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["WIND_ACCESS_START"])
        dirt_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["DIRT_ACCESS_START"])
        lightning_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["LIGHTNING_ACCESS_START"])
        holy_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["HOLY_ACCESS_START"])
        curse_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["CURSE_ACCESS_START"])
        bleed_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["BLEED_ACCESS_START"])
        nature_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["NATURE_ACCESS_START"])
        mental_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["MENTAL_ACCESS_START"])
        twohanded_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["TWOHANDED_ACCESS_START"])
        polearm_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["POLEARM_ACCESS_START"])
        onehanded_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["ONEHANDED_ACCESS_START"])
        stab_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["STABBING_ACCESS_START"])
        cut_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["CUTTING_ACCESS_START"])
        crush_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["CRUSHING_ACCESS_START"])
        small_arms_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["SMALL_ARMS_ACCESS_START"])
        shields_access_updatable = int(data["RACES_BUILDER"]["PERMISSIONS"][massive_2[j]]["SHIELDS_ACCESS_START"])
        if i != j:
            print(str(fire_access_updatable) + " " +
                  str(water_access_updatable) + " " +
                  str(wind_access_updatable) + " " +
                  str(dirt_access_updatable) + " " +
                  str(lightning_access_updatable) + " " +
                  str(holy_access_updatable) + " " +
                  str(curse_access_updatable) + " " +
                  str(bleed_access_updatable) + " " +
                  str(nature_access_updatable) + " " +
                  str(mental_access_updatable) + " " +
                  str(twohanded_access_updatable) + " " +
                  str(polearm_access_updatable) + " " +
                  str(onehanded_access_updatable) + " " +
                  str(stab_access_updatable) + " " +
                  str(cut_access_updatable) + " " +
                  str(crush_access_updatable) + " " +
                  str(small_arms_access_updatable) + " " +
                  str(shields_access_updatable)
                  )
            if (fire_access_now == fire_access_updatable) and \
                    (water_access_now == water_access_updatable) and \
                    (wind_access_now == wind_access_updatable) and \
                    (dirt_access_now == dirt_access_updatable) and \
                    (lightning_access_now == lightning_access_updatable) and \
                    (holy_access_now == holy_access_updatable) and \
                    (curse_access_now == curse_access_updatable) and \
                    (bleed_access_now == bleed_access_updatable) and \
                    (nature_access_now == nature_access_updatable) and \
                    (mental_access_now == mental_access_updatable) and \
                    (twohanded_access_now == twohanded_access_updatable) and \
                    (polearm_access_now == polearm_access_updatable) and \
                    (onehanded_access_now == onehanded_access_updatable) and \
                    (small_arms_access_now == small_arms_access_updatable) and \
                    (shields_access_now == shields_access_updatable) and \
                    (cut_access_now == cut_access_updatable) and \
                    (stab_access_now == stab_access_updatable) and \
                    (crush_access_now == crush_access_updatable):
                print(massive_1[i] + " эквивалентен " + massive_2[j])


