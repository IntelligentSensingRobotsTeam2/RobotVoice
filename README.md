# wukong-robot

安装教程： https://wukong.hahack.com/#/install   
使用tutorial: https://wukong.hahack.com/#/   

## 环境要求 ##

### Python 版本 ###

只支持 Python 3.5+，不支持 Python 2.x 。

### 设备要求 ###


## 配置 ##


把技能插件包 https://github.com/IntelligentSensingRobotsTeam2/VoiceSkillPlugin 放到根目录 ~/.wukong/文件夹下（新建）   

参考[配置文件的注释](https://github.com/wzpan/wukong-robot/blob/master/static/default.yml)进行配置即可。注意不建议直接修改 default.yml 里的内容，否则会给后续通过 `git pull` 更新带来麻烦。你应该拷贝一份放到 `$HOME/.wukong/config.yml` 中，或者在运行的时候按照提示让 robot 为你完成这件事。   


## 运行 ##

``` bash
python3 mainVoice.py   

python3 mainVoice.py admin 默认开启管理员模式
```
### 呼叫
唤醒词'ABC'
重新训练唤醒词: https://wukong.hahack.com/#/tips?id=_2-%e4%bf%ae%e6%94%b9%e5%94%a4%e9%86%92%e8%af%8d

## 技能 ##

### 普通人
询问天气： '北京明天会下雨吗'   
咨询疫情: '佛山目前确诊人数有多少'   
地点导航: '出口在哪里/洗手间怎么去/怎么去咨询台'   

### 管理员
可通过启动时命令指令默认启动管理员权限   
通过cmdRecv/cmdServer.py udp服务器接受消息(启动主程序后自动开启监听)   
(可通过`cmdRecv/RosUdpServer.py` 往server发送命令做测试。修改端口、ip)      
在接受到管理员认证消息后('admin')20秒内唤醒‘开启管理员权限’即可开启。   

机器人移动： ‘往前走/后退3米’ ‘左转/逆时针转30度’   
消毒：‘开启/关闭消毒/喷洒’ ‘停下来’   

语音通过udp发送指令，可通过`cmdRecv/RosUdpServer.py`测试接受通讯。   

