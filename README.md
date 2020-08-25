# ImagePixels
MS Dhoni's picture rendered using python, where each pixel is a picture from his career.

---
### 1. Collect images.
In my case I scraped gettyimages site to get around 5000 images of MS Dhoni.
### 2. Resize and convert the images to greyscale.
Convert all the images collected to grescale and 1:1 aspect ratio.
I converted all the images to 100 by 100 pixels.
It can done be with other resolutions as well, as long as they are 1:1. 
### 3. Calculate average intensity of a images.
Add all the intensities of the pixels in the greyscale image and divide by total number of pixels.
### 4. Render the image
Choose the picture you want to use for rendering and resize it.
Access each pixel intensity in the image and replace it with the corresponding image with same intensity.
If there isn't a image with same intensity, then replace it with a image having closest intensity.
