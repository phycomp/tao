from pandas import read_excel
pede=read_excel('班務系統-崇慧國語培德班-單週(日)出席狀況_至1003.xlsx')
PEDE=pede.transpose()
from numpy import nan, where, apply_along_axis, vectorize
from re import compile
def rtrvAbsence(cols, rgExp):
    absntInfo=[]
    for elmnt in cols.values:
        if elmnt is not nan and compile(rgExp).match(elmnt):
            absntInfo.append('')
        else:absntInfo.append(elmnt)
    print(absntInfo, len(absntInfo))
    #rsltAbsenct=where(cols.values!='實到')
    #rtrvAbs= vectorize(lambda elmnt, rgExp: not bool(compile(rgExp).match(elmnt)) if elmnt is not nan else nan)#)#
    #rtrvAbs= lambda elmnt, rgExp: '' if elmnt is not nan and compile(rgExp).match(elmnt) else 'None'#)#
    #print(list(rtrvAbs))
    #rsltAbsnt = apply_along_axis(rtrvAbsnt, -1, cols.values, args=('實到|補課',))#where(rtrvAbs(cols.values, '實到|補課')  nan)
    #rsltCols=cols.values[rsltAbsnt]
    #rsltLen=len(rsltAbsnt)
    #print(rsltLen, rsltAbsnt)
    #np.apply_along_axis(sigmoid, -1,np.array([ -0.54761371  ,17.04850603 ,4.86054302])) 
#pede.apply(rtrvAbsence, axis=1, args=('實到|補課',))
def mnplAbsnt(taommbr):
    return pede[taommbr].apply(lambda elmnt:False if elmnt is not nan and compile('實到|補課').match(elmnt) else True) #

for taommbr in pede.columns.values:
    #print(taommbr)
    rsltInfo=mnplAbsnt(taommbr)#.apply(lambda elmnt:compile('實到|補課').match(elmnt) if elmnt is not nan else elmnt)
    #print(len(rsltInfo))
    rsltAbs=zip(pede.日期[rsltInfo].values, pede.題目[rsltInfo].values)
    rsltAbs=list(rsltAbs)
    #print('rsltAbs', rsltAbs)
    if rsltAbs:
        if len(rsltAbs)<=2:
            print(taommbr, 1-len(rsltAbs)/32., '全勤')#, len(rsltAbs), rsltAbs)
        else:
            print(taommbr, 1-len(rsltAbs)/32.)#, len(rsltAbs), rsltAbs)
        for cmb in rsltAbs:
            clssMtch=cmb[1]
            clssLink=mtchClss.get(clssMtch)#zip(pede.日期[rsltInfo].values, pede.題目[rsltInfo].values):
            if cmb[0]<'2021/10/17' and clssLink: print('|'.join([cmb[0], cmb[1], clssLink]), end='\n')
            else: print('|'.join(cmb), end='\n')
    else:print(taommbr, 1.0,  '全勤')
#PEDE.apply(rtrvAbsence, axis=0, args=('實到|補課',))

from re import findall
mtchClss=dict(findall('\d+\/\d+.*\-(.*)\n(https:.*)\n', clssInfo))
