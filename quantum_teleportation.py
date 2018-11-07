from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from cmath import pi

# Init computer
qr = QuantumRegister(3)
cr = ClassicalRegister(2)
crout = ClassicalRegister(1, "out")
qc = QuantumCircuit(qr, cr, crout)

# QASM program
# Eve prepares the Bell State
qc.h(qr[0])
qc.cx(qr[0], qr[1])

qc.barrier()

# Alice receives qr[1] from Eve
# Alice has some quantum state in qr[2]
qc.u3(pi/4, pi/3, pi/2, qr[2])

# Alice prepares the teleportation
qc.cx(qr[2], qr[1])
qc.h(qr[2])
qc.measure(qr[1], cr[0])
qc.measure(qr[2], cr[1])

qc.barrier()

# Bob receives qr[0] from Eve
# Bob receives cr[0] & cr[1] from Alice
# Bob completes teleportation from Alice
qc.x(qr[0]).c_if(cr, 1)
qc.x(qr[0]).c_if(cr, 3)
qc.z(qr[0]).c_if(cr, 2)
qc.z(qr[0]).c_if(cr, 3)

# Bob measures the quantum state from Alice (not part of QT algo)
qc.measure(qr[0], crout[0])

# set operation registers to zero so that output is easier to read
qc.reset(qr[1])
qc.measure(qr[1], cr[0])
qc.measure(qr[1], cr[1])

print(qc.qasm())

# Compile and run the Quantum circuit on a simulator backend
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim)
sim_result = job_sim.result()

# Show the results
print("Simulation: ", sim_result)
print(sim_result.get_counts(qc))
