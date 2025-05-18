import numpy as np
import subprocess
import time
import cv2

# 用于生成字符画的像素
pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"


# 按帧读取视频
def video2imgs(video_name, size):
    """
    :param video_name: 字符串, 视频文件的路径
    :param size: 二元组，(宽, 高)，用于指定生成的字符画的尺寸
    :return: 一个img对象的列表，img对象实际上就是 numpy.ndarray 数组
    """

    img_list = []

    # 从指定文件创建一个VideoCapture对象
    cap = cv2.VideoCapture(video_name)

    # 如果cap对象已经初始化完成了，就返回true，换句话说这是一个 while true 循环
    while cap.isOpened():
        # cap.read() 返回值介绍：
        # ret 表示是否读取到图像
        # frame 为图像矩阵，类型为 numpy.ndarry.
        ret, frame = cap.read()
        if ret:
            # 转换成灰度图
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # resize 图片，保证图片转换成字符画后，能完整地在命令行中显示
            img = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)

            # 分帧保存转换结果
            img_list.append(img)
        else:
            break

    # 结束时要释放空间
    cap.release()

    return img_list


# 图像转化为字符画
def img2chars(img):
    """
    :param img: numpy.ndarray, 图像矩阵
    :return: 字符串的列表：图像对应的字符画，其每一行对应图像的一行像素
    """
    res = []

    # 灰度是用8位表示的，最大值为255。
    # 这里将灰度转换到0-1之间
    # 使用 numpy 的逐元素除法加速，这里 numpy 会直接对 img 中的所有元素都除以 255
    percents = img / 255

    # 将灰度值进一步转换到 0 到 (len(pixels) - 1) 之间，这样就和 pixels 里的字符对应起来了
    # 同样使用 numpy 的逐元素算法，然后使用 astype 将元素全部转换成 int64 值
    indexes = (percents * (len(pixels) - 1)).astype(np.int64)

    # 要注意这里的顺序和 之前的 size 刚好相反（numpy 的 shape 返回 (行数、列数)）
    height, width = img.shape
    for row in range(height):
        line = ""
        for col in range(width):
            index = indexes[row][col]
            # 添加字符像素（最后面加一个空格，是因为命令行有行距却没几乎有字符间距，用空格当间距）
            line += pixels[index] + " "
        res.append(line)

    return res


# 转换所有的帧
def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))

    return video_chars


# 播放字符视频
def play_video(video_chars):
    """
    播放字符视频
    :param video_chars: 字符画的列表，每个元素为一帧
    :return: None
    """

    # 获取字符画的尺寸
    width, height = len(video_chars[0][0]), len(video_chars[0])

    for pic_i in range(len(video_chars)):
        # 显示 pic_i，即第i帧字符画
        for line_i in range(height):
            # 将pic_i的第i行写入第i列。
            print(video_chars[pic_i][line_i])
        time.sleep(1 / 24)  # 粗略地控制播放速度。

        # 调用 shell 命令清屏
        # subprocess.run("clear", shell=True) # linux 版
        subprocess.run("cls", shell=True)  # cmd ，windows 版


if __name__ == "__main__":
    imgs = video2imgs(input(), (64, 48))
    video_chars = imgs2chars(imgs)
    input("转换完成，按回车键开始播放！")
    play_video(video_chars)
