'''
Created on Feb 14, 2015

@author: abhishekkumar
'''
import os;
class Utility(object):
    @staticmethod
    def readFile(fileName):
        fileObj = open(fileName);
        wordList =[];
        fileStr = fileObj.read();
        wordList.append(fileStr.lower().split(" "));
        #print wordList;
        return wordList;
    @staticmethod
    def readDir(dirName):
        fileList = os.listdir(dirName);
        return fileList;
    @staticmethod
    def getWordsCountDict(wordList):
        wordDictCount = {};
        for i in range(0,len(wordList)):
            for j in range(0, len(wordList[i])):
                if(wordDictCount.has_key(wordList[i][j])):
                    wordDictCount[wordList[i][j]]=wordDictCount[wordList[i][j]] +1;
                else:
                    wordDictCount[wordList[i][j]] = 1;
        return wordDictCount; 
    @staticmethod
    def sumList(list):
        sum =0;
        for i in range(0,len(list)):
            sum =sum +list[i];
        return sum;
    @staticmethod
    def multFeatureWeights(weight,featuresList):
        output=[];
        for i in range(0,len(featuresList)):
            listMult =map(lambda pair: pair[0]*pair[1], zip(weight, featuresList[i]));
            output.append(sum(listMult));
        return output;
    @staticmethod
    def matrixXminusOper(x,inputList):
        outputList=[];
        for i in range (0,len(inputList)):
            outputList.append(x-inputList[i]);
        return outputList;
    @staticmethod
    def readFileStop(fileName):
        fileObj = open(fileName);
        wordList =[];
        fileStr = fileObj.read();
        wordList.append(fileStr.lower().split("\n"));
        #print wordList;
        return wordList;
    @staticmethod
    def populateStopWords(fileName):
        sentList = Utility.readFileStop(fileName);
        wordDict = Utility.getWordsCountDict(sentList);
        print len(wordDict);
        return wordDict;
            
        
    
        
       
    