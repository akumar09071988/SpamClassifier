'''
Created on Feb 16, 2015

@author: abhishekkumar
'''
import math;
class Sigmoid(object):
    @staticmethod
    def getSigmoidVal(inputList):
        #print len(args);
        output = [];
        for i in range(0,len(inputList)):
            #print inputList[i];
            val = 0.0;
            try :
                val = 1.0/(1.0+math.exp(inputList[i]));
            except OverflowError: val =0.01;
            if(val==1):val = 0.99;
            output.append(val);
        #  print output;
        return output;
    


        
        
        