#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Timeline
from pyecharts.charts import Pie

app = Flask(__name__)

data总=pd.read_csv('datazong.csv',encoding='utf-8')

zuojia = pd.read_csv('zuojia.csv',encoding='gbk')
X轴=[str(x) for x in zuojia.loc[:,'网络作家']]
Y轴=[str(x) for x in zuojia.loc[:,'版税收入（万元）']]


def bar_datazoom_inside() -> Timeline:
    tl = Timeline()
    for i in range(2014, 2020):
        c = (
            Bar(
            init_opts=opts.InitOpts(
                    animation_opts=opts.AnimationOpts(
                        animation_delay=1000, animation_easing="elasticOut"
                    )
                )
            )
            .add_xaxis(list(zip(list(data总.set_index('类别').index))))
            .add_yaxis("显示",list(data总["{}".format(i)]))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="纵横小说月票榜"),
                datazoom_opts=opts.DataZoomOpts(type_="inside"),
                visualmap_opts=opts.VisualMapOpts(type_="color", max_=250000, min_=200,pos_right='20',pos_top='middle'),
                toolbox_opts=opts.ToolboxOpts(),
            )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
        )
    )
        tl.add(c, "{}年".format(i))
    return tl


def pie_rosetype() -> Pie:
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(X轴, Y轴)],
            radius=["30%", "60%"],
            center=["50%", "60%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2018作家版税收入榜单",pos_top = 'middle'))
        .set_series_opts(
            label_opts=opts.TextStyleOpts(font_style='oblique')
        )
    )
    return c
@app.route("/")
def home():
   return render_template("home.html")

@app.route("/chart")
def index():
    return render_template("index.html")

@app.route("/data_sheet")
def datazong():
   return render_template("datazong.html")

@app.route("/barChart")
def get_bar_chart():
    tl = bar_datazoom_inside()
    return tl.dump_options_with_quotes()

@app.route("/2")
def index2():
    return render_template("index2.html")

@app.route("/barChart2")
def get_bar_chart2():
    c = pie_rosetype()
    return c.dump_options_with_quotes()

@app.route("/four")
def data1():
   return render_template("2014_all.html")

@app.route("/five")
def data2():
    return render_template("2015_all.html")

@app.route("/six")
def data3():
   return render_template("2016_all.html")

@app.route("/seven")
def data4():
    return render_template("2017_all.html")

@app.route("/eigth")
def data5():
    return render_template("2018_all.html")

@app.route("/nine")
def data6():
    return render_template("2019_all.html")

@app.route("/income")
def data7():
    return render_template("zuojia.html")


if __name__ == "__main__":
    app.run()

# In[ ]:





# In[ ]:





# In[ ]:




