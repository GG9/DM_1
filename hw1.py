import numpy as np
import pickle
def list2pickle(large_list,file_name="array.pkl"):
    try:
        fh = open(file_name, 'wb')
        pickle.dump(large_list, fh)
    except (EnvironmentError, pickle.PicklingError) as err:
        raise str(err)
def pickle2list(file_name="array.pkl"):
    try:
        fh = open(file_name, 'rb')
        return pickle.load(fh)
    except (EnvironmentError, pickle.PicklingError) as err:
        raise str(err)


def readFile():
    item_list=[]
    with open('input.txt','r') as f:
        for line in f:
            items=line.strip().split(' ')
            item_list.append(items)
    return item_list



def basic_data_mining(large_list):
    array2d = np.zeros([20000,20000],dtype=np.int16)
    for list in large_list:
        for item1 in list:
            for item2 in list:
                if item1 is not item2:
                    array2d[int(item1),int(item2)]+=1
    return array2d
def basic_find_special(large_list,rule_num):
    for i in range(20000):
        for j in range(20000):
            if (large_list[i,j]>rule_num) :
                print(str(i)+"  >>"+str(j) +" : "+str(large_list[i,j]))



if __name__=="__main__":
    #list = readFile()
    #array = basic_data_mining(list[:])
    #list2pickle(list)
    array  = pickle2list()
    print(type(array))
    print(array.size())

    print("array complete")
    basic_find_special(array,1000)


