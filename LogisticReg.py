'''
Created on Feb 17, 2015

@author: abhishekkumar
'''
from TrainPredictObject import TrainPredictObject;
from costFunctionReg import  costFunctionReg;
from Utility import Utility;
from decimal import Decimal;
from sigmoidFunction import Sigmoid
class Logisticreg(object):
    '''
    classdocs
    '''
    def _initiaLizeWeights(self,size):
        for i in range(0,size):
            self.weightList.append(0);
            
    def _calCost(self,trainObj):
        print "entering loop-----------------------------";
        cost = Decimal('+Infinity');
        prob = [];
        for i in range(0,self.numIter):
            costFuncObj = costFunctionReg(trainObj.xList,trainObj.yList,self.lambdaVal,self.lambdaVal,self.weightList);
            #if(costFuncObj.cost<cost):
            cost = costFuncObj.cost;
            prob = costFuncObj.prob0;
            self.weightList = costFuncObj.weightList;
            #else:break;
                
            
            #print "next iteration----------------------------------------";
        return prob;
        
    def _predict(self,trainPredObj):
        outPut = Utility.multFeatureWeights(self.weightList, trainPredObj.xList);
        prob = Sigmoid.getSigmoidVal(outPut);
        #print prob;
        predYList = [];
        for i in range(0,len(prob)):
            if(prob[i]<0.5):predYList.append(1);
            else:predYList.append(0);
        #print predYList;
        #print trainPredObj.yList;
        return predYList;
    def _calAccuracy(self,predList,actualList):
        wrong =0;
        for i in range(0,len(predList)):
            if(predList[i]!=actualList[i]):wrong+=1;
        wrongFraction = float(wrong)/float(len(actualList));
        correctFraction =1.0 - wrongFraction;
        return correctFraction*100;
            
        
           
        

    def __init__(self, trainObj,predObj,lambdaVal,learningRate,numIter):
        '''
        Constructor
        '''
        self.lambdaVal=lambdaVal;
        self.learningRate=learningRate;
        self.numIter =numIter;
        self.trainObj = trainObj;
        self.predObj = predObj;
        self.weightList =[];
        self._initiaLizeWeights(len(trainObj.vocabDict));
        prob = self._calCost(trainObj);
        predList =self._predict(predObj);
        self.accuracy =self._calAccuracy(predList, predObj.yList);
        