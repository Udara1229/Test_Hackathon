#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import pytesseract


# In[ ]:





# In[3]:


img = cv2.imread("F:/UNI/icds2021-mini-hackathon/OCR/002.png") # read an image


# In[7]:


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[8]:


text = pytesseract.image_to_string(img) # extract text
print(text)


# In[9]:


file = open('output_perferct.txt','a') # write to a file
file.write(text)
file.close()


# In[10]:


img2 = cv2.imread("F:/UNI/icds2021-mini-hackathon/OCR/006.jpg") #read an image


# In[11]:


text = pytesseract.image_to_string(img2)
print(text)


# In[12]:


# resizing the image
# it's recommended if you’re working with images that have a DPI of less than 300 dpi (dots per inch)
img2= cv2.resize(img2,None, fx=.5, fy=0.5)


# In[13]:


#convert to gray scale
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


# In[14]:


text2= pytesseract.image_to_string(gray)
print(text2)


# In[15]:


#still some wroeds are wiered.lets try adaptive thresholding
adaptive_threshold = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,85, 11 )


# In[16]:


text2= pytesseract.image_to_string(adaptive_threshold)
print(text2)


# In[20]:


#still some wroeds are wiered.lets try adaptive thresholding
adaptive_threshold = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,91, 11 )
text2= pytesseract.image_to_string(adaptive_threshold)
print(text2)


# In[ ]:





# In[ ]:




