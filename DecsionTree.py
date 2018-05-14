from numpy import *
from math import log

#load "iris.data" to workspace

traindata = loadtxt("C:/Users/fengying/PycharmProjects/datamining/iris.txt",delimiter = ',',usecols = (0,1,2,3),dtype = float)
trainlabel = loadtxt("C:/Users/fengying/PycharmProjects/datamining/iris.txt",delimiter = ',',usecols = (range(4,5)),dtype = str)
feaname = ["#0","#1","#2","#3"] # feature names of the 4 attributes (features)

def calentropy(label):
    n = label.size # the number of samples
    #print (n)
    count = {} #create dictionary "count"
    for curlabel in label:
        if curlabel not in count.keys():
            count[curlabel] = 0
        count[curlabel] += 1
    entropy = 0
    #print count
    for key in count:
        pxi = float(count[key])/n #notice transfering to float first
        entropy -= pxi*log(pxi,2)
    return entropy


# split the dataset according to label "splitfea_idx"
args = mean(traindata,axis = 0)
def splitdata(oridata, splitfea_idx):
    arg = args[splitfea_idx]  # get the average over all dimensions
    idx_less = []  # create new list including data with feature less than pivot
    idx_greater = []  # includes entries with feature greater than pivot
    n = len(oridata)
    for idx in range(n):
        d = oridata[idx]
        if d[splitfea_idx] < arg:
            # add the newentry into newdata_less set
            idx_less.append(idx)
        else:
            idx_greater.append(idx)
    return idx_less, idx_greater

# testcode:2
# idx_less,idx_greater = splitdata(traindata,2)

# give the data and labels according to index
def idx2data(oridata, label, splitidx, fea_idx):
    idxl = splitidx[0]  # split_less_indices
    idxg = splitidx[1]  # split_greater_indices
    datal = []
    datag = []
    labell = []
    labelg = []
    for i in idxl:
        datal.append(append(oridata[i][:fea_idx], oridata[i][fea_idx + 1:]))
    for i in idxg:
        datag.append(append(oridata[i][:fea_idx], oridata[i][fea_idx + 1:]))
    labell = label[idxl]
    labelg = label[idxg]
    return datal, datag, labell, labelg


def choosebest_splitnode(oridata, label):
    n_fea = len(oridata[0])
    n = len(label)
    base_entropy = calentropy(label)
    best_gain = -1
    for fea_i in range(n_fea):  # calculate entropy under each splitting feature
        cur_entropy = 0
        idxset_less, idxset_greater = splitdata(oridata, fea_i)
        if(len(idxset_less)<5):
            break
        prob_less = float(len(idxset_less)) / n
        prob_greater = float(len(idxset_greater)) / n
        # entropy(value|X) = \sum{p(xi)*entropy(value|X=xi)}
        cur_entropy += prob_less * calentropy(label[idxset_less])
        cur_entropy += prob_greater * calentropy(label[idxset_greater])
        info_gain = base_entropy - cur_entropy  # notice gain is before minus after
        if (info_gain > best_gain):
            best_gain = info_gain
            best_idx = fea_i
    return best_idx


# create the decision tree based on information gain

def buildtree(oridata, label):
    if label.size == 0:  # if no samples belong to this branch
        return "NULL"
    listlabel = label.tolist()
    # stop when all samples in this subset belongs to one class
    if listlabel.count(label[0]) == label.size:
        return label[0]
        # return the majority of samples' label in this subset if no extra features avaliable
    if len(feaname) == 0:
        cnt = {}
        for cur_l in label:
            if cur_l not in cnt.keys():
                cnt[cur_l] = 0
            cnt[cur_l] += 1
        maxx = -1
        for keys in cnt:
            if maxx < cnt[keys]:
                maxx = cnt[keys]
                maxkey = keys
        return maxkey

    bestsplit_fea = choosebest_splitnode(oridata, label)  # get the best splitting feature
    print(bestsplit_fea, len(oridata[0]))
    cur_feaname = feaname[bestsplit_fea]  # add the feature name to dictionary
    print(cur_feaname)
    nodedict = {cur_feaname: {}}

    del(feaname[bestsplit_fea])  # delete current feature from feaname
    split_idx = splitdata(oridata, bestsplit_fea)  # split_idx: the split index for both less and greater
    data_less, data_greater, label_less, label_greater = idx2data(oridata, label, split_idx, bestsplit_fea)
    # build the tree recursively, the left and right tree are the "<" and ">" branch, respectively
    nodedict[cur_feaname]["<"] = buildtree(data_less, label_less)
    nodedict[cur_feaname][">"] = buildtree(data_greater, label_greater)
    return nodedict

mytree = buildtree(traindata,trainlabel)
print (mytree)
