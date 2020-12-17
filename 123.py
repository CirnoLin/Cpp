from tkinter import *
from tkinter.filedialog   import askopenfilename
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.messagebox import *

rows = 0  #记录数
page_num = 0   #总页数
page_idx = 0   #当前页数
page_show = 25 #每页记录数
arr = np.ones(6)
stock_df = pd.DataFrame(arr)  #DataFrame数据对象
names = ['日期','开盘价','最高价','收盘价','最低价','成交量','价格变动','涨跌幅','5日均价','10日均价','20日均价','5日均量','10日均量','20日均量']
# 设置中文字体，否则中文会出现方框状
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def showList(): #显示列表框数据
        list_items = []  #list框内容列表
        rows = stock_df.shape[0]
        start_idx = page_idx *  page_show  # 一页的开始记录下标
        end_idx = (page_idx + 1) *  page_show  #一页的结束记录下标
        show ="        "+  "  ".join([f"{i:8s}"for i in names]) #list框中标题行的字符串
        
        list_items.append(show)

        for idx in range(start_idx, end_idx + 1):
                if idx < rows :
                    rowdata =  stock_df.iloc[idx, ::]
                    lst = list(rowdata)
                   # lst_date=str(stock_df.index[idx])
                    lst = [f"{x:11.2f} " for x in lst]
                   # lst.insert(0,f"{lst_date[:10]:12s}")
                    
                    show = " ".join(lst)       #list框中一行数据的字符串
                    list_items.append(show)
        list_box_var.set(list_items)
def dataprocess():#对DataFrame对象数据进行数据清洗
        pass
def btn_open():
        global stock_df, page_num, rows
        filename = askopenfilename()
        
        stock_df = pd.read_excel(filename, sheet_name='2018-2020',names=names,index_col=0,skiprows=[0])
        #print(stock_df.head())
        #dataprocess()

        rows = stock_df.shape[0]
        page_num = rows / page_show

        showList()
def btn_next():#下一页
        global page_idx
        if page_idx == page_num-1:
                showinfo(title='最后一页提示', message='当前是最后一页。')
                return
        page_idx+=1
        showList()
def btn_previous():#前一页
        pass
def btn_fistpage():#第一页
        pass
def btn_lastpage():#最后一页
        pass

def btn_page():#指定一页
        pass


def btn_price():
        start_idx = page_idx *  page_show
        end_idx = (page_idx + 1) *  page_show

        x = np.arange(start_idx,end_idx+1)
        y = stock_df['收盘价'].values[start_idx:end_idx+1]


        plt.plot(x, y,
        color='#3589FF', # 线的颜色
        linestyle=':', # 线的风格
        linewidth=3, # 线的宽度
        marker='o', # 标记点的样式
        markerfacecolor='r', # 标记点的颜色
        markersize=10, # 标记点的大小
        alpha=0.7, # 图形的透明度
        label="sin(x)" #设置图例的label
        )
        #设置标题
        plt.title('国泰君安收盘价折线图')
        index_name = stock_df.index[start_idx:end_idx+1]
        index_name = [x.strftime('%Y-%m-%d') for x in index_name]
        plt.xticks(x,index_name)
        plt.gcf().autofmt_xdate() # 自动旋转日期标记
        plt.show()
def btn_change():
        start_idx = page_idx *  page_show
        end_idx = (page_idx + 1) *  page_show

        x = np.arange(0,end_idx+1-start_idx)
        y = stock_df['成交量'].values[start_idx:end_idx+1]

        # bar宽度
        bar_width = 0.5
        plt.bar(x, y, width=bar_width, alpha=0.7, label='成交量', color='b')

        # 显示数值标签
        for a, b in zip(x, y):
                plt.text(a, b, '%.0f' % b, ha='left', va= 'center', fontsize=7)
        #设置标题
        plt.title('国泰君安成交量柱状图')
        index_name = stock_df.index[start_idx:end_idx+1]
        index_name = [x.strftime('%Y-%m-%d') for x in index_name]
        plt.xticks(x+bar_width/2,index_name)
        plt.gcf().autofmt_xdate() # 自动旋转日期标记
        plt.show()



root = Tk()
root.title("国泰君安股价分析")   
width = 1000
height = 600
#设置窗口居屏幕中间显示
screenwidth = root.winfo_screenwidth()  
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)


top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)

bottom.pack(side=TOP,expand=YES,fill=BOTH)
top.config(bg = 'green')
bottom.config(bg = 'yellow')


btn1 = Button(top,text='打开', command=btn_open)
btn2 = Button(top,text='股价折线图', command=btn_price)
btn3 = Button(top,text='成交量图', command=btn_change)
btn4 = Button(top,text='下一页', command=btn_next)
#定义一个文本变量
list_box_var = StringVar()
#设置文本变量的值
show ="        "+  "  ".join([f"{i:8s}"for i in names])
list_box_var.set([show])

list_box = Listbox(bottom,listvar=list_box_var)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)

list_box.pack(side=TOP,expand=YES,fill=BOTH)


#list_items = ["a","b","c","d"]
#for item in list_items:
#    list_box.insert("end",item)#末尾插入


root.mainloop()
