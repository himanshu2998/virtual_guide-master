# virtual_guide-master

A Virtual Guide

Aim :- Guiding a user to a place with the help of our application

Procedure :-
 
 1. User clicks an image where he feels lost or want any guidance.
 2. The image is compared with images of our database through image maching algorithm called SSIM(structural similarity index measure).
 3. The image with highest value is fetched and user starts getting a video guide from that place along with nearby areas info.
 4. The users can repeat the process any times they wish to.


Why SSIM ?

Since our project involves guidance and usually people want guides on tourist places, hence structural similiraity would be the best option.
Also, we have conducted a researh between ssim, psnr, mse and uiqi image comparison methods in order to find best results and undoubtedly, ssim came out to give best results.
