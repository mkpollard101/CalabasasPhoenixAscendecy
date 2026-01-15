# Protocol 3: The Quantum Neuron (VQC)
# Project: CalabasasPhoenixAscendecy

from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit import Parameter
import numpy as np

def run_vqc_node():
    # The 'dial' the AI learns to turn
    theta = Parameter('θ')
    qc = QuantumCircuit(1, 1)

    # Rotating the data into higher dimensions
    qc.rx(theta, 0)
    qc.measure(0, 0)

    simulator = Aer.get_backend('qasm_simulator')
    
    # Testing the rotation limits (0 to 180 degrees)
    print(">>> Training Quantum Neuron...")
    for angle in [0, np.pi]:
        bound_circuit = qc.bind_parameters({theta: angle})
        job = execute(bound_circuit, simulator, shots=1024)
        print(f"Angle: {angle:.2f} rad -> Output: {job.result().get_counts()}")

if __name__ == "__main__":
    run_vqc_node()
