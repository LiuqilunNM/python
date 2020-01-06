## 页面介绍
页面有三个，分别是**受欢迎的小说类型**、**作家排榜**和**纵横小说总数据**，其中**受欢迎的小说类型**和**作家排榜**都有可交互的图表并配上相应的故事，**纵横小说总数据**则是有2014到2019的各类型小说排行的数据，还有作家收入排行的数据表可以查看。

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
在各个页面的左上角有一个点击查找的下拉框，可以从当前页面跳转到另外的两个页面，其中总数据的图标中可以查看历年来的各项小说类型排行的图表。

pythonanywhere(http://kalent.pythonanywhere.com/)

python_code(https://github.com/LiuqilunNM/python)
