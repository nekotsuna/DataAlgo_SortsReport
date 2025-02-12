import sort_algorithms
import time
import json
import random

def random_case(length):
  sample = []
  for i in range(length):
    sample.append(random.randrange(0, length, 1))
  return sample
  

data_file = open("data.json", "r")
data = json.load(data_file)

sorts = {}
for sort in data["sorts"]:
  sorts[sort] = getattr(sort_algorithms, sort)

result = {} 

for test_case in data["cases"]:
  create_sample = random_case

  for length in range(test_case["min"], test_case["max"], test_case["step"]):
    for sample_id in range(test_case["sample"]):
      sample = create_sample(length)

      key = test_case["type"] + "_" + str(length) + "_" + str(sample_id)
      result[key] = {}
      result[key]["type"] = test_case["type"]
      result[key]["length"] = length
      result[key]["sample_id"] = sample_id
      result[key]["result"] ={}
      
      for sort_name in sorts:
        start = time.process_time()
        sorts[sort_name](sample)
        end = time.process_time()

        trial_time = end - start
        result[key]["result"][sort_name] = trial_time

result_file = open("result.json", "w")
json.dump(result, result_file)
