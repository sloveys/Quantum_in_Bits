from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from cmath import pi

# Init computer
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)

# QASM program
# Eve prepares the Bell State
# Initial state: |00>
qc.h(qr[0]) # (|00> + |01>)/sqrt(2)
qc.cx(qr[0], qr[1]) # (|00> + |11>)/sqrt(2)

qc.barrier()

# Alice
# Alice recives qr[0] from Eve
message = [0,1] # the message Alice wants to send Bob
# Alice encodes the message into the quantum state
if (message[0] == 1):
    qc.x(qr[0]) # (|00> + |11>)/sqrt(2) --> (|01> + |10>)/sqrt(2)
if (message[1] == 1):
    qc.z(qr[0]) # (|wx> + |yz>)/sqrt(2) --> (|wx> - |yz>)/sqrt(2)

qc.barrier()

# Bob recives qr[0] from Alice and qr[1] from eve
# Bob decodes the original message from these two qubits
qc.cx(qr[0], qr[1])
qc.h(qr[0])
qc.measure(qr, cr) # bob measers the results to get Alices message

print(qc.qasm())

# Compile and run the Quantum circuit on a simulator backend
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim)
sim_result = job_sim.result()

# Show the results
print("Simulation: ", sim_result)
print(sim_result.get_counts(qc))
