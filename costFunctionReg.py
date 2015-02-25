'''
Created on Feb 17, 2015

@author: abhishekkumar
'''
from Utility import Utility;
from sigmoidFunction import Sigmoid;
import math;
class costFunctionReg(object):
    '''
    classdocs
    '''
    def _calFistPart(self,prob1):
        sum =0.0
        for i in range(0,len(self.yList)):
            val = self.yList[i];
            sum =sum+float(val*math.log(prob1[i]));
        return sum;
    def _calSecPart(self,prob0):
        sum =0.0;
        for i  in range(0,len(self.yList)):
            val = self.yList[i];
            value = float((1-val)*math.log(prob0[i]));
            sum = sum +val;
        return sum;
    def _calRegpart(self):
        sum =0.0;
        for i in range(0,len(self.weightList)):
            sum = sum + (self.weightList[i]*self.weightList[i]);
        sum = float(self.lambdaVal *sum)/2.0;
        return sum;
        
            
        
    def _calCost(self):
        multiList = Utility.multFeatureWeights(self.weightList, self.xList);
        self.prob0=Sigmoid.getSigmoidVal(multiList);
        #print len(self.prob0);
        #print len(self.yList);
        self.prob1 = Utility.matrixXminusOper(1, self.prob0);
        firstPart = self._calFistPart(self.prob1);
        secPart = self._calSecPart(self.prob0);
        regpart = self._calRegpart();
        #print firstPart;
        #print secPart;
        cost = firstPart+secPart-regpart;
        return cost;
        
        
    def _gradAscend(self,prob1):
        gradList=[];
        for i in range(0,len(self.weightList)):
            sum =0.0;
            for j in range(0,len(self.yList)):
                val = float(self.xList[j][i] *(self.yList[j]-prob1[j]));
                sum = sum +val;
            sum = sum - (self.lambdaVal*self.weightList[i]);
            gradList.append(sum);
        return gradList;
    def _updateWeights(self,gradList):
        for i in range(0,len(gradList)):
            self.weightList[i] = self.weightList[i]+(self.learningRate*gradList[i]);

    def __init__(self, xList,yList,lambdaVal,learningRate,weightList):
        '''
        Constructor
        '''
        
        self.xList = xList;
        self.yList = yList;
        self.weightList = weightList;
        self.lambdaVal = lambdaVal;
        self.learningRate = learningRate;
        self.cost =self._calCost();
        #print "cost "+str(self.cost);
        gradList = self._gradAscend(self.prob1);
        #print gradList;
        self._updateWeights(gradList);
        #print self.weightList;