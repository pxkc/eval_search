import json, xlwt
import glob
import ipdb

row = None
def read_score(jsonfile):
    # ipdb.set_trace()
    with open(jsonfile) as f:  # 将json文件转化为字典
        load_data = json.load(f)
        attribute_all = load_data["attributes"]
    # book = xlwt.Workbook()  # 创建excel文件
    # sheet = book.add_sheet('sheet2')  # 创建一个表
    # title = ['序号', '性别', '年龄阶段', '上身服饰', '下身服饰', '上身服饰颜色', '下身服饰颜色', '上身服饰纹理', '背包', '上身服饰细分类', '是否戴帽子', '是否戴眼镜',
    # '是否撑伞', '是否使用手机', '身体朝向', '是否吸烟', '是否有手提物', '交通工具', '上方截断','下方截断', '遮挡','是否是正常人体']
    # #
    # for col in range(len(title)):  # 存入第一行标题
    #     sheet.write(0, col, title[col])
    data = []
    data.append(attribute_all["gender"]["name"])
    data.append(attribute_all["age"]["name"])
    data.append(attribute_all["upper_wear"]["name"])
    data.append(attribute_all["lower_wear"]["name"])
    data.append(attribute_all["upper_color"]["name"])
    data.append(attribute_all["lower_color"]["name"])
    data.append(attribute_all["upper_wear_texture"]["name"])
    data.append(attribute_all["bag"]["name"])
    data.append(attribute_all["upper_wear_fg"]["name"])
    data.append(attribute_all["headwear"]["name"])
    data.append(attribute_all["glasses"]["name"])
    data.append(attribute_all["umbrella"]["name"])
    data.append(attribute_all["cellphone"]["name"])
    data.append(attribute_all["orientation"]["name"])
    data.append(attribute_all["smoke"]["name"])
    data.append(attribute_all["carrying_item"]["name"])
    data.append(attribute_all["vehicle"]["name"])
    data.append(attribute_all["upper_cut"]["name"])
    data.append(attribute_all["lower_cut"]["name"])
    data.append(attribute_all["occlusion"]["name"])
    data.append(attribute_all["is_human"]["name"])
    global row
    row += 1
    data.insert(0, row)
    for index in range(len(data)):  # 依次写入每一行
        sheet.write(row, index, data[index])
    # book.save('score.xls')

# if __name__ == "__main__":
if __name__ == "__main__":
    all_json_path = glob.glob('./results/*.json')
    row = 0
    book = xlwt.Workbook()  # 创建excel文件
    sheet = book.add_sheet('sheet2')  # 创建一个表
    title = ['序号', '性别', '年龄阶段', '上身服饰', '下身服饰', '上身服饰颜色', '下身服饰颜色', '上身服饰纹理', '背包', '上身服饰细分类', '是否戴帽子', '是否戴眼镜',
    '是否撑伞', '是否使用手机', '身体朝向', '是否吸烟', '是否有手提物', '交通工具', '上方截断','下方截断', '遮挡','是否是正常人体']
    for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])
    for path in all_json_path:
        print (row)
        read_score(path)
    book.save('score.xls')