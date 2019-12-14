# Diabetic Retinopathy Detection
This project was born out of a research internship in association with UC Berkeley, SRM IST and IIT Kgp under the SPARC initiative. We own the sole rights to this work and wish to improve on it as a research endeavour.

## Abbreviations
 1. DR   : Diabetic Retinopathy
 2. NPDR : Non-Proliferative Diabetic Retinopathy
 
## Some preliminaries
Diabetic retinopathy is a diabetes complication that affects eyes. It's caused by damage to the blood vessels of the light-sensitive tissue at the back of the eye (retina). At first, diabetic retinopathy may cause no symptoms or only mild vision problems, but can later lead to complete blindness.

There are 5 levels 0 to 4:    

0. **No DR**
1. **Mild Nonproliferative Retinopathy**: At this stage, microaneurysms occur. They are small areas of balloon-like swelling in the retina's tiny blood vessels.
2. **Moderate Nonproliferative Retinopathy**: This stage is when blood vessels that nourish the retina are blocked.
3. Severe Nonproliferative Retinopathy. In this stage,Many more blood vessels are blocked, depriving several areas of the retina with their blood supply. These areas of the retina send signals to the body to grow new blood vessels for nourishment.
4. **Proliferative Retinopathy**: At this advanced stage, the signals sent by the retina for nourishment trigger the growth of new blood vessels. These new blood vessels are abnormal and fragile. They grow along the retina and along the surface of the clear, vitreous gel that fills the inside of the eye. By themselves, these blood vessels do not cause symptoms or vision loss. However, they have thin, fragile walls. If they leak blood, severe vision loss and even blindness can result.

## Goals
1. To detect the various stages of diabetic retinopathy, especially in the early stages, ie. NPDR with high levels of accuracy. 


## Existing Research
We went through over 100 research papers to understand both the biological aspect of what causes the idseases and also how to make the AI aspect of it work. We will update the papers here soon.
Some good linksfor the same.
[Google Blog 2016 ](https://ai.googleblog.com/2016/11/deep-learning-for-detection-of-diabetic.html)    
[Google Blog 2018 with Paper](https://ai.googleblog.com/2018/12/improving-effectiveness-of-diabetic.html)     
[Microsoft BLog 2018](https://blogs.technet.microsoft.com/machinelearning/2018/06/25/building-a-diabetic-retinopathy-prediction-application-using-azure-machine-learning/)     

## Our Work
We created two technical reports, describing our work:       
[Report 1](Reports/Report_1_Classification%20Stages%20of%20Diabetic%20Retinopathy%20through%20Deep%20CNN.pdf)        
[Report 2 with references](Reports/Report%20_2_Research%20Paper.pdf)


## Hurdles we faced 
1. Our main hurdle was the dataset from Kaggle, which is of significantly low quality and wrongly lablled.     
   a. We did drop the bad images manually, but     
   b. Some images are wrongly labelled, for eg some level 3 images are actually worse than a level 4 image, this confuses the algorithm enormously.       
   c. Also the dataset is heavily imbalanced with close to 86% of the 88702 images represtning level 0 or NO DR.
   
2. We could not devise an effective plan of how to combine multiple datasets, For eg DIARET DB has some 200 images are of really good quality, the reason we are particularly interested in doing this is described in the sections below.

## Our Plan of Improvement
Clearly many exisitng AI solutions already exist to detect Diabetic Retinopathy. 

## What sets us apart


Copyright © 2019-present Aditya Jyoti Paul, Sudharsan B

