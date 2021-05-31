# wukong-robot


## 环境要求 ##

### Python 版本 ###

wukong-robot 只支持 Python 3.5+，不支持 Python 2.x 。

### 设备要求 ###


## 升级

``` bash
python3 wukong.py update
```

如果提示升级失败，可以尝试在 wukong-robot 的根目录手动执行以下命令，看看问题出在哪。

``` sh
git pull
pip3 install -r requirements.txt
```

## 运行 ##

``` bash
python3 wukong.py
```

建议在 [tmux](http://blog.jobbole.com/87278/) 或 supervisor 中执行。

第一次启动时将提示你是否要到用户目录下创建一个配置文件，输入 `y` 即可。

然后通过唤醒词 “孙悟空” 唤醒 wukong-robot 进行交互（该唤醒词可自定义）。


## 配置 ##

参考[配置文件的注释](https://github.com/wzpan/wukong-robot/blob/master/static/default.yml)进行配置即可。注意不建议直接修改 default.yml 里的内容，否则会给后续通过 `git pull` 更新带来麻烦。你应该拷贝一份放到 `$HOME/.wukong/config.yml` 中，或者在运行的时候按照提示让 wukong-robot 为你完成这件事。

