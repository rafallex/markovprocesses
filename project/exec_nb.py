import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

path = 'Simulation.ipynb'
nb = nbformat.read(path, as_version=4)

print("Executing notebook...")
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': os.getcwd()}})

print("Writing notebook...")
nbformat.write(nb, path)

# Verify
code_cells = [c for c in nb.cells if c.cell_type == 'code']
counts = [c.execution_count for c in code_cells]
print(f"Execution counts: {counts}")
print("Done!")
