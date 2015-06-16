# encoding:utf-8

import md_api


class Spi(object):
    """
    base header CSecurityFtdcMdSpi
    """

    def __init__(self, api):
        """
        
        :param api:
        :return:
        """
        self.api = api

    def OnFrontConnected(self):
        """
        当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        """
        pass

    def OnFrontDisconnected(self, nReason):
        """
        当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        reason:
            0x1001 网络读失败
            0x1002 网络写失败
            0x2001 接收心跳超时
            0x2002 发送心跳失败
            0x2003 收到错误报文
        :param reason:int,
        """
        pass

    def OnHeartBeatWarning(self, nTimeLapse):
        """
        心跳超时警告。当长时间未收到报文时，该方法被调用。

        :param time_lapse:int, 距离上次接收报文的时间

        """
        pass

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        """
        错误应答
        :param rsp_info:
        :param request_id: int
        :param is_last: bool

        """
        pass

    def OnRspUserLogin(self, rsp_user_login, pRspInfo, nRequestID, bIsLast):
        """
        登录请求响应
        :param rsp_user_login:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        :return:
        """
        pass

    def OnRspUserLogout(self, user_logout, pRspInfo, nRequestID, bIsLast):
        """
        登出请求响应
        :param user_logout:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool

        """
        pass

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        """
        订阅行情应答
        :param specific_instrument:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """

        pass

    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        """
        取消订阅行情应答
        :param specific_instrument:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """

        pass

    def OnRtnDepthMarketData(self, OnRtnDepthMarketData):
        """
        深度行情通知
        :param depth_market_data:
        """
        pass


class MdApi(object):
    """
    """

    def __init__(self, flow_path=""):
        """

        :param flow_path:
        :return:
        """
        self.api = md_api.create_MdApi(flow_path)

    def Release(self):
        """
        删除接口对象本身
        不再使用本接口对象时,调用该函数删除接口对象
        """
        md_api.Release(self.api)

    def Init(self):
        """
        初始化
        初始化运行环境,只有调用后,接口才开始工作
        """
        md_api.Init(self.api)

    def Join(self):
        """
        等待接口线程结束运行
        :return :int,线程退出代码
        """
        return md_api.Join(self.api)

    def RegisterFront(self, address):
        """
        注册前置机网络地址
        网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        :param address: 前置机网络地址
        """
        md_api.RegisterFront(self.api, address)

    def RegisterSpi(self, md_spi):
        """
        注册回调接口
        :param md_spi: MdSpi instance, 派生自回调接口类的实例
        """

        md_api.RegisterSpi(self.api, md_api)

    def SubscribeMarketData(self, instrument_id, exchange_id):
        """
        订阅行情。
        :param instrument_id: list, 合约ID
        :param exchange_id: str
        :return: int
        """
        return md_api.SubscribeMarketData(self.api, instrument_id, exchange_id)

    def UnSubscribeMarketData(self, instrument_id, exchange_id):
        """
        退订行情。
        :param instrument_id: list, InstrumentID 合约ID
        :param exchange_id:  str
        :return: int
        """
        return md_api.UnSubscribeMarketData(self.api, instrument_id, exchange_id)

    def ReqUserLogin(self, user_login, request_id):
        """
        用户登录请求
        :param user_login: CSecurityFtdcReqUserLoginField
        :param request_id: int
        :return:int
        """

        return md_api.ReqUserLogin(self.api, user_login, request_id)

    def ReqUserLogout(self, user_logout, request_id):
        """
        登出请求
        :param user_logout: CSecurityFtdcReqUserLoginField
        :param request_id: int
        :return: int
        """

        return md_api.ReqUserLogout(self.api, user_logout, request_id)
