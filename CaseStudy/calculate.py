import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

def CO2():
    fig = plt.figure()
    '''创建3D轴对象'''
    ax = Axes3D(fig)
    '''X坐标数据'''
    X = np.arange(-2, 2, 0.1)
    '''Y坐标数据'''
    Y = np.arange(-2, 2, 0.1)
    '''计算3维曲面分格线坐标'''
    X, Y = np.meshgrid(X, Y)
    '''用于计算X/Y对应的Z值'''

    def f(x, y):
        return (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)

    '''plot_surface函数可绘制对应的曲面'''
    #ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1)
    ax.plot_wireframe(X,Y,f(X, Y))
    '''显示'''
    plt.show()
#Ball_3D(1)
#Gauss(1)
CO2()

def ball():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    #x = 10 * np.outer(np.cos(u), np.sin(v))
    #y = 10 * np.outer(np.sin(u), np.sin(v))
    #z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    x1 = 7 + 10 * np.outer(np.cos(u), np.sin(v))
    y1 = 7 + 10 * np.outer(np.sin(u), np.sin(v))
    z1 = 7 + 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    #ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')
    ax.plot_surface(x1, y1, z1, rstride=4, cstride=4, cmap=cm.coolwarm)
    ax.plot_wireframe(x1,y1,z1)
    plt.show()

def gauss():
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.exp((-0.5) * ((X * X) + (Y * Y)))
    Z = R  # （40x40）
    # mean, cov = [0, 1], [(1, .5), (.5, 1)]  #cov指的是协方差矩阵，也是对称阵。
    # data = np.random.multivariate_normal(mean, cov, 200)
    # np.random.randint(1,100,[5,5])
    data = [np.exp((-0.5) * (((X + i / 10) * (X + i / 10)) + ((Y + i / 10) * (Y + i / 10)))) for i in range(100)]

    fig = plt.figure()
    ax = Axes3D(fig)

    n = 1
    for i in range(100):
        ax = Axes3D(fig)
        if n==0:
            ax.plot_surface(X, Y, data[i], rstride=1, cstride=1, alpha=0.5, cmap=cm.coolwarm)
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.5, cmap=cm.coolwarm)
        else:
            ax.plot_wireframe(X,Y,Z)
            ax.plot_wireframe(X,Y,data[i])
        plt.pause(0.1)
#gauss()
