"""
@Project ：WeChat 
@File    ：DetectWeChatGroupMessage.py
@IDE     ：PyCharm 
@Author  ：Zilong
@Date    ：2023/2/27 21:10 
"""
from wxauto import *
import winsound
import uiautomation as uia
import time

wx = WeChat()
wx.GetSessionList()

def ChatWith(self, who, RollTimes=None):
    self.UiaAPI.SwitchToThisWindow()
    RollTimes = 5 if not RollTimes else RollTimes

    def roll_to(who=who, RollTimes=RollTimes):
        for i in range(RollTimes):
            if who not in self.GetSessionList()[:-1]:
                self.SessionList.WheelDown(wheelTimes=3, waitTime=0.1 * i)
            else:
                time.sleep(0.5)
                self.SessionList.ListItemControl(Name=who).Click(simulateMove=False)
                return 1
        return 0

    rollresult = roll_to()
    if rollresult:
        return 1
    else:
        self.Search(who)
        return roll_to(RollTimes=1)


def GetLastMessage(self):
    uia.SetGlobalSearchTimeout(1.0)
    MsgItem = self.MsgList.GetChildren()[-1]
    Msg = WxUtils.SplitMessage(MsgItem)
    uia.SetGlobalSearchTimeout(10.0)
    return Msg

def SendMsg(self, msg, clear=True):
    self.UiaAPI.SwitchToThisWindow()
    if clear:
        self.EditMsg.SendKeys('{Ctrl}a', waitTime=0)
    self.EditMsg.SendKeys(msg, waitTime=0)
    self.EditMsg.SendKeys('{Enter}', waitTime=0)

def run(object,SendObject,message,count,num):

    ChatWith(wx, object, RollTimes=2)
    print(wx.UiaAPI)
    time.sleep(5)

    flag = True
    keyword1 = "有"
    keyword2 = "放"
    keyword3 = "111"
    keyword4 = "号"
    keyword5 = "没"
    keyword6 = "吗"

    old_message = ""

    while flag:
        msg = GetLastMessage(wx)

        if msg != old_message:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+"  "+msg[0]+" : "+ msg[1])
            old_message = msg

        # 如果信息匹配！
        if (keyword1 in msg[1] or keyword2 in msg[1] or keyword3 in msg[1] or keyword4 in msg[1]) and keyword5 not in msg[1] and keyword6 not in msg[1]:
            print(msg[0] + " : " + msg[1] + message)

            ChatWith(wx, SendObject, RollTimes=None)
            for i in range(count):
                SendMsg(wx, message, clear=True)
                i += 1

            # 电脑发出音量提示
            duration = 1000*num  # millisecond
            freq = 440  # Hz
            winsound.Beep(freq, duration)

            flag = False










