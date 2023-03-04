# WeChat - DetectWeChatGroupMessage

## 代码功能简介：

    可以用于获取指定的微信群聊最新聊天内容，通过检测关键字做出相应的提醒，包括给特定人发送指定数目的消息提示，电脑发出指定时间的警示音。
    
## 代码运行效果展示：
![image](https://user-images.githubusercontent.com/85872598/222858485-c81b87ac-2a4d-46c7-b328-8e39b88aa163.png)
![image](https://user-images.githubusercontent.com/85872598/222859660-7ae46aa3-c3f3-4ffd-bd1c-2775d5f727b6.png)
    
    
## 安装使用说明：
1、首先需要在Python Terminal 中安装 wxauto 和 uiautomation （鼠标移动到红线地方可以使用快捷键安装）

2、之后需要登录微信，不能将界面隐藏到任务栏中最小化

3、修改DetectWeChatGroupMessage.py中keywords，这是用于检测微信消息中的关键字

（这里我的检测条件是1-4在并且5，6不在）


  ![image](https://user-images.githubusercontent.com/85872598/222861012-5055eca0-53c6-45da-8157-4347f00f8eea.png)

4、修改mian.py中的参数后运行

    目前run("文件传输助手","文件传输助手","Git：代码效果展示！",6,10)
    # 第一个参数：想要检测的微信群
    # 第二个参数：想要发送消息的对象
    # 第三个参数：想要发送的消息
    # 第四个参数：想要发送消息条数
    # 第五个参数：电脑提示音时间，单位秒
    
    
## 注意事项

只是一个小程序，用于检测法签申根群中的关键信息（是否有放号信息），类似相关群的群主可以使用程序检测到如果成员发布关键信息可以向群聊中连续发送10条提醒消息。编码的初心是为了方便，虽然最后还是没有抢到slot。请不要使用程序恶意连续发送骚扰信息。

## 免责声明

代码仅供交流学习使用，请勿用于非法用途和商业用途！如因此产生任何法律纠纷，均与作者无关！

## 支持

感谢对项目的支持
![image](https://user-images.githubusercontent.com/85872598/222904574-395f96dd-981b-4e9b-a574-4602515f2203.png)

