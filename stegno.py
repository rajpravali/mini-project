
from PIL import Image
import stepic

im = Image.open ("cat.jpg")
s=stepic.Steganographer(im)
im2=s.encode(im ,"hello")
#im2 = stepic.encode(im, '0987639987069730979076409784690y7689734')
im2.save('out.jpg')
im1 = Image.open('cat.jpg')
s = stepic.decode(im1)
print(s)
data = s.decode()
print(data)
