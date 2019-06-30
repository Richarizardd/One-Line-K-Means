### This is K-Means in one line.

![Kmeans](https://raw.githubusercontent.com/Richarizardd/One-Line-K-Means/master/kmeans.png)

```python
import numpy as np; KMeansFit = lambda X, centers, max_itr, k: [[np.mean(X[np.argmin([np.linalg.norm(X - m_r, axis=1) for m_r in centers], axis=0) == r], axis=0) for r in range(k)] for itr in range(max_itr)]
```

Turns out that np.linalg.norm is pretty good. 
