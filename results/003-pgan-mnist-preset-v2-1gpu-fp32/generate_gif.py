import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os 
from PIL import Image
import numpy as np

image_list = []
names = ['0000', '0160', '0320', '0480', '0621', '0761', '0901', '1041', '1182', '1322', '1462', '1603', '1743', '1863', '1984', '2104', '2224', '2344', '2465', '2585', '2705', '2826', '2946', '3046', '3146', '3246', '3346', '3447', '3547', '3647', '3747', '3847', '3947', '4047', '4147', '4247', '4347', '4448', '4548', '4648', '4748', '4848']
for i in range(len(names)):
    image = Image.open(f'fakes00{names[i]}.png')
    image_list.append(image)

print(image_list[1])

fig = plt.figure(figsize=(1,1))
plt.axis("off")
ims = [[plt.imshow(i, animated=True, cmap='gray')] for i in image_list]
anim = animation.ArtistAnimation(fig, ims, interval=1000, repeat_delay=1000, blit=True)
plt.show()
anim.save('transition.gif', dpi=80, writer='imagemagick')