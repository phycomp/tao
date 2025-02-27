from pandas import read_excel
from streamlit import sidebar, session_state, radio as stRadio, columns as stCLMN, text_area, text_input, multiselect, toggle as stToggle, data_editor #slider, markdown, dataframe, code as stCode, text_input, code as stCode  code as stCode, cache as stCache, 
from pandas import DataFrame, read_excel
from rndrCode import rndrCode
from dbUtil import runQuery

MENU, 表單=[], ['五年研究班', '先後天', '至善班', 'dfKLSS', '二十四節氣']
for ndx, Menu in enumerate(表單): MENU.append(f'{ndx}{Menu}')
with sidebar:
  menu=stRadio('表單', MENU, horizontal=True, index=0)
  srch=text_input('搜尋', '')
if menu==len(表單):
  pass
elif menu==MENU[3]:
  dfKLSS = session_state['dfKLSS']#=dfKLSS.rename(columns=dict(zip(oldCLMN, newCLMN)))
  data_editor(dfKLSS, num_rows='dynamic')
  #favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
  #markdown(f"Your favorite command is **{favorite_command}** 🎈")
elif menu==MENU[2]:
  #url='''https://docs.google.com/spreadsheets/d/1aOfkBTOYfS-N0lUU8WJ89ffAbn4HEnp6/edit?usp=sharing&ouid=100478161533138273084&rtpof=true&sd=true'''
  dfKLSS=read_excel('2024至善班課程表New.xlsx', dtype='str') # read_excel
  oldCLMN=dfKLSS.columns
  #rndrCode(['oldCLMN', oldCLMN])
  newCLMN=['2024年度景德國語至善班', '日期', '時間', '傳題題目', '所屬佛堂', '傳題講師', '聯絡電話', '炊事', '操持', '善歌', '課後課', '接待', '班員', '負責講師', '代課題目', '代課講師', '其它']
  dfKLSS = session_state['dfKLSS']=dfKLSS.rename(columns=dict(zip(oldCLMN, newCLMN)))
  #dfKLSS
  CLMN=dfKLSS.columns
  #rndrCode(CLMN)
  from dsetGrid import dsetGrid
  with sidebar:
    dset=dsetGrid(dfKLSS, CLMN)
    #dset, agValue, grdOPT=dsetGrid(dfKLSS, CLMN)
  if dset is not None:    #any(prgrph)
    #日期, 時間
    #getattr()#.to_list()#str#.['日期', '時間']
    #rndrCode(dset.columns)
    #'2024年度景德國語至善班', '日期', '時間', '傳題題目', '所屬佛堂', '傳題講師', '聯絡電話', '炊事', '操持', '善歌', '課後課', '接待', '班員', '負責講師', '代課題目', '代課講師', '其它'
    #['columnDefs', 'autoSizeStrategy', 'pagination', 'paginationAutoPageSize', 'rowSelection', 'rowMultiSelectWithClick', 'suppressRowDeselection', 'suppressRowClickSelection', 'groupSelectsChildren', 'groupSelectsFiltered', 'rowData', 'columnTypes']
    rndrCode(dset.values[0])
    至善班, 日期, 時間, 傳題題目, 所屬佛堂, 傳題講師, 聯絡電話, 炊事, 操持, 善歌, 課後課, 接待, 班員, 代課題目, 代課講師, 其它=dset.values[0]
    #'19' '2024/07/20(六)' '10:00~12:00' '前人行誼' '臸德' '林月娥' '0918-416689' '蘇妙康' '呂俊興' '林慧芳' '呂俊興' '劉諺錞' '班員' None None '07/27上課'
    傳題講師=代課講師 if 代課講師 else 傳題講師
    傳題題目=代課題目 if 代課題目 else 傳題題目
    rndrCode(所屬佛堂)
    #rndrCode()#.fromkeys(['paginationPageSize']))#gridOptions, paginationPageSize)
    #rndrCode([至善班, 日期, 時間, 傳題題目, 所屬佛堂, 傳題講師, 聯絡電話, 炊事, 操持, 善歌, 課後課, 接待, 班員, 負責講師, 代課題目, 代課講師])
    #至善班, 日期, 時間, 聯絡電話, 炊事, 操持, 善歌, 課後課, 接待, 班員, 負責講師, 代課題目, 代課講師=
    #option='pagination' #'rowSelection'
    #rndrCode([option, agValue.grid_options.get(option)])   #[int(至善班)+1]
    下列=int(至善班)+1
    #klssINFO=agValue.grid_options.get('rowData')[]
    #klssINFO=dfKLSS.loc[dfKLSS['2024年度景德國語至善班']==下列].values#['2024年度景德國語至善班']
    klssINFO=dfKLSS.loc[dfKLSS['2024年度景德國語至善班']==str(下列)]#['2024年度景德國語至善班']
    #agValue.grid_options.get('rowData')
    #klssINFO
    klssINFO=klssINFO.to_dict('list')
    #rndrCode([klssINFO])
    第二堂課後課, 第二堂傳題題目, 第二堂所屬佛堂, 第二堂傳題講師, 代課題目, 代課講師=klssINFO['課後課'], klssINFO['傳題題目'], klssINFO['所屬佛堂'], klssINFO['傳題講師'], klssINFO['代課題目'], klssINFO['代課講師']
    第二堂課後課, 第二堂傳題題目, 第二堂所屬佛堂, 第二堂傳題講師, 代課題目, 代課講師=map(lambda x:x[0], (第二堂課後課, 第二堂傳題題目, 第二堂所屬佛堂, 第二堂傳題講師, 代課題目, 代課講師))#=klssINFO['課後課'], klssINFO['傳題題目'], klssINFO['所屬佛堂'], klssINFO['傳題講師'], klssINFO['代課題目'], klssINFO['代課講師']
    #rndrCode([klssINFO, 代課題目, 代課講師])
    #rndrCode([代課題目, 代課講師, 第二堂傳題講師, 第二堂傳題題目])
    #第二堂所屬佛堂=第二堂所屬佛堂 if 第二堂所屬佛堂 else 所屬佛堂
    #第二堂傳題講師=代課講師 if 代課講師 else 第二堂傳題講師
    #第二堂傳題題目=代課題目 if 代課題目 else 第二堂傳題題目
    第二堂課後課=第二堂課後課 if 第二堂課後課 and not 'nan' else 課後課
    #rndrCode(['最後', 第二堂課後課, 第二堂傳題題目, 第二堂所屬佛堂, 第二堂傳題講師])
    #[int(至善班)]
    工作分配=f'''{日期} 10：00-15：30 課程流程方案如下：

10：00-10：10	善歌{善歌}|操持{操持}|接待{接待}
10：10-11：30	第一堂課	{傳題題目}	{所屬佛堂}	{傳題講師}
11：30-11：40	上午課後課	{課後課}
11：50		午獻香
12：00-13：00	用餐暨行意禪
13：00-13：10	操持{操持}	帶讀誦	接待{接待}
13：10-14：30	第二堂課	{第二堂傳題題目}	{第二堂所屬佛堂}{第二堂傳題講師}	課中休息點心時間
14：30-14：40	下午課後課	{第二堂課後課}

工作分配：操持{操持}|善歌{善歌}|課後課{課後課}|接待{接待}
聯繫傳題：李講師|廚師炊事：薛講師、{炊事}|聯繫班員：引保師 輔導講師
記得聯繫羅姐到佛堂上課 吳講師安排上台'''
  rndrCode(工作分配)
  班務佈達=f'''各位前賢大家好 又到了跟仙佛有約 一起精進學習的好時光
{日期} 10：00-15：30 景德至善班課程流程如下：

10：00-10：10	善歌{善歌}
10：10-11：30	第一堂課	{傳題題目}	{所屬佛堂}	{傳題講師}
11：30-11：40	上午課後課	{課後課}
11：50		午獻香
12：00-13：00	用餐暨行意禪
13：00-13：10	操持	帶讀誦	接待
13：10-14：30	第二堂課	{第二堂傳題題目}	{第二堂所屬佛堂}{第二堂傳題講師}	課中休息點心時間
14：30-14：40	下午課後課	{第二堂課後課}'''
  rndrCode(班務佈達)
elif menu==MENU[1]:
  tblName='sutra'
  sutraCLMN=queryCLMN(tblSchm='public', tblName=tblName, db='sutra')
  #rndrCode(sutraCLMN)
  fullQuery=f'''select {','.join(sutraCLMN)} from {tblName} where 章節~'中庸';'''
  rsltQuery=runQuery(fullQuery, db='sutra')
  #rndrCode([fullQuery, rsltQuery])
  rsltDF=session_state['rsltDF']=DataFrame(rsltQuery, index=None, columns=sutraCLMN)
  rsltDF#[rsltDF['章節']=='中庸']
elif menu==MENU[0]:
  研究班=['新民', '至善', '培德', '行德', '崇德']
  from glob import glob
  課表=glob('*.xlsx')
  #課表=['研究班課程表_20211127124219.xlsx', '研究班課程表_20211127124446.xlsx', '研究班課程表_20211218084608.xlsx', '研究班課程表_20220105014936.xlsx', '研究班課程表_20220105014936新.xlsx', '研究班課程表_20220105021721.xlsx', '研究班課程表_20220106204042.xlsx', '研究班課程表_20230110143853.xlsx', '研究班課程表_20231206203146.xlsx', '研究班課程表_20231207175256.xlsx', '至善班課程表_20231206203146.xlsx']
  with sidebar:
    fvClss=stRadio('研究班', 研究班, horizontal=True, index=0)
    sutraKlss=stRadio('課表', 課表, horizontal=True, index=0)
  if sutraKlss:
    研究班DF=read_excel(sutraKlss)  #'至善班課程表_20231206203146.xlsx'
    rndrCode(sutraKlss)
    研究班DF
  #崇德班DF=read_excel('2023年度台北崇慧國語崇德班單週日研究班班員.xlsx')
  #崇德班DF
  sutraCLMN=['章節', '內容']
  #rsltQuery=runQuery(f'''select {','.join(sutraCLMN)} from "AB";''', db='fiveClass')
  #rsltDF=session_state['rsltDF']=DataFrame(rsltQuery, columns=sutraCLMN, index=None)
  #sutraDF=session_state['rsltDF']=DataFrame([['', '']], columns=sutraCLMN, index=[0])
  #DF[DF.fiveClass.str.contains('', case=False)]
