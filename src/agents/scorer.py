import json

def calculate_score(data):
    # 身体参数
    age_score = 0
    if data["Age"] < 18:
        age_score = 15
    elif 18 <= data["Age"] <= 40:
        age_score = 25
    elif 41 <= data["Age"] <= 60:
        age_score = 15
    else:
        age_score = 10

    bmi = data["Weight"] / (data["Height"] ** 2)
    bmi_score = 0
    if bmi < 18.5:
        bmi_score = 10
    elif 18.5 <= bmi <= 24.9:
        bmi_score = 30
    elif 25 <= bmi <= 29.9:
        bmi_score = 20
    else:
        bmi_score = 5

    family_history_score = 10 if data["family_history_with_overweight"] == "yes" else 20

    obesity_class_score = 0
    if data["NObeyesdad"] == "Insufficient_Weight":
        obesity_class_score = 25
    elif data["NObeyesdad"] == "Normal_Weight":
        obesity_class_score = 30
    elif data["NObeyesdad"] == "Overweight_Level_I":
        obesity_class_score = 20
    elif data["NObeyesdad"] == "Overweight_Level_II":
        obesity_class_score = 15
    elif data["NObeyesdad"] == "Obesity_Level_I":
        obesity_class_score = 10
    elif data["NObeyesdad"] == "Obesity_Level_II":
        obesity_class_score = 5
    elif data["NObeyesdad"] == "Obesity_Level_III":
        obesity_class_score = 0

    # 饮食习惯
    favc_score = 10 if data["FAVC"] == "yes" else 20

    fcvc_score = 0
    if data["FCVC"] == 3:
        fcvc_score = 30
    elif data["FCVC"] == 2:
        fcvc_score = 20
    else:
        fcvc_score = 10

    ncp_score = 0
    if data["NCP"] == 3:
        ncp_score = 20
    elif data["NCP"] == 1:
        ncp_score = 10
    else:
        ncp_score = 15

    caec_score = 0
    if data["CAEC"] == "no":
        caec_score = 20
    elif data["CAEC"] == "Sometimes":
        caec_score = 15
    elif data["CAEC"] == "Frequently":
        caec_score = 12
    else:
        caec_score = 5

    # 运动与生活方式
    smoke_score = 0 if data["SMOKE"] == "no" else 20

    ch2o_score = 0
    if data["CH2O"] >= 2:
        ch2o_score = 20
    elif 1 <= data["CH2O"] < 2:
        ch2o_score = 15
    else:
        ch2o_score = 5

    scc_score = 20 if data["SCC"] == "yes" else 10

    faf_score = 0
    if data["FAF"] >= 5:
        faf_score = 30
    elif 3 <= data["FAF"] < 5:
        faf_score = 20
    elif 1 <= data["FAF"] < 3:
        faf_score = 10
    else:
        faf_score = 5

    tue_score = 0
    if data["TUE"] < 2:
        tue_score = 20
    elif 2 <= data["TUE"] < 4:
        tue_score = 15
    else:
        tue_score = 10

    # 不良习惯与环境
    calc_score = 0
    if data["CALC"] == "no":
        calc_score = 20
    elif data["CALC"] == "Sometimes":
        calc_score = 15
    else:
        calc_score = 5

    mtrans_score = 0
    if data["MTRANS"] == "Bike":
        mtrans_score = 20
    elif data["MTRANS"] == "Walking":
        mtrans_score = 16
    elif data["MTRANS"] == "Public_Transportation":
        mtrans_score = 15
    else:
        mtrans_score = 10

    # 计算总分
    print(age_score, bmi_score, family_history_score, obesity_class_score, favc_score, fcvc_score, ncp_score, caec_score, smoke_score, ch2o_score, scc_score, faf_score, tue_score, calc_score, mtrans_score)
    total_score = ((age_score + bmi_score + family_history_score + obesity_class_score) * 0.40 +
                   (favc_score + fcvc_score + ncp_score + caec_score) * 0.25 +
                   (smoke_score + ch2o_score + scc_score + faf_score + tue_score) * 0.25 +
                   (calc_score + mtrans_score) * 0.1)

    total_score = round(total_score, 2)
    return total_score

# 读取JSON文件
with open('../data/resident.json', 'r') as file:
    datas = json.load(file)

print(len(datas))

# 计算分数
for data in datas:
    score = calculate_score(data)
    print(score)
    data["score"] = score

with open('../data/resident.json', 'w') as file:
    json.dump(datas, file, indent=4) 


