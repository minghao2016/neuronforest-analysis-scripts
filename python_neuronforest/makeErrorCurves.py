import matplotlib.pyplot as plt
import numpy as np

def makeErrorCurves((pThresholds, pErr, pTp, pFp, pPos, pNeg, pSqErr),(minThresholdIdxPixel,maxThresholdIdxPixel),
                    (rThresholds, rErr, rTp, rFp, rPos, rNeg),(minThreshIdxRand,maxThreshIdxRand)):
    plt.close('all')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    fig.set_facecolor('white')

    labels(ax1,"Threshold","Rand F-Score","Rand F-Score")
    ax1.plot(rThresholds,rErr)
    # ax1.set_xlim([rThresholds[minThreshIdxRand], rThresholds[maxThreshIdxRand]])

    labels(ax2,"False Positive","True Positive","Rand Error ROC") #todo: do this beforehand?
    rFpRate = rFp/rNeg
    rFpRate, idxs = np.sort(rFpRate),np.argsort(rFpRate)
    rTpRate = rTp[idxs]/rPos
    # check to make sure it is monotonically increasing
    ax2.plot(rFpRate,rTpRate)
    ax2.set_ylim([0,1])

    labels(ax3,"Threshold","Pixel Error","Pixel Error")
    ax3.plot(pThresholds,pErr)
    # ax3.set_xlim([pThresholds[minThresholdIdxPixel], pThresholds[maxThresholdIdxPixel]])

    labels(ax4,"False Positive","True Positive","Pixel Error ROC")
    ax4.plot(pFp/pNeg,pTp/pPos)
    ax4.set_ylim([0,1])


    plt.tight_layout()
    plt.show()

def labels(ax, x='x-label',y='y-label',title='title',fontsize=15):
    ax.locator_params(axis = 'x', nbins = 5)
    ax.locator_params(axis = 'y', nbins = 5)
    ax.set_xlabel(x, fontsize=fontsize)
    ax.set_ylabel(y, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize+10)


