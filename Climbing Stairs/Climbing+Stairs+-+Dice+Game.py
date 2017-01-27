
# coding: utf-8

# In[35]:

import matplotlib.pyplot as plt
import numpy as np


# In[36]:

np.random.seed(123)
all_walks = []


# In[37]:

# Simulate random walk 500 times
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)


# In[38]:

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))


# In[39]:

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]


# In[40]:

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()


# In[41]:

# Chances of reaching 60 steps
b = 0.0
for a in ends :
    if a > 60:
        b = b+1
print("Number of walks ending in more than 60 steps " + str(b))
print(" My chance of reaching atleast 60 steps is " + str(b/500))

