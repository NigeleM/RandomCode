
"""This problem was asked by Spotify.

You have access to ranked lists of songs for various users. Each song
is represented as an integer,
and more preferred songs appear earlier in each list.
For example, the list [4, 1, 7] indicates that
a user likes song 4 the best, followed by songs 1 and 7.
Given a set of these ranked lists, interleave them to create a
playlist that satisfies everyone's priorities.
For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}.
In this case
a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].""" 


# Probably a bad solution
# feels like it could be cleaner
back =  [[1,7,3],[2,1,6,7,9],[3,9,5]]

def rankList(data):
    rankdata = []
    ranknewdata = []
    count = 0
    for datum in data:
        count += 1
        for val,info in enumerate(datum):
            if count > len(data) -1:
                count = len(data) - 1
            if datum == data[count]:
                #print(data[count])
                if info not in ranknewdata:
                    ranknewdata.append(info)   
            elif info in data[count]:
                if data[count].index(info) > val:
                    continue
                else:
                    ranknewdata.append(info)
            else:
                ranknewdata.insert(val,info)
                
        
    return ranknewdata        

print(rankList(back))
print("expected -> ", [2, 1, 6, 7, 3, 9, 5])
