import wordcloud
import jieba
import imageio
import matplotlib.pyplot as plt
import os


def getChoice(notice, range_a, range_b):
    num = input(notice)
    while True:
        if num.isnumeric() and range_a <= int(num) <= range_b:
            return int(num)
        else:
            print("输入有误，请确定选择范围为[{}, {}]".format(range_a, range_b))
            num = input("请重新输入: ")


def readFile(file_name):
    while True:
        if file_name.endswith('.txt') is not True:
            file_name += '.txt'
        try:
            file = open(file_name, "r", encoding='utf-8')
            t = file.read()
            file.close()
            return t
        except FileNotFoundError:
            print("文件不存在，请确认文件路径是否正确(形如: C:\\Users\\python.txt)")
            file_name = input("请重新输入: ")
        except UnicodeDecodeError:
            print("文件格式错误，请确认是否为txt格式(形如: C:\\Users\\python.txt)")
            file_name = input("请重新输入: ")


def cutWords(txt):
    choice = getChoice("是否需要添加词汇<1>是 <2>否 【添加一些你认为不是词语但是不可分割的词语。比如\"小泽工作室\"中的\"小泽\"\n"
                       "对于字典来说不是词语，在分割时会被分为\"小\"和\"泽\"为了不这样，就需要将\"小泽\"添加到词典中】", 1, 2)
    if choice == 1:
        word = input("请输入不可分割词汇(输入-1结束): ")
        while word != '-1':
            jieba.add_word(word)
            print("添加词汇成功")
            word = input("请输入不可分割词汇(输入-1结束): ")
    print("\n正在分词...")
    ls = jieba.cut(txt)
    return " ".join(ls)


def getImage(file_name):
    while True:
        try:
            mask = imageio.imread(file_name)
            return mask
        except FileNotFoundError:
            print("文件不存在，请确认文件路径是否正确(形如: C:\\Users\\picture.png)")
            file_name = input("请重新输入: ")
        except UnicodeDecodeError:
            print("文件格式错误，请确认是否为图片格式png, jpg等(形如: C:\\Users\\picture.png)")
            file_name = input("请重新输入: ")


def getFont():
    font_path = input("请输入自己所在路径(形如C:\\Windows\\Fonts\\Segoe Script\\segoesc.ttf): ")
    while os.path.exists(font_path) is not True:
        font_path = input("字体路径有误，请重新输入(形如C:\\Windows\\Fonts\\Segoe Script\\segoesc.ttf): ")
    if font_path.endswith('.ttf') is not True:
        font_path += '.ttf'
    return font_path


def main():
    print("@@@@@@@@欢迎来到词云生成器@@@@@@@@")
    file_name = input("请输入txt文档所在路径: ")
    file_info = readFile(file_name)
    print("文件内容读取成功")
    txt = cutWords(file_info)
    main_choice = getChoice("是否要改变词云形成形状？<1>是 <2>否 ", 1, 2)
    color_mask = None
    if main_choice == 1:
        file_name = input("请输入形状图片所在路径: ")
        color_mask = getImage(file_name)
        print("获取形状图片信息成功")
        image_colors = wordcloud.ImageColorGenerator(color_mask)
    plt.ion()
    while True:
        plt.close(1)
        back_color = input("请输入背景颜色的英文单词(red, black, white等): ")
        scale = getChoice("请输入图片清晰度(1比较模糊, 4较为清晰) ", 1, 100)

        choice = getChoice("是否使用默认字体<1>是 <2>否 ", 1, 2)
        font_path = "msyh.ttc"
        if choice == 2:
            font_path = getFont()

        repeat = False
        choice = getChoice("是否允许词汇重复出现<1>是 <2>否 ", 1, 2)
        if choice == 1:
            repeat = True

        max_words = getChoice("请输入最大出现词汇数量(默认200): ", 1, 99999)

        print("正在生成词云，时间可能较长，请稍后。。。(P.S. 显示时图片可能较模糊，但保存后图片会很清晰)")
        w = wordcloud.WordCloud(font_path=font_path,
                                background_color=back_color,
                                width=1000, height=700,
                                mask=color_mask,
                                scale=scale,
                                repeat=repeat,
                                max_words=max_words)

        w.generate(txt)
        if main_choice == 1:
            choice = getChoice("词云底色是否要与形状图片相同<1>是 <2>否 ", 1, 2)
            if choice == 1:
                w.recolor(color_func=image_colors)
        print("生成图片中。。。")
        plt.figure(1)
        plt.imshow(w)
        plt.axis('off')
        plt.pause(0.001)
        plt.show()
        if getChoice("是否满意<1>是 <2>否 ", 1, 2) == 1:
            break

    name = input("请输入保存图片名: ")
    print("图片保存中。。。")
    w.to_file(name + ".png")
    name = input("图片保存成功！")


main()
