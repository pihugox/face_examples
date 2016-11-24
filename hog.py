#!/usr/bin/python

##sudo apt-get install python-tk

## correr con ./hog.py faces/*.jpg

import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, color, exposure
import matplotlib.image as mpimg
import sys
import time

plt.ion()

for f in sys.argv[1:]:
	#image = color.rgb2gray(data.astronaut())
	image = color.rgb2gray(mpimg.imread(f))

	start_time = time.time();
	fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
	                    cells_per_block=(1, 1), visualise=True)
	print("Horiented Object Histogram in %s seconds" % (time.time() - start_time))
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

	ax1.axis('off')
	ax1.imshow(image, cmap=plt.cm.gray)
	ax1.set_title('Input image')
	ax1.set_adjustable('box-forced')

	# Rescale histogram for better display
	hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

	ax2.axis('off')
	ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
	ax2.set_title('Histogram of Oriented Gradients')
	ax1.set_adjustable('box-forced')
	plt.plot()


	print raw_input('Press enter to continue')
