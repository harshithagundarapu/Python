import numpy as np
# Create arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2], [3, 4], [5, 6]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Display array attributes
arrays = [array_1d, array_2d, array_3d]
for i in range(len(arrays)):
 array = arrays[i]
print(f"\nArray {i+1} Attributes:")
print(f"Dimensions (ndim): {array.ndim}")
print(f"Shape: {array.shape}")
print(f"Size (elements): {array.size}")
print(f"Data Type (dtype): {array.dtype}")
