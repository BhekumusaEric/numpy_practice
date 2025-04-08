import numpy as np

x = np.array([5,4,2,8,9,6])
print(np.__version__)
print(type(x))
print(x.dtype)
print(x.shape)
print(x.size)

new = x * [2,2,5,2,4,6]
select = [0,1,2]
x[select] = 5
print(x)
print(x.std())
print(x.mean())
print(x.max())
print(x.min())
print(x.conjugate())

from matplotlib import pyplot as plt

plt.axes
plt.plot(x, x)

import os
from PIL import Image
from IPython.display import IFrame
import requests
url = 'https://www.ibm.com/'
r= requests.get(url)
print(r.status_code)
print(r.request.body)

header = r.headers
print(header['Content-Type'])
r.text[0:]