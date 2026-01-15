# Protocol 2: Quantum Entanglement (The Bell State)
# Project: CalabasasPhoenixAscendecy
# Objective: Create a non-local link between two qubits (Einstein's "Spooky Action")

from qiskit import QuantumCircuit, Aer, execute

def engage_entanglement():
    # 1. Initialize 2 Qubits and 2 Classical Bits
    qc = QuantumCircuit(2, 2)

    # 2. Apply Hadamard to Qubit 0 (Put it in Superposition)
    qc.h(0)

    # 3. Apply CNOT Gate (Control: 0, Target: 1)
    # This "entangles" them. If Qubit 0 flips, Qubit 1 flips with it.
    qc.cx(0, 1)

    # 4. Measure both qubits
    qc.measure([0, 1], [0, 1])

    # 5. Run Simulation
    print(">>> Engaging Entanglement Link...")
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)

    # 6. Telemetry
    print(f"Entangled Results: {counts}")
    # You should ONLY see '00' and '11'.
    # You should almost NEVER see '01' or '10' (noise aside).

if __name__ == "__main__":
    engage_entanglement()
