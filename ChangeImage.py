from PIL import Image
def remove_red_box(image_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    red_threshold = 50  # 红色阈值设定
    for item in data:
        # 判断像素颜色是否为红色（R大于阈值，G和B小于阈值）
        #if item[0] > item[1] + item[2] and item[0] - item[1] > red_threshold and item[0] - item[2] > red_threshold:
        #    new_data.append((255, 255, 255, 0))  # 替换为透明像素
        #print(item[0],item[1],item[2])

        if item[0] > 220 and item[1] > 220 and item[2] > 220 :
            new_data.append((255, 255, 255, 0))  # 替换为透明像素
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save("D:\\Temp\\output.png", "PNG")
    
# 示例：去除图片中的红色边框
remove_red_box("D:\\Temp\\微信图片.png")
