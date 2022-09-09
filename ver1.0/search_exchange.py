import matlab
import matlab.engine
import os
import numpy as np
import pandas as pd

print(os.getcwd())
os.chdir('F:\pyfiles\learn')
engine = matlab.engine.start_matlab()
engine.init()

def FluxAnalysis(target,C_source):
    # engine = matlab.engine.start_matlab()

    flux = engine.flux_analysis(target,C_source)
    # ls = np.array(flux)
    return flux

def SearchObj(name):
    # engine = matlab.engine.start_matlab()
    res = engine.search_obj(name)
    return res

# target = 'tr_acar7p/atpNo1'
# C_source = 'rxsp0005'
# flux = FluxAnalysis(target,C_source)


# ls = np.array(flux)
# data = pd.DataFrame(ls)
# # check if there is an existing file
# #
# writer = pd.ExcelWriter('ls.xlsx')  # 写入Excel文件
# data.to_excel(writer, 'page_1', float_format='%.5f')  # ‘page_1’是写入excel的sheet名
# writer.save()
# writer.close()


# fo = open("flx.csv", "w")
# fo.write(",".join(ls)+ "\n")
# fo.close()