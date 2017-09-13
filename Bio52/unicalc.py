from data import UNICALC_DB as database
import math

def merge(units1, units2):
  '''
  Given two lists of sorted units, returns a single list of sorted units

  >>> merge(['m', 'm', 's'], ['kg', 'm', 's', 's'])
  ['kg', 'm', 'm', 'm', 's', 's', 's']
  '''

  L = list() # empty list to be returned later

  while ((len(units1) > 0) and (len(units2) > 0)): #keep looping until one of the lists is empty
    if(units1[0] < units2[0]): #appends the alphabetically first unit onto L
      L.append(units1[0])
      units1 = units1[1:]
    else:
      L.append(units2[0])
      units2 = units2[1:]

  L += units1 + units2 #appends what is left to the list L
  '''for one in UNICALC_DB:
  	while (units1[counter1] == one)'''

  return L # replace this line with your code

#print(merge(['m', 'm', 's'], ['kg', 'm', 's', 's']))


def nMerge(units, n):
  '''
  Given a sorted list of units and a non-negative integer n, returns a sorted 
  version of n copies of units.

  >>> nMerge(['kg', 'm', 's'], 0)
  []
  >>> nMerge(['kg', 'm', 's'], 1)
  ['kg', 'm', 's']
  >>> nMerge(['kg', 'm', 's'], 2)
  ['kg', 'kg', 'm', 'm', 's', 's']
  '''
  L = list() #Final list
  for x in units: #every element in units
  	for y in range(n): #appends n number of times
  		L.append(x)

  return L # replace this line with your code

#print(nMerge(['kg', 'm', 's'], 1))
#print(nMerge(['kg', 'm', 's'], 2))


def cancel(units1, units2):
  '''
  Give two sorted lists of units, returns a new, sorted list of all the units in 
  units1 after canceling with units2. 
  >>> cancel(['m', 'm', 's'], ['kg', 'm', 's', 's'])
  ['m']
  >>> cancel(['m', 's'], ['kg', 'm', 's', 's'])
  []
  >>> cancel(['m', 's', 's', 's'], ['kg', 'm', 's', 's'])
  ['s']
  >>> cancel(['kg', 'm', 's', 's'], ['m', 'm', 's'])
  ['kg', 's']
  '''
  L = list() #new list to return
  counter = 0 
  a = list(units2) #copies onto new list so original is not changed

  while (counter < len(units1)): 
  	if(units1[counter] in a): #if same or exist in units2, then remove from units2
  		a.remove(units1[counter])
  	else:
  		L.append(units1[counter]) #if does not exist in units2 then add to L
  	counter += 1


  '''for x in units1:
  	if (x in units2):
  	  units1.remove(x)
  	  units2.remove(x) '''


  return L # returns list L
  


#print(cancel(['m', 'm', 's'], ['kg', 'm', 's', 's']))
#print(cancel(['kg', 'm', 's', 's'], ['m', 'm', 's']))
#print(cancel(['m', 's', 's'], ['kg', 'm', 's', 's']))
#print('s' in ['kg', 'm', 's', 's'])

def simplify(quantity):
  '''
  Takes a quantity and returns another quantity of the same value, but having 
  canceled out any shared elements between the numerator and denominator. 

  >>> simplify( (1.0, ['m', 'm', 's'], ['m', 's', 's'], 0.0) )
  (1.0, ['m'], ['s'], 0.0)
  >>> simplify( (1.0, ['kg', 'm', 'm', 's'], ['kg', 'kg', 'm', 's'], 0.0) )
  (1.0, ['m'], ['kg'], 0.0)
  '''

  a = cancel(quantity[1],quantity[2]) #cancel numerator
  b = cancel(quantity[2],quantity[1]) #cancel denominator

  return (quantity[0],a,b,quantity[3]) # return newly cancled units

#print(simplify( (1.0, ['m', 'm', 's'], ['m', 's', 's'], 0.0) ))

def multiply(quantity1, quantity2):
  '''
  Takes in two quantities and returns a simplified quantity representing 
  their product. 

  >>> multiply( (42.0, ['kg', 'm', 'm'], ['s', 's'], 1.0), (42.0, ['s'], ['kg', 'm'], 1.0) )
  (1764.0, ['m'], ['s'], 59.39696961966999)
  >>> multiply( (2.0, ['meter'], ['amp', 'w'], 0.01), (0.5, ['kg', 'x'], ['s'], 0.01) )
  (1.0, ['kg', 'meter', 'x'], ['amp', 's', 'w'], 0.020615528128088305)
  '''
  number = quantity1[0]*quantity2[0]
  num = cancel(quantity1[1],quantity2[2]) + (cancel(quantity2[1],quantity1[2])) #cancel numerator
  #print(cancel(quantity1[1],quantity2[2]))
  #print(cancel(quantity2[1],quantity1[2]))
  #print(num)
  den = cancel(quantity1[2],quantity2[1]) + (cancel(quantity2[2],quantity1[1])) #cancel denominator
  error = quantity1[0]*quantity2[0]*math.sqrt(math.pow((quantity1[3]/quantity1[0]),2) + math.pow((quantity2[3]/quantity2[0]),2))

  return (number,num,den,error) # replace this line with your code
#print(multiply( (42.0, ['kg', 'm', 'm'], ['s', 's'], 1.0), (42.0, ['s'], ['kg', 'm'], 1.0) ))
#print(multiply( (2.0, ['meter'], ['amp', 'w'], 0.01), (0.5, ['kg', 'x'], ['s'], 0.01) ))

def power(quantity, p):
  '''
  Takes in a quantity and an integer p and returns the result of quantity raised
  to the power p.

  >>> power( (200.0, ['euro'], [], 1.0), 0 )
  (1.0, [], [], 0.0)

  >>> power( (200.0, ['euro'], [], 1.0), -1 )
  (0.005, [], ['euro'], 2.5e-05)

  >>> power( (200.0, ['euro'], [], 1.0), 3 )
  (8000000.0, ['euro', 'euro', 'euro'], [], 120000.0)
  '''

 # x = p 
  number = math.pow(quantity[0],p)
  if (p >= 0):
  	num = nMerge(quantity[1],p)
  	den = nMerge(quantity[2],p)
  else:
  	num = nMerge(quantity[2],-p)
  	den = nMerge(quantity[1],-p)
  #a = math.pow((quantity[3]/quantity[0]),2) * math.pow(p,2)
  #if (a < 0):
  #	a = -a
 # b = math.sqrt(math.pow((quantity[3]/quantity[0]),2) * math.pow(p,2))
  error = abs(p) * math.pow(quantity[0],p-1) * quantity[3]
  
  return (number,num,den,error) # replace this line with your code
#print(power( (200.0, ['euro'], [], 1.0), 0 ))
#print(power( (200.0, ['euro'], [], 1.0), -1 ))
#print(power( (200.0, ['euro'], [], 1.0), 3 ))

def divide(quantity1, quantity2):
  '''
  Takes in two quantities and returns a simplified quantity representing 
  their quotient. 

  >>> divide( (42.0, ['kg', 'm', 'm'], ['s', 's'], 1.0), (42.0, ['kg', 'm'], ['s'], 1.0) )
  (1.0, ['m'], ['s'], 0.03367175148507369)
  >>> divide( (2.0, ['meter'], ['amp', 'w'], 0.01), (0.5, ['kg', 'x'], ['s'], 0.01) )
  (4.0, ['meter', 's'], ['amp', 'kg', 'w', 'x'], 0.08246211251235322)
  '''
  number = 1/quantity2[0] * quantity1[0]
  num = cancel(quantity1[1],quantity2[1]) + (cancel(quantity2[1],quantity1[1])) #cancel numerator
  #print(cancel(quantity1[1],quantity2[2]))
  #print(cancel(quantity2[1],quantity1[2]))
  #print(num)
  den = cancel(quantity1[2],quantity2[2]) + (cancel(quantity2[2],quantity1[2])) #cancel denominator
  
  error = quantity1[0]*(1/quantity2[0])* math.sqrt(math.pow((quantity1[3]/quantity1[0]),2) + math.pow((quantity2[3]/quantity2[0]),2))

  return (number,num,den,error) # replace this line with your code

#print(divide( (42.0, ['kg', 'm', 'm'], ['s', 's'], 1.0), (42.0, ['kg', 'm'], ['s'], 1.0) ))
#print(divide( (2.0, ['meter'], ['amp', 'w'], 0.01), (0.5, ['kg', 'x'], ['s'], 0.01) ))


def isSimplified(num, denom):
	for numerator in num:
		if numerator in database.keys():
			return False
	for denominator in denom:
		if denominator in database.keys():
			return False
	return True

def normalizeUnit(unit):
  '''
  Takes in a string unit and returns the equivalent normalized quantity.

  >>> normalizeUnit('weber')
  (1.0, ['kg', 'meter', 'meter'], ['ampere', 'second', 'second', 'second', 'second'], 0.0)
  >>> normalizeUnit('ampere')
  (1.0, ['ampere'], [], 0.0)
  '''
  num, denom = [], []
  num += database[unit][1]
  denom += database[unit][2]
  numAppended, denomAppended = len(num), len(denom)
  while 1:
  	tempNum, tempDenom = [], []
  	for i in range(numAppended):
  		temp = num.pop()
  		if temp in database.keys():
  			tempNum += database[temp][1]
  			tempDenom += database[temp][2]
  		else:
  			tempNum.append(temp)
  	for i in range(denomAppended):
  		temp = denom.pop()
  		if temp in database.keys():
  			tempNum += database[temp][2]
  			tempDenom += database[temp][1]
  		else:
  			tempDenom.append(temp)
  	numAppended = len(tempNum)
  	denomAppended = len(tempDenom)
  	num += tempNum
  	denom += tempDenom
  	if isSimplified(num, denom):
  		break

  return (1.0, cancel(num, denom), cancel(denom, num), 0.0) #cancel denominator



print(normalizeUnit('weber'))
print(normalizeUnit('foot'))



def normalizeQuantity(quantity):
  '''
  Takes in a quantity and returns the equivalent normalized quantity.

  >>> normalizeQuantity( (42.0, ['weber'], ['ampere', 'volt'], 1.0) )
  (42.0, [], ['ampere', 'second'], 1.0)
  >>> normalizeQuantity( (14.4, ['foot'], [], 0.3) )
  (4.389040707264, ['meter'], [], 0.091438348068)
  >>> normalizeQuantity( (2.0, ['foot'], ['minute'], 0.1) )
  (0.010159816452, ['meter'], ['second'], 0.0005079908226)
  '''

  pass # replace this line with your code


def add(quantity1, quantity2):
  '''
  Takes two quantities and returns their normalized sum.

  >>> add( (42.0, ['inch'], [], 1.0), (42.0, ['inch'], [], 1.0) )
  (2.13356145492, ['meter'], [], 0.03592037554409925)

  >>> add( (42.0, ['inch'], [], 1.0), (42.0, ['s'], [], 1.0) )
  Traceback (most recent call last):
  ValueError: unit mismatch
  '''

  pass # replace this line with your code


def subtract(quantity1, quantity2):
  '''
  Takes two quantities and returns their normalized difference.

  >>> subtract( (42.0, ['inch'], [], 1.0), (42.0, ['inch'], [], 1.0) )
  (0.0, ['meter'], [], 0.03592037554409925)
  >>> subtract( (42.0, ['inch'], [], 1.0), (42.0, ['s'], [], 1.0) )
  Traceback (most recent call last):
  ValueError: unit mismatch
  '''

  pass # replace this line with your code


def convert(quantity1, quantity2):
  '''
  Convert one quantity to another.

  >>> convert( (1.0, ['week'], [], 0.0), (1.0, ['day'], [], 0.0) )
  (7.0, [], [], 0.0)
  '''

  return normalizeQuantity(divide(quantity1, quantity2))

values = [0,1,2,3,4,5,6]
print(values[::-1])

def mystery(f,l):
  if not l:
    return False
  elif f(l[0]):
    return True
  else: 
    return mystery(f,l[1:])

print(mystery(print,[1,2,3]))
