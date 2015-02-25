'''
Created on Feb 17, 2015

@author: abhishekkumar
'''
from Utility import Utility;
class PreProcessLogReg(object):
    '''
    this class is used to preprocess files
    '''
    def _populateVocab(self,wordsDictCount):
        for key in wordsDictCount:
            if(self.vocabDict.has_key(key)):continue;
            else:
                if(self.stopWordsDict!=None):
                    if(self.stopWordsDict.has_key(key)):continue;
                self.vocabDict[key] =1;
                self.vocabList.append(key);
                
    def _makeXList(self,exampleList):
        for i in range(0,len(exampleList)):
            wordsCountDict = exampleList[i];
            examList=[];
            for word in self.vocabList:
                if(wordsCountDict.has_key(word)):
                    examList.append(wordsCountDict[word]);
                else:
                    examList.append(0);
            self.xList.append(examList);
                
                
    def _processDir(self):
        exampleList =[];
        for key in self.trainDict:
            fileList = Utility.readDir(self.trainDict[key]);
            folderName = self.trainDict[key];
            for file in fileList:
                if(file=='.DS_Store'):continue;
                self.yDict[folderName+"/"+file] = self.classDict[key];
                self.yList.append(self.classDict[key]);
                sentList = Utility.readFile(folderName+"/"+file);
                wordsDictCount = Utility.getWordsCountDict(sentList);
                exampleList.append(wordsDictCount);
                self._populateVocab(wordsDictCount);
        self._makeXList(exampleList);
        
                


    def __init__(self, trainDict,classDict,stopWordsDict=None):
        self.trainDict = trainDict;
        self.classDict = classDict;
        self.yDict={};
        self.yList=[];
        self.vocabDict ={};
        self.vocabList =[];
        self.xList=[];
        self.stopWordsDict =stopWordsDict;
        self._processDir();

        '''
        Constructor
        '''
        