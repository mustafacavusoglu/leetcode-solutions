
from collections import defaultdict


def mostPopularCreator(creators, ids, views):
    
    # total views by creator & list of videos by creator
    tot, vid = defaultdict(int), defaultdict(list)                    
    
    
    for c, i, v in zip(creators, ids, views):
        tot[c] += v                                                   
        vid[c].append((-v,i))                                         
    m = max(tot.values())                                             
    
    
    return [[c,min(v)[1]] for c, v in vid.items() if tot[c] == m]


creators = ["alice","bob","alice","chris"]
ids = ["one","two","three","four"]
views = [5,10,5,4]

mostPopular = mostPopularCreator(creators, ids, views)
# Output: [["alice","one"],["bob","two"]]