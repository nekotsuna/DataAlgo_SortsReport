import sort_algorithms
import time
import json
import copy
from make_array import make_array as make_sample

data_file = open("data.json", "r")
data = json.load(data_file)

sorts = {}
for sort in data["sorts"]:
  sorts[sort] = getattr(sort_algorithms, sort)

result = {} 

for test_case in data["cases"]:
  create_sample = getattr(make_sample, test_case["function"])

  length = test_case["min"]
  while length < test_case["max"]:
    for sample_id in range(test_case["sample"]):
      sample, seed = create_sample(length)
      sorted_sample = sorted(sample)

      key = test_case["type"] + "_" + str(length) + "_" + str(sample_id)
      print(key)
      result[key] = {}
      result[key]["type"] = test_case["type"]
      result[key]["length"] = length
      result[key]["seed"] = seed
      result[key]["sample_id"] = sample_id
      result[key]["result"] ={}
      
      for sort_name in sorts:
        sample_copied = copy.copy(sample)

        start = time.process_time()
        ret_list = sorts[sort_name](sample_copied)
        end = time.process_time()

        if(ret_list !=  sorted_sample):
          print("error: return list is not matched to sample list")

        trial_time = end - start
        result[key]["result"][sort_name] = trial_time

    length = eval("length" + test_case["step"]) 

result_file = open("result.json", "w")
json.dump(result, result_file)
