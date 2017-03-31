import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ],
              [8, 8],
              [1, 0.6],
              [9,11]])


class KMeans:
    def __init__(self,itera=300,k=2,tol=0.001):
        self.k=k
        self.tol=tol
        self.itera=itera
    def fit(self,data):
        self.data=data
        self.centroid={}
        self.pts={}
        for i in range(self.k):
          self.centroid[i]=self.data[i];
        for i in range(self.k):
            self.pts[i]=[]
        for x in range(self.itera):
         for X in self.data:
            print X
            dis=[np.linalg.norm(X-self.centroid[centro]) for centro in self.centroid]
            print dis
            dist=dis.index(min(dis))
            print dist
            self.pts[dist].append(X)
            #print self.pts[1]
         for clas in self.pts:
            self.centroid[clas]=np.average(self.pts[clas],axis=0)

            a=self.centroid[0][0]
            b=self.centroid[0][1]
            c=self.centroid[1][0]
            d=self.centroid[1][1]


        plt.scatter(df[:,0],df[:,1])
        plt.scatter(a,b)
        plt.scatter(c,d )

        plt.show()

    def predict(self,Y):
        pass
clf=KMeans()
clf.fit(df)
