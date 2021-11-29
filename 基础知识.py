

0、 dataframe 的生成 ：

    dates=['2017-12-01','2017-12-05','2017-12-17','2017-12-28','2018-01-05','2018-01-09']
    val=[5,2,3,6,1,7]
    df = pd.DataFrame(list(zip(dates, val)),
               columns =['date', 'val'])


1、变量名是区分大小写的。

2、字符串的查找：in() \ not in \ find()

3、列表系列：

    列表：[] -> 里面的数据类型不唯一

    列表的合并：extend()

    列表的添加/删除 ：insert(),pop("参数是数据的位置"), remove("具体的元素")

4、字典系列：“健”必须是唯一的

    字典的新建：dictDemo = {}

    元组 --> 字典 ： 字典 = dict(元组)

    keys() values() items()

4-2、
    关于set : print(set(d10['渠道'])) , set 是可以遍历的：
    for qd in set(d10['渠道']):
        print(qd)

5、元组系列：


6、形参，实参


7、匿名函数

    f = lambda x,y : x+y


8、列表的生成
    list1 = []
    list2 = []

    [m + n for i in list1 for n in list2]

9、map(function , agrs)
    a = map(lambda x ,y :x+y ,[1,2,3],[4,5,6])
    for i in a:
        print (i)

    map函数生成的结果序列不会直接把全部结果显示出来，要获取结果需要
    for 循环编列出来 ，也可以使用list 方法，将结果变成一个列表。

    b = list(map( lambda x ,y :x + y , [1,2,3], [4,5,6] ))
	

10、DataFrame 系列

    DataFrame 的新建：columns , index

11、pandas 导入外部数据

    pandas.read_x() : csv / excel

    参数：sheet_name / sheet 的顺序

          usecols:[ 列1,列2 ,, ]

          index_col:表示用 .xlsx 文件中的第几列做行索引

          nrows：需要导入的行数

          encoding = “utf-8” : Python 默认的编码格式就是utf-8
          如果是csv（.csv）格式的文件，那么在导入的时候需要把编码格式更改为 gbk.

          engine: 文件路径或者文件名中包含中文时 engine='python' encoding='utf-8-sig'
                    当调用read_csv()方法时，默认使用C语言作为解析语言，我们需要把默认值C更改为Python，
                        如果文件格式是CSV UTF-8(逗号分隔)(*.csv)，那么编码格式也需要跟着变为utf-8-sig，
                        如果文件格式是CSV(逗号分隔)(*.csv)格式，对应的编码格式则为gbk。


12、python导入SQL

    import pymysql

    eng = pymysql.connect(host='localhost' ,
                    user='user',
                    password='password',
                    db = 'databaseName',
                    charset = 'utf8'
    )

    pd.read_sql(sql , eng) # sql : 查询语句

13、缺失值删除

    df.dropna() : 默认是删除有缺失值的行（只要有缺失值，就删除）

    df.dropna(how = "all")

    df.dropna(subset=["age","sex"]) # 通过参数来删除age和sex中含有空数据的全部

    d1_ck=df.dropna(axis=0,how='any')
    如果 axis = 0，.dropna(axis) 方法将删除包含 NaN 值的任何行
    如果 axis = 1，.dropna(axis) 方法将删除包含 NaN 值的任何列

    print(df.isnull().sum().sum()) # 统计整个 dataframe 中的None 数量
    print(df.isnull().sum())        # 统计每列 中的None 数量
    print(df['city'].isnull().sum()) # 统计某列 中的None 数量




14、缺失值填充

    df.fillna(0) : 为缺失值填充 0

    df.fillna({"性别":"男" , "年龄":30 }) :为不同的列的缺失值填充不同的zhi

    d3['退件位置']=d3['退件位置'].fillna('仓内')

14-1、
    df['Age']  = df['Age'].fillna(df['Age'].mean())  # 用平均值填充空值

    df['Fare'] = df['Fare'].fillna(df['Fare'].mean())

    df['Embarked'] = df['Embarked'].fillna( df['Embarked'].value_counts().index[0]) # 用数量最多项填充


15、重复值删除

    df.drop_duplicates()

    df.drop_duplicates(subset=["姓名","学号"]) # 利用自定义列判断去重

    df.drop_duplicates(subset=["姓名"], keep = "last")
        # 默认是保留第一个相同值，可以自定义为最后一个（“last”）,
        # 也可以不保留（全部删除，keep = False）


16、异常值的检测与处理

    replace()

    df["年纪"].replace(240,33) # 将 年纪中 240 的替换为 33

    df.replace(np.NaN,0)

    df["年纪"].replace([250,260] ,30) # 将 年纪 中 250，260 替换为 30

    df["年纪"].replace({"A":"a" , "B":"b", "C":"c"}) # 将 年纪 中 250，260 替换为 30


17、数据类型的问题

    int  float  object  string  unicode  datetime

    info() : 获得每列的数据类型

    dtype: 获取某一列的数据类型

    df["唯一识别码"].dtype

    df["识别码"].astype("float64") # 将识别码 从int转为float


18、索引问题

    set_index()


19、重命名、重置索引

    df.rename(columns={"编号": "新编号" ,"名称":"新名称"})

    df.rename(index={ 1:"一" ,2:"二" ,3:"三"})

    df.rename(columns={ "":"", "":""} , index={1:"" ,2:"" })


20、索引(set_index 和 reset_index 是一对相反的操作)

    set_index([])  # 将columns 转化为 index
    --------------------------------------
        set_index(["column_02","column_01"])

    reset_index()  # 将index 转化为 columns  # 非常重要，尤其是在 groupby 方法操作中。
    --------------------------------------
        df.reset_index()          # 默认将全部index 转化为columns

        df.reset_index(level = 0) # 将第0级索引转化为columns
        df.reset_index(level = 1) # 将第1级索引转化为columns

        df.reset_index(drop = True) # 将原索引删除，不加入 columns


21、列选择或是行选择

    选取列：
    ------------------------------------
        通过列名：
        ========
            df['订单编号']

            df[["订单编号","姓名","日期"]]

        通过列序号：
        ==========
            df.iloc[:,[0,2]] # 获得第1列和第3列的数值

            df.iloc[:,0:3] # 获得连续列的数值(切片索引)


    选取行：
    ------------------------------------
    df.iloc[0:3] # 选择第一行到第四行



    选取特定的行并赋值：
    -------------------------------------
    titanic.loc[titanic['Embarked'] == 'S' , 'Embarked'] = 0
    titanic.loc[titanic['Embarked'] == 'C' , 'Embarked'] = 1
    titanic.loc[titanic['Embarked'] == 'Q' , 'Embarked'] = 2







22、选择符合条件的行

    df[(df["年纪"]< 200) & (df["编号"] < 102)]


23、行和列的共同选择[ix已经被官方取消了，推荐试用 iloc[] ,loc[]]

    # loc ：loc() 传入行列名称

        (1)普通索引 + 普通索引
            df.loc[["一","二"],["姓名","年纪","学校"]]

        (2)位置索引 + 位置索引
            df.iloc([0,1],[1,3])

        (3)布尔索引 + 普通索引
            df[df["年纪"] < 200 ]["订单编号","地址"]

        (4)切片索引 + 切片索引
            df.iloc[0:2,1:3]

        (5)切片索引+ 普通索引（普通索引用loc,切片索引用iloc,交叉索引用 ix）。这个组合要特别注意。
            df.ix[0:3 ,["姓名","识别码"]]


24、排序

    df.sort_values(by=["col02"])

    df.sort_values(by=["col"] ,ascend= False)

    df.sort_values(by = ["col1","col2"] , ascending= [True,False])


25、数值删除
        （1）删除列
            df.drop(["销售ID","成交时间"] ,axis=1)

            df.drop(df.columns[[3,4]],axis = 1)

            df.drop(columns = ["销售ID", "成交时间"])

        （2）删除行
            df.drop(["行名1","行名2"] ,axis =0)

            df.drop(df.index[[0,1]] ,axis=0) # 还可以传入行号。

            df.drop(index=["行1","行2"]) # 这个时候就不需要传入 axis参数了。

            删除特定的行：
                df[df["年纪"] < 30]


26、计数
    value_counts()

    df['销售Id'].value_counts()

    df['销售Id'].value_counts(normalize =True) # 获得占比

    df["销售Id"].unique()



27、数值查找
    df["年纪"].isin([21,31])


28、区间区分

    cut()方法 -- 默认：左开右闭（通过参数 right 调整 ）
        pd.cut(df[""] , , )

    df = pd.DataFrame()
    df['data'] = [0,7,4,2,8,6,5,8,1,10]
    df['cut']=pd.cut(df['data'],[0,2,4,6,8,10], labels=['0-2','2-4','4-6',' 6-8','8-10' ] , right =False ,include_lowest =True)
    print(df)

    qcut()方法: 没搞懂



29、插入数据

    列插入：
    -------
    df.insert(1,"商品类型",["类型1","类型2","类型3"]) # 在第2列处 插入一列

    df["商品类型"] = ["类型1","类型2","类型3"]


    行插入：
    -------






30、转置
        df.T

    索引重塑

        df.stack()

        df.unstack()

    长宽表转换



31、
	chaifenlie = df.iloc[0:100,8] # 获得第9列的数据，进行拆分
	lies = chaifenlie.str.split(',',expand=True) # 注意 expand的用意 


32、
    data = {'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou', 'Chongqing'],
           'year': [2016,2016,2015,2017,2016, 2016],
           'population': [2100, 2300, 1000, 700, 500, 500]}
    frame = pd.DataFrame(data, columns = ['year', 'city', 'population', 'debt'])

    # 使用apply函数, 如果city字段包含'ing'关键词，则'判断'这一列赋值为1,否则为0
        frame['panduan'] = frame.city.apply(lambda x: 1 if 'ing' in x else 0)

32-1、apply 的另外一个用法：

    data['淡旺季'] = data.apply(lambda x: x['salary']+ x['age'],axis=1)





33、

    id  attrs
    A 1,2,5,3
    B 3,1,2,5
    C 1,2,0,3
    D 1,7,5,3
    E 2,1,6,8
    我们想把他拆分成多列,做法如下:

    首先进行拆分 data_df = data_df[‘attrs’].str.split(’,’, expand=True)

    然后用pd.concat把多列加回data_df，pd.concat([], axis=1, names=new_names)

    合起来就是

    pd.concat([data_df, data_df[‘attrs’].str.split(’,’, expand=True)], axis=1,names=new_names)


34、

	writer=pd.ExcelWriter("C:/Users/wlt/Desktop/XXX.xls")

	mon1.to_excel(excel_writer=writer,sheet_name='201901')
	mon2.to_excel(excel_writer=writer,sheet_name='201902')
	writer.save()
	writer.close()

34-2、    def file_xlsx(name,df):
            bf =r'F:\PBI临时文件\JDW总表监控\{}.xlsx'.format(name)
            print(bf)
            writer = pd.ExcelWriter(bf)
            df.to_excel(writer,'sheet1',index=False)
            writer.save()

35、

	import pandas as pd

	df1 = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]}, columns=['a', 'b'])
	df2 = pd.DataFrame({'a':[7,8,9], 'b':[6,5,4]}, columns=['a', 'b'])

	def write_last_sheet():
	df1.to_excel('output2.xlsx', sheet_name='Sheet1', startcol=0, index=False)
	df2.to_excel('output2.xlsx', sheet_name='Sheet2', startcol=0, index=False)

	def write_multi_sheet():
	write = pd.ExcelWriter('output1.xlsx')
	df1.to_excel(write, sheet_name='Sheet1', startcol=0, index=False)
	df2.to_excel(write, sheet_name='Sheet2', startcol=0, index=False)
	write.save()

	write_last_sheet()
	write_multi_sheet()


36、

	writer=pd.ExcelWriter("C:/Users/wlt/Desktop/XXX.xls")

	mon1.to_excel(excel_writer=writer,sheet_name='201901')
	mon2.to_excel(excel_writer=writer,sheet_name='201902')
	mon3.to_excel(excel_writer=writer,sheet_name='201903')


37、copy 相关问题

	dataUpdata = mergeDataFrame[mergeDataFrame['计算列'] >0].copy()

    d1_ck = df[['order_no','退件位置']].copy(deep=True)

38、
	print([column for column in nihao if ('address' in column or 'Address' in column)])


39、

	nihao = pd.DataFrame(data)
	needDealNameColumn = [column for column in nihao if ('address' in column or 'Address' in column)]

	for i in needDealNameColumn:
		nihao[i] = nihao[i].map(
			lambda x: x.replace("，", "").replace(",", "") if type(x) == str else str(x).replace("，", "").replace(",", ""))

	print(nihao)
	

40、list 中获得 某个值的索引 
	dealDataPart02.columns.to_list().index("name")


41、数据块的结合(暂时就这么理解)

    concat : 上下连接（默认 是上下连接 ; 左右连接 [ 拆分合并的情况下这种方式用的比较多 ] -> : axis = 1 ）

    merge  : 左右连接

    data = {"nihao":[1,2,3,6] , "wohao":[53,45,34,76] , "dajiahao":[64,56,45,43] }
    nihao = pd.DataFrame(data)
    data2 = {"nihao":[2,3,5] , "wohao":[5443,4335,3434] , "dajiahao":[6453,55436,4235] }
    nihao2 = pd.DataFrame(data2)

    woh = pd.concat([nihao,nihao2]).reset_index(drop=True)
    print(woh)
    print('=================================================================================================')
    fsf = pd.merge(nihao,nihao2[['nihao','dajiahao']] ,left_on='nihao',right_on='nihao',how='left')
    print(fsf)

41-2:

    df_02 = pd.concat([df_01,
                       df_01.iloc[0:2, 8].str.split(',', expand=True)],
                       axis=1)

42、列的分裂

    pd.concat([dataFrameSiLunFirst,
               dataFrameSiLunFirst.iloc[0:rowNum, 8].str.split(',', expand=True)],
               axis=1)


43、数据查找 - query() : 这个方法其实不是很常用


44、累加函数


45、sample()

    df.sample(n=8) # 随机抽取 8行数据

    df.sample(frac = 0.6 , random_state = 2 ) # 随机抽取60% 的行，并且设置随机数种子，每次能抽取到一样的样本


46、 where() : 用来根据条件替换行或列中的值，如果满足条件，则保持原来的值，如果不满足，则替换为其他值
             : 用作全局范围内的替换

    df['age'].where(df['age'] > 5 , 0)


47、isin() , 也是一种过滤方法，

    years = ['2010','2014','2017']

    df[df.year.isin(years)]


48、pct_change() ,



49、rank() , 这是一个复杂的问题



50、melt() , 用于将宽表变成窄表 ，是 pivot() 透视逆转操作函数。

    df1 = pd.DataFrame({'city': {0: 'a', 1: 'b', 2: 'c'},
                        'day1': {0: 1, 1: 3, 2: 5},
                        'day2': {0: 2, 1: 4, 2: 6},
                          'id': {0: 423, 1: 343, 2: 633}
                        })

    print( df1 )
    print('=========================================')
    what = pd.melt(df1, id_vars=['city','id']) # id_vars 处填写的是不需要调整的字段
    print(what)



51、多条件的筛选

     1)---
        result = df[(df['age'] < 35) & (df['point'] < 75) | ~(df['state'] == 'NY')]

     2)---
        data = pd.DataFrame({'name':['sam','sanj','sam','sam','ji'] ,
                             'nianji':[12,56,98,62,45] ,
                             'add':['上海','南京','北京','温州','义乌'] } )
        nihao =  data[(data['name']== 'sam') & (data['nianji'].isin([98,62])) ]
        print(nihao)




52、
    mergeDataFrame.renames(columns={"appcode_abbrn_y": "UN_appcode_abbrn"}, inplace=True)

    appcode_abbrn_dict = {'DP': 6, 'GD': 5, 'BD': 4, 'MT': 3, 'EL': 2, 'UN': 1}

    mergeDataFrame['UN_appcode_abbrn_Num'] = mergeDataFrame['UN_appcode_abbrn'].map(appcode_abbrn_dict)


53、cut() | qcut()

    da = {"nihao":[121,198,34,567,445,156,248, 164,82,325,515] }
    daD = pd.DataFrame(da)
    print(daD['nihao'].min() , daD['nihao'].max())
    print('------------------------------------------------------')
    daD['分段1'] = pd.cut(daD['nihao'] ,[0,100,200,500,800],labels=[ '阶段一','阶段二','阶段三','阶段四'] )
    daD['分段3'] = pd.cut(daD['nihao'] , 4)
    print('-====================================================-')
    daD['分段4'] = pd.qcut(daD['nihao'],6)
    daD['分段2'] = pd.qcut(daD['nihao'] ,[0,0.1,0.36,0.85,1])
    print(daD['分段2'].value_counts() )
    print('******************************************************')
    print(daD)


54、list中去除None和 nan

    list_a=[None,1,1,3]
    while None in list_a:
        list_a.remove(None)

    print("--------------------------------")

    new_list=[]
    for elem in list_a:
        if not np.isnan(elem):
            new_list.append(elem)

    print('================================')

    综合两者：
        list_a=[elem if not np.isnan(elem) else None for elem in list_a ]
        while None in list_a:
            list_a.remove(None)

55、 isnan()


56、dataframe 的上下方向的集合
    2.result = df1.append(df4)
    3.result = df1.append([df2, df3])
    4.result = df1.append(df4, ignore_index=True)


57、两列数据组装成矩阵

    def nihao():
        lst_1 = list(range(8941, 10307, 5))  # 列
        lst_2 = list(range(3160, 3921,  5))  # 行
        lst_3 = []
        result = []

        for l2 in lst_2:
            tmp = []
            for l1 in lst_1:
                val =   float(l1/100),float(l2/100),round(l1/100 + 0.05,2),round(l2/100 + 0.05,2)
                result.append(val)
                tmp.append(val)
            lst_3.append(tmp)

        nihao = pd.DataFrame(lst_3, columns=lst_1, index=lst_2)
        # nihao.to_excel('xizang.xlsx')
        result = pd.DataFrame(result)
        print(result.shape)
        # result.to_excel('xizang_result.xlsx')


58、pdndas从数据库中抽取数据

    def fasdf():
        sql = 'SELECT * FROM `shange_othercity_qinghai`'
        con = pymysql.connect(host='192.168.10.221',
                                user='px',
                                password='123456',
                                db='fse_universe_keywords',
                                charset='utf8')
        data = pd.read_sql(sql ,con)
        # shanges = data['shange']
        shangeFenLie = data['shange'].str.split(',',expand=True)
        print(shangeFenLie.columns.to_list())



59、pyhon 的基础语法知识需要加强

60、字典
    根据字典的key, 读取value 值
    kwargs = {
        'SQL_CONN': sqlConn,
        'KEY_WORDS_PATH': keyWordsPath,
        'APP_CODE': appCode
    }
    print( kwargs['TABLES'] )


61、接替换行符
    replace("\n", "") # 换行
    replace("\r", "") # 插入一空行


62、在 python 中，*args 和 **kwargs 都代表 1个 或 多个 参数的意思。
        *args 传入tuple 类型的无名参数，而 **kwargs 传入的参数是 dict 类型


63、python中双下划线和单下划线


64、python解析 json


65、读写文件

    模式   可做操作   若文件不存在   是否覆盖
      r    只能读        报错          -
      r+   可读可写      报错          是
      w    只能写        创建          是
      w+　 可读可写      创建          是
      a　 只能写         创建          否，追加写
      a+  可读可写       创建          否，追加写
      xb : 以二进制的方式操作上述内容


66、python 的同步异步问题 asyncio

    同步 ：指完成事务的逻辑，先执行第一个事务，如果阻塞了，会一直等待，直到这个事务完成，再执行第二个事务，顺序执行。。
    异步 ：是和同步相对的，异步是指在处理调用这个事务的之后，不会等待这个事务的处理结果，直接处理第二个事务去了，通过状态、通知、回调来通知调用者处理结果

    async def 用来定义异步函数，其内部有异步操作。每个线程有一个事件循环，主线程调用asyncio.get_event_loop()时会创建事件循环。

    requests是同步的库，如果想异步的话需要引入aiohttp。这里引入一个类，from aiohttp import ClientSession，首先要建立一个session对象，然后用session对象去打开网页。
        session可以进行多项操作，比如post, get, put, head等。

    首先async def 关键字定义了这是个异步函数，await 关键字加在需要等待的操作前面。



67、查询某个字段的数据类型  ：df[‘ID’].dtype


68、添加排名

    df = pd.DataFrame({
        "sort_by": ["a","a","a","a","b","b","b", "a"],
         "x": [100.5,200,200,500,1,2,3, 200],
         "y": [4000,2000,2000,1000,500.5,600.5,600.5, 100.5]
    })

    df = df.sort_values(by=["x","y"], ascending=False)
    df['rank']= tuple(zip(df.x,df.y))
    df['rank']= df.groupby('sort_by',sort=False)['rank'].apply(lambda x : pd.Series(pd.factorize(x)[0])).values
    print(df)


68-2、

    对 groupby 的理解：df 使用groupby

    groupby()后的聚合函数 是个特别诡异的函数，它只会对数值型的列做运算，新生成的dataframe 中是不包含 字符串类型的列的。

68-3、
    data = {"班级":['xiaoming','xiaohua','xiaoming','xiaoming','xiaohong','xiaohong','xiaohua'],
            "年假":[4,8,6,5,3,2,9],
            "嗲":['shen','me','shen','me','shen','me','shen'],
            "发":[4,5,8,9,6,5,9] }

    df = pd.DataFrame(data)
    print(df)
    print('-----------------------------------')
    d4 = df.groupby(['班级','嗲'], sort=False)['年假'].sum().reset_index()
    print(d4)


69、
    a = 3
    b = 4

    a,b = b,a

    print(a)


70、杂集：

    liesNewOrder.groupby("分组号").count()

    chaifenlie = df.iloc[0:50000,8] # 获得第9列的数据，进行拆分
    lies = chaifenlie.str.split(',',expand=True)
    lies = lies.replace({"[":"" , "]":"" },replace=True)


70-1、dataframe 列中的 列表列拆分为多个列

    data = {"nihao":[[23,2,43],[24,32] ,[89,2,0]] }
    df = pd.DataFrame(data)
    shenme = pd.DataFrame(df['nihao'].values.tolist())
    print(shenme)




71、csv 中文乱码问题

    dataframe.to_csv('数据集.csv' , index= False, encoding="utf_8_sig")


72、字典的生成一、

    d = dict(url = 'index.html' , title = 'nimeide')
    print(d)

    字典的生成二、
    dis = {}
    dis["channel_code"] = "name"
    dis["des"] = "xiaoming"
    print(dis)




73、python 中的 时间|日期 处理

    '%Y-%m-%d %H:%M:%S' : 时间格式的主要表达形式

    import datetime

    start = '2016-12-14'
    datestart   = datetime.datetime.strptime(start, '%Y-%m-%d')  # 字符串 转 时间格式
    datestart02 = datestart.strftime('%Y:%m:%d')                 # 时间   转 字符串

    时间和日期的处理基本是在 time和datetime 这两个模块中处理的

        获得 “ 时间间隔 ” ： datetime.timedelta(weeks=1) # days、weeks、seconds ...

        time.strftime(format[, t]) # 时间格式 转 字符串
        datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 获得当前时间
73-2、

    import time
    import datetime

    # 获取今天是第几周
    print(time.strftime('%W'))
    # 获取当前是周几(0-6,0代表周一)
    today=datetime.datetime.now().weekday()
    print(today)
    # 获取指定日期属于当年的第几周
    week=datetime.datetime.strptime('20190803','%Y%m%d').strftime('%W')
    print(week)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    today_03 = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
    print(today_03)
    nows = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(nows)
    print('=-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-=')


74、
    df.pct_change() : 默认是y轴方向的比较
    df.pct_change(axis='columns') : 添加 axis='columns' 后表示x轴方向的比较
    该函数有如下数个参数 ：periods = n ;


75、python 数据处理的8个方法

    1）、
        x = [1,2,3,4]
        out = [item**2 for item in x]
        print(out)

    2)、lambda函数
        y  = lambda x :x**2   # x的平方


    3)、map() 和 filter()

        map通过对列表中每个元素执行某种操作并将其转换为新列表。
        aList = [4,5,9,3]
        xiaohua =  list(map( lambda x:x**2 , aList ))
        print(xiaohua)

        Filter函数接受一个列表和一条规则,结果得到原始列表的一个子集
        xiaoga = list(filter(lambda x:x >3 ,aList))
        print(xiaoga)

    4)、arange 和 linspace()
        Linspace以指定数目均匀分割区间，所以给定区间start和end，以及等分分割点数目num，linspace将返回一个NumPy数组
            nihao = np.linspace(2,6,6)
            print(list(nihao))

    5)、Axis


    6)、Concat、Merge、Joi


    7)、Apply:一个函数应用于指定轴上的每一个元素(apply的基本操作单位是Series)

        def churn_trans(x):
            if x == 'yes':
                return 1
            else:
                return 0

        df['column_int'] = df['column_char'].apply(churn_trans)



    8)、Pivot Tables
        nih = {'name':['dang','fsafda','gfdg'] ,
                'age':[4,5,6] ,
                'what':['kjh','gfdc','gfdc'],
                'num':[45,32,15],
                'grade':[8,5,4] }

        df = pd.DataFrame(nih)
        pilotName = pd.pivot_table(df, index=["what", "name"],values=["age"])



76、

# print('========================================')

# train_data = np.array(lies)            #先将数据框转换为数组
# train_data_list = train_data.tolist()  #其次转换为列表
# listTo = np.array(train_data_list)       #以数组形式打出来方便看
#
# # print(type(listTo)) # numpy.ndarray
# listTo2 = listTo.tolist()
#
# #一下这步骤是针对本示例做的特殊操作。
# for i in listTo2:
#     while None in i:
#         i.remove(None)
#     if len(i)> 13:
#         listTo2.remove(i)
#
# dealedDataFrame = pd.DataFrame(listTo2).iloc[:,0:13] # 获得连续列的数值(切片索引)
# print(dealedDataFrame.shape)
#
# print(dealedDataFrame.tail(20))

# 对结果表排序

liesNewOrder.groupby("分组号").count()

print(universeDataFrame.columns.to_list())

df.groupby(['class']).head(2)

,validate="one_to_many"
mergeDataFrame = pd.merge(rankNo1DataFrame ,universeDataFrameLast[["分组号","appcode_abbrn"]],left_on="分组号" ,right_on ="分组号" ,how='left')


77、小数部分保留2位
    benqi_ul_dataframe["对比"] = benqi_ul_dataframe["duibi"].map(lambda x: "%.0f%%" % (x * 100))     #  这个“对比” 用于 展示


78、分组后求数量
    benqi_amount  = benqi_ul_dataframe.groupby('forCal_02')
    id_name_benqi = benqi_amount.size().index
    id_num_benqi  = benqi_amount.size().values
    dataBenqi = {"forCal": id_name_benqi, "amount": id_num_benqi}
    pingPaiNumBenQiDataframe = pd.DataFrame(dataBenqi)

79、zonghe_sub  = zonghe_sub.rename(columns={"amount_x": "上期品牌数", "amount_y": "本期品牌数"})


80、# 统计每家门店中品牌下降达到0.7 的数量，这个结果是要本粘贴到 主体明细 表中的
    dataframe2 = benqi_ul_dataframe[['forCal_02', 'duibi']][benqi_ul_dataframe['duibi'] < 0.7]
    xia = dataframe2.groupby('forCal_02').count()
    duibi_07_dataframe = xia.reset_index()

81、
    zonghe_sub_05.loc[(zonghe_sub_05['下降低于0.7品牌占比'] == 'nan%') & (zonghe_sub_05['本期品牌数'] != 0), '下降低于0.7品牌占比'] = '0%'



82、loc 和 iloc 的区别

    取得 a 列：
        方法1： df['a']
        方法2： df.loc[:, 'a']    # 取第a列
        方法3： df.iloc[:, 0]  # 0 是 a列所在的 列序号


    取得倒数 第1行 ：
        方法1 ： df.iloc[-1]
        方法2 ： df.iloc[-1,:] # 也可以直接用-1即可
        df.iloc[1:4]

82-2、

    for df1 ,df2 in df.groupby(['key1']):
    print(df1)
    print(df2)



83、 数据类型转化

    df['column01'] = df['column01'].astype("int");

    df['column02'] = df['column02'].astype("float");

    df.loc[:,'time_column'] = pd.to_datetime(df.loc[:,'time_column'])


84、as_index = False 和 reset_index() 的效果是一样的。
    df.groupby('ulp_base_sex', as_index=False )['user_log_acct'].agg({'ulp_base_sex_account':'count'})

    hao = pd.DataFrame(nihao)
    women = hao.groupby('add' ,as_index=False ).agg({'age':'count'})

85、
    x = user_df['province'][::-1] # 切片方法，让列表反向。冒号分隔为{起始位置:终止位置:步长}
                                  # 其中步长为正，从左往右取，步长为负，从右往左取。

86、
    # 强制转换为 数字，不能转换的则变为 Nan

    train_df['TotalCharges'] =
        train_df['TotalCharges'].convert_objects(conver_number=True)

    # 看看到底哪些数据不可转换
    unconvert_df = train_df[pd.isnull(train_df['TotalCharges'])]
    print(unconvert_df)


87、# 将总消费额填充为月消费额

    train_df.loc[:,'TotalCharges'].replace(to_replace=np.nan ,
                                            value = train_df.loc[:,'MonthlyCharges'],
                                            inplace = True)

    # 'tenure' 入网时长从 0 变为 1

    train_df.loc[:,'tenure'].replace(to_replace=0 ,value= 1 ,inplace = True)


88、# 连续特征进行分箱

    pd.qcut(train_df['tenure'] , 5 ).unique()


89、

    from sklearn import preprocessing

    le = preprocessing.LabelEncoder()

    df['column01'] = le.fit_transform(df['column01'])

90、
    X_train = train_df.drop(['column01','column02','column03'] , axis=1 )

91、
    df.to_csv( filePath , sep='\t', index=False )

92、
    数据库中查询结果 --> 转为 DataFrame

    con = pymysql.connect(host="",
                          port=,
                          user="",
                          passwd="",
                          charset="utf8",
                          autocommit=True,database='')
    cur = con.cursor()

    SQL = 'select * from demo_table ... ... '
    cur.execute(SQL)
    data = cur.fetchall() # 数据集合（tuple）
    column = cur.description  # 字段名集合（tuple）

    columns=[column[i][0] for i in range(len(column))]
    df=pd.DataFrame([list(i)for i in data],columns=columns)
    return df  # 这个df 就是正常的 dataframe


93、关于时间日期的一些操作：

    d1['业务日期']=pd.to_datetime(d1['业务日期'])
    d1['月']=d1['业务日期'].dt.month.astype('str')
    d1['年']=d1['业务日期'].dt.year.astype('str')

94、索引循环 列循环
    for i in d1.index:
        if d1.loc[i,'业务日期'].year==2020:
            d1.loc[i,'淡旺季']='20201'
        elif d1.loc[i,'业务日期'].month in [1,9,10,11,12]:
            d1.loc[i, '淡旺季'] = '20211'

94-2 、
    d1['所属月份'] = d1['业务日期'].dt.strftime('%m')
    d1['所属月份'].value_counts()

95、构建业务日期

    dw = pd.DataFrame(pd.date_range(start='20210101',end=nows,periods=None,freq='D'),columns=['业务日期'])
    dw['业务日期']=pd.to_datetime(dw['业务日期'])
    dw['星期几']=dw['业务日期'].dt.day_name()
    dw['星期几_数字话表达']=dw['业务日期'].dt.weekday+1
    dw['dayofweek'] = dw['业务日期'].dt.dayofweek+1
    print(dw)

95-2、日历的构建

    from datetime import datetime

    x = datetime(2004, 10, 30, 12, 12, 12)
    d = x.isocalendar()
    dd = x.date()
    print("Date : ", str(dd), " ; in isocalendar is : ", d)
    print(d[0] , d[1] , d[2])
    print('-------------------------------------------------------')

    y = datetime(2021, 1, 4, 10, 3, 33)
    f  = y.isocalendar()
    ff = y.date()
    print(  str(ff) , f )
    # 周序号
    print(  f[0]  ,  f[1]  , f[2]  )

96、
    dw = pd.DataFrame(pd.date_range(start='20210101',end=nows,periods=None,freq='D'),columns=['业务日期'])
    dw['业务日期']=pd.to_datetime(dw['业务日期'])
    dw['周序数']=dw['业务日期'].dt.isocalendar().week
    dw['moon']=dw['业务日期'].dt.month.astype('str')
    dw['day']=dw['业务日期'].dt.day.astype('str')
    dw['日期']=dw['moon']+'.'+dw['day']

    dw_min=dw[['周序数','日期']].drop_duplicates(['周序数'],keep='first')
    dw_max=dw[['周序数','日期']].drop_duplicates(['周序数'],keep='last')

    dwm=pd.merge(dw_min,dw_max,on=['周序数'],how='outer')
    dwm['周期']=dwm['日期_x']+'-'+dwm['日期_y']
    print(dwm)



97、dyw=pd.read_excel(u"F:\\其他部门\\妥投分位源数据往期.xlsx",dtype={'淡旺季': 'str','淡旺季': 'int'})
    dk =pd.read_excel(r'D:\134.xlsx',sheet_name='KPI调整表',
                 dtype=dict(zip(['TTD','年月'],['int','str'])))


98、
    import pandas as pd
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_rows', 10000000)
    pd.set_option('display.max_columns', 10000000)
    pd.set_option('max_colwidth', 10000000)

99、获得某列的空值数量

    for col_name in df.columns:
        print(col_name)
        cnt = list(df[col_name].isna()).count(True)
        print(cnt)

99-1、删除某列

    del df[col_name]


100、demo 数据

    company=["A","B","C"]
    data=pd.DataFrame({
            "company":[company[x] for x in np.random.randint(0,len(company),10)],
            "salary" :np.random.randint(5,50,10),
            "age"    :np.random.randint(15,50,10)
        }
    )

101、关于时间


#coding=utf-8

import pandas as pd
import openpyxl
import pymysql
import datetime,time
import pyecharts.options as opts
from pyecharts.charts import Line,Grid,Page
from pyecharts.globals import ThemeType
nows = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

import numpy as np

import time
import datetime
# 获取今天是第几周
print(time.strftime('%W'))
# 获取当前是周几(0-6,0代表周一)
today=datetime.datetime.now().weekday()
# 获取指定日期属于当年的第几周
week=datetime.datetime.strptime('20190825','%Y%m%d').strftime('%W')


102、
    x_data_1 = ["2020/10/{}".format(i + 1) for i in range(30)]
    x_data_2 = ["2019/10/{}".format(i + 1) for i in range(30)]
    y_data_1 = [random.randint(10, 50) for _ in range(30)] # 选取30个数（在10-50之间）
    y_data_2 = [random.randint(20, 60) for _ in range(30)]

    print(x_data)
    print(y_data)

    print("-----------------------------------------------")

    import random
    x_data = ["2020/10/{}".format(i + 1) for i in range(30)]
    y_data = [random.randint(10, 20) for i in range(len(x_data))]

103、zip和 dict

    a = [1,2,3]
    b = [4,5,6]
    zipped = zip(a,b)     # 返回一个对象
    print(zipped)
    d = dict(zipped)
    print(d)


104、dataframe 中的字段值转 元组

    print(tuple(data['company'])) -- 返回 如：('A', 'C', 'C','A', 'A', 'B')
    print(tuple(dataframe)) --  返回字段名字


105、list 中是否有某个值 ：

    boolean  ifExist = 'demoStr' in demoList
    boolean  ifExist = demoList.count('demoStr') > 0:
    boolean  ifExist = demoList.find('demoStr') > 0:

106、round()

    djs['总妥投率'] = round((djs['票数']/djs['总票数']),3)

107、dataframe 求差集

    df1-df2

    df = pd.concat([df1, df2, df2]).drop_duplicates(subset=['filed_name', 'filed_type'], keep=False)#df1-df2
    print(df)


    df2-df1

    df = pd.concat([df2, df1, df1]).drop_duplicates(subset=['filed_name', 'filed_type'], keep=False) #df2-df1
    print(df)


108、
    d2 = d1.groupby('order_id' ,as_index=False ).agg("count")


109、Series 转为 Dataframe

    import pandas as pd

    data = {"key":['hua','hua','gou','gou','gou','shenm','gou','gou','gou','shenm','me','ming','ming'],
            'value':[ 34,23,43,24,37,64,23,45,23,23,43,24,37 ]}

    nihao = pd.DataFrame(data)
    df = nihao.groupby('key').size()
    print(df)
    print('---------------------------------')
    dff = df.reset_index(name='count')
    print(dff)
    print('=================================')
    dff3 = dff[dff['count']>2]['key']
    print('-----------------')

    print(dff3.values)
    print('********************************')
    print(list(dff3.index))


    ----------------- Series 转 Dataframe 的demo2 -------------------------------

    df_ser_01 = df[option].value_counts()
    print(df_ser_01.head())
    df_01 = {option: df_ser_01.index , 'count': df_ser_01.values }
    df_02 = pd.DataFrame(df_01)
    df_02["cumsum"] = df_02["count"].cumsum(axis=0)
    df_02["cumsumRate"] =  round(df_02["count"] / zongling ,2 )

110、
    print list(set(b).difference(set(a))) # b中有而a中没有的
    print list(set(a).difference(set(b))) # a中有而b中没有的

111、
    database[column_name].str.contains(index_, na=False)


112、科学计数法的问题

    def deal_str(data):
        data = str(data)+'\t'
        return data

    df_order_total['order_no'] = df_order_total['order_no'].map(deal_str)

    df_order_total.to_csv('C:\\AmazonRate\\df_order_total.csv',index= False, encoding="utf_8_sig")


113、plt 显示中文问题

    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['font.family']='sans-serif'
    plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

    df01 = pd.read_csv('E:/LoanStats_securev1_2018Q1.csv',encoding='gbk')


114、正则表达式 的相关


115、copy


116、dataframe 转 list

    data = {"order_no":['001','002','003','004','004','003'],
            "event_code":[1,2,3,44,5,6],
            "add":['海关','什么','间谍','海关','仓库','这是仓']
             }

    df = pd.DataFrame(data)
    shen = df[['event_code','order_no']]
    print(shen.values.tolist())

    me = [tuple(x) for x in df.values]
    print(me)
    print(me[0])
    print(me[0][2])


117、时间间隔计算
    filePath_04_05 = r'C:\Users\hp\Desktop\ban\xin-04-05.csv'
    df_04_05 = pd.read_csv(filePath_04_05 )
    df_04_05['起飞时间'] = df_04_05['起飞时间'].map(lambda  x: datetime.datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))
    df_04_05['主单落地时间'] = df_04_05['主单落地时间'].map(lambda  x: datetime.datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))
    df_04_05['时间差'] = df_04_05['主单落地时间']  - df_04_05['起飞时间']
    print('----------- 04-05 ----------- ')


118、
    import datetime,time
    nows=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(nows)


119、对与字段值的重新填写，字段重新填值

    data = {"nihao":['fs','fss','fsss','fssss'], "wohao":[12,56,21,12], "dajiahao":[46,58,31,90] }
    df = pd.DataFrame(data)
    print(df)
    df.loc[df['wohao']==12,'dajiahao']='已发送'
    等价于
    df['dajiahao'][df['wohao']==12]='已发送'
    print(df)



120、为 index(索引) 重新命名

    person_n = [x for x in range(1,51)]
    fortune = pd.DataFrame([100 for i in range(50)], index = person_n, columns= ['column_01'])
    print(fortune)
    print('--------------------')
    fortune.index.name = 'id'
    print(fortune)

120-2、concat- 合并且删除 index

    import pandas as pd

    d1 = pd.DataFrame({"name":['xiaowng' ,'fsdf' ],"age":[45 , 14],"add":[ 'ssss','dddd' ]})
    d2 = pd.DataFrame({"name":['shenm' ,'nimede' ],"age":[98 , 13],"add":[ 'rrrr','www' ]})

    df = pd.concat([d1,d2])
    print(df)
    # df=df.reset_index()
    # print(df)
    print('=============')
    df=df.reset_index().drop(['index'],axis=1)
    print(df)


121、strftime() 和 strptime() 的区别

    strptime：字符串转 日期格式

    start_time =  st.date_input('开始日期：',  datetime.datetime.strptime('2021-08-16', '%Y-%m-%d') )
    end_time = st.date_input('结束日期：'   ,  datetime.datetime.strptime('2021-08-30', '%Y-%m-%d'))

    strftime：日期格式转字符串格式
    start_time = start_time.strftime('%Y-%m-%d')
    end_time   = end_time.strftime('%Y-%m-%d')



122、

    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身


123、删除某些缺失率比较高的列

    name = ['Cindy','John','Matt']
    point = [78,None,None]

    df_grade = pd.DataFrame(name, columns=['name'])
    df_grade = pd.concat([df_grade, pd.DataFrame(point,columns=['point'])],axis=1)
    print(df_grade)

    print('=====================================================================')

    for col_name in df_grade.columns:
        print(col_name)
        cnt = list(df_grade[col_name].isna()).count(True)
        print(cnt)

    print('=====================================================================')
    def remove_the_null(data  ,a):  #第二个参数：当缺失率达到多少时，直接删除
        t=[]
        for col_name in data.columns:
            changdu = len(data[col_name])
            cnt = list(data[col_name].isna()).count(True)
            if (cnt / changdu > a):
                del data[col_name]

                t.append(col_name)
        print(data )
        print('------------------')
        print(t)
        return data , t


    print(id(df_grade))
    shene = remove_the_null(df_grade,0.9)
    print(id(shene[0]))

123-2 、缺失数据的填充
    def data_cleaning(df):
        cols = df.columns
        for col in cols:
            if df[col].dtype ==  'object':
                df[col].fillna('缺失数据', inplace = True)
            else:
                df[col].fillna(0, inplace = True)
        return(df)

124、array 转 list , reverse的运用

    ata01 = {"name":['xiaowang','xiaohua','xiaogou','xiaozhu','xiaoming','xiaogang','xiaoli','xiaoyu','xiaoding'],
              "age":[42,34,24,23,58,34,24,23,58],
              '周序号':['7月第1周','7月第1周','7月第2周','7月第2周','7月第3周','7月第3周','7月第4周','8月第1周','8月第2周' ]
              }

    df01 = pd.DataFrame(data01)
    options = np.array(df01['周序号'].unique()).tolist()
    print(id(options))
    options.reverse()
    print(id(options))


125、
    data = {"fs":[56,85,89],"fwrew":[56,85,89],"dgd":[56,84,89]}
    import pandas as pd

    df = pd.DataFrame(data)
    print(df)
    print('------------------')
    print(df[df.index == 1] )

126、

    filePath = r"C:\Users\hp\Desktop\nihao.xlsx"
    df = pd.read_excel(filePath ,dtype=str)      # 防止excel 字符串类型的数字的最前端的0 丢失（如036945，01258）
    print(df)


127、查询一组数据中距离某个值最接近的一个数及其索引

    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        print(idx)
        print(array[idx])
        return array[idx]



128、多个dataframe合并成一个Dataframe

    data01 = {"name":[ "fsdf" ] , "add":[ "ad"  ],"class":[ "fdsf" ]}
    data02 = {"name":[ "fsdf01" ] , "add":[ "ad01"  ],"class":[ "fdsf01" ]}
    data03 = {"name":[ "fsdf02" ] , "add":[ "ad02"  ],"class":[ "fdsf02" ]}

    df01 = pd.DataFrame(data01)
    df02 = pd.DataFrame(data02)
    df03 = pd.DataFrame(data03)

    lists = [df01, df02, df03]

    print(df01)
    print('-----------------')
    print(pd.concat(lists))

129、为 dataframe 赋值 ：

    nihao = {"A":[23,59,32],"B":['fds','gsdf','gdfs'],"C":[24,234,122],"D":['fsd','fsdf','fsdf']}
    df = pd.DataFrame(nihao)
    print(df)
    print('-------------------')
    for i in range(df.shape[0] ):
        a = df.iloc[i,0]
        if a < 50:
            df.iloc[i, 2] = 100

    print('==================')
    print(df)


130、捕获异常

    try:

        --- some code ---

    except Exception as e:
        print("打印出错信息：",str(e))


131、python 时间序列： https://www.cnblogs.com/xrszff/p/10960132.html

131-2、：
    df_01_02['交付时间'] =  df_01_02['交付时间'].map(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H:%M:%S'))

132、获得一个日期序列

    dw = pd.DataFrame(pd.date_range(start='20210101',end=nows,periods=None,freq='D'),columns=['业务日期'])

133、排序

    zhouqi_tru = list(set(zip(d10['周序数'] , d10['周期'])))
    zhouqi_tru.sort(key=lambda x: x[0])
    

134、
    titanic.loc[titanic['Embarked'] == 'S' , 'Embarked'] = 0
    titanic.loc[titanic['Embarked'] == 'C' , 'Embarked'] = 1
    titanic.loc[titanic['Embarked'] == 'Q' , 'Embarked'] = 2

135、dataframe 的变更

    df1=pd.DataFrame(index=[i for i in range(0,3)],columns=['weeks','months'])
    print(df1)
    print('----------------------')
    count=0
    for i in range(10):
        df1.loc[count,'weeks']= i+1
        count+=1
    print(df1)

136、 dataframe 的笛卡尔处理：此外注意字典(dict) 的运用

    w_df = DataFrame(['col1','col2','col3'],columns=['col'])
    d_df = DataFrame(['val_01','val_02' ],columns=['val'])

    new_df = DataFrame(columns=['col','val'])
    for w_index,w_row in w_df.iterrows():
        for d_index,d_row in d_df.iterrows():
            w_data = w_row['col']
            d_data = d_row['val']

            row =  DataFrame([dict(col=w_data, val=d_data), ])
            new_df = new_df.append(row,ignore_index=True)

    print (new_df)

    https://blog.csdn.net/silentwater/article/details/51187715








