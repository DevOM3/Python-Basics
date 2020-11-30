import barcode
import random

num = random.randint(1, 10000000000000)

print(num)

bar = barcode.get_barcode_class('ean13')
img_bar = bar(u'{}'.format(num))

file = open('barcode.svg', "wb")

img_bar.write(file)
