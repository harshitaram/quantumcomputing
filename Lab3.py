#!/usr/bin/env python
# coding: utf-8

# # Introduction
# These labs will be an introduction to the Qiskit Framework, which is a Python package, developed by IBM, for construction, testing, optimizing, simulating and running quantum circuits on real quantum computers!
# 
# Qiskit works by declaratively building up quantum circuits by creating Quantum and Classical Registers, creating a circuit object and then adding gates to the circuit that act on specific qubits.
# # This Lab
# In this particular lab assignment, these exercises build up to more complex circuits, and you will be creating circuits based on a given input and a given output.
# 
# When considering the state of a circuit in this lab, consider the "top" qubit, qubit 0 in a bitstring representing the state of the circuit. The following circuit numbering is a representation of where each qubit should be considered to be in the bitstring.
# 
# # Some helpful programming hints:
# Some helpful programming hints:
# 
# - The line circuit.draw(), where circuit is your Qiskit circuit, will draw out the circuit so you can visualize it.
# - op = qiskit.quantum_info.Operator(circuit) will create an operator object, and op.data will let you look at the overall matrix for a circuit.
# - Keep in mind that Qiskit has a different relationship between the drawing and mathematical representation than we have. Specifically, they place the left-most bit at the bottom rather than at the top. You can [**watch this video**](https://youtu.be/Gf7XFFKS9jE) for more information. This has several implications.
# - If you look at a circuit the way we do, then the state vector ends up being stored as \[00, 10, 01, 11\] rather than \[00, 01, 10, 11\] (where the qubit on top is still the left-most qubit).
# - In reality, though, Qiskit also considers the qubit order to be swapped (little endian), where the top qubit is the least significant (right-most) bit. That is for qubits from top to bottom q0, q1, q2, the bitstring is q2, q1, q0. So the state vector is still \[00, 01, 10, 11\] from this perspective. We can see this in the CX gate.
# 
# ```
# q0_0: ──■──  
#       ┌─┴─┐  
# q0_1: ┤ X ├  
#       └───┘  
# ```
#    
# This ordering also affects the matrix, resulting in the following for CX:  
# ```
# [[1, 0, 0, 0],  
#  [0, 0, 0, 1],  
#  [0, 0, 1, 0],  
#  [0, 1, 0, 0]]  
# ```
# 
# Which will take \[00: w, 01: x, 10: y, 11: z\] to \[00: w, 01: z, 10: y, 11: x\] in little endian form, and \[00: w, 01: y, 10: z, 11: x\] in big endian form (most significant bit first).
# 
# # Grading:  
# - The output matrix of your circuit will be compared against a baseline circuit, your circuit will be compared against this matrix.
# - If they do not match, we will test the circuit with different inputs and compare against the expected values.
# - You will receive feedback for whether the circuit runs. If it does not, you will receive an error message. If it runs with no message, it means that your circuit runs, but not necessarily that the answer is correct.
# - **Do not change any function names or return types**
# # Qiskit Example
# This is an example for how to build a circuit using Qiskit. It will go over how to create a circuit and apply basic gates to the qubits.
# 
# # Circuit Creation
# 
# We create a quantum circuit by first creating a quantum register with the number of qubits that will be included in the overall quantum circuit. We can also create a classical register that will hold the measurement outcomes if there any measurement operations in the circuit.
# ``` python
# # Allocate a 3-Qubit Quantum Register
# qrex = qiskit.QuantumRegister(3)
# # Allocate a 3-Bit Classical Register 
# crex = qiskit.ClassicalRegister(3)
# # Create a Quantum Circuit with a 3-Qubit Quantum Register and a 3-Bit Classical Register
# qcex = qiskit.QuantumCircuit(qrex, crex)
# ```
# 
# # Gate Addition
# For most of the circuits we will be using, gates are methods of the quantum circuit. For a single-qubit gate, indicate which qubit the gate is being applied to. For a two-qubit gate like the CNOT gate, the order of the qubits matters (control and target). For the two-qubit SWAP gate, the order doesn't matter.
# 
# ``` python
# qcex.x(qrex[0]) # Apply an X gate to the first qubit.
# qcex.z(qrex[1]) # Apply a Z gate to the second qubit.
# qcex.h(qrex[2]) # Apply an H gate to the third qubit.
# qcex.cx(qrex[0], qrex[1]) # Apply a CNOT gate where the control is the first qubit and the target is the second.
# qcex.cx(qrex[1], qrex[0]) # Apply a CNOT gate where the control is the second qubit and the target is the first.
# qcex.swap(qrex[1], qrex[2]) # Apply a SWAP gate between the second and third qubits. 
# 
# qcex.measure(qrex, crex) # Applies a measurement across all the qubits to the classical register
# 
# # To look at the circuit diagram, use .draw()
# qcex.draw()
# ```
# 

# # Pre-Exercise
# ```
#                 ┌───┐
# q0_0: ──■───────┤ H ├──X───────
#       ┌─┴─┐┌───┐└───┘  |  ┌───┐
# q0_1: ┤ X ├┤ X ├───────|──┤ X ├
#       └───┘└─┬─┘┌───┐  |  └───┘
# q0_2: ───────■──┤ Z ├──X───────
#                 └───┘
#     
# ```
# Recreate the following circuit in Qiskit. Don't worry about spacing, just get the gates in the right order. The number of qubits in the register needs to match the number of qubits in the pictured circuit. You may need to adjust this in the code provided.
# 

# In[85]:


import qiskit
#from qiskit import Aer

def hw1_0_response():
    qrpre = qiskit.QuantumRegister(3)
    qcpre = qiskit.QuantumCircuit(qrpre)
    # Put your code here (spaces for indentation)
    qcpre.cx(qrpre[0], qrpre[1])
    qcpre.cx(qrpre[2], qrpre[1])
    qcpre.h(qrpre[0])
    qcpre.z(qrpre[2])
    qcpre.swap(qrpre[0], qrpre[2])
    qcpre.x(qrpre[1]) 
    # End Code
  
    #qcpre.draw()

    return qcpre

#hw1_0_response()

#statevector_sim = Aer.get_backend('statevector_simulator')
#result = qiskit.execute(hw1_0_response(), backend = statevector_sim).result()
#print(result.get_statevector())


# # Exercise 1: 1 Qubit Circuit
# Starting in state |0⟩ create a circuit that generates a √(2)/2|0⟩ - √(2)/2|1⟩ state, or |-⟩.
# 
# You may include helper functions if needed.

# In[86]:


import qiskit

def hw1_1_response():
    qr1 = qiskit.QuantumRegister(1)
    qc1 = qiskit.QuantumCircuit(qr1)
    
    # Put your code here (spaces for indentation)
     
    qc1.x(qr1[0])
    qc1.h(qr1[0])
    
    # End Code

    return qc1



# # Exercise 2: 2 Qubit Circuit
# This time, we will not assume a known starting state. Starting in unknown state α|00⟩ + β|11⟩, create a circuit that transforms that state to a root(2)/2 * (β|00⟩-α|01⟩+β|10⟩+α|11⟩) state.
# 
# You may include helper functions if needed.

# In[87]:


import qiskit

def hw1_2_response():
    qr2 = qiskit.QuantumRegister(2)
    qc2 = qiskit.QuantumCircuit(qr2)

    # Put your code here (spaces for indentation)
    qc2.h(qr[0])
    qc2.h(qr[1])

    # Apply CNOT gate with control on qubit 0 and target on qubit 1
    qc2.cx(qr[0], qr[1])

    # Apply Hadamard gate on qubit 0
    qc2.h(qr[0])

    # End Code

    return qc2

      


# # Exercise 3: 2 Qubit Circuit
# Create a circuit that performs the following transformations:
# 
# - starting in state |00⟩ generates a √(2)/2 * (-|10⟩+|11⟩) state
# - starting in state |11⟩ generates a √(2)/2 * (|00⟩-|01⟩) state.
# **Hint:** You will need to use a CNOT Gate.
# 
# You may include helper functions if needed.

# In[88]:


import qiskit

def hw1_3_response():
    qr3 = qiskit.QuantumRegister(2)
    qc3 = qiskit.QuantumCircuit(qr3)
    
    # |00⟩ to |11⟩
    qc3.x(qr3[0])
    qc3.h(qr3[1])
    qc3.cx(qr3[1], qr3[0])
    qc3.h(qr3[0])


    return qc3
      


# # Exercise 4: 2 Qubit Circuit
# Create a circuit that:
# 
# - starting in state |00⟩ generates a 1/2 * (|00⟩ - |01⟩ - |10⟩ + |11⟩) state,
# - starting in state |10⟩ generates a 1/2 * (|00⟩ + |01⟩ - |10⟩ - |11⟩) state,
# - starting in state |01⟩ transforms to a 1/2 * (|00⟩ - |01⟩ + |10⟩ - |11⟩) state
# - starting in state |11⟩ transforms to a 1/2 * (|00⟩ + |01⟩ + |10⟩ + |11⟩) state
# **Hint:** It may be helpful to consider using SWAP Gate.
# 
# You may include helper functions if needed.
# 
# Code Editor
# 
# 1
# 

# In[89]:


import qiskit

def hw1_4_response():
    qr4 = qiskit.QuantumRegister(2)
    qc4 = qiskit.QuantumCircuit(qr4)
    
    # Put your code here (spaces for indentation)
    qc4.h(qr4[0])

    # (|01⟩ - |00⟩)
    qc4.swap(qr4[0], qr4[1])

    qc4.h(qr4[0])
    
    # End Code

    return qc4


# # Submission
# Congratulations on completing the lab!  
# Make sure you:
# 1. Download your lab as a python script (File-> Save and Export Notebook As...->Executable Script
# 2. Rename the downloaded file to **LabAnswers.py**
# 3. Upload the **LabAnswers.py** file to gradescope
# 4. Ensure the autograder runs successfully 
