# Explainable Diabetic Retinopathy Detection
This project was born out of a research internship in association with UC Berkeley, SRM IST and IIT Kgp under the SPARC initiative. We own the rights to this work and wish to improve on it as a research endeavour.     

We have in this document, described the past and current goals, methodologies, hurdles, how we plan to mitigate some of them and the rationale behind this project.

## Abbreviations
 1. DR   : Diabetic Retinopathy
 2. NPDR : Non-Proliferative Diabetic Retinopathy
 
## Some preliminaries
Diabetic retinopathy is a diabetes complication that affects eyes. It's caused by damage to the blood vessels of the light-sensitive tissue at the back of the eye (retina). At first, diabetic retinopathy may cause no symptoms or only mild vision problems, but can later lead to complete blindness.

There are 5 levels 0 to 4:    

0. **No DR**
1. **Mild Nonproliferative Retinopathy**: At this stage, microaneurysms occur. They are small areas of balloon-like swelling in the retina's tiny blood vessels.
2. **Moderate Nonproliferative Retinopathy**: This stage is when blood vessels that nourish the retina are blocked.
3. **Severe Nonproliferative Retinopathy**: In this stage,Many more blood vessels are blocked, depriving several areas of the retina with their blood supply. These areas of the retina send signals to the body to grow new blood vessels for nourishment.
4. **Proliferative Retinopathy**: At this advanced stage, the signals sent by the retina for nourishment trigger the growth of new blood vessels. These new blood vessels are abnormal and fragile. They grow along the retina and along the surface of the clear, vitreous gel that fills the inside of the eye. By themselves, these blood vessels do not cause symptoms or vision loss. However, they have thin, fragile walls. If they leak blood, severe vision loss and even blindness can result.

## Goals
1. To detect the various stages of diabetic retinopathy, especially in the early stages, ie. NPDR with high levels of accuracy. 
2. To accurately warn patents in case of early stage or non-prioliferative DR.
3. *Now we wish to make the AI explainable, capable of not only making the predictions but actually detecting each anomaly and wighing them in to announce its final label and being able to argue or prove why it is right.*


## Existing Research
We went through over 100 research papers to understand both the biological aspect of what causes the diseases and also how to make the AI aspect of it work. All the papers we studied and referred are hosted on [GDrive](https://drive.google.com/drive/folders/1w6qTQNr7eQvBS1_xEwjuw7_FdEOuVDZp?usp=sharing).       

Selected online links:     
[Google Blog 2016](https://ai.googleblog.com/2016/11/deep-learning-for-detection-of-diabetic.html)    
[Google Blog 2018 with Paper](https://ai.googleblog.com/2018/12/improving-effectiveness-of-diabetic.html)     
[Microsoft BLog 2018](https://blogs.technet.microsoft.com/machinelearning/2018/06/25/building-a-diabetic-retinopathy-prediction-application-using-azure-machine-learning/)     

## Our Work
We tried a lot of things in the beginning, over 20 preprocessing techniques, and ultimately zeroed in on the ones we are currently using. We also tried many different architectures. A detailed report of our final architecture and findings are illustrated in two technical reports:       
[Report 1](Reports/Report_1_Classification%20Stages%20of%20Diabetic%20Retinopathy%20through%20Deep%20CNN.pdf)        
[Report 2 with references](Reports/Report%20_2_Research%20Paper.pdf)


## Hurdles we faced 
1. Our main hurdle was the dataset from Kaggle, which is of significantly low quality and wrongly labelled.     
   a. We did drop the bad images manually, but     
   b. Some images are wrongly labelled, for eg some level 3 images are actually worse than a level 4 image, this confuses the algorithm enormously.       
   c. Also the dataset is heavily imbalanced with close to 86% of the 88702 images representing Level 0 or NO DR.
   
2. We could not devise an effective plan of how to combine multiple datasets, For eg DIARET DB has some 200 images are of really good quality, the reason we are particularly interested in doing this is described in the sections below.

## What sets us apart
Clearly many exisitng AI solutions already exist to detect Diabetic Retinopathy. However, we are planning to build an agent capable of not only giving an output label but being able to defend its output before an expert panel. This will require it to have a deep understanding of the pathology.

#### Scenario:
An image is shown to a doctor and an AI agent.
Both come up with their predictions, but what is the use of the AI prediction, other than at most a nudge to the doctors?    
To make the AI prediction actually useful, we have to bring in **explainability** and the **ability to argue**

## Our Plan of Improvement in that Direction

Hence instead of only giving predictions, we decided to divide our goal into the following steps:
1) Image quality quantification:     
  a) image quality verification;      
  b) imaging artifact detection;     
  c) iatrogenic lesion detection (laser scars, etc.) (highly optional)     

2) Location and segmentation of retinal structures: 

     a) retinal vessles 

     - vessel diameter;    
     - artery and vein classification;      
     - vessel occlusion detection.     

     b) fovea   
     c) optic disc  

      - cup and rim;   
      - cupping.   
3) Segmentation of abnormalities:   
    a) blood vessel related abnormalities 
  
    - hemorrhages;   
    - microaneurysms;      
    - neovascularizations;     
    - nerve fiber infarcts (cottonwool spots).     

   b) pigment epithelium related abnormalities (cannot be currently done as we are working on BW images from preprocessing)

    - drusen;    
    - hyper and hypopigmentation.    

   c) choroid related abnormalities   (not enough labelled data for this)  

    - nevus and melanoma detection;    
    - uveitis related choroidal lesions.    

Then a panel of experts would agree upon some sort of importance for each of these factors, and the AI would, based on the importance of each of these factors by the intensity if the factors predict a label

Thus the **architecture** would look like :
1. An **AI for localization and segmentation** of the multitude of anomalies mentioned above (using CNNs)
2. A **hypervisor** layer which is not ML but a hard coded Expert System for now
3. A **Decision Tree** giving the final prediction based on each feature's importance(from level 2) and detected intensity (from level 1)
    
      > Thus if anyone challenges its prediction, it can point out the exact sequence of deterministic steps it went through to make the prediction, making it an invaluable tool to physicians as it could also show featues the physician might miss. 
       
Later on the hypervisor's importance weights could be modified to make the system more robust, once we have the necessary data.

Copyright © 2019-present Aditya Jyoti Paul, Sudharsan B
