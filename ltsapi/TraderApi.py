# encoding:utf-8


from __future__ import absolute_import


from ltsapi.Trader.TraderApi import CSecurityTraderSpi, CSecurityTraderApi


class TraderSpi(object):
    """
    base CSecurityFtdcTraderSpi
    """

    def __init__(self):
        pass

    def OnFrontConnected(self):
        """
        当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        """
        super(TraderSpi, self).OnFrontConnected()

    def OnFrontDisconnected(self, reason):
        """
        当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        :param reason:错误原因
                       0x1001 网络读失败
                       0x1002 网络写失败
                       0x2001 接收心跳超时
                       0x2002 发送心跳失败
                       0x2003 收到错误报文
        """
        super(TraderSpi, self).OnFrontDisconnected(reason)

    def OnHeartBeatWarning(self, time_lapse):
        """
        心跳超时警告。当长时间未收到报文时，该方法被调用。
        :param time_lapse:  距离上次接收报文的时间
        """
        assert isinstance(time_lapse, int), "time_lapse must be integer"
        super(TraderSpi, self).OnHeartBeatWarning(time_lapse)

    def OnRspError(self, rsp_info, request_id, is_last):
        """
        错误应答
        :param rsp_info: RspInfoField
        :param request_id:int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspError(rsp_info, request_id, is_last)

    def OnRspUserLogin(self, rsp_user_login, rsp_info, request_id, is_last):
        """
        登录请求响应
        :param rsp_user_login:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspUserLogin(rsp_user_login, rsp_info, request_id, is_last)

    def OnRspUserLogout(self, user_logout, rsp_info, request_id, is_last):
        """
        登出请求响应
        :param user_logout:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspUserLogout(user_logout, rsp_info, request_id, is_last)

    def OnRspOrderInsert(self, input_order, rsp_info, request_id, is_last):
        """
        报单录入请求响应
        :param input_order:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspOrderInsert(input_order, rsp_info, request_id, is_last)

    def OnRspOrderAction(self, input_order_action, rsp_info, request_id, is_last):
        """
        报单操作请求响应
        :param input_order_action:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspOrderAction(input_order_action, rsp_info, request_id, is_last)

    def OnRspUserPasswordUpdate(self, user_password_update, rsp_info, request_id, is_last):
        """
        用户口令更新请求响应
        :param user_password_update:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspUserPasswordUpdate(user_password_update, rsp_info, request_id, is_last)

    def OnRspTradingAccountPasswordUpdate(self, trading_account_password_update, rsp_info, request_id, is_last):
        """
        资金账户口令更新请求响应
        :param trading_account_password_update:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspTradingAccountPasswordUpdate(trading_account_password_update,
                                                                 rsp_info,
                                                                 request_id,
                                                                 is_last)

    def OnRspQryExchange(self, exchange, rsp_info, request_id, is_last):
        """
        请求查询交易所响应
        :param exchange:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryExchange(exchange, rsp_info, request_id, is_last)

    def OnRspQryInstrument(self, instrument, rsp_info, request_id, is_last):
        """
        请求查询合约响应
        :param instrument:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryInstrument(instrument, rsp_info, request_id, is_last)

    def OnRspQryInvestor(self, investor, rsp_info, request_id, is_last):
        """
        请求查询投资者响应
        :param investor:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryInvestor(investor, rsp_info, request_id, is_last)

    def OnRspQryTradingCode(self, trading_code, rsp_info, request_id, is_last):
        """
        请求查询交易编码响应
        :param trading_code:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryTradingCode(trading_code, rsp_info, request_id, is_last)

    def OnRspQryTradingAccount(self, trading_account, rsp_info, request_id, is_last):
        """
        请求查询资金账户响应
        :param trading_account:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryTradingAccount(trading_account, rsp_info, request_id, is_last)

    def OnRspQryDepthMarketData(self, depth_market_data, rsp_info, request_id, is_last):
        """
        请求查询行情响应
        :param depth_market_data:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryDepthMarketData(depth_market_data, rsp_info, request_id, is_last)

    def OnRspQryBondInterest(self, bond_interest, rsp_info, request_id, is_last):
        """
        请求查询债券利息响应
        :param bond_interest:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryBondInterest(bond_interest, rsp_info, request_id, is_last)

    def OnRspQryMarketRationInfo(self, market_ration_info, rsp_info, request_id, is_last):
        """
        请求查询市值配售信息响应
        :param market_ration_info:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryMarketRationInfo(market_ration_info, rsp_info, request_id, is_last)

    def OnRspQryInstrumentCommissionRate(self, instrument_commission_rate, rsp_info, request_id, is_last):
        """
        请求查询合约手续费率响应
        :param instrument_commission_rate:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryInstrumentCommissionRate(instrument_commission_rate, rsp_info, request_id,
                                                                is_last)

    def OnRspQryOrder(self, order, rsp_info, request_id, is_last):
        """
        请求查询报单响应
        :param order:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryOrder(order, rsp_info, request_id, is_last)

    def OnRspQryTrade(self, trader, rsp_info, request_id, is_last):
        """
        请求查询成交响应
        :param trader:
        :param rsp_info:
        :param request_id: int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryTrade(trader, rsp_info, request_id, is_last)

    def OnRspQryInvestorPosition(self, investor_position, rsp_info, request_id, is_last):
        """
        请求查询投资者持仓响应
        :param investor_position:
        :param rsp_info:
        :param request_id:int,
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryInvestorPosition(investor_position, rsp_info, request_id, is_last)

    def OnRtnOrder(self, order):
        """
        报单通知
        :param order:
        """
        super(TraderSpi, self).OnRtnOrder(order)

    def OnRtnTrade(self, trade):
        """
        成交通知
        :param trade:
        """
        super(TraderSpi, self).OnRtnTrade(trade)

    def OnErrRtnOrderInsert(self, input_order, rsp_info):
        """
        报单录入错误回报
        :param input_order:
        :param rsp_info:
        """

        super(TraderSpi, self).OnErrRtnOrderInsert(input_order, rsp_info)

    def OnErrRtnOrderAction(self, order_action, rsp_info):
        """
        报单操作错误回报
        :param order_action:
        :param rsp_info:
        """

        super(TraderSpi, self).OnErrRtnOrderAction(order_action, rsp_info)

    def OnRspFundOutByLiber(self, input_fund_transfer, rsp_info, request_id, is_last):
        """
        Liber发起出金应答
        :param input_fund_transfer:
        :param rsp_info:
        :param request_id:int,
        :param is_last:bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspFundOutByLiber(input_fund_transfer, rsp_info, request_id, is_last)

    def OnRtnFundOutByLiber(self, fund_transfer):
        """
        Liber发起出金通知
        :param fund_transfer:

        """

        super(TraderSpi, self).OnRtnFundOutByLiber(fund_transfer)

    def OnErrRtnFundOutByLiber(self, input_fund_transfer, rsp_info):
        """
        iber发起出金错误回报
        :param input_fund_transfer:
        :param rsp_info:
        """

        super(TraderSpi, self).OnErrRtnFundOutByLiber(input_fund_transfer, rsp_info)

    def OnRtnFundInByBank(self, fund_transfer):
        """
        银行发起入金通知
        :param fund_transfer:
        """

        super(TraderSpi, self).OnRtnFundInByBank(fund_transfer)

    def OnRspQryFundTransferSerial(self, fund_transfer, rsp_info, request_id, is_last):
        """
        资金转账查询应答
        :param fund_transfer:
        :param rsp_info:
        :param request_id: int
        :param is_last: bool,
        """
        common.check_lts_parameter_type(request_id, is_last)
        super(TraderSpi, self).OnRspQryFundTransferSerial(fund_transfer, rsp_info, request_id, is_last)

    def __del__(self):
        pass


class TraderApi(CSecurityTraderApi):
    """
    base CSecurityFtdcTraderApi
    """
    def __init__(self):
        pass

    # todo static method or classmethod
    @classmethod
    def CreateFtdcTraderApi(cls, path=""):
        """
        创建TraderApi
        :param path: 存贮订阅信息文件的目录，默认为当前目录
        :return:创建出的UserApi
        """
        return super(TraderApi, cls).CreateFtdcTraderApi(path)

    def Release(self):
        """
        删除接口对象本身
        不再使用本接口对象时,调用该函数删除接口对象

        """
        super(TraderApi, self).Release()

    def Init(self):
        """
        初始化
        初始化运行环境,只有调用后,接口才开始工作
        """
        super(TraderApi, self).Init()

    def Join(self):
        """
         等待接口线程结束运行
        :return:int ,线程退出代码
        """
        return super(TraderApi, self).Join()

    def GetTradingDay(self):
        """
        获取当前交易日, 只有登录成功后,才能得到正确的交易日
        :return: 获取到的交易日
        """
        return super(TraderApi, self).GetTradingDay()

    def RegisterFront(self, address):
        """
        注册前置机网络地址
        网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        :param address: 前置机网络地址
        """
        super(TraderApi, self).RegisterFront(address)

    def RegisterSpi(self, trader_spi):
        """
        注册回调接口

        :param trader_spi: SPI 派生自回调接口类的实例

        """
        assert isinstance(trader_spi, TraderSpi), "TraderSPI must be instance TraderSpi"
        assert issubclass(trader_spi, CSecurityTraderSpi), "TraderSpi must be subclass CSecurityTraderSpi"
        super(TraderApi, self).RegisterSpi(trader_spi)

    def SubscribePrivateTopic(self, resume_type):
        """
        订阅私有流。
        ResumeType:
            SECURITY_TERT_RESTART:从本交易日开始重传
            SECURITY_TERT_RESUME:从上次收到的续传
            SECURITY_TERT_QUICK:只传送登录后私有流的内容
        该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
        :param resume_type: 私有流重传方式
        """
        super(TraderApi, self).SubscribePrivateTopic(resume_type)

    def SubscribePublicTopic(self, resume_type):
        """
        订阅公共流。
        ResumeType:
            SECURITY_TERT_RESTART:从本交易日开始重传
            SECURITY_TERT_RESUME:从上次收到的续传
            SECURITY_TERT_QUICK:只传送登录后公共流的内容
        该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        :param resume_type: 公共流重传方式
        """
        super(TraderApi, self).SubscribePublicTopic(resume_type)

    def ReqUserLogin(self, req_user_login, request_id):
        """
        用户登录请求
        :param req_user_login:
        :param request_id: int
        :return:int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqUserLogin(req_user_login, request_id)

    def ReqUserLogout(self, user_logout, request_id):
        """
         登出请求
        :param user_logout:
        :param request_id: int
        :return:int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqUserLogout(user_logout, request_id)

    def ReqOrderInsert(self, input_order, request_id):
        """
        报单录入请求

        :param input_order:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqOrderInsert(input_order, request_id)

    def ReqOrderAction(self, input_order_action, request_id):
        """
        报单操作请求
        :param input_order_action:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqOrderAction(input_order_action, request_id)

    def ReqUserPasswordUpdate(self, user_password_update, request_id):
        """
        用户口令更新请求
        :param user_password_update:
        :param request_id: int
        :return:int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqUserPasswordUpdate(user_password_update, request_id)

    def ReqTradingAccountPasswordUpdate(self, trading_account_password_update, request_id):
        """
        资金账户口令更新请求
        :param trading_account_password_update:
        :param request_id: int
        :return:int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqTradingAccountPasswordUpdate(trading_account_password_update, request_id)

    def ReqQryExchange(self, qry_exchange, request_id):
        """
         请求查询交易所
        :param qry_exchange:
        :param request_id: int
        :return:int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryExchange(qry_exchange, request_id)

    def ReqQryInstrument(self, qry_instrument, request_id):
        """
        请求查询合约
        :param qry_instrument:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryInstrument(qry_instrument, request_id)

    def ReqQryInvestor(self, qry_investor, request_id):
        """
        请求查询投资者
        :param qry_investor:
        :param request_id: int
        :return:int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryInvestor(qry_investor, request_id)

    def ReqQryTradingCode(self, qry_trading_code, request_id):
        """
        请求查询交易编码
        :param qry_trading_code:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryTradingCode(qry_trading_code, request_id)

    def ReqQryTradingAccount(self, qry_trading_account, request_id):
        """
        请求查询资金账户
        :param qry_trading_account:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryTradingAccount(qry_trading_account, request_id)

    def ReqQryDepthMarketData(self, qry_depth_market_data, request_id):
        """
        请求查询行情
        :param qry_depth_market_data:
        :param request_id: int
        :return: int
        """
        return super(TraderApi, self).ReqQryDepthMarketData(qry_depth_market_data, request_id)

    def ReqQryBondInterest(self, qry_bond_interest, request_id):
        """
        请求查询债券利息
        :param qry_bond_interest:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryBondInterest(qry_bond_interest, request_id)

    def ReqQryMarketRationInfo(self, qry_market_ration_info, request_id):
        """
        请求查询市值配售信息
        :param qry_market_ration_info:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryMarketRationInfo(qry_market_ration_info, request_id)

    def ReqQryInstrumentCommissionRate(self, qry_instrument_commission_rate, request_id):
        """
        请求查询合约手续费率
        :param qry_instrument_commission_rate:
        :param request_id: int
        :return:int
        """
        return super(TraderApi, self).ReqQryInstrumentCommissionRate(qry_instrument_commission_rate, request_id)

    def ReqQryOrder(self, qry_order, request_id):
        """
        请求查询报单
        :param qry_order:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryOrder(qry_order, request_id)

    def ReqQryTrade(self, qry_trade, request_id):
        """
        请求查询成交
        :param qry_trade:
        :param request_id:  int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryTrade(qry_trade, request_id)

    def ReqQryInvestorPosition(self, qry_investor_position, request_id):
        """
        请求查询投资者持仓
        :param qry_investor_position:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqQryInvestorPosition(qry_investor_position, request_id)

    def ReqFundOutByLiber(self, input_fund_transfer, request_id):
        """
        Liber发起出金请求
        :param input_fund_transfer:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)
        return super(TraderApi, self).ReqFundOutByLiber(input_fund_transfer, request_id)

    def ReqQryFundTransferSerial(self, qry_fund_transfer_serial, request_id):
        """
        资金转账查询请求
        :param qry_fund_transfer_serial:
        :param request_id: int
        :return: int
        """
        common.check_lts_parameter_type(request_id)

        return super(TraderApi, self).ReqQryFundTransferSerial(qry_fund_transfer_serial, request_id)
