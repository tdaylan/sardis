import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

import datetime, os

import troia
import tdpy
import nicomedia

def init(
         
         typesyst, \

         dicttroiinpt=None, \
         
         # a string distinguishing the run to be used in the file names
         strgcnfg=None, \
         
         # the path in which the run folder will be placed
         pathbase=None, \
        
        ):
    '''
    Run troia on simulated and observed data, inferring the occurrence rate
    '''
    
    # construct global object
    gdat = tdpy.gdatstrt()
    
    # copy locals (inputs) to the global object
    for attr, valu in locals().items():
        if '__' not in attr and attr != 'gdat':
            setattr(gdat, attr, valu)

    # string for date and time
    gdat.strgtimestmp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
   
    print('sardis initialized at %s...' % gdat.strgtimestmp)
    
    # paths
    ## path of the sardis data folder
    gdat.pathbasesard = os.environ['SARDIS_DATA_PATH'] + '/'
    ## base path of the run
    if gdat.pathbase is None:
        gdat.pathbase = gdat.pathbasesard
    
    gdat.pathdatapipe = gdat.pathbase + 'data/'
    gdat.pathvisupipe = gdat.pathbase + 'visuals/'
    
    if gdat.strgcnfg is None:
        gdat.strgcnfg = '%s' % (gdat.typesyst)

    gdat.pathcnfg = gdat.pathbase + gdat.strgcnfg + '/'

    gdat.pathsimu = gdat.pathcnfg + 'simulation/'
    gdat.pathobsd = gdat.pathcnfg + 'observed/'

    #listtoiitarg = np.loadtxt(path)

    dictmileinptglob = dict()
    #dictmileinptglob['dictboxsperiinpt'] = dict()
    #dictmileinptglob['dictboxsperiinpt']['factosam'] = 0.1
    
    gdat.typesimu = 'Synthetic'

    # select targets
    if gdat.typesimu != 'Synthetic':
        dictpopltici = nicomedia.retr_dictpopltic8(typepopl='TIC_m060')
        listtici = dictpopltici['TIC']
    
    if gdat.dicttroiinpt is None:
        gdat.dicttroiinpt = dict()
        gdat.dicttroiinpt['pathbase'] = gdat.pathsimu
        gdat.dicttroiinpt['typesyst'] = gdat.typesyst
        gdat.dicttroiinpt['listlablinst'] = [['TESS'], []]
        if gdat.typesimu == 'Synthetic':
            gdat.dicttroiinpt['liststrgtypedata'] = [['simutargsynt'], []]
        else:
            gdat.dicttroiinpt['liststrgtypedata'] = [['simutargpartinje'], []]

    # simulated run to get the precision and recall
    dicttroyoutp = troia.init( \
               **gdat.dicttroiinpt, \
               #listtoiitarg=listtoiitarg, \
               #listlablinst=[['TESS'], []], \
               #typepopl='prev', \
              )

    
    troia.init()

