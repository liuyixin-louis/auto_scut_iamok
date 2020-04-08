# python实现华工iamok每日报平安自动打卡
## 背景

学校现在每天都得手动[报平安](https://iamok.scut.edu.cn)，一不小心就忘记了。。有了python，再也不用担心忘记打卡了！

## 如何使用

:one:简单配置：学号和密码；打卡时间；

![image-20200408130750090](https://picbed-1301760901.cos.ap-guangzhou.myqcloud.com/image-20200408130750090.png)

![image-20200408130808031](https://picbed-1301760901.cos.ap-guangzhou.myqcloud.com/image-20200408130808031.png)

:two:然后在挂在后台就好了！到点会自动打卡！

```python
python ./fuck_iamok.py
```

![image-20200408131546001](https://picbed-1301760901.cos.ap-guangzhou.myqcloud.com/image-20200408131546001.png)



## 工具

* python语言
* selenium模块实现仿真操作
* apscheduler模块做定时调度