#醫藉下載點 https://drive.google.com/drive/u/0/folders/1Vl-syXQ8N2BIRwtdQHLi-8ci7g4ts2gz
from dbUtil import runQuery
from pandas import DataFrame, read_csv
from streamlit import session_state, radio as stRadio, sidebar, markdown #cache as stCache, multiselect, pyplot, altair_chart, text as stText#plotly_chart, dataframe,  
from stUtil import rndrCode,  mkGrid, dsetGrid
from re import findall, search, DOTALL
from os.path import basename
from st_aggrid import AgGrid, GridUpdateMode    #, DataReturnMode, GridOptionsBuilder, JsCode
from streamlit import text_input, columns as stCLMN
from os import listdir, walk as osWalk
from os.path import splitext, isdir, isfile

def rcrsveDIR(drctry):
  totalDIR=[]
  for 根, DIR, fname in osWalk(drctry):
    #rndrCode([根, DIR, fname, isdir(f'{根}/{DIR}')])
    if isdir(根) and 根!=drctry:totalDIR.append(根)
  return totalDIR
def rcrsve章節(醫書):
  CHAPTER=[]
  for 根, DIR, fname in osWalk(醫書):
    #rndrCode([根, DIR, fname, isdir(f'{根}/{DIR}')])
    if isfile(根):CHAPTER.append(根)
  return fname
def rndrBook(book):
  chapter=listdir(book) #:=menu[1:])
  #chapter = sorted(chapter, key=str)  #lambda x:x[:-4]splitext(x)[0]
  chapter = sorted(chapter, key=lambda x:splitext(x[:-4])[0])  #
  #chapter.sort(key=lambda x:splitext(x[:-4]))
  chptr=stRadio(f'{book}章節', chapter, index=0, horizontal=True)
  if chptr:
    fullBook=f"{book}/{chptr}"
    try:
      herbalCntxt=session_state[fullBook]
    except:
      herbalCntxt=open(fullBook).read()
      session_state[fullBook]=herbalCntxt
    mkPARA(herbalCntxt)

def mkPARA(herbalCntxt):
    節=findall('=(.*)=', herbalCntxt)
    #prgrph=stRadio('段落', map(lambda x:search('[\u4e00-\u9fff]+', x)[0], 節), index=0, horizontal=True)
    PARA=map(lambda x:search('[\u4e00-\u9fff]+', x)[0], 節)
    CLMN='段落'
    #rndrCode(findall('\n\n(=.*=.*?\n\n)=', herbalCntxt, DOTALL))
    leftPane, rightPane=stCLMN([1,1])
    with leftPane:
      dfPARA=DataFrame(PARA, columns=[CLMN], index=None)
      prgrph=dsetGrid(dfPARA, CLMN)

    if prgrph is not None:    #any(prgrph)
      #段落=findall(f'=\+({prgrph})=\+(.*)\n=', herbalCntxt)
      with rightPane:
        段落=findall(f'=.{prgrph.values[0]}=.(.*?)\n=', herbalCntxt, DOTALL)
        try:
          rndrCode(段落[0])   #prgrph.values[0], 
        except:
          段落=findall(f'=.{prgrph.values[0]}=.(.*?)', herbalCntxt, DOTALL)
          rndrCode(段落[0])   #prgrph.values[0], 
表單, MENU=[], ['醫書', '笈成檢閱系統', '醫宗金鑑', '資料庫', 'recursiveRoot', 'bookCSV', '目錄夾']# #, 'nuvFilter', 'CSV', 'SurvivalAnalysis', 'miscStage', 'cncrCLMN', 'nuvStage', 'StartDate',  'AJCC期別', 'fullStage完整期別', '期別值AJCC', 'HPA整併期別']   #Profiling[step1, step2, step3, step4]=vghcarAna='AllCancer', 三部份
for ndx, Menu in enumerate(MENU): 表單.append(f'{ndx}{Menu}')
with sidebar:
  menu = stRadio('MENU', 表單, index=0, horizontal=True)
  srch=text_input('搜尋', '')
  if srch:
    CLMN=['醫書章節', '內容']   #醫書章節,內容 rndrCode(','.join(CLMN))
    qryPttrn=' or '.join([f"{v} ~ '{srch}'" for v in CLMN])
    rsltHRBL=runQuery(f"""select {','.join(CLMN)} from hbook where {qryPttrn} limit 100;""", db='herbal') #內容~'{srch}'
    hrblDF=DataFrame(rsltHRBL, columns=CLMN)
    hrblDF
def walkDir(目錄):
  #'醫籍':'章節'
  醫籍=DataFrame([['', '']], columns=['醫書', '章節'])  #{'醫籍':'', '章節':''}, index=[0], orient='index', orient='index') #
  ndx=0
  for 根, DIR, FNAME in osWalk(目錄):
    if not DIR:
      醫章={}
      for fname in FNAME:
        章節=f'{根}/{fname}'
        try:
          herbalCntxt=open(章節).read()
          醫籍.loc[ndx] = [章節, herbalCntxt]
          ndx+=1
        except:
          pass
          #rndrCode([章節])
        #醫章[章節]=herbalCntxt
        #hrbl典={'章節':醫章, '醫籍':章節}
        #rndrCode(hrblINFO)
        #醫籍.from_dict(hrbl典)   #, orient='index', ignore_index=True
      #rndrCode([醫籍])
      #rndrCode([醫章.keys()])
    #醫籍['醫籍']=根
  醫籍.to_csv(f'/tmp/{目錄}.csv', sep='\x06')
  #醫籍
  #rndrCode()
  #hrblDF=DataFrame.from_dict(醫籍, orient='columns')    # index=, , index=None
      #根=根.replace('/', '_')
  #hrblDF.to_csv(f'/tmp/{目錄}.csv', sep='\x06')
  #hrblDF
if menu==len(表單):
  pass
  #clmnDF.T
#elif menu==表單[7]:
elif menu==表單[6]:
  #for 根, DIR, FNAME in osWalk('.'):
  #  #rndrCode([根, DIR, FNAME])
  #  break
  #DIR.remove('pages')
  #DIR.remove('__pycache__')
  #for 目錄 in DIR:
  #  walkDir(目錄)
  MD=open('/home/trinity/CSV.md').read()
  outPut=''
  for csv in MD.replace(' ', '').split(',')[:-1]:
    outPut+=f"\copy hbook from {csv} with(format csv, header, delimiter E'\x06');\n"
  rndrCode(outPut)
  open('output.sql', 'w').write(outPut)
elif menu==表單[5]:
  #hrblDF=open('/tmp/book.csv').read()
  hrblDF=session_state['hrblDF']
  #hrblDict={}
  #fewBook=hrblDF.to_dict('list')['醫籍'][:10]
  for 目錄 in hrblDF.values:
    walkDir(目錄[0])
  """
  for hbook in fewBook:
    dictHRBL={}
    #rndrCode(['hbook', hbook])
    for 根, DIR, FNAME in osWalk(hbook):
      rndrCode([根, DIR, FNAME])
      #醫籍DF[dset.values[0]]['章']=fname
      for fname in FNAME:
        fullName=f'{根}/{fname}'
        herbalCntxt=open(fullName).read()
        dictHRBL[fullName]=herbalCntxt
      hrblDict[根]=dictHRBL
    #rndrCode([dictHRBL.keys()]) #dict_keys(['叢桂草堂醫案', '外科選要', '咽喉脈證通論', '醫林改錯_1', '外科十法', '修崑崙證驗', '炮炙全書', '海藥本草', '毓麟驗方', '傷寒論注'])

  """
elif menu==表單[4]:
  CLMN='醫籍'
  from numpy import where as npWhere
  for 根, DIR, FNAME in osWalk('.'):
    #rndrCode([根, DIR, FNAME])
    break
  session_state['hrblDF']=hrblDF=DataFrame({CLMN:DIR}, index=None, dtype=str)  #columns=[], 
  #hrblDF.to_csv('/tmp/herbal.csv')
  rndrCode([hrblDF, hrblDF.columns])
  with sidebar:
    #醫書=stRadio('醫籍', DIR, horizontal=True)
    dset=dsetGrid(hrblDF, CLMN)
  if dset is not None:
    chptr={}
    for 根, DIR, FNAME in osWalk(dset.values[0]):
      #醫籍DF[dset.values[0]]['章']=fname
      for fname in FNAME:
        fullName=f'{根}/{fname}'
        herbalCntxt=open(fullName).read()
        chptr[fname]=herbalCntxt
      #hrblDF[['醫籍']==dset.values[0]]df[df['total'] == 0].index.values
      #ndxName=hrblDF.iloc[npWhere(hrblDF.loc[:, '醫籍'] == dset.values[0])]
      #ndxName=hrblDF.loc[hrblDF['醫籍']==dset.values[0]]
      #rndrCode(ndxName)
      #hrblDF.loc[ndxName, '章']=herbalCntxt
      #ndxName=hrblDF['醫籍'].iloc(dset.values[0])
      #hrblDF['章'][ndxName]=herbalCntxt
      #rndrCode([根, DIR, fname, fullName, herbalCntxt])     # .query(f'醫籍=={dset.values[0]}')
      stWrite([chptr.keys(), chptr])
elif menu==表單[3]:
  #ajccCLMN=session_state['ajccCLMN']
  #bookDF=session_state['bookDF']
  #bookDF.to_csv('/tmp/book.csv')
  #rndrCode(bookDF)
  #for book in bookDF:
  CLMN, fullQuery='醫書', f'select 醫書 from 醫籍;'  # set (醫書)=book
  rsltHerbal=runQuery(fullQuery, db='herbal')   #, commitType='insert'
  dsetDF=DataFrame(rsltHerbal, columns=[CLMN])
  with sidebar:
    dset=dsetGrid(dsetDF, CLMN)
  if dset is not None:
    rndrCode(dset.values[0])
    #rndrCode(rsltHerbal)
  #
elif menu==表單[2]:     #'CLMN'
  DIR='醫宗金鑑'
  DIRs=rcrsveDIR(DIR)
  DIRs=map(lambda x:x.split('/')[-1], DIRs)
  with sidebar:
    醫書=stRadio('醫書', DIRs, horizontal=True)
  if 醫書:
    章節=rcrsve章節(f'{DIR}/{醫書}')
    leftPane, rightPane=stCLMN([1, 6])
    with leftPane:
      章節=sorted(章節, key=lambda x:x[:-4])
      章=stRadio('章節', 章節, index=0)
    with rightPane:
      if 章:
        herbalCntxt=open(f'{DIR}/{醫書}/{章}'). read()
        rndrCode(herbalCntxt)

elif menu==表單[1]:   #Filter
  try:
    CHAP=session_state['笈成']
  except:
    session_state['笈成']=CHAP=listdir('笈成檢閱系統v1.4.8/data')
  with sidebar:
    chap=stRadio('CHAP', CHAP, horizontal=True, index=0)
  if chap:
    leftPane, rightPane=stCLMN([1, 1])
    chptr=listdir(f'笈成檢閱系統v1.4.8/data/{chap}')
    with leftPane:
      chp=stRadio('', chptr, horizontal=True)
    with rightPane:
      ssssName=f'{chap}/{chp}'
      if chp:
        try:
          chpCntxt=session_state[ssssName]
        except:
          session_state[ssssName]=chpCntxt=open(f'笈成檢閱系統v1.4.8/data/{chap}/{chp}').read()
        rndrCode(chpCntxt)
  #for patient in TXTs: idvCSV(DIR, patient)
elif menu==表單[0]:   #Filter
  with sidebar:
    #session_state[tchwkTBL]=tchwkDF=DataFrame(data=tchwkDF, columns=tchwkCLMN, index=None)
    try:
      bookDF=session_state['bookDF']
    except:
      allBook=open('allBook.md').readline().replace(' ', '')
      allBook=allBook.split(',')#[:10]
      session_state['bookDF']=bookDF=DataFrame(allBook, columns=['醫經'], index=None)
    CLMN="醫經"
    dsetDF=dsetGrid(bookDF, CLMN)
  if dsetDF is not None:    # and any(dsetDF)
    #book=stRadio('醫書', dsetDF, horizontal=True)
    #if book:
    rndrBook(dsetDF.values[0])
