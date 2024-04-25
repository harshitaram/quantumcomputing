import math ## this may be useful!!
import numpy as np 
import sys
import parent_qubit
import nqubit

if __name__ == "__main__":
    
    ourQ = nqubit.NQubit(2)
    #v = [1, 0, 0, 1, 1, 0]
    #ourQ.set_value(-1, 1)
    print(ourQ.get_num_qubits())
    print(ourQ.to_bra_ket())
    print(ourQ.get_values())
    print(ourQ.apply_not_gate(0))
    print(ourQ.apply_not_gate(0))
    print(ourQ.apply_hadamard_gate(0))
    print(ourQ.apply_z_gate(0))
    print(ourQ.apply_hadamard_gate(0))

    exit()

