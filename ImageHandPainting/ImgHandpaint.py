# -*- coding: utf-8 -*-
"""
使用pillow库和numpy实现图像手绘效果
"""
import numpy as np
from PIL import Image
a = np.array(Image.open('D:/Python/Spyder/touxiang.jpg').convert('L')).astype('float')
depth = 20  # 预设深度值为10，取值范围是0-100
grad = np.gradient(a)  # 取图像灰度的梯度值
grad_x ,grad_y = grad # 提取x和y方向的梯度值
grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100 # 根据深度调整x和y方向的梯度值

A = np.sqrt(grad_x**2 + grad_y**2 + 1)  # 梯度归一化
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1 / A  # 构造x，y轴梯度的三位归一化单位坐标系

vec_el = np.pi / 2  # 光源的俯视角度，弧度值
vec_az = np.pi / 4   # 光源的方位角度弧度制
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x轴的影响
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y轴的影响
dz = np.sin(vec_el)  # 光源对z轴的影响

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
b = b.clip(0, 255)  # 为了避免数据越界，将生成的灰度值裁剪到0-255之间
im = Image.fromarray(b.astype('uint8'))
im.save('D:/Python/Spyder/touxiang1.jpg')


 

