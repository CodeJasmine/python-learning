# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud

# 构建并配置词云对象
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#6c909e',
    colormap='Pastel1',
    font_path='./res/font/SimHei.ttf'
)

# 调用jieba的cut方法对原始文本进行中文分词，得到string
txt = '如果你不曾来过，我的生命一片荒芜\
        单调色从不斑斓，瘦弱的黑白线从不宽阔\
        也不会有极致的喜悦，看一眼照片都心花怒放\
        如果你不曾来过，我的希望一片空白\
        听不出情歌的滋味，体会不出泪水咸淡的忧伤\
        也不会记得拥抱，想融化在你的身旁\
        光明路和芒山路我终于记住了\
        等你的每一天，我走过好几遍\
        如果有下次，我认路了\
        不用你送我，我送你，陪着才能走完\
        快到第一次相遇的时间了\
        我就在原地，怎样我都不怪你\
        我习惯了等你的出现\
        来，不来，过去和现在都不是我的终点\
        我将你存进银河，满目星辉都是你\
        我将你揉进风尘，四季轮换都相遇'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出
w.to_file('./res/img/output4.png')
