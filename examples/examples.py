import sardis
import sys


def cnfg_TESS():

    #pathdata = os.environ['SARDIS_DATA_PATH'] + '/data/'
    #print(pathdata)
    #cmnd = 'scp pdo2:/pdo/qlp-data/\{'
    #for k in range(1, 30):
    #    for i in range(1, 5):
    #        for j in range(1, 5):
    #            cmnd += ''
    #            'sector-%d/ffi/cam%d/ccd%d/BLS/blsanal_sum.txt,' % (k, i, j)
    #
    #cmnd += '\} %sblsanal_sum_%02d%d%d.txt' % (pathdata, k, i, j)
    #print(cmnd)
    ##cmnd = os.system(cmnd)

    sardis.init('PlanetarySystem')

globals().get(sys.argv[1])(*sys.argv[2:])

