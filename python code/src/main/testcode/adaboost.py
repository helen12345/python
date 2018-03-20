# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:52:11 2018

@author: hanhong
"""

import numpy as np


def loadSimpleData():
    datMat = np.matrix([[1., 2.1], [2., 1.1], [1.3, 1.], [1., 1.], [2., 1.], [2., 0.9]])
    classLabels = [1., 1., -1., -1., -1., 1.]
    return datMat, classLabels


def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = 1.0
    return retArray


def buildStump(dataArr, classLabels, D):
    dataMatrix = np.mat(dataArr);
    labelMat = np.mat(classLabels).T
    m, n = np.shape(dataMatrix)
    numstemps = 10.0;
    bestStump = {};
    bestClasEst = np.mat(np.zeros((m, 1)))
    minErr = np.inf
    for i in range(n):
        rangeMin = dataMatrix[:, i].min();
        rangeMax = dataMatrix[:, i].max();
        stepSize = (rangeMax - rangeMin) / numstemps
        for j in range(-1, int(numstemps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = np.mat(np.ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightError = D.T * errArr
                # print("split:dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (
                #     i, threshVal, inequal, weightError))
                if weightError < minErr:
                    minErr = weightError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minErr, bestClasEst


def adaBoostTrainDS(dataArr, classLabels, numIt=40):  ###numIt 迭代次数
    weakClassArr = []
    m = np.shape(dataArr)[0]
    D = np.mat(np.ones((m, 1)) / m)
    aggClassEst = np.mat(np.zeros((m, 1)))
    for i in range(numIt):
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        print("D:", D.T)
        alpha = float(0.5 * np.log((1.0 - error) / max(error, 1e-16)))  #####1e-2 = 0.01  float 将矩阵转换成float数值
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print('classEst:', classEst.T)
        expon = np.multiply(-1 * alpha * np.mat(classLabels).T, classEst)
        D = np.multiply(D, np.exp(expon))
        D = D / np.sum(D)
        aggClassEst += alpha * classEst
        print('aggClassEst:', aggClassEst.T)
        aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T, np.ones((m, 1)))
        errorRate = np.sum(aggErrors) / m
        print('total error:', errorRate)
        if errorRate == 0.0: break
    return weakClassArr


def adaClassify(datToClass, classifierArr):
    dataMatrix = np.mat(datToClass)
    m = np.shape(dataMatrix)[0]
    aggClassEst = np.mat(np.zeros((m, 1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'],
                                 classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha'] * classEst
        print(aggClassEst)
    return np.sign(aggClassEst)


def plotROC(predStrengths, classLabels):
    import matplotlib.pyplot as plt
    cur = (1.0, 1.0)
    ySum = 0.0
    numPosClas = np.sum( np.array(classLabels) == 1.0)
    yStep = 1/float(numPosClas)
    xStep = 1/float( len( classLabels) - numPosClas)
    sortedIndicies = predStrengths.argsort()
    fig = plt.figure();
    fig.clf()
    ax = plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0; delY = yStep
        else:
            delX = xStep;delY = 0;
            ySum += cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY], c = 'b')
        cur = (cur[0] - delX,cur[1]-delY)
    ax.plot([0,1], [0,1],'b--')
    plt.xlabel('False Positive Rate');plt.ylabel('True Positive Rate');
    plt.title('ROC curve for Adaboost Horse Colic Detection Systom')
    ax.axis([0,1,0,1])
    plt.show()
    print('the Area Under the Curve is:',ySum * xStep)




datMat, classLabels = loadSimpleData();
classifierArr = adaBoostTrainDS(datMat, classLabels, 9)
print(classifierArr)
pred = adaClassify([[0, 0], [5, 5]], classifierArr)
print(pred)




# datMat, classLabels = loadSimpleData();
# D = np.mat(np.ones((5, 1)) / 5)
# bestStump, minErr, bestClasEst = buildStump(datMat, classLabels, D)
# print(bestClasEst, minErr)
