import json
from flask import Flask, jsonify,request
import time
from qiskit_ibm_runtime import QiskitRuntimeService, Options, Sampler
from qiskit import QuantumCircuit
from quantum_serverless.serializers import program_serializers, serializers

app = Flask(__name__)



def circuit_invoke(cir):
    circuit=cir
    
    service = QiskitRuntimeService()
    options = Options(optimization_level=1)
    backend = service.backend("ibmq_qasm_simulator")
    sampler = Sampler(backend=backend, options=options)
    print("You just have invoked quantam funtion")
    job = sampler.run(circuits=circuit)
    print("Processing completed")
    result = job.result()
    print(result)    
    return result
def objectify(data):
  jsonData = json.loads(data)
  serializedSubExps = jsonData['sub-experiments']
  numExp = len(serializedSubExps)
  listSC = []
  for i in range(0, numExp):
    v = serializedSubExps[i]
    lc = []
    for cstr in v['sub-circuits']:
      sub_circuits = serializers.circuit_deserializer(cstr)
      lc.append(sub_circuit)
    listSC.append(lc)
  return listSC

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello there, you are inside api!"})
@app.route('/process', methods=['POST'])
def process_request():
    #Get the payload extracted
    payload = request.get_json()

    # retrive list of all circuits
    circuit_list=objectify(payload)
    circuit_output=[]

    # For single circuit
    response=circuit_invoke(circuit_list[0])
    circuit_output.append(response)

    # For multiple circuit 
    # Submit all the circuits in the circuit_list
    # for circuit in circuit_list:
    #     response=circuit_invoke(circuit)
    #     circuit_output.append(response)
    
    result = json.dump(message='Success')
    result = json.dumps(circuit_output=circuit_output)
    return response


if __name__ == "__main__":
    app.run(debug=True)