'''
Created on Feb 14, 2015

@author: abhishekkumar
'''
import os;
from ReadFile import ReadFile;
class ReadDirectory(object):
    '''
    This file is used to read directory
    '''
    def _populateWordsDict(self,wordsList):
        for i in range(0,len(wordsList)):
            innerList = wordsList[i];
            for k in range(0,len(innerList)):
                words = innerList[k];
                if(self.stopWordsDict!=None):
                    if(self.stopWordsDict.has_key(words)):continue;
                if(self.wordsDict.has_key(words)):
                    self.wordsDict[words] =self.wordsDict[words] +1;
                else:
                    self.wordsDict[words] =1; 
                self.totalWords+=1;
                 
    def __init__(self, dirName,stopWordsDict =None):
        self.dirName = dirName;
        self.wordsDict={};
        self.stopWordsDict = stopWordsDict;
        self.totalWords =0;
        fileList =os.listdir(dirName);
        self.count = len(fileList)
        for fileName in fileList:
            rdFileObj = ReadFile(dirName+'/'+fileName); 
            wordsList = rdFileObj.getWords();
            self._populateWordsDict(wordsList);
        
        
        
        