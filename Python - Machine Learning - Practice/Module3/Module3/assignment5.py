#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
#
df = pd.read_csv('D:\Online COurses\Python\Data\Module3\Module3\Datasets\\wheat.data', header = 0)
print(df.head(5))




#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
df = df.drop(labels = ['id'], axis = 1)
print(df.head(5))


#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
plt.figure()
andrews_curves(df,'wheat_type',alpha = 0.4)



plt.show()


