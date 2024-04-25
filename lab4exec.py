import math ## this may be useful!!
import numpy as np 
import sys
import module_dir.qubit as qubit


if __name__ == "__main__":
    
    ourQ = qubit.Qubit 

    qlist = [1/(math.sqrt(2)), -1 * (1/(math.sqrt(2)))]
    f = 1/(math.sqrt(2))
    v = f.as_integer_ratio
    #print("test: " + str(v[0]) + "/" + str(v[1]))
    #qubit.Qubit.setvalue(ourQ, "|1>")
    qubit.Qubit.setvalue(ourQ, "|0>")
    qubit.Qubit.setvalue(ourQ, qlist)
    #testQ = qubit.Qubit 
    
    print(qubit.Qubit.getvalue_braket(ourQ))
    print("not result: ")
    print(qubit.Qubit.getvalue_vector(ourQ))
    qubit.Qubit.gate_not(ourQ)
    #print((1/(math.sqrt(2))) * np.matrix([[1, 1], [1, -1]]))
    #mZ = np.matrix([[1, 0], [0, -1]])
    #print("Z result: ")
    #Z_result = mZ.dot([1/(math.sqrt(2)), -1 * (1/(math.sqrt(2)))])
    #print(Z_result.flatten('F'))

    qubit.Qubit.gate_Z(ourQ)
    #print(ourQ)
    

    exit()
