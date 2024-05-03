import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

import datetime, os

import troia
import tdpy

def init(
         dicttroiinpt=None, \
        ):
    '''
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
    

    path = os.environ['SARDIS_DATA_PATH'] + '/data/'
    
    #listtoiitarg = np.loadtxt(path)

    dictmileinptglob = dict()
    #dictmileinptglob['dictboxsperiinpt'] = dict()
    #dictmileinptglob['dictboxsperiinpt']['factosam'] = 0.1
    
    if gdat.dicttroiinpt is None:
        gdat.dicttroiinpt = dict()
        gdat.dicttroiinpt['typesyst'] = 'PlanetarySystem'
    troia.init( \
               **gdat.dicttroiinpt, \
               #listtoiitarg=listtoiitarg, \
               #listlablinst=[['TESS'], []], \
               #typepopl='prev', \
              )

    troia.init()

