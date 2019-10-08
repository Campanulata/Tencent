from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('z.xlsx')

df = df[['姓名','核心课程第4节作业']]
df['核心课程第4节作业'].astype('int')
df=df[df['核心课程第4节作业']<1000]
print(df)
new_worlds = " ".join(df['姓名'])
# 参照图片
coloring = np.array(Image.open("./img/lz3.jpg"))

# simkai.ttf 必填项 识别中文的字体，例：simkai.ttf，
my_wordcloud = WordCloud(repeat=False,background_color="white", max_words=800,font_step=1, 
                     mask=coloring, max_font_size=200, random_state=30, scale=1,font_path="./img/simkai.ttf").generate(new_worlds)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 保存图片
my_wordcloud.to_file('./img/wordcloud.png')