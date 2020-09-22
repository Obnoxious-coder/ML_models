#!/usr/bin/env python
# coding: utf-8

# In[9]:


#https://www.youtube.com/watch?v=6DjFscX4I_c&t=229s

import cv2


# In[10]:


import pytesseract

#add tesseract binary dependency to system variable.


# In[16]:


img =cv2.imread('img.png')


# In[17]:


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[30]:


# pytesseract.image_to_string(img)
hI,wI,k=img.shape
boxes=pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b=b.split(' ')
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hI-y),(w,hI-h),(0,0,255),0.2)


# In[32]:


cv2.imshow('img',img)
cv2.waitKey(0)


# In[ ]:




