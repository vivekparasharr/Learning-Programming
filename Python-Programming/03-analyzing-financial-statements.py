
# input
mnthly_rev=[23,25,23,21,32,20,26,24,28,32,24,22]
mnthly_expns=[12,15,10,14,17,9,18,14,17,15,16,12]

# processing
import numpy as np
r=np.array(mnthly_rev)
e=np.array(mnthly_expns)

# profit for each month
p=r-e # this cant be done with lists
p_aftr_tax=0.7*p
p_margin=p_aftr_tax/r
good_months=[p_aftr_tax > np.mean(p_aftr_tax)]
bad_months=[p_aftr_tax < np.mean(p_aftr_tax)]
best_month=np.max(p_aftr_tax)
worst_month=np.min(p_aftr_tax)

np.where(p_aftr_tax == np.max(p_aftr_tax))
# numpy.where() function iterates over a bool array, and for every True, it yields corresponding the element array x, and for every False, it yields corresponding item from array y. So, it returns an array of elements from x where the condition is True and elements from y elsewhere. 
# in our example we get (array([9], dtype=int64),) as output
# this means, max value of the array exists at following indices array([9],)
# if it existis muliple times then all indices where it exists will be returned
