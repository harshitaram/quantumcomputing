import math ## this may be useful!!
import numpy as np 

class Qubit:

    # Default Constructor
    #  Constructor without input arguments
    #  Initialize value to white or |0>
    def __init__(self):
        self.state = [1.0, 0.0]   # initialize to 100% 0


    # These are standard "setters" and "getters" 
    # You need to support inputs of both list and string
    # String is bra-ket notation, list is vector notation
    # Inputs: v - either a string (braket notation) or list (vector)
    #   The precise string will be something like |0> or |1>
    #   But it may have extra spaces surrounding it...
    # Outputs: none
    # Function: It sets the self.state based on the input value
    def setvalue(self,v):

        if (type(v) == str):
            if v.find('|1>') == -1: #take account of spaces in string
                self.state = [1.0 , 0.0]
                print("String: " + "|0>")
            else:
                self.state = [0.0, 1.0] #parse string 
                print("String: " + "|1>")
        elif (type(v) == list):
            self.state = [v[0], v[1]]
            print("List: " + "[" + str(v[0]) + " , " + str(v[1]) + "]") 
        # Use the input to set the self.state properly */
        return
            

    # String is bra-ket notation, list is vector notation
    # Inputs: none
    # Outputs: string
    #   It should take the form a|0> + b|1> where a, b are the amplitudes
    #   Please be careful to follow this form exactly, otherwise the regex capture won't work
    #   To test, you can go to https://regex101.com/r/SAflUm/1 and check your output
    # Function: It expresses the state as a string, braket notation, and returns it
    def getvalue_braket(self):
        s = str(str(self.state[0]) + "|0>" + " + " + str(self.state[1]) + "|1> ")
        print("Braket notation: " + s)
        return s


    # String is bra-ket notation, list is vector notation
    # Inputs: none
    # Outputs: list
    # Function: It expresses the state as a vector and returns it
    def getvalue_vector(self):
        
        print("vector")
        return [self.state[0], self.state[1]]


	# notgate
    # Inputs: none
    # Outputs: none
    # Function: Perform a not gate on the qubit
    def gate_not(self):
        a = self.state[0]
        b = self.state[1]
        self.state = [b , a] ##ARE WE SUPPOSED TO CHANGE THE STATE OR JUST PRINT RESULT
        print(self)


	# hgate
    # Inputs: none
    # Outputs: none
    # Function: Perform a hadamard gate on the qubit
    def gate_H(self):
        H_gate = (1/(math.sqrt(2))) * np.matrix([[1, 1], [1, -1]])
        in_vec = [self.state[0], self.state[1]]
        out_arr = np.dot(H_gate, in_vec)
        out_vec = out_arr.tolist()
        a = out_vec[0][0]
        print(a, type(a))
        b = out_vec[0][1]
        self.state = [a, b]
        print(self)


	# zgate
    # Inputs: none
    # Outputs: none
    # Function: Perform a z gate on the qubit
    def gate_Z(self):
        Z_gate = np.matrix([[1, 0], [0, -1]])
        in_vec = [self.state[0], self.state[1]]
        out_arr = np.dot(Z_gate, in_vec)
        out_vec = np.array(out_arr)
        a = out_vec[0][0]
        print(a, type(a))
        b = out_vec[0][1]
        self.state = [a, b]
        print(self)


	# measure
    # Inputs: none
    # Outputs: int result - result of measurement (0 or 1)
    # Function: Perform a measurement based on the qubit state. 
    #   this both changes the qubit state as a result of the measurement
    #   and returns the result of the measurement.
    def measure(self):
        print("measure implemented")
        a = self.state[0]
        b = self.state[1]
        prob_0 = a * a 
        randog = np.random.default_rng()
        rando = randog.random()  
        if prob_0 <= rando:
            self.state = [1.0, 0.0]
            return 0
        else:
            self.state = [0.0, 1.0]
            return 1
        

    #/* these are for grading purposes - do NOT change anything below this line!!! */
    def compare(qb1, qb2):
        # if they are equal within a certain precision
        # because they are floats, we must put in a fudge factor
        i = 0
        for v1 in qb1.state:
            v2 = qb2.state[i]
            if ((v1 - v2) > 0.01):
                return 1
            elif ((v2 - v1) > 0.01):
                return -1
            i += 1
        # if all values are equivalent, then the two are equal
        return 0

