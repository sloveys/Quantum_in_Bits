from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from cmath import pi

# init computer
qr = QuantumRegister(2) # create a 2 qubit register
cr = ClassicalRegister(2) # create a 2 bit register
qc = QuantumCircuit(qr, cr)

# Write your QASM program here
qc.measure(qr, cr) # example line

# This just prints our QASM code
print(qc.qasm())

# Compile and run the Quantum circuit on a simulator backend
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim)
sim_result = job_sim.result()

# Show the results
print("Simulation: ", sim_result)
print(sim_result.get_counts(qc))
