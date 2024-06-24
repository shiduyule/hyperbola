2024-06-24
import cv2
import numpy as np

def find_hyperbola_vertex_distance(image_path):
    # 读取图像并进行灰度化处理
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 使用高斯模糊进行降噪
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 使用Canny边缘检测
    edges = cv2.Canny(blurred, 50, 150)
    
    # 使用findContours检测轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # 筛选出最大的轮廓（假设双曲线是最大的轮廓之一）
    largest_contour = max(contours, key=cv2.contourArea)
    
    # 拟合椭圆
    ellipse = cv2.fitEllipse(largest_contour)
    
    # 提取椭圆的长轴和短轴
    (center, axes, orientation) = ellipse
    major_axis_length = max(axes)
    
    # 计算椭圆的顶点
    angle_rad = np.radians(orientation)
    dx = (major_axis_length / 2) * np.cos(angle_rad)
    dy = (major_axis_length / 2) * np.sin(angle_rad)
    vertex1 = (int(center[0] + dx), int(center[1] - dy))
    vertex2 = (int(center[0] - dx), int(center[1] + dy))
    
    # 计算顶点间的欧几里得距离
    distance = np.sqrt((vertex1[0] - vertex2[0])**2 + (vertex1[1] - vertex2[1])**2)
    
    return vertex1, vertex2, distance

# 示例用法
image_path = 'your_image_path_here.jpg'
vertex1, vertex2, distance = find_hyperbola_vertex_distance(image_path)
print(f"顶点1: {vertex1}, 顶点2: {vertex2}, 顶点间距: {distance}")
