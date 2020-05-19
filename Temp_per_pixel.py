#!/usr/bin/env python
# coding: utf-8

# In[78]:


import flirimageextractor
from matplotlib import cm
from matplotlib import pyplot as plt
import cv2


# In[79]:


image = cv2.imread('Transformer.jpg')
plt.subplot(1,1,1)

plt.imshow(image)
plt.show()


# In[80]:


rows,cols,color = image.shape
print(image.shape)


# In[81]:


flir = flirimageextractor.FlirImageExtractor(palettes=[cm.jet, cm.bwr, cm.gist_ncar])
flir.process_image('Transformer.jpg')


# In[82]:


flir.save_images()


# In[83]:


flir.plot()


# In[84]:


thermal = flir.get_thermal_np()


# In[85]:



flir.check_for_thermal_image('Transformer.jpg')


# In[89]:


for i in range(image.shape[0]):
    for j in range(0,image.shape[1]):
        pixel=image[i,j]
        temperature = thermal[i,j]
        print(pixel,temperature )
        
        #print(temperature)
       # temp=thermal[j*image.shape[0]+ i]
       # 
       # print(temp)
        


# In[ ]:




