import random

def rollDie():
  # Returns a random int between 1 and 6
  return random.choice([1,2,3,4,5,6])

print(rollDie())

def rollN(n):
  result=''
  for i in range(n):
    result=result + str(rollDie())+" "
  print(result)

print(rollDie())
print(rollN(10))    

def flip(numFlips):
  heads=0
  for i in range(numFlips):
    if random.choice(('H','T'))=='H':
      heads +=1
  return heads/numFlips

print(flip(5))

def flipSim(numFlipsPerTrial,numTrials):
  fracHeads=[]
  for i in range(numTrials):
    fracHeads.append(flip(num.FlipsPerTrial))
    mean= sum(fracHeads)/len(fracHeads)
  return mean  

# print(flipSim(10,1))

def flipPlot(minExp, maxExp):
  ratios,diffs,xAxis=[],[],[]
  for exp in range(minExp, maxExp +1):
    xAxis.append(2**exp)
  for numFlips in xAxis:
    numHeads=0
    for n in range (numFlips):
      if random.choice(('H','T'))=='H':
        numHeads +=1
    numTails = numFlips - numHeads
    try:
      ratios.append(numHeads/numTails)
      diffs.append(abs(numHeads - numTails))
    except ZeroDivisionError:
      contiune
  pylab.title('Difference Between Heads and Tails')
  pylab.xlabel('Number of Flips')
  pylab.ylabel('Abs(#Heads - #Tails)')  
  pylab.plot(xAxis, diffs, 'k')
  pylab.figure()
  pylab.title('Heads/Tails Ratios')
  pylab.xlabel('Number of Flips')
  pylab.ylabel('#Heads/#Tails')
  pylab.plot(xAxis, ratios, 'k')     

random.seed(0)
