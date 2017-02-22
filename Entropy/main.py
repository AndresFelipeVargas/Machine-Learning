from math import log

def entropy(parameters):
    sum = 0.0
    for i in parameters:
        sum -= i*float(log(i,2))
    return sum

def gini(parameters):
    sum = 0.0
    for i in parameters:
        sum += i*(1-i)
    return sum

def infoGain(newResult, oldResult):
    return oldResult- newResult

notSurvived = (549.0/891.0)
survived = (342.0/891.0)

defaultEntorpy = entropy([notSurvived] + [survived])

# Gender survival
genderNotSurvivedMale = (468.0/549.0)
genderNotSurvivedFemale = (81.0/549.0)
genderNotSurvived = [genderNotSurvivedMale] + [genderNotSurvivedFemale]

genderSurvivedMale = (109.0/342.0)
genderSurvivedFemale = (233.0/342.0)
genderSurvived = [genderSurvivedMale] + [genderSurvivedFemale]

male = (577.0/891.0)
female = (314.0/891.0)

genderEntropy = male*entropy([genderNotSurvivedMale] + [genderSurvivedMale]) + female*entropy([genderNotSurvivedFemale] + [genderSurvivedFemale])

# Class survival
class1NotSurvived = (80.0/216.0)
class2NotSurvived = (97.0/184.0)
class3NotSurvived = (372.0/491.0)

class1Survived = (136.0/216.0)
class2Survived = (87.0/184.0)
class3Survived = (119.0/491.0)

class1 = (216.0/891)
class2 = (184.0/891)
class3 = (491.0/891)

classEntropy = class1*entropy([class1NotSurvived] + [class1Survived]) + class2*entropy([class2NotSurvived] + [class2Survived]) + class3*entropy([class3NotSurvived] + [class3Survived])

# Class survival
embarkedCNotSurvived = (75.0/168.0)
embarkedQNotSurvived = (47.0/77.0)
embarkedSNotSurvived = (427.0/644.0)

embarkedCSurvived = (93.0/168.0)
embarkedQSurvived = (30.0/77.0)
embarkedSSurvived = (217.0/644.0)

embarkedC = (168.0/891)
embarkedQ = (77.0/891)
embarkedS = (644.0/891)

classEntropy = embarkedC*entropy([embarkedCNotSurvived] + [embarkedCSurvived]) + embarkedQ*entropy([embarkedQNotSurvived] + [embarkedQSurvived]) + embarkedS*entropy([embarkedSNotSurvived] + [embarkedSSurvived])


print "%.4f" % defaultEntorpy
print "%.4f" % classEntropy
print "%.4f" % infoGain(classEntropy, defaultEntorpy)