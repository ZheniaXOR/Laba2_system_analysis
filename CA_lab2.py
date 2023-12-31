import numpy as np

X11 = np.array([0, 0.11, 0.21, 0.03, 0.45, 1.5, 0, 0, 0, 0.1, 0, 0.5, 0.6, 0.5, 0, 0.3, 0, 0.01, 0, 0.29, 0.19, 1, 0.1, 0, 0.87, 0.97, 1, 0.1, 0, 0.4, 0,1, 1, 0.93, 0.41, 0.31, 0, 0.11, 0, 0, 1.5, 0.15, 0, 1, 0.91, 0.87, 0.73, 0.69, 0.55, 0.41]);
X12 = np.array([0, 0.12, 0.22, 0.32, 0, 1.9, 2, 0.21, 0.22, 0.3, 0.4, 0.5, 0.6, 0.43, 0, 0.23, 0.13, 0.9, 1, 0.28, 0.18, 0, 0.9, 0.31, 0, 0.11, 0, 0, 1.5, 1.3, 1.1, 0, 0, 0.12, 0.68, 0, 0.88, 0, 1, 0.7, 0.8, 0.94, 1, 0, 0.12, 0.28, 0.34,0.95,0.84,0.73]);
X21 = np.array([0, 0.13, 0.23, 0.33, 0.7, 0.4, 0.3, 0.2, 0.1, 0.7, 0.6, 0.5, 0.4, 0.3, 0.4, 0, 0.6, 0.09, 1, 0.27, 0.17, 1, 0.9, 0, 0.88, 0, 1, 0.7, 0.8, 0.9, 1, 0, 0, 0.11, 0.4, 0.3, 0.2, 0.1, 0, 1, 0, 0.93, 1, 1, 0.93, 0.89, 0.75, 1, 0, 0.12]);
X22 = np.array([0, 0.14, 0.24, 0.34, 1, 1.5, 1.6, 1.7, 0, 1, 1, 1, 0.96, 0.2, 0.4, 0.6, 0.8, 0, 0, 0.26, 0.16, 0, 0.1, 0.3, 0.2, 0.1, 0, 1, 0, 0, 0, 1, 1, 0.9, 1, 0.7, 0.8, 0.56, 0.4, 0.34, 0.28, 0.12, 0, 0, 0.14, 0.2, 0.36, 0, 0.46, 0.45]);
X31 = np.array([0, 0.15, 0.25, 0.35, 1.1, 1.5, 0.4, 0.3, 0.2, 0.1, 1, 0, 0.95, 0, 0.62, 0.72, 0, 0.92, 1, 0.25, 0.15, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, 1, 0.99, 0, 1, 0, 0.55, 0.49, 0.33, 0.27, 0.11, 0, 0, 0.15, 0.21, 0.37, 1.76, 0.38, 0.36]);
X32 = np.array([0, 0.16, 0.26, 0.36, 0.46, 0.56, 0.66, 0.76, 0.08, 0.96, 1, 1, 0.94, 0.84, 0.74, 0.64, 0.54, 0.44, 0.34, 0.24, 0.14, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 0, 0.18, 0.22, 0.36, 0.4, 0.54, 0.68, 0.72, 0.86, 0.9, 1, 1, 0.96, 0.82, 0.78, 0.64, 0.5, 0.46]);
Y1 = np.array([0.844, 1.137962, 1.380722, 1.525082, 2.4676, 5.472, 3.7668, 2.1842, 1.1624, 1.9056, 2.664, 2.184, 2.946602, 1.7658, 1.565824, 1.931464, 1.4398, 2.464144, 2.796, 1.472322, 1.228682, 2.194, 2.5468, 1.7502, 1.9092, 1.7998, 1.854, 1.6836, 2.6924, 2.6704, 2.3376, 1.834, 2.284, 2.379146, 2.056, 2.0428, 1.9928, 1.476842, 2.263746, 2.085026, 2.570682, 2.255034, 2.244, 1.744, 1.857962, 1.971986, 2.049986, 4.302296, 2.225376, 2.067066]);
Y2 = np.array([1.0128, 1.21758, 1.656866, 1.67759, 2.96112, 6.0192, 4.52016, 2.40262, 1.39488, 2.09616, 3.1968, 2.4024, 3.535922, 1.94238, 1.878989, 2.12461, 1.72776, 2.710558, 3.3552, 1.619554, 1.474418, 2.4134, 3.05616, 1.92522, 2.29104, 1.97978, 2.2248, 1.85196, 3.23088, 2.93744, 2.80512, 2.0174, 2.7408, 2.617061, 2.4672, 2.24708, 2.39136, 1.624526, 2.71649, 2.293529, 3.084818, 2.480537, 2.6928, 1.9184, 2.229554, 2.169185, 2.459983, 4.732526, 2.670451, 2.273773]);
Y3 = np.array([0.7596, 0.91037, 1.24265, 1.220066, 2.22084, 4.3776, 3.39012, 1.74736, 1.04616, 1.52448, 2.3976, 1.7472, 2.651942, 1.41264, 1.409242, 1.545171, 1.29582, 1.971315, 2.5164, 1.177858, 1.105814, 1.7552, 2.29212, 1.40016, 1.71828, 1.43984, 1.6686, 1.34688, 2.42316, 2.13632, 2.10384, 1.4672, 2.0556, 1.903317, 1.8504, 1.63424, 1.79352, 1.181474, 2.037371, 1.668021, 2.313614, 1.804027, 2.0196, 1.3952, 1.672166, 1.577589, 1.844987, 3.441837, 2.002838,1.653653]);
Y4 = np.array([0.70896, 0.864851, 0.864856, 1.159062, 2.072784, 4.15872, 3.164112, 1.659992, 0.976416, 1.448256, 2.23776, 1.65984, 2.475146, 1.342008, 1.315292, 1.467913, 1.209432, 1.872749, 2.34864, 1.118965, 1.032093, 1.66744, 2.139312, 1.330152, 1.603728, 1.367848, 1.55736, 1.279536, 2.261616, 2.029504, 1.963584, 1.39384, 1.91856, 1.808151, 1.72704, 1.552528, 1.673952, 1.1224, 1.901547, 1.58462, 2.159373, 1.713826, 1.88496, 1.32544, 1.560688, 1.498709, 1.721988, 3.269745, 1.869316, 1.57097]);


min_val = np.min(X11)
max_val = np.max(X11)

# нормалізація в проміжок [0, 1]
normalized_X11 = (X11 - min_val) / (max_val - min_val)
tuple(normalized_X11);
#---------------------------------------------------------------

min_val = np.min(X12)
max_val = np.max(X12)

# нормалізація в проміжок [0, 1]
normalized_X12 = (X12 - min_val) / (max_val - min_val)
tuple(normalized_X12);
#---------------------------------------------------------------

min_val = np.min(X21)
max_val = np.max(X21)

# нормалізація в проміжок [0, 1]
normalized_X21 = (X21 - min_val) / (max_val - min_val)
tuple(normalized_X21);
#---------------------------------------------------------------

min_val = np.min(X22)
max_val = np.max(X22)

# нормалізація в проміжок [0, 1]
normalized_X22 = (X22 - min_val) / (max_val - min_val)
tuple(normalized_X22);
#---------------------------------------------------------------

min_val = np.min(X31)
max_val = np.max(X31)

# нормалізація в проміжок [0, 1]
normalized_X31 = (X31 - min_val) / (max_val - min_val)
tuple(normalized_X31);
#---------------------------------------------------------------

min_val = np.min(X32)
max_val = np.max(X32)

# нормалізація в проміжок [0, 1]
normalized_X32 = (X32 - min_val) / (max_val - min_val)
tuple(normalized_X32);
#---------------------------------------------------------------

min_val = np.min(Y1)
max_val = np.max(Y1)

# нормалізація в проміжок [0, 1]
normalized_Y1 = (Y1 - min_val) / (max_val - min_val)
tuple(normalized_Y1);
#---------------------------------------------------------------

min_val = np.min(Y2)
max_val = np.max(Y2)

# нормалізація в проміжок [0, 1]
normalized_Y2 = (Y2 - min_val) / (max_val - min_val)
tuple(normalized_Y2);
#---------------------------------------------------------------

min_val = np.min(Y3)
max_val = np.max(Y3)

# нормалізація в проміжок [0, 1]
normalized_Y3 = (Y3 - min_val) / (max_val - min_val)
tuple(normalized_Y3);
#---------------------------------------------------------------

min_val = np.min(Y4)
max_val = np.max(Y4)

# нормалізація в проміжок [0, 1]
normalized_Y4 = (Y4 - min_val) / (max_val - min_val)
tuple(normalized_Y4);
#---------------------------------------------------------------

