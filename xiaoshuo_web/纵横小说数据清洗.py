#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df2014 = pd.read_csv('zonghengcsv/2014/2014_all.csv',encoding='gbk')


# In[3]:


df2014 = pd.read_csv('zonghengcsv/2014/2014_all.csv',encoding='gbk')
df2014.drop_duplicates('类别')['类别'].values.tolist()
票数2014=df2014[df2014.类别.isin(df2014.drop_duplicates('类别')['类别'].values.tolist())].groupby("类别").sum().drop(['时间'], axis=1)


# In[4]:


票数2014.columns=['2014']
票数2014


# In[5]:


df2015 = pd.read_csv('zonghengcsv/2015/2015_all.csv',encoding='gbk')
df2015.drop_duplicates('类别')['类别'].values.tolist()
票数2015=df2015[df2015.类别.isin(df2015.drop_duplicates('类别')['类别'].values.tolist())].groupby("类别").sum().drop(['时间'], axis=1)
票数2015.columns=['2015']
票数2015


# In[6]:


df2016 = pd.read_csv('zonghengcsv/2016/2016_all.csv',encoding='gbk')
df2016.drop_duplicates('类别')['类别'].values.tolist()
票数2016=df2016[df2016.类别.isin(df2016.drop_duplicates('类别')['类别'].values.tolist())].groupby("类别").sum().drop(['时间'], axis=1)
票数2016.columns=['2016']
票数2016


# In[7]:


df2017 = pd.read_csv('zonghengcsv/2017/2017_all.csv',encoding='gbk')
df2017.drop_duplicates('类别')['类别'].values.tolist()
票数2017=df2017[df2017.类别.isin(df2017.drop_duplicates('类别')['类别'].values.tolist())].groupby("类别").sum().drop(['时间'], axis=1)
票数2017.columns=['2017']
票数2017


# In[8]:


df2018 = pd.read_csv('zonghengcsv/2018/2018_all.csv',encoding='gbk')
df2018.drop_duplicates('类别')['类别'].values.tolist()
票数2018=df2018[df2018.类别.isin(df2018.drop_duplicates('类别')['类别'].values.tolist())].groupby("类别").sum().drop(['时间'], axis=1)
票数2018.columns=['2018']
票数2018


# In[9]:


df2019 = pd.read_csv('zonghengcsv/2019/2019_all.csv',encoding='gbk')
df2019.drop_duplicates('类别')['类别'].values.tolist()
票数2019=df2019[df2019.类别.isin(df2019.drop_duplicates('类别')['类别'].values.tolist())].groupby("类别").sum().drop(['时间'], axis=1)
票数2019.columns=['2019']
票数2019


# In[10]:


dataA=pd.merge(票数2014,票数2015,on='类别',how='outer')
dataB=pd.merge(dataA,票数2016,on='类别',how='outer')
dataC=pd.merge(dataB,票数2017,on='类别',how='outer')
dataD=pd.merge(dataC,票数2018,on='类别',how='outer')
data总=pd.merge(dataD,票数2019,on='类别',how='outer')


# In[11]:


data总.fillna(0)


# In[12]:


data总.to_csv('datazong.csv')


# In[19]:



from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Timeline




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
bar_datazoom_inside().render_notebook()


# In[14]:


bar_datazoom_inside().render('每年小说受欢迎变化.html')


# In[14]:


zuojia = pd.read_csv('zuojia.csv',encoding='gbk')
X轴=[str(x) for x in zuojia.loc[:,'网络作家']]
Y轴=[str(x) for x in zuojia.loc[:,'版税收入（万元）']]


# In[16]:


from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie


def pie_rosetype() -> Pie:
    v = Faker.choose()
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
pie_rosetype().render_notebook()


# In[ ]:





# In[ ]:




