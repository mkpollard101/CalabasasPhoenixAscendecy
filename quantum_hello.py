# Protocol 1: Quantum Superposition Initialization
# Project: CalabasasPhoenixAscendecy
# Objective: Demonstrate qubit superposition (0 and 1 simultaneous state)

from qiskit import QuantumCircuit, Aer, execute

def engage_superposition():
    # 1. Initialize System: 1 Qubit, 1 Classical Bit
    qc = QuantumCircuit(1, 1)

    # 2. Apply Hadamard Gate (H)
    # This transforms the state |0> into (|0> + |1>) / sqrt(2)
    # The qubit is now in a valid superposition.
    qc.h(0)

    # 3. Collapse State (Measurement)
    qc.measure(0, 0)

    # 4. Run Simulation (1024 shots to verify probabilistic distribution)
    print(">>> Engaging Quantum Simulator...")
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)

    # 5. Telemetry
    print(f">>> Protocol Complete. State Distribution: {counts}")
    # Target Outcome: ~50% '0' and ~50% '1'

if __name__ == "__main__":
    engage_superposition()
