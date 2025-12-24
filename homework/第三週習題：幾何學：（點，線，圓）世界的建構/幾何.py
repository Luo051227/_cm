import numpy as np
from typing import Tuple, Union, List

class GeometryTransformer:
    @staticmethod
    def translate(points: np.ndarray, dx: float, dy: float) -> np.ndarray:
        """
        平移變換
        :param points: 頂點矩陣 (N, 2)
        :param dx, dy: 平移向量分量
        """
        offset = np.array([dx, dy]) # 对应数学公式 v = [dx, dy]
        return points + offset # 对应 P' = P + v

    @staticmethod
    def scale(points: np.ndarray, s: float, pivot: np.ndarray = np.array([0, 0])) -> np.ndarray:
        """
        縮放變換
        :param s: 縮放倍率
        :param pivot: 縮放中心
        """
        # 将点移至原点 -> 缩放 -> 移回
        return (points - pivot) * s + pivot # 对应 P' = C + s(P-C)

    @staticmethod
    def rotate(points: np.ndarray, theta_deg: float, pivot: np.ndarray = np.array([0, 0])) -> np.ndarray:
        """
        旋轉變換
        :param theta_deg: 旋轉角度 (度)
        :param pivot: 旋轉中心
        """
        theta = np.radians(theta_deg)
        c, s = np.cos(theta), np.sin(theta)
        
        # 定義旋轉矩陣 R
        R = np.array([[c, -s], 
                      [s,  c]]) # 对应数学公式 R = [[cos, -sin], [sin, cos]]
        
        # 向量化運算: (points - pivot) @ R.T + pivot
        # 使用 @ 進行矩陣乘法，處理所有頂點
        relative_coords = points - pivot
        rotated_coords = relative_coords @ R.T # 对应 P' = R(P-C)
        return rotated_coords + pivot

# --- 物件化封裝範例 ---

class Circle:
    def __init__(self, center: Tuple[float, float], radius: float):
        self.center = np.array(center)
        self.radius = radius

    def transform(self, dx: float = 0, dy: float = 0, s: float = 1, theta_deg: float = 0, pivot: Tuple[float, float] = None):
        """對圓進行複合變換"""
        if pivot is None: pivot = self.center # 預設以圓心為中心
        p_pivot = np.array(pivot)
        
        # 1. 旋轉與平移圓心
        new_center = GeometryTransformer.rotate(self.center.reshape(1,2), theta_deg, p_pivot)
        new_center = GeometryTransformer.translate(new_center, dx, dy)
        self.center = new_center.flatten()
        
        # 2. 縮放半徑
        self.radius *= s

class Triangle:
    def __init__(self, p1, p2, p3):
        self.vertices = np.array([p1, p2, p3], dtype=float)

    def apply_transform(self, dx=0, dy=0, s=1, theta_deg=0, pivot=None):
        if pivot is None: pivot = np.mean(self.vertices, axis=0) # 預設以重心為中心
        p_pivot = np.array(pivot)
        
        # 複合運算
        pts = self.vertices
        pts = GeometryTransformer.rotate(pts, theta_deg, p_pivot)
        pts = GeometryTransformer.scale(pts, s, p_pivot)
        pts = GeometryTransformer.translate(pts, dx, dy)
        self.vertices = pts

# --- 測試案例 ---
tri = Triangle((0,0), (2,0), (1,2))
print(f"原始頂點:\n{tri.vertices}")

# 將三角形旋轉 90 度並放大 2 倍
tri.apply_transform(s=2, theta_deg=90)
print(f"變換後頂點:\n{tri.vertices}")
