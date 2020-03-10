import wordcloud  # 生成词云库
import jieba  # 结巴分词库
import imageio  # 分析图片色彩
import matplotlib.pyplot as plt  # 做图库
import os  # 读取文件


# 读取文件内容
def readFile(fileName):
    while True:
        if fileName.endswith('.txt') is not True:
            fileName += '.txt'
        try:
            file = open(fileName, "r", encoding='utf-8')
            t = file.read()
            file.close()
            return t
        except FileNotFoundError:
            print("文件不存在，请确认文件路径是否正确(形如: C:\\Users\\python.txt)")
            fileName = input("请重新输入: ")
        except UnicodeDecodeError:
            print("文件格式错误，请确认是否为txt格式(形如: C:\\Users\\python.txt)")
            fileName = input("请重新输入: ")


# 读取图片内容
def getImage(fileName):
    while True:
        try:
            mask = imageio.imread(file_name)
            return mask
        except FileNotFoundError:
            print("文件不存在，请确认文件路径是否正确(形如: C:\\Users\\picture.png)")
            fileName = input("请重新输入: ")
        except UnicodeDecodeError:
            print("文件格式错误，请确认是否为图片格式png, jpg等(形如: C:\\Users\\picture.png)")
            fileName = input("请重新输入: ")


print("@@@@@@@@欢迎来到词云生成器@@@@@@@@")
file_name = ".\\test\\我有一个梦想.txt"  # 修改路径
file_info = readFile(file_name)
print("文件内容读取成功")

# 视情况执行还是不执行下面的代码 #
jieba.add_word("")  # 添加不切割词汇
txt = " ".join(jieba.cut(file_info))
file_name = ".\\test\\五角星.png"  # 输入形状图片所在路径
color_mask = getImage(file_name)
print("获取形状图片信息成功")
image_colors = wordcloud.ImageColorGenerator(color_mask)  # 获取图片形状底色
# 视情况执行还是不执行上面的代码 #

back_color = "white"  # 背景颜色的英文单词(red, black, white等):
scale = 3  # 图片清晰度(1比较模糊, 4较为清晰)
font_path = ".\\test\\手写风字体.ttf"  # 字体路径
repeat = False  # 是否允许重复出现词汇 True / False
max_words = 200  # "请输入最大出现词汇数量(默认200): "
print("正在生成词云，时间可能较长，请稍后。。。(P.S. 显示时图片可能较模糊，但保存后图片会很清晰)")
w = wordcloud.WordCloud(font_path=font_path,
                        background_color=back_color,
                        width=1000, height=700,  # 图片的宽和长
                        mask=color_mask,
                        scale=scale,
                        repeat=repeat,
                        max_words=max_words,
                        max_font_size=None,  # 最大字号，默认为None
                        min_font_size=4)  # 最小字号，默认为4
w.generate(txt)

# w.recolor(color_func=image_colors)  # 更改词云颜色，视情况要还是不要

print("生成图片中。。。")
plt.imshow(w)  # 生成图片
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图片
name = "test"  # 修改图片名
print("图片保存中。。。")
w.to_file(name + ".png")
name = input("图片保存成功！")
