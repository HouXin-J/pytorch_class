#_*_coding:utf-8 _*_
# import numpy as np
# import visdom
# import time
#

#
#
# # #单张图像显示与更新demo
# # image = viz.image(np.random.rand(3,256,256),opts={'title':'image1','caption':'How random.'})
# # for i in range(10):
# #     viz.image(np.random.randn( 3, 256, 256),win = image)
# #     time.sleep(0.5)
# #多图像显示与更新demo
# images = viz.images(
#         np.random.randn(50, 3, 64, 64),
#         opts=dict(title='Random images', caption='How random.',nrow=5)
#     )
# for i in range(10):
#     viz.images(np.random.randn(50, 3, 64, 64),win = images)
#     time.sleep(0.5)




from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
# import visdom
from visdom import Visdom
import numpy as np
import math
import os.path
import getpass
from sys import platform as _platform
from six.moves import urllib

viz = Visdom(env="Test2") # 创建环境名为Test2
viz.text('Hello World', win='text1')
viz.text('Hi', win='text1',append=True)

# # viz = Visdom()
# assert viz.check_connection()
#
# try:
#     import matplotlib.pyplot as plt
#     plt.plot([1, 23, 2, 4])
#     plt.ylabel('some numbers')
#     plt.title("testestsetsetset")
#     viz.matplot(plt)
#
# except BaseException as err:
#     print('Skipped matplotlib example')
#     print('Error message: ', err)
#
#
# import time
# Y = np.random.rand(100)
# old_scatter = viz.scatter(
#     X=np.random.rand(100, 2),
#     Y=(Y[Y > 0] + 1.5).astype(int),
#     opts=dict(
#         legend=['Didnt', 'Update'],
#         xtickmin=-50,
#         xtickmax=50,
#         xtickstep=0.5,
#         ytickmin=-50,
#         ytickmax=50,
#         ytickstep=0.5,
#         markersymbol='cross-thin-open',
#     ),
# )
#
# #对窗口进行更新,包括标注,坐标,样式等
# viz.update_window_opts(
#     win=old_scatter,
#     opts=dict(
#         legend=['Apples', 'Pears'],
#         xtickmin=0,
#         xtickmax=1,
#         xtickstep=0.5,
#         ytickmin=0,
#         ytickmax=1,
#         ytickstep=0.5,
#         markersymbol='cross-thin-open',
#     ),
# )
#
#
# time.sleep(5)
#
#
