import math 
import numpy as np 

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

class ParentQubit():
  def __init__(self, numqubits=1):
    self.numqubits = numqubits
    self.state = [[1.0, 0.0] for _ in range(2**numqubits)] # initialize each to |0>
    self.phase = [1.0] * (2 ** numqubits)
    #[1,0]
    #ParentQubit(int numqubits):
    #Constructor: initialize all bits to 0
  def amplitude(self, i):
      a_square = self[i][0] ** 2
      b_square = self[i][1] ** 2
      amp = math.sqrt(a_square + b_square)
      return(amp)
  
  def set_value(self, v, i):
      self.state[i][0] = v
      """ count = self.numqubits * 2 
      num = math.ceil(count / i) 
      j = 0
      if i % 2 == 0: #even
        j = 0
      else:
         j = 1
      self.state[num-1][j] = v """
# v is a float
# i is an integer
# set the ith value to v
# Combinations are always ordered in increasing order from 0 to 2^num_qubits-1.
# Values are negative if the phase should be negative.
  def set_values(self, v):
    self.state = v ###no for loop needed?
# v is an array of length 2^num_qubits
# set the amplitudes to v
# Combinations are always ordered in increasing order from 0 to 2^num_qubits-1.
  def get_value(self, i):
      return self.state[i][0]
  
# i is an integer
# return the amplitude of the ith configuration
  def get_values(self):
    amps = self.state
    return amps
# return the amplitudes of all configurations
  def set_phase(self, p, i):
    self.phase[i] = p
# p is a float
# i is an integer
# set the phase of the ith configuration to p
# Values are negative if the phase should be negative.
  def set_phases(self, p):
    self.phase = p
# p is an array of length 2^num_qubits
# set the phases to p
# Values are negative if the phase should be negative.
  def get_phase(self, i):
    phasev = self.phase[i]
    if phasev >= 0:
      return 1
    else:
      return -1
# i is an integer
# return the phase of the ith configuration
# return +1 for positive phase and -1 for negative phase
  def get_num_qubits(self):
    num = self.numqubits
    return num
# return the number of qubits
  def merge_qubits(self, pq):
    new_numqubits = self.numqubits + pq.numqubits
    new_states = self.state + pq.state #'+' does list concatenation in this context
    new_phases = self.phase + pq.phase
    merged_qubit = ParentQubit(new_numqubits)
    merged_qubit.state = new_states
    merged_qubit.phase = new_phases
    return merged_qubit
# pq is a ParentQubit
# this merges two sets of qubits and returns a new one that has
# a number of qubits that is the sum of the two
# the new qubits are ordered from the first qubit of the first set
# to the last qubit of the second set
  def to_bra_ket(self):
    bra_ket = ""
    for i, amplitude in enumerate(self.state):
      if amplitude[0] != 0:
        if amplitude[0] < 0:
            bra_ket += "- "
        elif i > 0:
            bra_ket += "+ "
        bra_ket += str(abs(amplitude[0]))
        bra_ket += "|"
        binary_i = bin(i)[2:].zfill(self.numqubits) #converts index value to binary and replaces leading 'Ob characters with appropriate amount of leading 0s according to number of qubits
        bra_ket += binary_i
        bra_ket += "> "
    return bra_ket
  
  
# return a string representation of the state in bra-ket notation
# e.g. 0.5|00> + 0.5|01> - 0.5|10> + 0.5|11>
# Note that we did '-' here; we want the formatting to look nice, e.g. we would not want "|00> + -|01>"
 
  """ j = 0
    if i is None:
        for j in range(len(self.state)-1):
            first = self.state[j]
            second = self.state[j+1]
            self.state[j] = second
            self.state[j+1] = first
            j = j+2
    else:
        if i % 2 == 0: #even
          first = self.state[i]
          second = self.state[i+1]
          self.state[i] = second
          self.state[i+1] = first
        else:
          first = self.state[i-1]
          second = self.state[i]
          self.state[i-1] = second
          self.state[i] = first """
  

# i is an integer
# apply the NOT gate to the ith qubit
# if i is None, apply the NOT gate to all qubits
  def apply_hadamard_gate(self, i=None):
     H_gate = (1/(math.sqrt(2))) * np.matrix([[1, 1], [1, -1]])
     j = 0
     if i is None:
       mod_H = H_gate 
       for j in range(self.numqubits-1):
          mod_H = np.kron(mod_H, H_gate)
       in_vec = self.state
       out_arr = np.dot(mod_H, in_vec)
       self.state = out_arr.tolist()
     else:
        mod_H = np.eye(2) 
        for j in range(self.numqubits-1):
          if j == i:
            mod_H = np.kron(mod_H, H_gate)
          else:
            mod_H = np.kron(mod_H, np.eye(2))
        in_vec = self.state
        out_arr = np.dot(mod_H, in_vec)
        self.state = out_arr.tolist()
        #a = out_vec[0][0]
        #b = out_vec[0][1]
        #self.state[first] = a
        #self.state[second] = b
     return(self.state)
# i is an integer
# apply the Hadamard gate to the ith qubit
# if i is None, apply the Hadamard gate to all qubits
  def apply_z_gate(self, i=None):
     Z_gate = np.matrix([[1, 0], [0, -1]])
     j = 0
     if i is None:
       mod_Z = Z_gate 
       for j in range(self.numqubits-1):
          mod_Z = np.kron(mod_Z, Z_gate)
       in_vec = self.state
       out_arr = np.dot(mod_Z, in_vec)
       self.state = out_arr.tolist()
     else:
        mod_Z = Z_gate 
        for j in range(self.numqubits-1):
          if j == i:
            mod_Z = np.kron(mod_Z, Z_gate)
          else:
            mod_Z = np.kron(mod_Z, np.eye(2))
        if i % 2 == 0: #even
          first = i
          second = i+1
          #in_vec = [self.state[first] , self.state[second]]
        else:
          first = i-1
          second = i
          #in_vec = [self.state[first] , self.state[second]]
        out_arr = np.dot(mod_Z, self.state)
        self.state = out_arr.tolist()
        #out_vec = out_arr.tolist()
        #a = out_vec[0][0]
        #b = out_vec[0][1]
        #self.state[first] = a
        #self.state[second] = b

        # Update phase array accordingly
        self.phase[first] *= -1
        self.phase[second] *= -1

     print(self.state)
# i is an integer
# apply Z to the ith qubit
# if i is None, apply the Z gate to all qubits
  def apply_cnot_gate(self, i, j):
        cnot_gate = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, 1],
                          [0, 0, 1, 0]])

        # Compute the Kronecker product of identity matrices
        permutation = list(range(self.numqubits))
        permutation[i], permutation[j] = permutation[j], permutation[i]

        # Permute rows and columns of the CNOT gate matrix
        cnot_gate_permuted = cnot_gate[permutation][:, permutation]

        # Compute the Kronecker product of identity matrices
        identity_matrix = np.eye(2)
        kronecker_matrices = [identity_matrix if k != i else cnot_gate_permuted for k in range(self.numqubits)]
        cnot_gate_matrix = np.kron(*kronecker_matrices)

        # Apply the controlled gate to the state vector
        self.state = np.dot(cnot_gate_matrix, self.state)

        return(self.state)
# i and j are integers
#apply the CNOT gate with i as the control and j as the target
  def apply_swap_gate(self, i, j):
    custom_swap_gate = np.eye(2 ** self.numqubits)
    custom_swap_gate[:, [i, j]] = custom_swap_gate[:, [j, i]]  # Swap columns i and j
  
    self.state = np.dot(custom_swap_gate, self.state)
    print(self)

# i and j are integers
# apply the SWAP gate to the ith and jth qubits

  def measure(self):
     concatenated_binary = 0
     for i in range(self.state):
            amplitude_0 = self.state[2*i]
            #amplitude_1 = self.state[2*i + 1]
            prob_0 = amplitude_0 ** 2
            
            # Perform measurement for the current qubit
            randog = np.random.default_rng()
            rando = randog.random()  
            if prob_0 <= rando:
                concatenated_binary = (concatenated_binary << 1) | 1
                # Set the state to |0> for the current qubit
                self.state[2*i] = 1.0
                self.state[2*i + 1] = 0.0
            else:
                concatenated_binary = (concatenated_binary << 1) | 0
                # Set the state to |1> for the current qubit
                self.state[2*i] = 0.0
                self.state[2*i + 1] = 1.0

     return concatenated_binary
# measure all qubits in the register
# return the value measured in the register (big endian)