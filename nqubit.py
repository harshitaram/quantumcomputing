from parent_qubit import ParentQubit
import math 
import numpy as np

class NQubit(ParentQubit):
   pass 
   """  def __init__(self, numqubits):
        #ParentQubit.__init__(self, numqubits = numqubits)
        super().__init__(numqubits = numqubits)
    
    
    def merge_qubits(self, pq):
        #merged_qubit = ParentQubit.merge_qubits(self, pq)
        return self.merge_qubits(pq)
    
    def to_bra_ket(self):
        self.to_bra_ket
        #braket = ParentQubit.to_bra_ket(self)
        return self.to_bra_ket()
    
    def apply_not_gate(self, qb=None):
        if qb is None:
         for j in range(len(self.state)):
            first = self.state[j]
            second = self.state[j+1]
            self.state[j] = second
            self.state[j+1] = first
            j = j+2
        else:
         if j % 2 == 0: #even
          first = self.state[j]
          second = self.state[j+1]
          self.state[j] = second
          self.state[j+1] = first
         else:
          first = self.state[j-1]
          second = self.state[j]
          self.state[j-1] = second
          self.state[j] = first
        return(self)
    
    def apply_cnot_gate(self, ctrl, targ):
        post_cnot = self.apply_cnot_gate(ctrl, targ)
        return post_cnot
    
    def apply_hadamard_gate(self, qb=None):
        H_gate = (1/(math.sqrt(2))) * np.matrix([[1, 1], [1, -1]])
        if qb is None:
         in_vec = self.state
         out_arr = np.dot(H_gate, in_vec)
         self.state = out_arr.tolist()
        else:
            if qb % 2 == 0: #even
                first = self.state[qb]
                second = self.state[qb+1]
                in_vec = [first, second]
            else:
                first = self.state[qb-1]
                second = self.state[qb]
                in_vec = [first , second]
            out_arr = np.dot(H_gate, in_vec)
            out_vec = out_arr.tolist()
            a = out_vec[0][0]
            b = out_vec[0][1]
            self.state[first] = a
            self.state[second] = b
        return(self)
    
    def apply_swap_gate(self, qubit1, qubit2):
        if qubit1 >= self.numqubits or qubit2 >= self.numqubits:
            raise ValueError("Invalid qubit index: Out of range")
        swap_matrix = np.zeros((2 ** self.numqubits, 2 ** self.numqubits))
        for i in range(len(swap_matrix)):
            binary_i = bin(i)[2:].zfill(self.numqubits)
            swapped_binary = list(binary_i)
            swapped_binary[qubit1], swapped_binary[qubit2] = swapped_binary[qubit2], swapped_binary[qubit1]
            swapped_index = int("".join(swapped_binary), 2)
            swap_matrix[i][swapped_index] = 1
        self.state = np.dot(swap_matrix, self.state) """