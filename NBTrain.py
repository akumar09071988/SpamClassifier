'''
Created on Feb 14, 2015

@author: abhishekkumar
'''
from ClassesAttr import ClassesAttr;

class NBTrain(object):
    '''
    This trains Naive Bayes Classifier
    '''

    def _getTotalUniqueWords(self):
        for key in self.classesDict:
            rdObj = self.classesDict[key];
            tempDict = rdObj.wordsCountDict;
            for key1 in tempDict:
                if(self.vocabDict.has_key(key1)):continue;
                else:self.vocabDict[key1] = 'Y';
                
    def _setProbVocab(self):
        for key in self.vocabDict:
            for key1 in self.classesDict:
                classAttr = self.classesDict[key1];
                tempDict = classAttr.wordsCountDict;
                denominator = float(classAttr.totalWords+(self.laplaceConstant*len(self.vocabDict)));
                if(tempDict.has_key(key)):
                    num = float(tempDict[key]+self.laplaceConstant);
                    prob = num / denominator;
                else:
                    prob = float(self.laplaceConstant)/denominator;
                newKey = key+"|"+key1;
                self.probDict[newKey] = prob;
                
            
            
    def __init__(self, classesDict,laplaceConstant):
        self.classesDict = classesDict;
        self.laplaceConstant=laplaceConstant;
        self.probDict ={};
        self.vocabDict={};
        self._getTotalUniqueWords();
        self._setProbVocab();
        #print len(self.vocabDict);
        #print len(self.probDict);
        
        