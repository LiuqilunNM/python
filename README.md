## 页面介绍
页面有四个，一个是我们设置的首页，底部有三个链接，一个是纵横中文网的首页，一个则是**查查数据**，里面有总的数据表和2014年到2019年历年来的各种类别书籍的数据图表，还有一张作家收入排行的数据表，还有一个是**读读故事**，里面有两个交互式的图表和两篇关于小说和作家收入的文章。

### 功能实现
实现数据的python——>HTML页面交互。

#### HTML文档描述
html文档
index.html 和index2.html主要实现的是将数据以交互式的形式呈现出来以及加上两篇文章，并对界面进行排版美化。

2014_all.html、2015_all.html、datazong.html、zuojia.html等则是关于数据图表的显示，使得数据更加容易看见和抓取。

#### PYTHON文档描述
一共三个个python文档
xiaoshou_web.py和flask_xiaoshou.py主要负责页面的显示和跳转,纵横小说数据清洗.py则是负责交互式数据图表的可视化

#### webapp的动作描述
在首页底部有三个点击框，分别对应的是三个不同的页面，**查查数据**里的左上方的下拉框有历年来的小说数据图表和作家收入以及总数据表，还有**读读故事**的对应链接，**读读故事**里有两个下拉框，分别是顶部时的左上方有点击跳转的下拉框和把页面拉到底部时左上方的下拉框，都可以把页面去到另外一篇文章等其他页面的链接。

我主要负责的是**读读故事**里的HTML页面制作排版以及对应的链接设置

pythonanywhere(http://kalent.pythonanywhere.com/)

python_code(https://github.com/LiuqilunNM/python)
