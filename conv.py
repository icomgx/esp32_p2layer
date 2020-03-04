#!/usr/bin/env python

# @file bmp2hex.py
# @author Robert Gallup 2016-02
#
# Author:    Robert Gallup (bg@robertgallup.com)
# License:   MIT Opensource License
#
# Copyright 2016-2018 Robert Gallup
#


import array
import math
import os
import sys
from PIL import Image
import cv2
import ast

result_h2x = []


class DEFAULTS(object):
    STRUCTURE_NAME = 'GFXMeta'
    VERSION = '2.3'


def getLONG(a, n):
    return (a[n + 3] * (2 ** 24)) + (a[n + 2] * (2 ** 16)) + (a[n + 1] * (2 ** 8)) + (a[n])


# Utility function. Return an int from array (little endian)
def getINT(a, n):
    return (a[n + 1] * (2 ** 8)) + (a[n])


# Reverses pixels in byte
def reflect(a):
    r = 0
    for i in range(8):
        r <<= 1
        r |= (a & 0x01)
        a >>= 1
    return r


# Main conversion function
def bmp2hex(infile, tablewidth, sizebytes, invert, raw, named, double, xbm):
    # Set the table name to the uppercase root of the file name
    tablename = os.path.splitext(infile)[0].upper()

    # Convert tablewidth to characters from hex bytes
    tablewidth = int(tablewidth) * 6

    # Initilize output buffer
    outstring = ''

    # Open File
    fin = open(os.path.expanduser(infile), "rb")
    uint8_tstoread = os.path.getsize(os.path.expanduser(infile))
    valuesfromfile = array.array('B')
    try:
        valuesfromfile.fromfile(fin, uint8_tstoread)
    finally:
        fin.close()

    # Get bytes from file
    values = valuesfromfile.tolist()

    # Exit if it's not a Windows BMP
    if (values[0] != 0x42) or (values[1] != 0x4D):
        sys.exit("Error: Unsupported BMP format. Make sure your file is a Windows BMP.")

    # Calculate width, heigth
    dataOffset = getLONG(values, 10)  # Offset to image data
    pixelWidth = getLONG(values, 18)  # Width of image
    pixelHeight = getLONG(values, 22)  # Height of image
    bitDepth = getINT(values, 28)  # Bits per pixel
    dataSize = getLONG(values, 34)  # Size of raw data

    # Calculate line width in bytes and padded byte width (each row is padded to 4-byte multiples)
    byteWidth = int(math.ceil(float(pixelWidth * bitDepth) / 8.0))
    paddedWidth = int(math.ceil(float(byteWidth) / 4.0) * 4.0)

    # For auto (sizebytes = 0), set sizebytes to 1 or 2, depending on size of the bitmap
    if sizebytes == 0:
        if (pixelWidth > 255) or (pixelHeight > 255):
            sizebytes = 2
        else:
            sizebytes = 1

    # The invert byte is set based on the invert command line flag (but, the logic is reversed for 1-bit files)
    invertbyte = 0xFF if invert else 0x00
    if bitDepth == 1:
        invertbyte = invertbyte ^ 0xFF
    try:
        for i in range(pixelHeight):
            for j in range(byteWidth):
                ndx = dataOffset + ((pixelHeight - 1 - i) * paddedWidth) + j
                v = values[ndx] ^ invertbyte
                if xbm:
                    v = reflect(v)
                # print ("{0:#04x}".format(v))
                outstring += "{0:#04x}".format(v) + ", "
                result_h2x.append(v)
    finally:
        return result_h2x


# ---------------------------------------------------------------------------------------------------

# 转灰度
def conv2(imagePath, savePath):
    im = Image.open(imagePath)
    im.convert(mode="L").save(savePath)


# 转1位图
def conv3(imagePath, savePath):
    im = Image.open(imagePath)
    im.convert(mode="1").save(savePath)


# 二值化
def conv4(imagePath, savePath):
    img = cv2.imread(imagePath, 0)
    # blur = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    cv2.imwrite(savePath, thresh)


# 转码
def createCode(imgPath):
    ra = bmp2hex(imgPath, "0", "0", False, False, False, False, True)
    return ra


# 帧的字码文件转换成数组
def fileH2xToList(filePath):
    data = open(filePath, 'r')
    res = data.read()
    data.close()
    r2es = res.strip('[')
    r3es = r2es.strip(']')
    arr = r3es.split(',')
    a2rr = list(map(int, arr))
    return a2rr


# fc文件转换成字典
def flTodic(flPath):
    data = open(flPath, 'r')
    res = data.read()
    data.close()
    result_dic = ast.literal_eval(res)
    return result_dic


# fc帧文件转换成数组
def flH2xToList(flvalue):
    r2es = flvalue.strip('[')
    r3es = r2es.strip(']')
    arr = r3es.split(',')
    a2rr = list(map(int, arr))
    return a2rr

