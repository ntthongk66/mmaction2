import pickle
obj = pickle.load(open("E:\download\demo_skeleton.pkl", "rb"))
import pprint
import json
with open("hiout.txt", "a") as f:
    pprint.pprint(obj, stream=f)
    # json.dump(obj, f, indent=2)