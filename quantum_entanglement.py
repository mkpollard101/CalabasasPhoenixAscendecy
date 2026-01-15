from qiskit import QuantumCircuit, Aer, execute

def engage_entanglement():
    # Initialize 2 Qubits
    qc = QuantumCircuit(2, 2)
    # Apply Hadamard to Qubit 0
    qc.h(0)
    # Apply CNOT to Entangle
    qc.cx(0, 1)
    # Measure
    qc.measure([0, 1], [0, 1])

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1024)
    print(f"Entangled Results: {job.result().get_counts()}")

if __name__ == "__main__":
    engage_entanglement()
