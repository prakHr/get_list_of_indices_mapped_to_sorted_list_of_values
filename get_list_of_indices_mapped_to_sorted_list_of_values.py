from sortsmith import SortedList
from pprint import pprint

def get_list_of_indices_mapped_to_sorted_list_of_values(list_of_values,start_idx,stop_idx):
    value_to_id_map = {}
    iterator = 0
    for value in list_of_values:
        value_to_id_map[value] = value_to_id_map.get(value,[]) + [iterator]
        iterator+=1
    sl = SortedList(list_of_values)
    values = list(sl.islice(start_idx,stop_idx+1))
    actual_positions_from_original_lists_in_a_map = {}
    for val in values:
        actual_positions_from_original_lists_in_a_map[val] = value_to_id_map[val]
    return {
        "actual_positions_from_original_lists":actual_positions_from_original_lists_in_a_map,
        "sorted_list":list(sl),
        "original_list":list_of_values,
        "start_idx-1_based":start_idx+1,
        "stop_idx-1_based":stop_idx+1
    }

if __name__=="__main__":
    list_of_values = [3,3,3,1,2,4]
    start_idx = 0
    stop_idx = 2
    results = get_list_of_indices_mapped_to_sorted_list_of_values(list_of_values,start_idx,stop_idx)
    pprint(results)
