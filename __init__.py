from ReadDirectory import  ReadDirectory;
from NBTrain import NBTrain;
from ClassesAttr import ClassesAttr;
from NBPredict import NBPredict;
from PreProcessLogReg import PreProcessLogReg;
from sigmoidFunction import Sigmoid;
from TrainPredictObject import TrainPredictObject;
from LogisticReg import Logisticreg;
from Utility import Utility;
import sys;

def nbFunc(dirDict,dirTestDict,classDict,laplaceConstant,stopWordsDict=None):
    classObjDict={}
    for key in dirDict:
        rDirObj  = ReadDirectory(dirDict[key],stopWordsDict);
        classObj = ClassesAttr();
        classObj.type = key;
        classObj.numOfDocs = rDirObj.count;
        classObj.totalWords = rDirObj.totalWords;
        classObj.uniqeWords = len(rDirObj.wordsDict);
        classObj.wordsCountDict = rDirObj.wordsDict;
        classObjDict[key] = classObj;
    nbTrainObj = NBTrain(classObjDict,laplaceConstant);    
    nbPredictObj = NBPredict(classObjDict,nbTrainObj,dirTestDict,laplaceConstant);
    if(stopWordsDict!=None):
        print str(nbPredictObj.accuracy) + " accuracy in Naive bayes with laplace constanct "+str(laplaceConstant)+" with stop words";
    else:
        print str(nbPredictObj.accuracy) + " accuracy in Naive bayes with laplace constanct "+str(laplaceConstant) +" without stopwords";
    
def logisticRegFunc(dirDict,dirTestDict,classDict,numIter,lambdaVal,wordsDict=None):
    preProcessTrainObj = PreProcessLogReg(dirDict,classDict,wordsDict);
    trainObj = TrainPredictObject();
    trainObj.vocabDict = preProcessTrainObj.vocabDict;
    trainObj.vocabList = preProcessTrainObj.vocabList;
    trainObj.yDict = preProcessTrainObj.yDict;
    trainObj.yList = preProcessTrainObj.yList;
    trainObj.xList = preProcessTrainObj.xList;
    preProcessTrainObj1 = PreProcessLogReg(dirTestDict,classDict);
    trainObj1 = TrainPredictObject();
    trainObj1.vocabDict = preProcessTrainObj1.vocabDict;
    trainObj1.vocabList = preProcessTrainObj1.vocabList;
    trainObj1.yDict = preProcessTrainObj1.yDict;
    trainObj1.yList = preProcessTrainObj1.yList;
    trainObj1.xList = preProcessTrainObj1.xList;
    logReg = Logisticreg(trainObj,trainObj1,lambdaVal,0.04,numIter);
    if(wordsDict!=None):
        print "accuracy "+ str(logReg.accuracy)+" number of iter "+str(numIter)+" lmbdaVal "+ str(lambdaVal)+ " with stop words";
    else:
        print "accuracy "+ str(logReg.accuracy)+" number of iter "+str(numIter)+" lmbdaVal "+ str(lambdaVal)+ " without stop words";
def main():
    print sys.argv
    trainFolder = sys.argv[4];
    testFolder = sys.argv[5];
    dirDict={};
    dirDict['spam'] = trainFolder+"/spam";
    dirDict['ham'] = trainFolder+"/ham";
    dirTestDict ={};
    dirTestDict['spam'] = testFolder+"/spam";
    dirTestDict['ham'] = testFolder+"/ham";
    classDict={};
    classDict['spam'] =1;
    classDict['ham']=0;
    laplaceConstant=2;
    wordsDict = Utility.populateStopWords('stopwords.txt');
    lambdaVal = float(sys.argv[1]);
    numIter = int(sys.argv[2]);
    laplaceConstant = sys.argv[3];
    #print wordsDict;
    nbFunc(dirDict, dirTestDict, classDict,float(laplaceConstant));
    nbFunc(dirDict,dirTestDict, classDict,float(laplaceConstant),wordsDict);
    logisticRegFunc(dirDict,dirTestDict,classDict,numIter,lambdaVal,wordsDict);
    logisticRegFunc(dirDict,dirTestDict,classDict,numIter,lambdaVal);
            
    
    
    
    
if __name__ == '__main__':
        main();