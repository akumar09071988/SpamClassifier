'''
Created on Feb 14, 2015

@author: abhishekkumar
'''

class ReadFile(object):
    def _getNumLines(self,filePath):
        self.num_lines =sum(1 for line in open(filePath));
        
    def getWords(self):
        self.wordList =[];
        for i in range(0,self.num_lines):
            line = self.fileObj.next();
            self.wordList.append(line.lower().split(' '));
        return self.wordList;

    def __init__(self, fileName):
        self.fileName = fileName;
        self.fileObj = open(fileName);
        self._getNumLines(fileName);
        
        