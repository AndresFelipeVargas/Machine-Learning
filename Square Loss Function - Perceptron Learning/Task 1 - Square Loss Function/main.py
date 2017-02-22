'''******************************************

Task 1:  A and B

In this task you will explore a linear model for the boolean function A and B listed in truth table below:

A   B   A and B
0   0     0
0   1     0
1   0     0
1   1     1


Begin with a linear model that assumes all the coefficients are 0.  Using this model, describe and calculate the
squared loss function, L2 of this first model.

******************************************'''
from math import pow

# Function that will compute the hypothesis of given deltas. Make sure that listOfX[0] = 0.
def hypothesis(listOfX, listOfP):
    result = listOfP[0]

    # Run a loop to add that does the following: Summation from i = 1 to n of (x of i)*(theta of i)
    for i in range(1, len(listOfP)):
        result += listOfX[i]*listOfP[i]

    return result

def costFunction(listOfX, listOfY, listOfP):
    cost = 0
    m = len(listOfX)

    for i in range(m):
        cost += pow(hypothesis([0] + listOfX[i], listOfP) - listOfY[i][0],2)

    cost = (1.0/(2.0*m))*cost

    return cost

def main():
    # Create a list with the variables(x), outputs(y) and the thetas.
    #           A B
    listOfX = [[0,0],
               [0,1],
               [1,0],
               [1,1]]

    #        A and B
    listOfY = [[0],
               [0],
               [0],
               [1]]

    listOfP = [0, 0, 0] # Number of thetas to be used is n + 1

    m = (len(listOfX))
    cost = None
    oldCost = None

    # Run the loop indefinitely until the cost function does not change
    while (True):
        # Round the cost function to 7 decimal places
        cost = "%.10f" % costFunction(listOfX, listOfY, listOfP)

        # If the cost is not changing, then the minimum is found. Break out of the infinite loop
        if(cost == oldCost):
            break

        sum = 0
        tempDelta = []
        learnRatio = .1
        oldCost = cost

        # This loop does the gradient decent
        for j in range(len(listOfP)):
            oldDelta = listOfP[j]

            # Treat all list as mathematical vectors. To do this properly, the 0th index of all x rows must be zero.
            # This is done my concatenating [0] and the x rows
            for i in range(m):
                if(j == 0):
                    sum += (hypothesis([0] + listOfX[i], listOfP) - listOfY[i][0])

                else:
                    sum += (hypothesis([0] + listOfX[i], listOfP) - listOfY[i][0]) * ([0] + listOfX[i])[j]

            # Finalize the derivative computations
            derivative = (1.0/float(m))*sum

            # Place the new delta in the temp delta list. This is done so that all of the deltas are simultaneously
            # updated when all of the new deltas are computed.
            tempDelta.append(oldDelta - (learnRatio*derivative))

        listOfP = tempDelta

    # Once the cost function meets the criteria, output final cost and the theta variables that made that possible
    print "The final cost for the function is: ", "%.5f" % float(cost)

    print "The thetas that produce lowest cost function are: "
    for i in range(len(listOfP)):
        print "theta(", i, ") :", "%.5f" % listOfP[i]

main()