import trie
import csv
word_list = []

full_name_root = trie.Node()
middle_name_root = trie.Node()
last_name_root = trie.Node()

with open('test_data_sample.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    counter=0
    for w in reader:
        full_name = ""
        word_list.append(w)
        #print("Added : " + w[0] + "Index in list : " + str(counter))
        #first_name_root.add_word(w[0].lower(),index_in_list=counter)
        full_name += w[0].lower()
        if len(w) > 1:
            middle_name_root.add_word(w[1].lower(),index_in_list=counter)
            full_name += w[1].lower() 
        if len(w) > 2:
            last_name_root.add_word(w[2].lower(),index_in_list=counter)
            full_name += w[2].lower()
        full_name_root.add_word(full_name, index_in_list=counter)
        counter+=1


def getName(index):
    name = ""
    l = len(word_list[index])
    for i in range(0,l):
        name = name + " " + word_list[index][i]
    return name.strip()
    

def convert_into_list_of_dict(list_of_names):
    result=[]
    for word in list_of_names:
        result.append({"name": word})
    return result


def get_from_trie(root, query):
    index_list = root.auto_complete_word(query.lower())
    name_list = [getName(i) for i in index_list]
    name_list.sort(lambda x,y: cmp(len(x), len(y)))
    return name_list


def get_results(query):
    
    full_name_result = get_from_trie(full_name_root, query)
    middle_name_result = get_from_trie(middle_name_root, query)
    last_name_result = get_from_trie(last_name_root, query)
    final_result = full_name_result + middle_name_result + last_name_result
    return convert_into_list_of_dict(final_result)


def process_term(query):
    # If search term consists if spaces then 
    name_list = query.split(' ')
    result = ""
    for name in name_list:
        result = result + name.lower()
    return result

