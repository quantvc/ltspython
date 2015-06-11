# encoding:utf-8

from __future__ import absolute_import

from MdApi import CSecurityMdSpi #CSecurityMdApi#
#from . import common


class MdSpi(CSecurityMdSpi):
    """
    base header CSecurityFtdcMdSpi

    """

    def __init__(self):
        pass

    def OnFrontConnected(self):
        """
        当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        """
        super(MdSpi, self).OnFrontConnected()

    def OnFrontDisconnected(self, reason):
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
        assert isinstance(reason, int), "reason parameter must be integer."
        super(MdSpi, self).OnFrontDisconnected(reason)

    def OnHeartBeatWarning(self, time_lapse):
        """
        心跳超时警告。当长时间未收到报文时，该方法被调用。

        :param time_lapse:int, 距离上次接收报文的时间

        """
        assert isinstance(time_lapse, int), "time_lapse parameter must be integer."
        super(MdSpi, self).OnHeartBeatWarning(time_lapse)

    def OnRspError(self, rsp_info, request_id, is_last):
        """
        错误应答
        :param rsp_info:
        :param request_id: int
        :param is_last: bool

        """
        #common.check_lts_parameter_type(request_id, is_last)
        super(MdSpi, self).OnRspError(rsp_info, request_id, is_last)

    def OnRspUserLogin(self, rsp_user_login, rsp_info, request_id, is_last):
        """
        登录请求响应
        :param rsp_user_login:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        :return:
        """
        #common.check_lts_parameter_type(request_id, is_last)
        super(MdSpi, self).OnRspUserLogin(rsp_user_login, rsp_info, request_id, is_last)

    def OnRspUserLogout(self, user_logout, rsp_info, request_id, is_last):
        """
        登出请求响应
        :param user_logout:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool

        """
        #common.check_lts_parameter_type(request_id, is_last)
        super(MdSpi, self).OnRspUserLogout(user_logout, rsp_info, request_id, is_last)

    def OnRspSubMarketData(self, specific_instrument, rsp_info, request_id, is_last):
        """
        订阅行情应答
        :param specific_instrument:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        #common.check_lts_parameter_type(request_id, is_last)
        super(MdSpi, self).OnRspSubMarketData(specific_instrument, rsp_info, request_id, is_last)

    def OnRspUnSubMarketData(self, specific_instrument, rsp_info, request_id, is_last):
        """
        取消订阅行情应答
        :param specific_instrument:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        #common.check_lts_parameter_type(request_id, is_last)
        super(MdSpi, self).OnRspUnSubMarketData(specific_instrument, rsp_info, request_id, is_last)

    def OnRtnDepthMarketData(self, depth_market_data):
        """
        深度行情通知
        :param depth_market_data:
        """
        super(MdSpi, self).OnRtnDepthMarketData(depth_market_data)

    def __del__(self):
        pass

#
# class MdApi(CSecurityMdApi):
#     """
#     base CSecurityFtdcMdApi
#     """
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def CreateFtdcMdApi(path):
#         """
#         创建MdApi,modify for udp marketdata
#
#         :param path: 存贮订阅信息文件的目录，默认为当前目录
#         :return: c++ class Instance 创建出的UserApi
#         """
#         # todo need to fix some
#
#         return super(CSecurityMdApi, CSecurityMdApi).CreateFtdcMdApi(path)
#
#     def Release(self):
#         """
#         删除接口对象本身
#         不再使用本接口对象时,调用该函数删除接口对象
#         """
#         super(MdApi, self).Release()
#
#     def Init(self):
#         """
#         初始化
#         初始化运行环境,只有调用后,接口才开始工作
#         """
#         super(MdApi, self).Init()
#
#     def Join(self):
#         """
#         等待接口线程结束运行
#         :return :int,线程退出代码
#         """
#         return super(MdApi, self).Join()
#
#     def GetTradingDay(self):
#         """
#         获取当前交易日,只有登录成功后,才能得到正确的交易日
#         :return : str,获取到的交易日
#         """
#         return super(MdApi, self).GetTradingDay()
#
#     def RegisterFront(self, address):
#         """
#         注册前置机网络地址
#         网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
#         “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
#         :param address: 前置机网络地址
#         """
#         super(MdApi, self).RegisterFront(address)
#
#     def RegisterSpi(self, md_spi):
#         """
#         注册回调接口
#         :param md_spi: MdSpi instance, 派生自回调接口类的实例
#         """
#         assert isinstance(md_spi, MdSpi), "Must CSecurityFtdcMdSpi instance."
#         assert issubclass(md_spi, CSecurityMdSpi), "Must CSecurityFtdcMdSpi subclass "
#         super(MdApi, self).RegisterSpi(md_spi)
#
#     def SubscribeMarketData(self, instrument_id, exchange_id):
#         """
#         订阅行情。
#         :param instrument_id: list, 合约ID
#         :param exchange_id: str
#         :return: int
#         """
#         assert isinstance(instrument_id, list), "InstrumentID must be list. "
#         return super(MdApi, self).SubscribeMarketData(instrument_id, len(instrument_id), exchange_id)
#
#     def UnSubscribeMarketData(self, instrument_id, exchange_id):
#         """
#         退订行情。
#         :param instrument_id: list, InstrumentID 合约ID
#         :param exchange_id:  str
#         :return: int
#         """
#         assert isinstance(instrument_id, list), "InstrumentID must be list. "
#         return super(MdApi, self).UnSubscribeMarketData(instrument_id, len(instrument_id), exchange_id)
#
#     def ReqUserLogin(self, user_login, request_id):
#         """
#         用户登录请求
#         :param user_login: CSecurityFtdcReqUserLoginField
#         :param request_id: int
#         :return:int
#         """
#         common.check_lts_parameter_type(request_id)
#
#         return super(MdApi, self).ReqUserLogin(user_login, request_id)
#
#     def ReqUserLogout(self, user_logout, request_id):
#         """
#         登出请求
#         :param user_logout: CSecurityFtdcReqUserLoginField
#         :param request_id: int
#         :return: int
#         """
#         common.check_lts_parameter_type(request_id)
#         return super(MdApi, self).ReqUserLogout(user_logout, request_id)
#
#     def __del__(self):
#         pass
