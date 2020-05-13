import numpy
from PIL import Image


def openImage(imagePath):
    imOrig = Image.open(imagePath)
    im = numpy.array(imOrig)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue, imOrig]


def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = numpy.linalg.svd(channelDataMatrix)
    aChannelCompressed = numpy.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
    k = singularValuesLimit

    leftSide = numpy.matmul(uChannel[:, 0:k], numpy.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = numpy.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    return aChannelCompressed


# MAIN PROGRAM:
# print('Image Compression using SVD :')
# start = timeit.default_timer()
# aRed, aGreen, aBlue, originalImage = openImage('/home/sachin/Downloads/me.jpeg')
#
# # image width and height:
# imageWidth = 512
# imageHeight = 512
#
# # number of singular values to use for reconstructing the compressed image
# singularValuesLimit = 160
#
# aRedCompressed = compressSingleChannel(aRed, singularValuesLimit)
# aGreenCompressed = compressSingleChannel(aGreen, singularValuesLimit)
# aBlueCompressed = compressSingleChannel(aBlue, singularValuesLimit)
#
# imr = Image.fromarray(aRedCompressed, mode=None)
# img = Image.fromarray(aGreenCompressed, mode=None)
# imb = Image.fromarray(aBlueCompressed, mode=None)
#
# newImage = Image.merge("RGB", (imr, img, imb))
#
# #originalImage.show()
# #newImage.show()
#
# # CALCULATE AND DISPLAY THE COMPRESSION RATIO
# mr = imageHeight
# mc = imageWidth
#
# originalSize = mr * mc * 3
# compressedSize = singularValuesLimit * (1 + mr + mc) * 3
#
# stop = timeit.default_timer()
#
# print('Original size: %d' % originalSize)
#
# print('Compressed size: %d' % compressedSize)
#
# print('Ratio compressed size / original size:')
# ratio = compressedSize * 1.0 / originalSize
# print(ratio)
#
# print('Compressed image size is ' + str(round(ratio * 100, 2)) + '% of the original image ')
#
# print('Time: ', stop - start)
#
# print('DONE!!')