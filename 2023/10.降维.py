import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import neighbors,decomposition,manifold
# 高维背景
scale1 = 4
scale2 = 10
disp_input=[]
for a in range(int(scale1)):
    for b in range(int(scale1)):
        for c in range(int(scale1)):
            for d in range(int(scale1)):
                for e in range(int(scale1)):
                    for f in range(int(scale2)):
                        for g in range(int(scale2)):
                            for h in range(int(scale1)):
                                disp_input.append([
                                    a/scale1,
                                    b/scale1,
                                    c/scale1,
                                    d/scale1,
                                    e/scale1,
                                    f/scale2,
                                    g/scale2,
                                    h/scale1,
                                    ])
disp_input = pd.DataFrame(disp_input)
from sklearn.decomposition import PCA
model = PCA(n_components=2)
pca_result = pd.DataFrame(model.fit_transform(disp_input))
pca_result = (pca_result-pca_result.min())/(pca_result.max()-pca_result.min())
plt.figure(dpi=200)
plt.scatter(pca_result.iloc[:,0], pca_result.iloc[:,1], c='red')
plt.show()
