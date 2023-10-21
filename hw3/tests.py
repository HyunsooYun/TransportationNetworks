import os
import sys
import traceback

import network
import path
import utils
   
IS_MISSING = -1

def approxEqual(value, target, tolerance):
   if (abs(target) <= tolerance ): return abs(value) <= tolerance
   return abs(float(value) / target - 1) <= tolerance
   
def check(name, value, target, tolerance):
   if approxEqual(value, target, tolerance):
      return True
   else:
      print("\nWrong %s: your value %s, correct value %s"
               % (name, value, target))
      return False

def acyclicShortestPath(testFileName):

   print("Running acyclic shortest path test: " + str(testFileName) + "...", end='')
   
   try:
      with open(testFileName, "r") as testFile:
         # Read test information
         try:
            fileLines = testFile.read().splitlines()
            pointsPossible = IS_MISSING
            networkFile = IS_MISSING
            tripsFile = IS_MISSING
            origin = IS_MISSING
            backlink = list()
            cost = list()
            for line in fileLines:
               # Ignore comments and blank lines
               if len(line.strip()) == 0 or line[0] == '#':
                  continue
                   
               # Set points possible
               if pointsPossible == IS_MISSING:
                  pointsPossible = int(line)
                  continue
                  
               # Identify network files
               if networkFile == IS_MISSING:
                  networkFile = os.path.normpath(line)
                  continue
               if tripsFile == IS_MISSING:
                  tripsFile = os.path.normpath(line)
                  continue
                  
               # Read origin
               if origin == IS_MISSING:
                  origin = int(line)
                  continue
                  
               # Read answer
               answerRow = line.split()
               backlink.append(answerRow[0])
               cost.append(float(answerRow[1]))
                  
         except:
            print("\nError running test %s, attempting to continue with remaining tests.  Exception details: " % testFileName)
            traceback.print_exc(file=sys.stdout)
            return 0, 0
            
         # Now run the actual test
         try:
            testNetwork = network.Network(networkFile, tripsFile)
            testNetwork.findTopologicalOrder()
            testNetwork.createTopologicalList()
            studentBacklink, studentCost = testNetwork.acyclicShortestPath(origin)
            for i in range(1, testNetwork.numNodes + 1):
               if check("Node %d cost" % i,studentCost[i],cost[i-1],0.01) == False \
                                             or studentBacklink[i] != backlink[i-1]:
                  print("...fail")
                  return 0, pointsPossible
         except utils.NotYetAttemptedException:
            print("...not yet attempted")
            return 0, pointsPossible
         except:
            print("\nException raised, attempting to continue:")
            traceback.print_exc(file=sys.stdout)                     
            print("\n...fail")
            return 0, pointsPossible
            
         print("...pass")
         return pointsPossible, pointsPossible

         
   except IOError:
      print("\nError running test %s, attempting to continue with remaining tests.  Exception details: " % testFileName)
      traceback.print_exc(file=sys.stdout) 
      return 0, 0

def shortestPath(testFileName):

   print("Running shortest path test: " + str(testFileName) + "...", end='')
   
   try:
      with open(testFileName, "r") as testFile:
         # Read test information
         try:
            fileLines = testFile.read().splitlines()
            pointsPossible = IS_MISSING
            networkFile = IS_MISSING
            tripsFile = IS_MISSING
            origin = IS_MISSING
            backlink = list()
            cost = list()
            for line in fileLines:
               # Ignore comments and blank lines
               if len(line.strip()) == 0 or line[0] == '#':
                  continue
                   
               # Set points possible
               if pointsPossible == IS_MISSING:
                  pointsPossible = int(line)
                  continue
                  
               # Identify network files
               if networkFile == IS_MISSING:
                  networkFile = os.path.normpath(line)
                  continue
               if tripsFile == IS_MISSING:
                  tripsFile = os.path.normpath(line)
                  continue
                  
               # Read origin
               if origin == IS_MISSING:
                  origin = int(line)
                  continue
                  
               # Read answer
               answerRow = line.split()
               backlink.append(answerRow[0])
               cost.append(float(answerRow[1]))
                  
         except:
            print("\nError running test %s, attempting to continue with remaining tests.  Exception details: " % testFileName)
            traceback.print_exc(file=sys.stdout)
            return 0, 0
            
         # Now run the actual test
         try:
            testNetwork = network.Network(networkFile, tripsFile)
            studentBacklink, studentCost = testNetwork.shortestPath(origin)
            for i in range(1, testNetwork.numNodes + 1):
               costCheck = check("Node %d cost" % i,studentCost[i],cost[i-1],0.01)
               if costCheck == False:
                  print("...fail")
                  return 0, pointsPossible               
            # Now costs are correct, check backlinks (accounting for ties)
            for i in range(1, testNetwork.numNodes + 1):                           
               if backlink[i-1] == utils.NO_PATH_EXISTS:
                  if studentBacklink[i] != utils.NO_PATH_EXISTS:
                     print("Node %d backlink should be %s", i, utils.NO_PATH_EXISTS)
                     backlinkCheck = False
                  else:
                     backlinkCheck = True
               else:
                  studentBacknode = testNetwork.link[studentBacklink[i]].tail
                  backlinkCheck = check("Backlink to node %d leads to wrong cost" % i, cost[studentBacknode-1] + testNetwork.link[studentBacklink[i]].cost, cost[i-1],0.01)
               if backlinkCheck == False:
                  print("...fail")
                  return 0, pointsPossible
         except utils.NotYetAttemptedException:
            print("...not yet attempted")
            return 0, pointsPossible
         except:
            print("\nException raised, attempting to continue:")
            traceback.print_exc(file=sys.stdout)                     
            print("\n...fail")
            return 0, pointsPossible
            
         print("...pass")
         return pointsPossible, pointsPossible

         
   except IOError:
      print("\nError running test %s, attempting to continue with remaining tests.  Exception details: " % testFileName)
      traceback.print_exc(file=sys.stdout) 
      return 0, 0

def allOrNothing(testFileName):

   print("Running all-or-nothing test: " + str(testFileName) + "...", end='')
   
   try:
      with open(testFileName, "r") as testFile:
         # Read test information
         try:
            fileLines = testFile.read().splitlines()
            pointsPossible = IS_MISSING
            networkFile = IS_MISSING
            tripsFile = IS_MISSING
            origin = IS_MISSING
            answer = dict()
            for line in fileLines:
               # Ignore comments and blank lines
               if len(line.strip()) == 0 or line[0] == '#':
                  continue
                   
               # Set points possible
               if pointsPossible == IS_MISSING:
                  pointsPossible = int(line)
                  continue
                  
               # Identify network files
               if networkFile == IS_MISSING:
                  networkFile = os.path.normpath(line)
                  continue
               if tripsFile == IS_MISSING:
                  tripsFile = os.path.normpath(line)
                  continue
                  
               # Read answer
               answerRow = line.split()
               answer[answerRow[0]] = float(answerRow[1])
                  
         except:
            print("\nError running test %s, attempting to continue with remaining tests.  Exception details: " % testFileName)
            traceback.print_exc(file=sys.stdout)
            return 0, 0
            
         # Now run the actual test
         try:
            testNetwork = network.Network(networkFile, tripsFile)
            student = testNetwork.allOrNothing()
            studentTSTT = sum([testNetwork.link[ij].cost * student[ij] for ij in testNetwork.link])
            answerTSTT = sum([testNetwork.link[ij].cost * answer[ij] for ij in testNetwork.link])            
            if check("TSTT "	, studentTSTT,answerTSTT,0.01) == False:
               print("...fail")
               return 0, pointsPossible
         except utils.NotYetAttemptedException:
            print("...not yet attempted")
            return 0, pointsPossible
         except:
            print("\nException raised, attempting to continue:")
            traceback.print_exc(file=sys.stdout)                     
            print("\n...fail")
            return 0, pointsPossible
            
         print("...pass")
         return pointsPossible, pointsPossible

         
   except IOError:
      print("\nError running test %s, attempting to continue with remaining tests.  Exception details: " % testFileName)
      traceback.print_exc(file=sys.stdout) 
      return 0, 0
