from ctypes import*
import numpy as np
import numpy.ctypeslib as npct
import cv2
# give location of dll
mydll = cdll.LoadLibrary("C:\\Users\\Acer PC\\source\\repos\\templateMatching\\x64\\Debug\\templateMatching.dll")
#array_2d_double = npct.ndpointer(dtype=c_uint8,  flags="C_CONTIGUOUS")
#array_3d_double = npct.ndpointer(dtype=c_uint8,  flags="C_CONTIGUOUS")
mydll.res.restype=c_int
#mydll.res.argtypes = [array_2d_double, array_3d_double]
mydll.res.argtypes = [c_char_p, c_char_p]
result=mydll.res( b"C:\\Users\\Acer PC\\Desktop\\New folder\\search.jpg",b"C:\\Users\\Acer PC\\Desktop\\New folder\\google.jpg" )
print (result)