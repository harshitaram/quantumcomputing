from parent_qubit import ParentQubit
import math 
import numpy as np 

class SingleQubit(ParentQubit):
    # def __init__(self):
    #     super().__init__(numqubits=1)
    
    # def set_value(self, v, i):
    #     self.state[i] = v
    
    # def set_values(self, v):
    #     self.state = v
    
    # def get_value(self, i):
    #     return self.state[i]
    
    # def get_values(self):
    #     return self.state
    
    # def set_phase(self, p, i):
    #     self.phase[i] = p
    
    # def set_phases(self, p):
    #     self.phase = p

    # def merge_qubits(self, pq):
    #     raise NotImplementedError("Cannot merge qubits for SingleQubit")
    
    # def to_bra_ket(self):
    #     bra_ket = "{:.2f}|0>".format(abs(self.state[0]))
    #     if self.state[1] != 0:
    #         if self.state[1] < 0:
    #             bra_ket += " - {:.2f}|1>".format(abs(self.state[1]))
    #         else:
    #             bra_ket += " + {:.2f}|1>".format(self.state[1])
    #     return bra_ket

    # def apply_not_gate(self, i=None):
    #     if i is None or i == 0 or i == 1:
    #          a = self.state[0]
    #          b = self.state[1]
    #          self.state = [b , a] ##ARE WE SUPPOSED TO CHANGE THE STATE OR JUST PRINT RESULT
    #     print(self)
    
    # def apply_hadamard_gate(self, i=None):
    #     if i is None or i == 0:
    #         h_gate = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
    #         self.state = np.dot(h_gate, self.state)
    #     else:
    #         raise ValueError("Invalid qubit index for SingleQubit")
    
    # def apply_z_gate(self, i=None):
    #     z_gate_matrix = np.array([[1, 0], [0, -1]])
    #     self.state = np.dot(z_gate_matrix, self.state)
    
    # def apply_swap_gate(self, i, j):
    #     raise NotImplementedError("Cannot apply SWAP gate for SingleQubit")
    
    # def apply_cnot_gate(self, i, j):
    #     raise NotImplementedError("Cannot apply CNOT gate for SingleQubit")
    
    def measure(self):
        a = self.state[0]
        b = self.state[1]
        prob_0 = a * a 
        randog = np.random.default_rng()
        rando = randog.random()  
        if prob_0 <= rando:
            self.state = [0.0, 1.0]
            return 1
        else:
            self.state = [1.0, 0.0]
            return 0