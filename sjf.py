

def sjf(jobs,index):
    newJob = jobs[:]
    value = jobs[index]
    newJob = sorted(newJob)

    cc = 0
    if min(jobs) == max(jobs):
      for times in jobs:
        cc += times

    print(cc)  
    if cc > 0:
      return cc
    
    for time in newJob:
        if time <= value:
            cc += time
       
    return cc






print(sjf([3,10,20,1,2],0))
print(sjf([3,10,10,20,1,2],2))
print(sjf([10,10,10,10],3))


