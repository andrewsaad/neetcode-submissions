from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    dic_map = {}
    for list_index in range(len(keys)):
        dic_map [keys[list_index]] = values[list_index]
        # dic_map =zip(list_index],values[list_index)
    return dic_map


def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    values=[]
    for keys_index in (keys):
        #print (keys_index)
        values.append(hash_map[keys_index])
    
    return values

# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
