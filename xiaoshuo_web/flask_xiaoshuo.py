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


@app.route("/chart")
def hello():
    tl = bar_datazoom_inside()
    return render_template('pyecharts.html',
                           myechart=tl.dump_options_with_quotes(),
                           host='http://chfw.github.io/jupyter-echarts/echarts',
                           script_list=tl.get_js_dependencies())


def bar_datazoom_inside() -> Timeline:
    tl = Timeline()
    for i in range(2014, 2020):
        c = (
            Bar()
            .add_xaxis(list(zip(list(data总.index))))
            .add_yaxis(list(data总["{}".format(i)]))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="纵横小说月票榜"),
                datazoom_opts=opts.DataZoomOpts(type_="inside"),
                visualmap_opts=opts.VisualMapOpts(type_="color", max_=250000, min_=200,pos_right='20',pos_top='middle'),
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


if __name__ == "__main__":
    app.run()


# In[ ]:




