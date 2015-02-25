'''
Created on Feb 14, 2015

@author: abhishekkumar
'''
from ClassesAttr import ClassesAttr;
from NBTrain import NBTrain;
from Utility import Utility;
import math;
from decimal import Decimal;
class NBPredict(object):
    '''
    this class predicts,it read one document and predicts 
    '''
    def _calculatePrior(self):
        totalDocs = 0;
        self.priorDict = {};
        for key in self.classObjDict:
            classObj = self.classObjDict[key];
            self.priorDict[key] = classObj.numOfDocs;
            totalDocs= totalDocs+ classObj.numOfDocs;
        for key in self.priorDict:
            self.priorDict[key] = float(self.priorDict[key])/float(totalDocs);
            
    def _predictDoc(self,wordsCountDict):
        predictClass ="";
        maxProb = Decimal('-Infinity');
        for i in range(0,len(self.classList)):
            className = self.classList[i];
            valueList =[];
            prior  = self.priorDict[className];
            valueList.append(math.log(prior));
            for key in wordsCountDict:
                times = wordsCountDict[key];
                if(self.nbTrainObj.probDict.has_key(key+"|"+className)):
                    probValue = self.nbTrainObj.probDict[key+"|"+className];
                    valueList.append(times*math.log(probValue));
                else:
                    classObj = self.classObjDict[className];
                    denom = classObj.totalWords+(self.laplaceConstant*len(self.nbTrainObj.vocabDict));
                    probValue = float(self.laplaceConstant)/float(denom);
                    valueList.append(times *math.log(probValue));
            currPredictVal = Utility.sumList(valueList);
            #print currPredictVal;
            #print className;
            if(currPredictVal>maxProb):
                #print "currPredcit>maxProb"+ str(maxProb);
                maxProb = currPredictVal;
                predictClass = className;
        #print "-------++++++++----------- "+predictClass;
        return predictClass;
    
    def _calculateAccuracy(self):
        correct = 0;
        for key in self.actualClassDict:
            actualVal = self.actualClassDict[key];
            predVal = self.predcitDict[key];
            #print key;
            #print actualVal;
            #print predVal;
            #print "------------------"
            if(actualVal == predVal):
                correct+=1;
        accuracy = float(correct)/float(len(self.actualClassDict));
        accuracy=accuracy*100;
        self.accuracy = accuracy;
        
        
            
        
        

    def __init__(self, classObjDict,nbTrainObj,dirDict,laplaceConstant):
        self.predcitDict = {};
        self.actualClassDict={};
        self.classObjDict = classObjDict;
        self.nbTrainObj = nbTrainObj;
        self.dirDict = dirDict;
        self.classList = dirDict.keys(); 
        self.laplaceConstant=laplaceConstant;
        for key in dirDict:
            dirName = dirDict[key];
            #print dirName;
            fileList = Utility.readDir(dirName);
            #print len(fileList);
            #print len(fileList);
            #print "loop start";
            count =0;
            for file in fileList:
                if(file =='.DS_Store'):continue;
                senList = Utility.readFile(dirName+'/'+file);
                tempWordsDict =Utility.getWordsCountDict(senList);
                self.actualClassDict[(dirName+'/'+file)] = key;
                self._calculatePrior();
                predictClass =self._predictDoc(tempWordsDict);
                self.predcitDict[(dirName+'/'+file)] = predictClass;
                if(predictClass == key):count = count +1;

            #print "loop end";
            #print count ;
        #print "accuracy check";
        self._calculateAccuracy();
            
            
        

                
                
            
        
        