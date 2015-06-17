# encoding:utf-8


class Base(object):
    def __repr__(self):
        pass

class Base(object):

    def __repr__(self):
        """
        :return:
        """

        return "<%s>" % ",".join(["%s:%s" % (item, value) for item, value in self.__dict__.iteritems()])



class RspInfoClass(object):
    """
    响应信息
    """

    def __init__(self, error_id, error_msg):
        """
        :param error_id: int, 错误代码
        :param error_msg: str,length:81 错误信息
        :return:
        """
        self.error_id = error_id
        self.error_msg = error_msg


class ExchangeClass(object):
    """
    交易所

    交易所属性 exchange_property:
        正常: SECURITY_FTDC_EXP_Normal '0'
        根据成交生成报单:SECURITY_FTDC_EXP_GenOrderByTrade '1'
    """

    def __init__(self, exchange_id, exchange_name, exchange_property):
        """
        :param exchange_id:str, length:9 交易所代码
        :param exchange_name:str, length:31 交易所名称
        :param exchange_property: str, length:1 交易所属性
        """
        self.exchange_id = exchange_id
        self.exchange_name = exchange_name
        self.exchange_property = exchange_property


class ProductClass(object):
    """
    产品

    产品类型 product_class:
        期货:SECURITY_FTDC_PC_Futures '1'
        期权:SECURITY_FTDC_PC_Options '2'
        组合:SECURITY_FTDC_PC_Combination '3'
        即期:SECURITY_FTDC_PC_Spot '4'
        期转现:SECURITY_FTDC_PC_EFP '5'
        证券A股:SECURITY_FTDC_PC_StockA '6'
        证券B股:SECURITY_FTDC_PC_StockB '7'
        ETF:SECURITY_FTDC_PC_ETF '8'
        ETF申赎:SECURITY_FTDC_PC_ETFPurRed '9'

    持仓类型 position_type:
        净持仓: SECURITY_FTDC_PT_Net '1'
        综合持仓: SECURITY_FTDC_PT_Gross '2'

    持仓日期类型 position_date_type:
        使用历史持仓: SECURITY_FTDC_PDT_UseHistory '1'
        不使用历史持仓: SECURITY_FTDC_PDT_NoUseHistory '2'
    """

    def __init__(self, product_id, product_name, exchange_id, product_class,
                 volume_multiple, price_tick, max_market_order_volume,
                 min_market_order_volume, max_limit_order_volume, min_limit_order_volume,
                 position_type, position_date_type, etf_min_trade_volume):
        """
        :param product_id: str, length:31 产品代码
        :param product_name: str, length:21  产品名称
        :param exchange_id: str,length:9 交易所代码
        :param product_class: str,length:1 产品类型
        :param volume_multiple:int, 合约数量乘数
        :param price_tick: float,double, 最小变动价位
        :param max_market_order_volume: int, 市价单最大下单量
        :param min_market_order_volume: int, 市价单最小下单量
        :param max_limit_order_volume: int, 限价单最大下单量
        :param min_limit_order_volume: int, 限价单最小下单量
        :param position_type: str, length:1,持仓类型
        :param position_date_type: str,length:1 持仓日期类型
        :param etf_min_trade_volume: int ETF最小交易单位
        """
        self.product_id = product_id
        self.product_name = product_name
        self.exchange_id = exchange_id
        self.product_class = product_class
        self.volume_multiple = volume_multiple
        self.price_tick = price_tick
        self.max_market_order_volume = max_market_order_volume
        self.min_market_order_volume = min_market_order_volume
        self.max_limit_order_volume = max_limit_order_volume
        self.min_limit_order_volume = min_limit_order_volume
        self.position_type = position_type
        self.position_date_type = position_date_type
        self.etf_min_trade_volume = etf_min_trade_volume


class InstrumentClass(object):
    """
    合约

    产品类型 product_class:
        期货:SECURITY_FTDC_PC_Futures '1'
        期权:SECURITY_FTDC_PC_Options '2'
        组合:SECURITY_FTDC_PC_Combination '3'
        即期:SECURITY_FTDC_PC_Spot '4'
        期转现:SECURITY_FTDC_PC_EFP '5'
        证券A股:SECURITY_FTDC_PC_StockA '6'
        证券B股:SECURITY_FTDC_PC_StockB '7'
        ETF:SECURITY_FTDC_PC_ETF '8'
        ETF申赎:SECURITY_FTDC_PC_ETFPurRed '9'

    合约生命周期状态 inst_life_phase:
        未上市: SECURITY_FTDC_IP_NotStart '0'
        上市: SECURITY_FTDC_IP_Started '1'
        停牌: SECURITY_FTDC_IP_Pause '2'
        到期: SECURITY_FTDC_IP_Expired '3'

    持仓类型 position_type:
        净持仓: SECURITY_FTDC_PT_Net '1'
        综合持仓: SECURITY_FTDC_PT_Gross '2'

    持仓交易类型 pos_trade_type:
        今日新增持仓能卖出: SECURITY_FTDC_PTT_CanSelTodayPos '1'
        今日新增持仓不能卖出:SECURITY_FTDC_PTT_CannotSellTodayPos '2'
    """

    def __init__(self, instrument_id, exchange_id, instrument_name,
                 exchange_inst_id, product_id, product_class, deliver_year,
                 deliver_month, max_market_order_volume, min_market_order_volume,
                 max_limit_order_volume, min_limit_order_volume, volume_multiple,
                 price_ticket, create_date, open_date, expire_date, start_deliver_date,
                 end_deliver_date, inst_life_phase, is_trading, position_type,
                 order_withdraw, min_buy_volume, min_sell_volume, right_model_id,
                 pos_trade_type, market_id):
        """
        :param instrument_id: str, length:31, 合约代码
        :param exchange_id: str,length:9, 交易所代码
        :param instrument_name: str, length:21, 合约名称
        :param exchange_inst_id: str, length:31, 合约在交易所的代码
        :param product_id: str, length:31, 产品代码
        :param product_class: str,length:1 产品类型
        :param deliver_year: int, 交割年份
        :param deliver_month: int, 交割月
        :param max_market_order_volume: int, 市价单最大下单量
        :param min_market_order_volume: int, 市价单最小下单量
        :param max_limit_order_volume: int, 限价单最大下单量
        :param min_limit_order_volume: int, 限价单最小下单量
        :param volume_multiple: int, 合约数量乘数
        :param price_ticket: double,float 最小变动价位
        :param create_date:  str, length:9 创建日
        :param open_date: str, length:9 上市日
        :param expire_date: str, length:9 到期日
        :param start_deliver_date: str, length:9 开始交割日
        :param end_deliver_date: str,length:9 结束交割日
        :param inst_life_phase: str,length:1 合约生命周期状态
        :param is_trading: c++:int(python bool) 当前是否交易
        :param position_type:str,length:1 持仓类型
        :param order_withdraw:c++:int(python bool) 报单能否撤单
        :param min_buy_volume: int,最小买下单单位
        :param min_sell_volume: int, 最小卖下单单位
        :param right_model_id: str,length:31 股票权限模版代码
        :param pos_trade_type: str,length:1 持仓交易类型
        :param market_id: str, length:31 市场代码
        """
        self.instrument_id = instrument_id
        self.exchange_id = exchange_id
        self.instrument_name = instrument_name
        self.exchange_inst_id = exchange_inst_id
        self.product_id = product_id
        self.product_class = product_class
        self.deliver_year = deliver_year
        self.deliver_month = deliver_month
        self.max_market_order_volume = max_market_order_volume
        self.min_market_order_volume = min_market_order_volume
        self.max_limit_order_volume = max_limit_order_volume
        self.min_limit_order_volume = min_limit_order_volume
        self.volume_multiple = volume_multiple
        self.price_ticket = price_ticket
        self.create_date = create_date
        self.open_date = open_date
        self.expire_date = expire_date
        self.start_deliver_date = start_deliver_date
        self.end_deliver_date = end_deliver_date
        self.inst_life_phase = inst_life_phase
        self.is_trading = is_trading
        self.position_type = position_type
        self.order_withdraw = order_withdraw
        self.min_buy_volume = min_buy_volume
        self.min_sell_volume = min_sell_volume
        self.right_model_id = right_model_id
        self.post_trade_type = pos_trade_type
        self.market_id = market_id


class BrokerClass(object):
    """
    经纪公司
    """

    def __init__(self, broker_id, broker_abbr, broker_name, is_active):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param broker_abbr:str,length:9 经纪公司简称
        :param broker_name:str,length:81 经纪公司名称
        :param is_active: c++ int(python bool)是否活跃
        """
        self.broker_id = broker_id
        self.broker_abbr = broker_abbr
        self.broker_name = broker_name
        self.is_active = is_active


class PartBrokerClass(object):
    """
    会员编码和经纪公司编码对照表
    """

    def __init__(self, broker_id, exchange_id, participant_id, is_active):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param exchange_id: str,length:9 交易所代码
        :param participant_id: str, length:11,会员代码
        :param is_active:  c++ int(python bool) 是否活跃
        """
        self.broker_id = broker_id
        self.exchange_id = exchange_id
        self.participant_id = participant_id
        self.is_active = is_active


class InvestorClass(object):
    """
    投资者

    证件类型 identified_card_type :
        组织机构代码: SECURITY_FTDC_ICT_EID '0'
        身份证: SECURITY_FTDC_ICT_IDCard '1'
        军官证: SECURITY_FTDC_ICT_OfficerIDCard '2'
        警官证: SECURITY_FTDC_ICT_PoliceIDCard '3'
        士兵证: SECURITY_FTDC_ICT_SoldierIDCard '4'
        户口簿: SECURITY_FTDC_ICT_HouseholdRegister  '5'
        护照: SECURITY_FTDC_ICT_Passport '6'
        台胞证: SECURITY_FTDC_ICT_TaiwanCompatriotIDCard  '7'
        回乡证: SECURITY_FTDC_ICT_HomeComingCard '8'
        营业执照号: SECURITY_FTDC_ICT_LicenseNo '9'
        税务登记号: SECURITY_FTDC_ICT_TaxNo 'A'
        其他证件: SECURITY_FTDC_ICT_OtherCard 'x'

    """

    def __init__(self, investor_id, broker_id, investor_group_id, investor_name,
                 identified_card_type, identified_card_no, is_active,
                 sh_branch_id, sz_branch_id):
        """
        :param investor_id:str,length:15 投资者代码
        :param broker_id: str,length:11 经纪公司代码
        :param investor_group_id: str,length:15 投资者分组代码
        :param investor_name: str, length:81 投资者名称
        :param identified_card_type: str,length:1 证件类型
        :param identified_card_no: str,length:51 证件号码
        :param is_active: c++ int (python bool) 是否活跃
        :param sh_branch_id: str,length:21 上海营业部编号
        :param sz_branch_id: str,length:21 深圳营业部编号
        """
        self.investor_id = investor_id
        self.broker_id = broker_id
        self.investor_group_id = investor_group_id
        self.investor_name = investor_name
        self.identified_card_type = identified_card_type
        self.identified_car_no = identified_card_no
        self.is_active = is_active
        self.sh_branch_id = sh_branch_id
        self.sz_branch_id = sz_branch_id


class TradingCodeClass(object):
    """
    交易编码
    client_type:
        普通: SECURITY_FTDC_CLT_Normal '1'
        信用交易: SECURITY_FTDC_CLT_Credit '2'
        衍生品账户: SECURITY_FTDC_CLT_Derive '3'
        其他类型: SECURITY_FTDC_CLT_Other '4'
    """

    def __init__(self, investor_id, broker_id, exchange_id, client_id,
                 is_active, account_id, pbu, client_type):
        """
        :param investor_id: str,length:15 投资者代码
        :param broker_id: str,length:11 经纪公司代码
        :param exchange_id: str,length:9 交易所代码
        :param client_id: str, length:21 客户代码
        :param is_active: c++ ,int(python bool) 是否活跃
        :param account_id: str,length:15 AccountID
        :param pbu: str,length:21 交易单元号
        :param client_type: str,length:1 ClientType
        """
        self.investor_id = investor_id
        self.broker_id = broker_id
        self.exchange_id = exchange_id
        self.client_id = client_id
        self.is_active = is_active
        self.account_id = account_id
        self.pbu = pbu
        self.client_type = client_type


class SuperUserClass(object):
    """
    管理用户
    """

    def __init__(self, user_id, user_name, password, is_active):
        """
        :param user_id:str,length:16 用户代码
        :param user_name:str,length:81 用户名称
        :param password: str,length:41 密码
        :param is_active: c++: int,(python bool) 是否活跃
        """
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.is_active = is_active


class SuperUserFunctionClass(object):
    """
    管理用户功能权限
    
    功能代码 function_code: 
        强制用户登出: SECURITY_FTDC_FC_ForceUserLogout '2'
        变更管理用户口令: SECURITY_FTDC_FC_UserPasswordUpdate '3'
        变更经纪公司口令: SECURITY_FTDC_FC_BrokerPasswordUpdate '4'
        变更投资者口令: SECURITY_FTDC_FC_InvestorPasswordUpdate '5'
        报单插入: SECURITY_FTDC_FC_OrderInsert '6'
        报单操作: SECURITY_FTDC_FC_OrderAction '7'
        同步系统数据: SECURITY_FTDC_FC_SyncSystemData '8'
        同步经纪公司数据: SECURITY_FTDC_FC_SyncBrokerData '9'
        超级查询: SECURITY_FTDC_FC_SuperQuery 'B'
        报单插入: SECURITY_FTDC_FC_ParkedOrderInsert 'C'
        报单操作: SECURITY_FTDC_FC_ParkedOrderAction 'D'
        同步动态令牌: SECURITY_FTDC_FC_SyncOTP 'E'
        未知单操作: SECURITY_FTDC_FC_UnkownOrderAction 'F'
        转托管: SECURITY_FTDC_FC_DepositoryTransfer 'G'
        余券划转: SECURITY_FTDC_FC_ExcessStockTransfer 'H'
    """

    def __init__(self, user_id, function_code):
        """
        :param user_id: str,length:16 用户代码
        :param function_code: 功能代码
        """
        self.user_id = user_id
        self.function_code = function_code


class BrokerUserClass(object):
    """
    经纪公司用户
    用户类型 user_type:
        投资者: SECURITY_FTDC_UT_Investor '0'
        操作员: SECURITY_FTDC_UT_Operator '1'
        管理员: SECURITY_FTDC_UT_SuperUser '2'
    """

    def __init__(self, broker_id, user_id, user_name, user_type, is_active, is_using_otp):
        """
        :param broker_id:str,length:11 经纪公司代码
        :param user_id: str, length:16 用户代码
        :param user_name:  str, length:81 用户名称
        :param user_type: str,length:1 用户类型
        :param is_active: c++: int,(python bool) 是否活跃
        :param is_using_otp: c++: int,(python bool) 是否使用令牌
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type
        self.is_active = is_active
        self.is_using_opt = is_using_otp


class BrokerUserFunctionClass(object):
    """
    经纪公司用户功能权限

    经纪公司功能代码 broker_function_code:
        强制用户登出: SECURITY_FTDC_BFC_ForceUserLogout '1'
        变更用户口令: SECURITY_FTDC_BFC_UserPasswordUpdate '2'
        同步经纪公司数据: SECURITY_FTDC_BFC_SyncBrokerData '3'
        报单插入: SECURITY_FTDC_BFC_OrderInsert '5'
        报单操作: SECURITY_FTDC_BFC_OrderAction '6'
        全部查询: SECURITY_FTDC_BFC_AllQuery '7'
        未知单操作: SECURITY_FTDC_BFC_UnkownOrderAction '8'
        转托管: SECURITY_FTDC_BFC_DepositoryTransfer '9'
        余券划转: SECURITY_FTDC_BFC_ExcessStockTransfer 'A'
        系统功能：登入/登出/修改密码等: SECURITY_FTDC_BFC_log 'a'
        基本查询：查询基础数据，如合约，交易所等常量: SECURITY_FTDC_BFC_BaseQry 'b'
        交易查询：如查成交，委托: SECURITY_FTDC_BFC_TradeQry 'c'
        交易功能：报单，撤单: SECURITY_FTDC_BFC_Trade 'd'
        转账: SECURITY_FTDC_BFC_Virement 'e'
        查询/管理：查询会话，踢人等: SECURITY_FTDC_BFC_Session 'g'
        同步动态令牌: SECURITY_FTDC_BFC_SyncOTP 'E'
    """

    def __init__(self, broker_id, user_id, broker_function_code):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param user_id: str, length:16 用户代码
        :param broker_function_code: 经纪公司功能代码
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.broker_function_code = broker_function_code


class TradingAccountClass(object):
    """
    资金账户
        账户类型 account_type:
        普通账户: SECURITY_FTDC_AcT_Normal '1'
        信用账户: SECURITY_FTDC_AcT_Credit '2'
        衍生品账户: SECURITY_FTDC_AcT_Derive '3'
        其他类型: SECURITY_FTDC_AcT_Other '4'
    """

    def __init__(self, broker_id, account_id, pre_mortgage,
                 pre_credit, pre_deposit, pre_balance, pre_margin,
                 interest_base, interest, deposit, withdraw, frozen_margin,
                 frozen_cash, frozen_commission, curr_margin, cash_in, commission,
                 balance, available, withdraw_quota, reserve, trading_day, credit,
                 mortgage, exchange_margin, delivery_margin, exchange_delivery_margin,
                 frozen_transfer_fee, frozen_stamp_tax, transfer_fee, stamp_tax,
                 conversion_amount, credit_amount, stock_value, bond_repurchase_amount,
                 reverse_repurchase_amount, currency_code, account_type, margin_trade_amount,
                 short_sell_amount, margin_trade_profit, short_sell_profit, ss_stock_value,
                 credit_ratio):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param account_id: str,length:15 投资者帐号
        :param pre_mortgage: double 上次质押金额
        :param pre_credit: double 上次信用额度
        :param pre_deposit: double 上次存款额
        :param pre_balance: double 上次结算准备金
        :param pre_margin: double 上次占用的保证金
        :param interest_base: double 利息基数
        :param interest: double 利息收入
        :param deposit: double 入金金额
        :param withdraw: double 出金金额
        :param frozen_margin: double 冻结的保证金
        :param frozen_cash: double 冻结的资金
        :param frozen_commission: double 冻结的手续费
        :param curr_margin: double  当前保证金总额
        :param cash_in: double 资金差额
        :param commission: double 手续费
        :param balance: double 结算准备金
        :param available: double 现金
        :param withdraw_quota: double 可取资金
        :param reserve: double 基本准备金
        :param trading_day:str,length:9 交易日
        :param credit: double 保证金可用余额
        :param mortgage: double 质押金额
        :param exchange_margin: double 交易所保证金
        :param delivery_margin: double 投资者交割保证金
        :param exchange_delivery_margin: double 交易所交割保证金
        :param frozen_transfer_fee: double 冻结的过户费
        :param frozen_stamp_tax: double 冻结的印花税
        :param transfer_fee: double 过户费
        :param stamp_tax: double 印花税
        :param conversion_amount: double 折算金额
        :param credit_amount: double 授信额度
        :param stock_value: double 证券总价值
        :param bond_repurchase_amount: double 国债回购占用资金
        :param reverse_repurchase_amount: double 国债逆回购占用资金
        :param currency_code:str,length:4 币种
        :param account_type: str,length:1 账户类型
        :param margin_trade_amount: double 融资买入金额
        :param short_sell_amount: double 融券卖出金额
        :param margin_trade_profit: double 融资持仓盈亏
        :param short_sell_profit: double 融券持仓盈亏
        :param ss_stock_value: double 融券总市值
        :param credit_ratio: double 维持担保比例
        """
        self.broker_id = broker_id
        self.account_id = account_id
        self.pre_mortgage = pre_mortgage
        self.pre_credit = pre_credit
        self.pre_deposit = pre_deposit
        self.pre_balance = pre_balance
        self.pre_margin = pre_margin
        self.interest_base = interest_base
        self.interest = interest
        self.deposit = deposit
        self.withdraw = withdraw
        self.frozen_margin = frozen_margin
        self.frozen_cash = frozen_cash
        self.frozen_commission = frozen_commission
        self.curr_margin = curr_margin
        self.cash_in = cash_in
        self.commission = commission
        self.balance = balance
        self.available = available
        self.withdraw_quota = withdraw_quota
        self.reserve = reserve
        self.trading_day = trading_day
        self.credit = credit
        self.mortgage = mortgage
        self.exchange_margin = exchange_margin
        self.delivery_margin = delivery_margin
        self.exchange_delivery_margin = exchange_delivery_margin
        self.frozen_transfer_fee = frozen_transfer_fee
        self.frozen_stamp_tax = frozen_stamp_tax
        self.transfer_fee = transfer_fee
        self.stamp_tax = stamp_tax
        self.conversion_amount = conversion_amount
        self.credit_amount = credit_amount
        self.stock_value = stock_value
        self.bond_repurchase_amount = bond_repurchase_amount
        self.reverse_repurchase_amount = reverse_repurchase_amount
        self.currency_code = currency_code
        self.account_type = account_type
        self.margin_trade_amount = margin_trade_amount
        self.short_sell_amount = short_sell_amount
        self.margin_trade_profit = margin_trade_profit
        self.short_sell_profit = short_sell_profit
        self.ss_stock_value = ss_stock_value
        self.credit_ratio = credit_ratio


class LoginForbiddenUserClass(object):
    """
    禁止登录用户
    """

    def __init__(self, broker_id, user_id):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param user_id: str, length:16 用户代码
        """
        self.broker_id = broker_id
        self.user_id = user_id


class MarketDataBaseClass(object):
    """
    行情基础属性
    """

    def __init__(self, trading_day, pre_settlement_price, pre_close_price,
                 pre_open_interest, pre_delta):
        """
        :param trading_day: str, length:9 交易日
        :param pre_settlement_price:  double 上次结算价
        :param pre_close_price: double 昨收盘
        :param pre_open_interest: double 昨持仓量
        :param pre_delta: double 昨虚实度
        """
        self.trading_day = trading_day
        self.pre_settlement_price = pre_settlement_price
        self.pre_close_price = pre_close_price
        self.pre_open_interest = pre_open_interest
        self.pre_delta = pre_delta


class MarketDataStaticClass(object):
    """
    行情静态属性
    """

    def __init__(self, open_price, highest_price, lowest_price, close_price,
                 upper_limit_price, lower_limit_price, settlement_price, curr_delta):
        """
        :param open_price: double 今开盘
        :param highest_price: double 最高价
        :param lowest_price: double 最低价
        :param close_price: double 今收盘
        :param upper_limit_price: double 涨停板价
        :param lower_limit_price: double 跌停板价
        :param settlement_price:  double 本次结算价
        :param curr_delta: double 今虚实度
        """
        self.open_price = open_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.close_price = close_price
        self.upper_limit_price = upper_limit_price
        self.lower_limit_price = lower_limit_price
        self.settlement_price = settlement_price
        self.curr_delta = curr_delta


class MarketDataLastMatchClass(object):
    """
    行情最新成交属性
    """

    def __init__(self, last_price, volume, turnover, open_interest):
        """
        :param last_price: double 最新价
        :param volume: int 数量
        :param turnover: double 成交金额
        :param open_interest: double 持仓量
        """
        self.last_price = last_price
        self.volume = volume
        self.turnover = turnover
        self.open_interest = open_interest


class MarketDataBestPriceClass(object):
    """
    行情最优价属性
    """

    def __init__(self, bid_price1, bid_volume1, ask_price1, ask_volume1):
        """
        :param bid_price1: double 申买价一
        :param bid_volume1: int 申买量一
        :param ask_price1: double 申卖价一
        :param ask_volume1: int 申卖量一
        """
        self.bid_price1 = bid_price1
        self.bid_volume1 = bid_volume1
        self.ask_price1 = ask_price1
        self.ask_volume1 = ask_volume1


class MarketDataBid23Class(object):
    """
    行情申买二、三属性
    """

    def __init__(self, bid_price2, bid_volume2, bid_price3, bid_volume3):
        """
        :param bid_price2: double 申买价二
        :param bid_volume2: int 申买量二
        :param bid_price3: double 申买价三
        :param bid_volume3: int 申买量三
        """
        self.bid_price2 = bid_price2
        self.bid_volume2 = bid_volume2
        self.bid_price3 = bid_price3
        self.bid_volume3 = bid_volume3


class MarketDataAsk23Class(object):
    """
    行情申卖二、三属性
    """

    def __init__(self, ask_price2, ask_volume2, ask_price3, ask_volume3):
        """
        :param ask_price2: double 申卖价二
        :param ask_volume2: int 申卖量二
        :param ask_price3:  double 申卖价三
        :param ask_volume3: int 申卖量三
        """
        self.ask_price2 = ask_price2
        self.ask_volume2 = ask_volume2
        self.ask_price3 = ask_price3
        self.ask_volume3 = ask_volume3


class MarketDataBid45Class(object):
    """
    行情申买四、五属性
    """

    def __init__(self, bid_price4, bid_volume4, bid_price5, bid_volume5):
        """
        :param bid_price4: double 申买价四
        :param bid_volume4: int 申买量四
        :param bid_price5: double 申买价五
        :param bid_volume5: int 申买量五
        """
        self.bid_price4 = bid_price4
        self.bid_volume4 = bid_volume4
        self.bid_price5 = bid_price5
        self.bid_volume5 = bid_volume5


class MarketDataAsk45Class(object):
    """
    行情申卖四、五属性
    """

    def __init__(self, ask_price4, ask_volume4, ask_price5, ask_volume5):
        """
        :param ask_price4: double 申卖价四
        :param ask_volume4: int 申卖量四
        :param ask_price5:  double 申卖价五
        :param ask_volume5: int 申卖量五
        """
        self.ask_price4 = ask_price4
        self.ask_volume4 = ask_volume4
        self.ask_price5 = ask_price5
        self.ask_volume5 = ask_volume5


class MarketDataUpdateTimeClass(object):
    """
    行情更新时间属性
    """

    def __init__(self, instrument_id, update_time, update_millisec, action_day):
        """
        :param instrument_id: str,length:31 合约代码
        :param update_time: str,length:9 最后修改时间
        :param update_millisec: int,  最后修改毫秒
        :param action_day: str,length:9 业务日期
        """
        self.instrument_id = instrument_id
        self.update_time = update_time
        self.update_millisec = update_millisec
        self.action_day = action_day


class MarketDataAveragePriceClass(object):
    """
    成交均价
    """

    def __init__(self, average_price):
        """
        :param average_price:  double, 当日均价
        """
        self.average_price = average_price


class MarketDataExchangeClass(object):
    """
    行情交易所代码属性
    """

    def __init__(self, exchange_id):
        """
        :param exchange_id: str, length:9 交易所代码
        """
        self.exchange_id = exchange_id


class DisseminationClass(object):
    """
    信息分发
    """

    def __init__(self, sequence_series, sequence_no):
        """
        :param sequence_series:int ,-32768~+32767 序列系列号
        :param sequence_no: int 序列号
        """
        self.sequence_series = sequence_series
        self.sequence_no = sequence_no


class InputFundTransferClass(object):
    """
    资金转账输入

    资金账户
        账户类型 account_type:
        普通账户: SECURITY_FTDC_AcT_Normal '1'
        信用账户: SECURITY_FTDC_AcT_Credit '2'
        衍生品账户: SECURITY_FTDC_AcT_Derive '3'
        其他类型: SECURITY_FTDC_AcT_Other '4'
    """

    def __init__(self, broker_id, investor_id, account_id, password,
                 user_id, trade_amount, digest, account_type):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str, length:15 投资者代码
        :param account_id: str, length:15 投资者资金帐号
        :param password: str,length:41 资金帐户密码
        :param user_id: str,length:16 用户代码
        :param trade_amount:  double 交易金额
        :param digest: str,length:36 摘要
        :param account_type: str,length:1 资金账户
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.account_id = account_id
        self.password = password
        self.user_id = user_id
        self.trade_amount = trade_amount
        self.digest = digest
        self.account_type = account_type


class FundTransferClass(object):
    """
    资金转账

    出入金方向 fund_direction:
        入金: SECURITY_FTDC_FD_In '1'
        出金: SECURITY_FTDC_FD_Out '2'
    """

    def __init__(self, broker_id, investor_id, account_id, password,
                 user_id, trade_amount, digest, session_id, liber_serial,
                 plate_serial, transfer_serial, trading_day, trade_time,
                 fund_direction, error_id, error_msg):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param account_id: str, length:15 投资者资金帐号
        :param password: str,length:41 资金帐户密码
        :param user_id: str,length:16 用户代码
        :param trade_amount: double 交易金额
        :param digest: str,length:36 摘要
        :param session_id: int 会话编号
        :param liber_serial: int Liber核心流水号
        :param plate_serial:int  转账平台流水号
        :param transfer_serial: str,length:13 第三方流水号
        :param trading_day: str,length:9 交易日
        :param trade_time: str,length:9  转账时间
        :param fund_direction: str,length:1 出入金方向
        :param error_id: 错误代码
        :param error_msg: 错误信息
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.account_id = account_id
        self.password = password
        self.user_id = user_id
        self.trade_amount = trade_amount
        self.digest = digest
        self.session_id = session_id
        self.liber_serial = liber_serial
        self.plate_serial = plate_serial
        self.transfer_serial = transfer_serial
        self.trading_day = trading_day
        self.trade_time = trade_time
        self.fund_direction = fund_direction
        self.error_id = error_id
        self.error_msg = error_msg


class QryFundTransferSerialClass(object):
    """
    资金转账查询请求

    资金账户
        账户类型 account_type:
        普通账户: SECURITY_FTDC_AcT_Normal '1'
        信用账户: SECURITY_FTDC_AcT_Credit '2'
        衍生品账户: SECURITY_FTDC_AcT_Derive '3'
        其他类型: SECURITY_FTDC_AcT_Other '4'
    """

    def __init__(self, broker_id, account_id, account_type):
        """
        :param broker_id:str,length:11 经纪公司代码
        :param account_id:str, length:15 投资者资金帐号
        :param account_type: 账户类型
        """
        self.broker_id = broker_id
        self.account_id = account_id
        self.account_type = account_type


class SpecificInstrumentClass(object):
    """
    指定的合约
    """

    def __init__(self, instrument_id, exchange_id):
        """
        :param instrument_id:  str, length:31, 合约代码
        :param exchange_id: str, length:9 交易所代码
        """
        self.instrument_id = instrument_id
        self.exchange_id = exchange_id


class SpecificExchangeClass(object):
    """
    指定的交易所
    """

    def __init__(self, exchange_id):
        """
        :param exchange_id: str, length:9 交易所代码
        """
        self.exchange_id = exchange_id


class DepthMarketDataClass(object):
    """
    深度行情
    """

    def __init__(self, trading_day, instrument_id, exchange_id, exchange_inst_id,
                 last_price, pre_settlement_price, pre_close_price, pre_open_interest,
                 open_price, highest_price, lowest_price, volume, turnover, open_interest,
                 close_price, settlement_price, upper_limit_price, lower_limit_price,
                 pre_delta, curr_delta, update_time, update_millisec, bid_price1, bid_volume1,
                 ask_price1, ask_volume1, bid_price2, bid_volume2, ask_price2, ask_volume2,
                 bid_price3, bid_volume3, ask_price3, ask_volume3, bid_price4, bid_volume4, ask_price4,
                 ask_volume4, bid_price5, bid_volume5, ask_price5, ask_volume5, average_price, action_day):
        """
        :param trading_day: str,length:9 交易日
        :param instrument_id: str, length:31,  合约代码
        :param exchange_id: str, length:9  交易所代码
        :param exchange_inst_id:  str, length:31, 合约在交易所的代码
        :param last_price: double 最新价
        :param pre_settlement_price: double 上次结算价
        :param pre_close_price: double 昨收盘
        :param pre_open_interest: double 昨持仓量
        :param open_price:  double 今开盘
        :param highest_price: double 最高价
        :param lowest_price: double 最低价
        :param volume: int 数量
        :param turnover: double 成交金额
        :param open_interest: int 持仓量
        :param close_price:double 今收盘
        :param settlement_price:double  本次结算价
        :param upper_limit_price: double 涨停板价
        :param lower_limit_price: double 跌停板价
        :param pre_delta: double 昨虚实度
        :param curr_delta: double 今虚实度
        :param update_time: str,length:9 最后修改时间
        :param update_millisec:  int 最后修改毫秒
        :param bid_price1: double  申买价一
        :param bid_volume1: int 申买量一
        :param ask_price1: double 申卖价一
        :param ask_volume1: int 申卖量一
        :param bid_price2: double 申买价二
        :param bid_volume2: int 申买量二
        :param ask_price2: double 申卖价二
        :param ask_volume2: int 申卖量二
        :param bid_price3: double 申买价三
        :param bid_volume3: int 申买量三
        :param ask_price3: double 申卖价三
        :param ask_volume3: int 申卖量三
        :param bid_price4: double 申买价四
        :param bid_volume4: int 申买量四
        :param ask_price4: double 申卖价四
        :param ask_volume4: int 申卖量四
        :param bid_price5: double 申买价五
        :param bid_volume5: int 申买量五
        :param ask_price5: double 申卖价五
        :param ask_volume5: int 申卖量五
        :param average_price: double 当日均价
        :param action_day: str,length:9  业务日期
        """
        self.trading_day = trading_day
        self.instrument_id = instrument_id
        self.exchange_id = exchange_id
        self.exchange_inst_id = exchange_inst_id
        self.last_price = last_price
        self.pre_settlement_price = pre_settlement_price
        self.pre_close_price = pre_close_price
        self.pre_open_interest = pre_open_interest
        self.open_price = open_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.volume = volume
        self.turnover = turnover
        self.open_interest = open_interest
        self.close_price = close_price
        self.settlement_price = settlement_price
        self.upper_limit_price = upper_limit_price
        self.lower_limit_price = lower_limit_price
        self.pre_delta = pre_delta
        self.curr_delta = curr_delta
        self.update_time = update_time
        self.update_millisec = update_millisec
        self.bid_price1 = bid_price1
        self.bid_volume1 = bid_volume1
        self.ask_price1 = ask_price1
        self.ask_volume1 = ask_volume1
        self.bid_price2 = bid_price2
        self.bid_volume2 = bid_volume2
        self.ask_price2 = ask_price2
        self.ask_volume2 = ask_volume2
        self.bid_price3 = bid_price3
        self.bid_volume3 = bid_volume3
        self.ask_price3 = ask_price3
        self.ask_volume3 = ask_volume3
        self.bid_price4 = bid_price4
        self.bid_volume4 = bid_volume4
        self.ask_price4 = ask_price4
        self.ask_volume4 = ask_volume4
        self.bid_price5 = bid_price5
        self.bid_volume5 = bid_volume5
        self.ask_price5 = ask_price5
        self.ask_volume5 = ask_volume5
        self.average_price = average_price
        self.action_day = action_day


class InstrumentTradingRightClass(object):
    """
    投资者合约交易权限

    投资者范围 investor_range:
        所有: SECURITY_FTDC_IR_All '1'
        投资者组: SECURITY_FTDC_IR_Group '2'
        单一投资者: SECURITY_FTDC_IR_Single '3'

    买卖 direction:
        买: SECURITY_FTDC_D_Buy '0'
        卖: SECURITY_FTDC_D_Sell '1'
        ETF申购: SECURITY_FTDC_D_ETFPur '2'
        ETF赎回: SECURITY_FTDC_D_ETFRed '3'
        现金替代，只用作回报: SECURITY_FTDC_D_CashIn '4'
        债券入库: SECURITY_FTDC_D_PledgeBondIn '5'
        债券出库: SECURITY_FTDC_D_PledgeBondOut '6'
        配股: SECURITY_FTDC_D_Rationed '7'
        转托管: SECURITY_FTDC_D_DepositoryTransfer '8'
        信用账户配股: SECURITY_FTDC_D_CreditRationed '9'
        担保品买入: SECURITY_FTDC_D_BuyCollateral 'A'
        担保品卖出: SECURITY_FTDC_D_SellCollateral 'B'
        担保品转入: SECURITY_FTDC_D_CollateralTransferIn 'C'
        担保品转出: SECURITY_FTDC_D_CollateralTransferOut 'D'
        融资买入: SECURITY_FTDC_D_MarginTrade 'E'
        融券卖出: SECURITY_FTDC_D_ShortSell 'F'
        卖券还款: SECURITY_FTDC_D_RepayMargin 'G'
        买券还券: SECURITY_FTDC_D_RepayStock 'H'
        直接还款: SECURITY_FTDC_D_DirectRepayMargin 'I'
        直接还券: SECURITY_FTDC_D_DirectRepayStock 'J'
        余券划转: SECURITY_FTDC_D_ExcessStockTransfer 'K'

    交易权限 trading_right:
        可以交易: SECURITY_FTDC_TR_Allow '0'
        不能交易: SECURITY_FTDC_TR_Forbidden '2'

    股票权限分类 instrument_range:
        所有: SECURITY_FTDC_INR_All '1'
        产品: SECURITY_FTDC_INR_Product '2'
        股票权限模版: SECURITY_FTDC_INR_Model '3'
        股票: SECURITY_FTDC_INR_Stock '4'
        市场: SECURITY_FTDC_INR_Market '5'
    """

    def __init__(self, instrument_id, investor_range, broker_id, investor_id,
                 direction, trading_right, exchange_id, instrument_range):
        """
        :param instrument_id:str, length:31 合约代码
        :param investor_range: str,length:1 投资者范围
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param direction: str,length:1 买卖
        :param trading_right: str,length:1 交易权限
        :param exchange_id: str, length:9 交易所代码
        :param instrument_range: str,length:1 股票权限分类
        """
        self.instrument_id = instrument_id
        self.investor_range = investor_range
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.direction = direction
        self.trading_right = trading_right
        self.exchange_id = exchange_id
        self.instrument_range = instrument_range


class InvestorPositionDetailClass(object):
    """
    投资者持仓明细

    投机套保标志 hedge_flag:
        投机: SECURITY_FTDC_HF_Speculation '1'
        套保: SECURITY_FTDC_HF_Hedge '3'

    买卖 direction:
        买: SECURITY_FTDC_D_Buy '0'
        卖: SECURITY_FTDC_D_Sell '1'
        ETF申购: SECURITY_FTDC_D_ETFPur '2'
        ETF赎回: SECURITY_FTDC_D_ETFRed '3'
        现金替代，只用作回报: SECURITY_FTDC_D_CashIn '4'
        债券入库: SECURITY_FTDC_D_PledgeBondIn '5'
        债券出库: SECURITY_FTDC_D_PledgeBondOut '6'
        配股: SECURITY_FTDC_D_Rationed '7'
        转托管: SECURITY_FTDC_D_DepositoryTransfer '8'
        信用账户配股: SECURITY_FTDC_D_CreditRationed '9'
        担保品买入: SECURITY_FTDC_D_BuyCollateral 'A'
        担保品卖出: SECURITY_FTDC_D_SellCollateral 'B'
        担保品转入: SECURITY_FTDC_D_CollateralTransferIn 'C'
        担保品转出: SECURITY_FTDC_D_CollateralTransferOut 'D'
        融资买入: SECURITY_FTDC_D_MarginTrade 'E'
        融券卖出: SECURITY_FTDC_D_ShortSell 'F'
        卖券还款: SECURITY_FTDC_D_RepayMargin 'G'
        买券还券: SECURITY_FTDC_D_RepayStock 'H'
        直接还款: SECURITY_FTDC_D_DirectRepayMargin 'I'
        直接还券: SECURITY_FTDC_D_DirectRepayStock 'J'
        余券划转: SECURITY_FTDC_D_ExcessStockTransfer 'K'

    成交类型 trade_type:
        普通成交: SECURITY_FTDC_TRDT_Common '0'
        期权执行: SECURITY_FTDC_TRDT_OptionsExecution '1'
        OTC成交: SECURITY_FTDC_TRDT_OTC '2'
        期转现衍生成交: SECURITY_FTDC_TRDT_EFPDerived '3'
        组合衍生成交: SECURITY_FTDC_TRDT_CombinationDerived '4'
        ETF申购: SECURITY_FTDC_TRDT_EFTPurchase '5'
        ETF赎回: SECURITY_FTDC_TRDT_EFTRedem '6'
    """

    def __init__(self, instrument_id, broker_id, investor_id, hedge_flag,
                 direction, open_date, trade_id, volume, open_price, trading_day, trade_type,
                 exchange_id, margin, exch_margin, last_settlement_price, settlement_price,
                 close_volume, close_amount, transfer_fee, stamp_tax, commission, account_id,
                 pledge_in_position, pledge_in_frozen_position, repurchase_position,
                 amount):
        """
        :param instrument_id:  str, length:31, 合约代码
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param hedge_flag: str,length:1 投机套保标志
        :param direction: str,length:! 买卖
        :param open_date: str, length:9  开仓日期
        :param trade_id: str,length:21 成交编号
        :param volume: int  数量
        :param open_price: double 开仓价
        :param trading_day: str, length:9 交易日
        :param trade_type: str,length:1 成交类型
        :param exchange_id: str, length:9 交易所代码
        :param margin: double 投资者保证金
        :param exch_margin: double 交易所保证金
        :param last_settlement_price: double 昨结算价
        :param settlement_price: double 结算价
        :param close_volume: int  平仓量
        :param close_amount: double 平仓金额
        :param transfer_fee: double 过户费
        :param stamp_tax: double 印花税
        :param commission: double 手续费
        :param account_id:  str,length:15 AccountID
        :param pledge_in_position: int 质押入库数量
        :param pledge_in_frozen_position: int 质押入库冻结数量
        :param repurchase_position: int 正回购使用的标准券数量
        :param amount: double 融资融券金额
        """
        self.instrument_id = instrument_id
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.hedge_flag = hedge_flag
        self.direction = direction
        self.open_date = open_date
        self.trade_id = trade_id
        self.volume = volume
        self.open_price = open_price
        self.trading_day = trading_day
        self.trade_type = trade_type
        self.exchange_id = exchange_id
        self.margin = margin
        self.exch_margin = exch_margin
        self.last_settlement_price = last_settlement_price
        self.settlement_price = settlement_price
        self.close_volume = close_volume
        self.close_amount = close_amount
        self.transfer_fee = transfer_fee
        self.stamp_tax = stamp_tax
        self.commission = commission
        self.account_id = account_id
        self.pledge_in_position = pledge_in_position
        self.pledge_in_frozen_position = pledge_in_frozen_position
        self.repurchase_position = repurchase_position
        self.amount = amount


class BondInterestClass(object):
    """
    债券利息
    """

    def __init__(self, trading_day, exchange_id, instrument_id, interest):
        """
        :param trading_day:  str, length:9 交易日
        :param exchange_id: str, length:9 交易所代码
        :param instrument_id: str, length:31 合约代码
        :param interest: double 利息
        """
        self.trading_day = trading_day
        self.exchange_id = exchange_id
        self.instrument_id = instrument_id
        self.interest = interest


class MarketRationInfoClass(object):
    """
    市值配售信息
    """

    def __init__(self, broker_id, investor_id, exchange_id, ration_volume):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param exchange_id:  str, length:9 交易所代码
        :param ration_volume: int 可配售手数
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.exchange_id = exchange_id
        self.ration_volume = ration_volume


class InstrumentCommissionRateClass(object):
    """
    合约手续费率

    投资者范围 investor_range:
        所有: SECURITY_FTDC_IR_All '1'
        投资者组: SECURITY_FTDC_IR_Group '2'
        单一投资者: SECURITY_FTDC_IR_Single '3'

    买卖 direction:
        买: SECURITY_FTDC_D_Buy '0'
        卖: SECURITY_FTDC_D_Sell '1'
        ETF申购: SECURITY_FTDC_D_ETFPur '2'
        ETF赎回: SECURITY_FTDC_D_ETFRed '3'
        现金替代，只用作回报: SECURITY_FTDC_D_CashIn '4'
        债券入库: SECURITY_FTDC_D_PledgeBondIn '5'
        债券出库: SECURITY_FTDC_D_PledgeBondOut '6'
        配股: SECURITY_FTDC_D_Rationed '7'
        转托管: SECURITY_FTDC_D_DepositoryTransfer '8'
        信用账户配股: SECURITY_FTDC_D_CreditRationed '9'
        担保品买入: SECURITY_FTDC_D_BuyCollateral 'A'
        担保品卖出: SECURITY_FTDC_D_SellCollateral 'B'
        担保品转入: SECURITY_FTDC_D_CollateralTransferIn 'C'
        担保品转出: SECURITY_FTDC_D_CollateralTransferOut 'D'
        融资买入: SECURITY_FTDC_D_MarginTrade 'E'
        融券卖出: SECURITY_FTDC_D_ShortSell 'F'
        卖券还款: SECURITY_FTDC_D_RepayMargin 'G'
        买券还券: SECURITY_FTDC_D_RepayStock 'H'
        直接还款: SECURITY_FTDC_D_DirectRepayMargin 'I'
        直接还券: SECURITY_FTDC_D_DirectRepayStock 'J'
        余券划转: SECURITY_FTDC_D_ExcessStockTransfer 'K'
    """

    def __init__(self, exchange_id, instrument_id, investor_range, broker_id, investor_id, direction,
                 stamp_tax_rate_by_money, stamp_tax_rate_by_volume, transfer_fee_rate_by_money,
                 transfer_fee_rate_by_volume, trade_fee_by_money, trade_fee_by_volume, margin_by_money,
                 min_trade_fee):
        """
        :param exchange_id:  str, length:9 交易所代码
        :param instrument_id: str, length:31 合约代码
        :param investor_range: str,length:1 投资者范围
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param direction: str,length:1 买卖方向
        :param stamp_tax_rate_by_money: double 印花税率
        :param stamp_tax_rate_by_volume: double 印花税率(按手数)
        :param transfer_fee_rate_by_money: double 过户费率
        :param transfer_fee_rate_by_volume: double 过户费率(按手数)
        :param trade_fee_by_money: double 交易费
        :param trade_fee_by_volume: double 交易费(按手数)
        :param margin_by_money: double 交易附加费率
        :param min_trade_fee: double 最小过户费
        """
        self.exchange_id = exchange_id
        self.instrument_id = instrument_id
        self.investor_range = investor_range
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.direction = direction
        self.stamp_tax_rate_by_money = stamp_tax_rate_by_money
        self.stamp_tax_rate_by_volume = stamp_tax_rate_by_volume
        self.transfer_fee_rate_by_money = transfer_fee_rate_by_money
        self.transfer_fee_rate_by_volume = transfer_fee_rate_by_volume
        self.trade_fee_by_money = trade_fee_by_money
        self.trade_fee_by_volume = trade_fee_by_volume
        self.margin_by_money = margin_by_money
        self.min_trade_fee = min_trade_fee


class ExcessStockInfoClass(object):
    """
    余券信息
    """

    def __init__(self, broker_id, investor_id, exchange_id, instrument_id,
                 excess_volume, excess_frozen_volume):
        """
        :param broker_id:str,length:11  经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param exchange_id: str, length:9 交易所代码
        :param instrument_id: str, length:31 合约代码
        :param excess_volume: int 余券数量
        :param excess_frozen_volume:  int 余券冻结数量
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.exchange_id = exchange_id
        self.instrument_id = instrument_id
        self.excess_volume = excess_volume
        self.excess_frozen_volume = excess_frozen_volume


class TraderOfferClass(object):
    """
    交易所交易员报盘机

    交易所交易员连接状态 trader_connect_status:
        没有任何连接: SECURITY_FTDC_TCS_NotConnected '1'
        已经连接: SECURITY_FTDC_TCS_Connected '2'
        已经发出合约查询请求: SECURITY_FTDC_TCS_QryInstrumentSent '3'
        订阅私有流: SECURITY_FTDC_TCS_SubPrivateFlow '4'
    """

    def __init__(self, exchange_id, branch_pbu, participant_id, password,
                 install_id, order_local_id, trader_connect_status, connect_request_date,
                 connect_request_time, last_report_date, last_report_time, connect_date,
                 connect_time, start_date, start_time, trading_day, broker_id):
        """
        :param exchange_id:   str, length:9 交易所代码
        :param branch_pbu: str,length:21 交易所交易员代码
        :param participant_id: str,length:11 会员代码
        :param password: str,length:41 密码
        :param install_id: int 安装编号
        :param order_local_id: str,length:13 本地报单编号
        :param trader_connect_status: str,length:1 交易所交易员连接状态
        :param connect_request_date: str,length:9 发出连接请求的日期
        :param connect_request_time: str,length:9 发出连接请求的时间
        :param last_report_date: str,length:9  上次报告日期
        :param last_report_time: str,length:9  上次报告时间
        :param connect_date:  str,length:9 完成连接日期
        :param connect_time: str,length:9  完成连接时间
        :param start_date:  str,length:9 启动日期
        :param start_time: str,length:9 启动时间
        :param trading_day: str,length:9  交易日
        :param broker_id: str,length:11 经纪公司代码
        """
        self.exchange_id = exchange_id
        self.branch_pbu = branch_pbu
        self.participant_id = participant_id
        self.password = password
        self.install_id = install_id
        self.order_local_id = order_local_id
        self.trader_connect_status = trader_connect_status
        self.connect_request_date = connect_request_date
        self.connect_request_time = connect_request_time
        self.last_report_date = last_report_date
        self.last_report_time = last_report_time
        self.connect_date = connect_date
        self.connect_time = connect_time
        self.start_date = start_date
        self.start_time = start_time
        self.trading_day = trading_day
        self.broker_id = broker_id


class MDTraderOfferClass(TraderOfferClass):
    """
    交易所行情报盘机
    """


class FrontStatusClass(object):
    """
    前置状态
    """

    def __init__(self, front_id, last_report_date, last_report_time, is_active):
        """
        :param front_id: int 前置编号
        :param last_report_date: str,length:9 上次报告日期
        :param last_report_time: str,length:9  上次报告时间
        :param is_active: c++:int, python(bool) 是否活跃
        """
        self.front_id = front_id
        self.last_report_date = last_report_date
        self.last_report_time = last_report_time
        self.is_active = is_active


class UserSessionClass(object):
    """
    用户会话
    """

    def __init__(self, front_id, session_id, broker_id, user_id,
                 login_date, login_time, ip_address, user_product_info,
                 interface_product_info, protocol_info, mac_address):
        """
        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param broker_id: str,length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param login_date: str,length:9 登录日期
        :param login_time: str,length:9 登录时间
        :param ip_address: str,length:16 IP地址
        :param user_product_info: str,length:11 用户端产品信息
        :param interface_product_info: str,length:11 接口端产品信息
        :param protocol_info: str,length:11 协议信息
        :param mac_address: str,length:21 Mac地址
        """
        self.front_id = front_id
        self.session_id = session_id
        self.broker_id = broker_id
        self.user_id = user_id
        self.login_date = login_date
        self.login_time = login_time
        self.ip_address = ip_address
        self.user_product_info = user_product_info
        self.interface_product_info = interface_product_info
        self.protocol_info = protocol_info
        self.mac_address = mac_address


class SyncDepositClass(object):
    """
    出入金同步
    """

    def __init__(self, deposit_seq_no, broker_id, investor_id, deposit,
                 is_force, account_id):
        """
        :param deposit_seq_no: str,length:15 出入金流水号
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param deposit: double 入金金额
        :param is_force:  c++ int, python bool 是否强制进行
        :param account_id: str,length:15 账户代码
        """
        self.deposit_seq_no = deposit_seq_no
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.deposit = deposit
        self.is_force = is_force
        self.account_id = account_id


class QryExchangeClass(object):
    """
    查询交易所
    """

    def __init__(self, exchange_id):
        """
        :param exchange_id: str,length:9 交易所代码
        """
        self.exchange_id = exchange_id


class QryProductClass(object):
    """
    查询产品
    """

    def __init__(self, product_id):
        """

        :param product_id: str, length:31 产品代码
        """
        self.product_id = product_id


class QryInstrumentClass(object):
    """
    查询合约
    """

    def __init__(self, instrument_id, exchange_id,
                 exchange_inst_id, product_id):
        """

        :param instrument_id: str, length:31, 合约代码
        :param exchange_id: str, length:9 交易所代码
        :param exchange_inst_id: str, length:31, 合约在交易所的代码
        :param product_id: str, length:31 产品代码
        """
        self.instrument_id = instrument_id
        self.exchange_id = exchange_id
        self.exchange_inst_id = exchange_inst_id
        self.product_id = product_id


class QryBrokerClass(object):
    """
    查询经纪公司
    """

    def __init__(self, broker_id):
        """

        :param broker_id: str,length:11 经纪公司代码
        """
        self.broker_id = broker_id


class QryPartBrokerClass(object):
    """
    查询经纪公司会员代码
    """

    def __init__(self, exchange_id, broker_id, participant_id):
        """

        :param exchange_id: str, length:9 交易所代码
        :param broker_id: str,length:11 经纪公司代码
        :param participant_id:  str, length:11 会员代码
        """
        self.exchange_id = exchange_id
        self.broker_id = broker_id
        self.participant_id = participant_id


class QryInvestorClass(object):
    """
    查询投资者
    """

    def __init__(self, broker_id, investor_id):
        """

        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id


class QryTradingCodeClass(object):
    """
    查询交易编码
    """

    def __init__(self, broker_id, investor_id,
                 exchange_id, client_id):
        """

        :param broker_id: str,length:11  经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param exchange_id: str,length:9 交易所代码
        :param client_id: str, length:21 客户代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.exchange_id = exchange_id
        self.client_id = client_id


class QrySuperUserClass(object):
    """
    查询管理用户
    """

    def __init__(self, user_id):
        """
        :param user_id: str,length:16 用户代码
        """
        self.user_id = user_id


class QrySuperUserFunctionClass(QrySuperUserClass):
    """
    查询管理用户功能权限
    """


class QryBrokerUserClass(object):
    """
    查询经纪公司用户
    """

    def __init__(self, broker_id, user_id):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        """
        self.broker_id = broker_id
        self.user_id = user_id


class QryBrokerUserFunctionClass(QryBrokerUserClass):
    """
    查询经纪公司用户权限
    """


class QryLoginForbiddenUserClass(QryBrokerUserClass):
    """
    查询禁止登录用户
    """


class QryTradingAccountClass(object):
    """
    查询资金账户
    """

    def __init__(self, broker_id, investor_id):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id


class QryDepthMarketDataClass(object):
    """
    查询行情
    """

    def __init__(self, instrument_id):
        """

        :param instrument_id: str, length:31, 合约代码
        """
        self.instrument_id = instrument_id


class QryInstrumentTradingRightClass(object):
    """
    查询合约交易权限
    """

    def __init__(self, exchange_id, broker_id,
                 investor_id, instrument_id):
        """

        :param exchange_id: str,length:9  交易所代码
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param instrument_id: str,length:31 合约代码
        """
        self.exchange_id = exchange_id
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.instrument_id = instrument_id


class QryInvestorPositionDetailClass(object):
    """
    查询投资者持仓明细
    """

    def __init__(self, broker_id, investor_id, instrument_id):
        """

        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param instrument_id: str,length:31 合约代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.instrument_id = instrument_id


class QryInvestorPositionClass(QryInvestorPositionDetailClass):
    """
    查询投资者持仓
    """


class QryBondInterestClass(object):
    """
    查询债券利息
    """

    def __init__(self, exchange_id, instrument_id):
        """

        :param exchange_id: str,length:9 交易所代码
        :param instrument_id: str,length:31 合约代码
        """
        self.exchange_id = exchange_id
        self.instrument_id = instrument_id


class QryMarketRationInfoClass(object):
    """
    查询市值配售信息
    """

    def __init__(self, broker_id, investor_id, exchange_id):
        """

        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者帐号
        :param exchange_id: str,length:9 交易所代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.exchange_id = exchange_id


class QryOrderActionClass(QryMarketRationInfoClass):
    """
    查询报单操作
    """


class QryInstrumentCommissionRateClass(object):
    """
    查询合约手续费率


    买卖 direction:
        买: SECURITY_FTDC_D_Buy '0'
        卖: SECURITY_FTDC_D_Sell '1'
        ETF申购: SECURITY_FTDC_D_ETFPur '2'
        ETF赎回: SECURITY_FTDC_D_ETFRed '3'
        现金替代，只用作回报: SECURITY_FTDC_D_CashIn '4'
        债券入库: SECURITY_FTDC_D_PledgeBondIn '5'
        债券出库: SECURITY_FTDC_D_PledgeBondOut '6'
        配股: SECURITY_FTDC_D_Rationed '7'
        转托管: SECURITY_FTDC_D_DepositoryTransfer '8'
        信用账户配股: SECURITY_FTDC_D_CreditRationed '9'
        担保品买入: SECURITY_FTDC_D_BuyCollateral 'A'
        担保品卖出: SECURITY_FTDC_D_SellCollateral 'B'
        担保品转入: SECURITY_FTDC_D_CollateralTransferIn 'C'
        担保品转出: SECURITY_FTDC_D_CollateralTransferOut 'D'
        融资买入: SECURITY_FTDC_D_MarginTrade 'E'
        融券卖出: SECURITY_FTDC_D_ShortSell 'F'
        卖券还款: SECURITY_FTDC_D_RepayMargin 'G'
        买券还券: SECURITY_FTDC_D_RepayStock 'H'
        直接还款: SECURITY_FTDC_D_DirectRepayMargin 'I'
        直接还券: SECURITY_FTDC_D_DirectRepayStock 'J'
        余券划转: SECURITY_FTDC_D_ExcessStockTransfer 'K'

    """

    def __init__(self, exchange_id, broker_id, investor_id, instrument_id, direction):
        """

        :param exchange_id: str,length:9 交易所代码
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param instrument_id: str,length:31 合约代码
        :param direction: str,length:1 买卖方向
        """
        self.exchange_id = exchange_id
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.instrument_id = instrument_id
        self.direction = direction


class QryExcessStockInfoClass(object):
    """
    查询余券信息
    """

    def __init__(self, broker_id, investor_id, exchange_id, instrument_id):
        """
        :param broker_id: str,length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param exchange_id: str,length:9 交易所代码
        :param instrument_id: str,length:31 合约代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.exchange_id = exchange_id
        self.instrument_id = instrument_id


class QryTraderOfferClass(object):
    """
    查询交易员报盘机
    """

    def __init__(self, exchange_id, participant_id, branch_pbu):
        """

        :param exchange_id: str,length:9 交易所代码
        :param participant_id: str, length:11 会员代码
        :param branch_pbu: str,length:21 交易所交易员代码

        """
        self.exchange_id = exchange_id
        self.participant_id = participant_id
        self.branch_pbu = branch_pbu


class QryMDTraderOfferClass(QryTraderOfferClass):
    """
    查询行情报盘机
    """


class QryFrontStatusClass(object):
    """
    查询前置状态
    """

    def __init__(self, front_id):
        """

        :param front_id: int 前置编号
        """
        self.front_id = front_id


class QryUserSessionClass(object):
    """
    查询用户会话
    """

    def __init__(self, front_id, session_id,
                 broker_id, user_id):
        """

        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        """
        self.front_id = front_id
        self.session_id = session_id
        self.broker_id = broker_id
        self.user_id = user_id


class QryOrderClass(object):
    """
    查询报单
    """

    def __init__(self, broker_id, investor_id, instrument_id,
                 exchange_id, order_sys_id, insert_time_start,
                 insert_time_end):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param investor_id: str,length:15  投资者代码
        :param instrument_id: str,length:31 合约代码
        :param exchange_id: str,length:9 交易所代码
        :param order_sys_id: str, length:21 报单编号
        :param insert_time_start: str,length:9  开始时间
        :param insert_time_end: str,length:9  结束时间
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.instrument_id = instrument_id
        self.exchange_id = exchange_id
        self.order_sys_id = order_sys_id
        self.insert_time_start = insert_time_start
        self.insert_time_end = insert_time_end


class QryErrOrderClass(object):
    """
    查询错误报单
    """

    def __init__(self, broker_id, investor_id):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param investor_id: str,length:15 投资者代码
        """
        self.broker_id = broker_id
        self.investor_id = investor_id


class QryErrOrderActionClass(QryErrOrderClass):
    """
    查询错误报单操作
    """


class QryTradeClass(object):
    """
    查询成交
    """

    def __init__(self, broker_id, investor_id, instrument_id,
                 exchange_id, trade_id,
                 trade_time_start, trade_time_end):
        """
        :param broker_id: str, length:11 经纪公司代码
        :param investor_id: str,length:15  投资者代码
        :param instrument_id: str,length:31 合约代码
        :param exchange_id: str,length:9 交易所代码
        :param trade_id: str,length:21 成交编号
        :param trade_time_start: str,length:9 开始时间
        :param trade_time_end: str,length:9  结束时间
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.instrument_id = instrument_id
        self.exchange_id = exchange_id
        self.trade_id = trade_id
        self.trade_time_start = trade_time_start
        self.trade_time_end = trade_time_end


class QrySyncDepositClass(object):
    """
    查询出入金流水
    """

    def __init__(self, broker_id, deposit_seq_no):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param deposit_seq_no: str,length:15 出入金流水号
        """
        self.broker_id = broker_id
        self.deposit_seq_no = deposit_seq_no


class UserPasswordUpdateClass(object):
    """
    用户口令变更
    """

    def __init__(self, broker_id, user_id,
                 old_password, new_password):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param old_password: str,length:41  原来的口令
        :param new_password: str,length:41  新的口令
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.old_password = old_password
        self.new_password = new_password


class TradingAccountPasswordUpdateClass(object):
    """
    资金账户口令变更域
    """

    def __init__(self, broker_id, account_id, old_password,
                 new_password):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param account_id: str,length:15 投资者帐号
        :param old_password: str,length:41 原来的口令
        :param new_password: str,length:41 新的口令
        """
        self.broker_id = broker_id
        self.account_id = account_id
        self.old_password = old_password
        self.new_password = new_password


class ManualSyncBrokerUserOTPClass(object):
    """
    手工同步用户动态令牌

    动态令牌类型 opt_type:
        无动态令牌: SECURITY_FTDC_OTP_NONE '0'
        时间令牌: SECURITY_FTDC_OTP_TOTP '1'

    """

    def __init__(self, broker_id, user_id, otp_type,
                 first_otp, second_otp):
        """
        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param otp_type: str,length:1 动态令牌类型
        :param first_otp: str,length:41 第一个动态密码
        :param second_otp: str,length:41 第二个动态密码
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.otp_type = otp_type
        self.first_otp = first_otp
        self.second_otp = second_otp


class BrokerUserPasswordClass(object):
    """
    经纪公司用户口令
    """

    def __init__(self, broker_id, user_id, password):
        """
        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param password: str,length:41  密码
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.password = password


class TradingAccountPasswordClass(object):
    """
    资金账户口令域
    """

    def __init__(self, broker_id, account_id, password):
        """
        :param broker_id: str, length:11 经纪公司代码
        :param account_id: str,length:15 投资者帐号
        :param password: str,length:41 密码
        """
        self.broker_id = broker_id
        self.account_id = account_id
        self.password = password


class UserRightClass(object):
    """
    用户权限

    客户权限类型 user_right_type:
        登录: SECURITY_FTDC_URT_Logon '1'
        银期转帐: SECURITY_FTDC_URT_Transfer '2'
        邮寄结算单: SECURITY_FTDC_URT_EMail '3'
        传真结算单: SECURITY_FTDC_URT_Fax '4'
        条件单: SECURITY_FTDC_URT_ConditionOrder '5'

    """

    def __init__(self, broker_id, user_id,
                 user_right_type, is_forbidden):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param user_right_type: str,length:1 客户权限类型
        :param is_forbidden: c++:int python:bool 是否禁止
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.user_right_type = user_right_type
        self.is_forbidden = is_forbidden


class InvestorAccountClass(object):
    """
    投资者账户

    账户类型 account_type :
        普通账户: SECURITY_FTDC_AcT_Normal '1'
        信用账户: SECURITY_FTDC_AcT_Credit '2'
        衍生品账户: SECURITY_FTDC_AcT_Derive '3'
        其他类型: SECURITY_FTDC_AcT_Other '4'
   """

    def __init__(self, broker_id, investor_id, account_id, is_default,
                 account_type, is_active):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param investor_id: str,length:15  投资者代码
        :param account_id: str,length:15 投资者帐号
        :param is_default: c++:int python:bool 是否主账户
        :param account_type: str,length:1 账户类型
        :param is_active: c++:int python:bool 是否活跃
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.account_id = account_id
        self.is_default = is_default
        self.account_type = account_type
        self.is_active = is_active


class UserIPClass(object):
    """
    用户IP
    """

    def __init__(self, broker_id, user_id, ip_address, ip_mask,
                 mac_address):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param ip_address: str, length:16 IP地址
        :param ip_mask: str, length:16 IP地址掩码
        :param mac_address: str,length:21 Mac地址
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.ip_address = ip_address
        self.ip_mask = ip_mask
        self.mac_address = mac_address


class BrokerUserOTPParamClass(object):
    """
    用户动态令牌参数

    动态令牌类型 opt_type:
        无动态令牌: SECURITY_FTDC_OTP_NONE '0'
        时间令牌: SECURITY_FTDC_OTP_TOTP '1'
    """

    def __init__(self, broker_id, user_id, otp_vendors_id,
                 serial_number, auth_key, last_drift, last_success,
                 otp_type):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param otp_vendors_id: str,length:2 动态令牌提供商
        :param serial_number: str,length:17 动态令牌序列号
        :param auth_key: str,length:41 令牌密钥
        :param last_drift:int 漂移值
        :param last_success: int 成功值
        :param otp_type: str,length:1 动态令牌类型
        """
        self.broker_id = broker_id
        self.user_id = user_id
        self.otp_vendors_id = otp_vendors_id
        self.serial_number = serial_number
        self.auth_key = auth_key
        self.last_drift = last_drift
        self.last_success = last_success
        self.otp_type = otp_type


class ReqUserLoginClass(object):
    """
    用户登录请求
    """

    def __init__(self, trading_day, broker_id, user_id, password,
                 user_product_info, interface_product_info, protocol_info,
                 mac_address, one_time_password, client_ip_address, auth_code):
        """

        :param trading_day: str,length:9 交易日
        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param password: str,length:41 密码
        :param user_product_info: str,length:11 用户端产品信息
        :param interface_product_info: str,length:11 接口端产品信息
        :param protocol_info: str,length:11 协议信息
        :param mac_address: str,length:21 Mac地址
        :param one_time_password: str,length:41 动态密码
        :param client_ip_address: str,length:16  终端IP地址
        :param auth_code: str,length:17 客户端认证码
        """
        self.trading_day = trading_day
        self.broker_id = broker_id
        self.user_id = user_id
        self.password = password
        self.user_product_info = user_product_info
        self.interface_product_info = interface_product_info
        self.protocol_info = protocol_info
        self.mac_address = mac_address
        self.one_time_password = one_time_password
        self.client_ip_address = client_ip_address
        self.auth_code = auth_code


class RspUserLoginClass(object):
    """
    用户登录应答
    """

    def __init__(self, trading_day, login_time, broker_id,
                 user_id, system_name, front_id, session_id, max_order_ref):
        """
        :param trading_day: str,length:9 交易日
        :param login_time: str,length:9 登录成功时间
        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        :param system_name: str,length:41 交易系统名称
        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param max_order_ref: str,length:13 最大报单引用
        """
        self.trading_day = trading_day
        self.login_time = login_time
        self.broker_id = broker_id
        self.user_id = user_id
        self.system_name = system_name
        self.front_id = front_id
        self.session_id = session_id
        self.max_order_ref = max_order_ref


class UserLogoutClass(object):
    """
    用户登出请求
    """

    def __init__(self, broker_id, user_id):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param user_id: str,length:16 用户代码
        """
        self.broker_id = broker_id
        self.user_id = user_id


class ForceUserLogoutClass(UserLogoutClass):
    """
    强制交易员退出
    """


class LogoutAllClass(object):
    """
    全部登出信息
    """

    def __init__(self, front_id, session_id, system_name):
        """

        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param system_name: str,length:41 系统名称
        """
        self.front_id = front_id
        self.session_id = session_id
        self.system_name = system_name


class InputOrderClass(object):
    """
    输入报单
    
    报单价格条件 order_price_type:
        即时成交剩余撤销市价单: SECURITY_FTDC_OPT_AnyPrice '1'
        限价: SECURITY_FTDC_OPT_LimitPrice '2'
        最优五档即时成交剩余撤销市价单: SECURITY_FTDC_OPT_BestPrice '3'
        最优五档即时成交剩余转限价市价单: SECURITY_FTDC_OPT_BestLimitPrice '4'
        全部成交或撤销市价单: SECURITY_FTDC_OPT_AllPrice '5'
        本方最优价格市价单: SECURITY_FTDC_OPT_ForwardBestPrice '6'
        对方最优价格市价单: SECURITY_FTDC_OPT_ReverseBestPrice '7'
        激活A股网络密码服务代码: SECURITY_FTDC_OPT_ActiveANetPassSvrCode 'G'
        注销A股网络密码服务代码: SECURITY_FTDC_OPT_InactiveANetPassSvrCode 'H'
        激活B股网络密码服务代码: SECURITY_FTDC_OPT_ActiveBNetPassSvrCode 'I'
        注销B股网络密码服务代码: SECURITY_FTDC_OPT_InactiveBNetPassSvrCode 'J'
        回购注销: SECURITY_FTDC_OPT_Repurchase 'K'
        指定撤销: SECURITY_FTDC_OPT_DesignatedCancel 'L'
        指定登记: SECURITY_FTDC_OPT_Designated 'M'
        证券参与申购: SECURITY_FTDC_OPT_SubscribingShares 'N'
        证券参与配股: SECURITY_FTDC_OPT_Split 'O'
        要约收购登记: SECURITY_FTDC_OPT_TenderOffer 'P'
        要约收购撤销: SECURITY_FTDC_OPT_TenderOfferCancel 'Q'
        证券投票: SECURITY_FTDC_OPT_Ballot 'R'
        可转债转换登记: SECURITY_FTDC_OPT_ConvertibleBondsConvet 'S'
        可转债回售登记: SECURITY_FTDC_OPT_ConvertibleBondsRepurchase 'T'
        权证行权: SECURITY_FTDC_OPT_Exercise 'U'
        开放式基金申购: SECURITY_FTDC_OPT_PurchasingFunds 'V'
        开放式基金赎回: SECURITY_FTDC_OPT_RedemingFunds 'W'
        开放式基金认购: SECURITY_FTDC_OPT_SubscribingFunds 'X'
        开放式基金转托管转出: SECURITY_FTDC_OPT_LOFIssue 'Y'
        开放式基金设置分红方式: SECURITY_FTDC_OPT_LOFSetBonusType 'Z'
        开放式基金转换为其他基金: SECURITY_FTDC_OPT_LOFConvert 'a'
        债券入库: SECURITY_FTDC_OPT_DebentureStockIn 'b'
        债券出库: SECURITY_FTDC_OPT_DebentureStockOut 'c'
        ETF申购: SECURITY_FTDC_OPT_PurchasesETF  'd'
        ETF赎回: SECURITY_FTDC_OPT_RedeemETF 'e'
    
    买卖 direction:
        买: SECURITY_FTDC_D_Buy '0'
        卖: SECURITY_FTDC_D_Sell '1'
        ETF申购: SECURITY_FTDC_D_ETFPur '2'
        ETF赎回: SECURITY_FTDC_D_ETFRed '3'
        现金替代，只用作回报: SECURITY_FTDC_D_CashIn '4'
        债券入库: SECURITY_FTDC_D_PledgeBondIn '5'
        债券出库: SECURITY_FTDC_D_PledgeBondOut '6'
        配股: SECURITY_FTDC_D_Rationed '7'
        转托管: SECURITY_FTDC_D_DepositoryTransfer '8'
        信用账户配股: SECURITY_FTDC_D_CreditRationed '9'
        担保品买入: SECURITY_FTDC_D_BuyCollateral 'A'
        担保品卖出: SECURITY_FTDC_D_SellCollateral 'B'
        担保品转入: SECURITY_FTDC_D_CollateralTransferIn 'C'
        担保品转出: SECURITY_FTDC_D_CollateralTransferOut 'D'
        融资买入: SECURITY_FTDC_D_MarginTrade 'E'
        融券卖出: SECURITY_FTDC_D_ShortSell 'F'
        卖券还款: SECURITY_FTDC_D_RepayMargin 'G'
        买券还券: SECURITY_FTDC_D_RepayStock 'H'
        直接还款: SECURITY_FTDC_D_DirectRepayMargin 'I'
        直接还券: SECURITY_FTDC_D_DirectRepayStock 'J'
        余券划转: SECURITY_FTDC_D_ExcessStockTransfer 'K'
        
    
    有效期类型 time_condition:
        立即完成，否则撤销: SECURITY_FTDC_TC_IOC '1'
        本节有效: SECURITY_FTDC_TC_GFS '2'
        当日有效: SECURITY_FTDC_TC_GFD '3'
        指定日期前有效: SECURITY_FTDC_TC_GTD '4'
        撤销前有效: SECURITY_FTDC_TC_GTC '5'
        集合竞价有效: SECURITY_FTDC_TC_GFA '6'
        
    成交量类型 volume_condition:
        任何数量: SECURITY_FTDC_VC_AV '1'
        最小数量: SECURITY_FTDC_VC_MV '2'
        全部数量: SECURITY_FTDC_VC_CV '3'
        
    触发条件 contingent_condition:
        立即: SECURITY_FTDC_CC_Immediately '1'
        止损: SECURITY_FTDC_CC_Touch '2'
        止赢: SECURITY_FTDC_CC_TouchProfit '3'
        预埋单: SECURITY_FTDC_CC_ParkedOrder '4'
        最新价大于条件价: SECURITY_FTDC_CC_LastPriceGreaterThanStopPrice '5'
        最新价大于等于条件价: SECURITY_FTDC_CC_LastPriceGreaterEqualStopPrice '6'
        最新价小于条件价: SECURITY_FTDC_CC_LastPriceLesserThanStopPrice '7'
        最新价小于等于条件价: SECURITY_FTDC_CC_LastPriceLesserEqualStopPrice '8'
        卖一价大于条件价: SECURITY_FTDC_CC_AskPriceGreaterThanStopPrice '9'
        卖一价大于等于条件价: SECURITY_FTDC_CC_AskPriceGreaterEqualStopPrice 'A'
        卖一价小于条件价: SECURITY_FTDC_CC_AskPriceLesserThanStopPrice 'B'
        卖一价小于等于条件价: SECURITY_FTDC_CC_AskPriceLesserEqualStopPrice 'C'
        买一价大于条件价: SECURITY_FTDC_CC_BidPriceGreaterThanStopPrice 'D'
        买一价大于等于条件价: SECURITY_FTDC_CC_BidPriceGreaterEqualStopPrice 'E'
        买一价小于条件价: SECURITY_FTDC_CC_BidPriceLesserThanStopPrice 'F'
        买一价小于等于条件价: SECURITY_FTDC_CC_BidPriceLesserEqualStopPrice 'H'
        
    
    强平原因 force_close_reason:

        非强平: SECURITY_FTDC_FCC_NotForceClose '0'
        资金不足: SECURITY_FTDC_FCC_LackDeposit '1'
        客户超仓: SECURITY_FTDC_FCC_ClientOverPositionLimit '2'
        会员超仓: SECURITY_FTDC_FCC_MemberOverPositionLimit '3'
        持仓非整数倍: SECURITY_FTDC_FCC_NotMultiple '4'
        违规: SECURITY_FTDC_FCC_Violation '5'
        其它: SECURITY_FTDC_FCC_Other '6'
        自然人临近交割: SECURITY_FTDC_FCC_PersonDeliv '7'


    """

    def __init__(self, broker_id, investor_id, instrument_id,
                 order_ref, user_id, exchange_id, order_price_type,
                 direction, comb_offset_flag, comb_hedge_flag,
                 limit_price, volume_total_original, time_condition, gtd_date,
                 volume_condition, min_volume, contingent_condition, stop_price,
                 force_close_reason, is_auto_suspend, business_unit,
                 request_id, user_force_close):
        """

        :param broker_id: str, length:11 经纪公司代码
        :param investor_id: str,length:15  投资者代码
        :param instrument_id: str,length:31 合约代码
        :param order_ref: str,length:13 报单引用
        :param user_id: str,length:16 用户代码
        :param exchange_id: str,length:9 交易所代码
        :param order_price_type: str, length:1 报单价格条件
        :param direction: str,length:1 买卖方向
        :param comb_offset_flag: str,length:5 组合开平标志
        :param comb_hedge_flag: str,length:5 组合投机套保标志
        :param limit_price:  str, length:16 价格
        :param volume_total_original: int 数量
        :param time_condition: str,length:1 有效期类型
        :param gtd_date: str, length:9 GTD日期
        :param volume_condition: str,length:1 成交量类型
        :param min_volume: int 最小成交量
        :param contingent_condition: str, length:1 触发条件
        :param stop_price: double 止损价
        :param force_close_reason: str, length:1 强平原因
        :param is_auto_suspend: c++:int python:bool 自动挂起标志
        :param business_unit: str,length:21 业务单元
        :param request_id: int 请求编号
        :param user_force_close: c++:int python:bool 用户强评标志
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.instrument_id = instrument_id
        self.order_ref = order_ref
        self.user_id = user_id
        self.exchange_id = exchange_id
        self.order_price_type = order_price_type
        self.direction = direction
        self.comb_offset_flag = comb_offset_flag
        self.comb_hedge_flag = comb_hedge_flag
        self.limit_price = limit_price
        self.volume_total_original = volume_total_original
        self.time_condition = time_condition
        self.gtd_date = gtd_date
        self.volume_condition = volume_condition
        self.min_volume = min_volume
        self.contingent_condition = contingent_condition
        self.stop_price = stop_price
        self.force_close_reason = force_close_reason
        self.is_auto_suspend = is_auto_suspend
        self.business_unit = business_unit
        self.request_id = request_id
        self.user_force_close = user_force_close


class InputOrderActionClass(object):
    """
    输入报单操作
    操作标志 action_flag:
        删除: SECURITY_FTDC_AF_Delete '0'
        修改: SECURITY_FTDC_AF_Modify '3'

    """

    def __init__(self, broker_id, investor_id, order_action_ref, order_ref,
                 request_id, front_id, session_id, exchange_id,
                 action_flag, limit_price, volume_change, user_id,
                 instrument_id, branch_pbu, order_local_id):
        """

        :param broker_id: str,length:11  经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param order_action_ref: int 报单操作引用
        :param order_ref: str,length:13 报单引用
        :param request_id: int 请求编号
        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param exchange_id: str, length:9 交易所代码
        :param action_flag: str,length:1 操作标志
        :param limit_price: double 价格
        :param volume_change: int 数量变化
        :param user_id: str,length:16 用户代码
        :param instrument_id: str, length:31, 合约代码
        :param branch_pbu: str, length:21 交易所交易员代码
        :param order_local_id: str,length:13 本地报单编号
        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.order_action_ref = order_action_ref
        self.order_ref = order_ref
        self.request_id = request_id
        self.front_id = front_id
        self.session_id = session_id
        self.exchange_id = exchange_id
        self.action_flag = action_flag
        self.limit_price = limit_price
        self.volume_change = volume_change
        self.user_id = user_id
        self.instrument_id = instrument_id
        self.branch_pbu = branch_pbu
        self.order_local_id = order_local_id


class OrderClass(InputOrderClass):
    """
    报单

    报单提交状态 order_submit_status:
        已经提交: SECURITY_FTDC_OSS_InsertSubmitted '0'
        撤单已经提交: SECURITY_FTDC_OSS_CancelSubmitted '1'
        修改已经提交: SECURITY_FTDC_OSS_ModifySubmitted '2'
        已经接受: SECURITY_FTDC_OSS_Accepted '3'
        报单已经被拒绝: SECURITY_FTDC_OSS_InsertRejected '4'
        撤单已经被拒绝: SECURITY_FTDC_OSS_CancelRejected '5'
        改单已经被拒绝: SECURITY_FTDC_OSS_ModifyRejected '6'

    报单来源 order_source:
        来自参与者: SECURITY_FTDC_OSRC_Participant '0'
        来自管理员: SECURITY_FTDC_OSRC_Administrator '1'

    报单状态 order_status:
        全部成交: SECURITY_FTDC_OST_AllTraded '0'
        部分成交还在队列中: SECURITY_FTDC_OST_PartTradedQueueing '1'
        部分成交不在队列中: SECURITY_FTDC_OST_PartTradedNotQueueing '2'
        未成交还在队列中: SECURITY_FTDC_OST_NoTradeQueueing '3'
        未成交不在队列中: SECURITY_FTDC_OST_NoTradeNotQueueing '4'
        撤单: SECURITY_FTDC_OST_Canceled '5'
        未知: SECURITY_FTDC_OST_Unknown 'a'
        尚未触发: SECURITY_FTDC_OST_NotTouched 'b'
        已触发: SECURITY_FTDC_OST_Touched 'c'
        

    报单类型 order_type:
        正常: SECURITY_FTDC_ORDT_Normal '0'
        报价衍生: SECURITY_FTDC_ORDT_DeriveFromQuote '1'
        组合衍生: SECURITY_FTDC_ORDT_DeriveFromCombination '2'
        组合报单: SECURITY_FTDC_ORDT_Combination '3'
        条件单: SECURITY_FTDC_ORDT_ConditionalOrder '4'
        互换单: SECURITY_FTDC_ORDT_Swap '5'

    """

    def __init__(self, order_local_id, participant_id, client_id, exchange_inst_id, branch_pbu,
                 install_id, order_submit_status, account_id, notify_sequence, trading_day, order_sys_id,
                 order_source, order_status, order_type, volume_traded, volume_total, insert_date, insert_time,
                 active_time, suspend_time, update_time, cancel_time, active_trader_id, clearing_part_id,
                 sequence_no, front_id, session_id, user_product_info, status_msg, active_user_id,
                 broker_order_seq, relative_order_sys_id, branch_id, trade_amount, is_etf,
                 *args, **kwargs):
        """

        :param order_local_id: str,length:13 本地报单编号
        :param participant_id: str,length:11 会员代码
        :param client_id:  str, length:21 客户代码
        :param exchange_inst_id: str,length:31 合约在交易所的代码
        :param branch_pbu:  str,length:21 交易所交易员代码
        :param install_id: int 安装编号
        :param order_submit_status: str,length:1 报单提交状态
        :param account_id: str, length:15 账户代码
        :param notify_sequence: int 报单提示序号
        :param trading_day: str,length:9 交易日
        :param order_sys_id: str,length:21 报单编号
        :param order_source: str,length:1 报单来源
        :param order_status: str, length:1 报单状态
        :param order_type: str, length:1 报单类型
        :param volume_traded: int 今成交数量
        :param volume_total: int 剩余数量
        :param insert_date: str, length:9 报单日期
        :param insert_time: str, length:9 委托时间
        :param active_time: str, length:9 激活时间
        :param suspend_time: str, length:9 挂起时间
        :param update_time: str, length:9 最后修改时间
        :param cancel_time: str, length:9 撤销时间
        :param active_trader_id:  str ,length:21 最后修改交易所交易员代码
        :param clearing_part_id:  str, length:11 结算会员编号
        :param sequence_no: int 序号
        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param user_product_info: str, length:11 用户端产品信息
        :param status_msg: str, length:81 状态信息
        :param active_user_id: str, length:16 操作用户代码
        :param broker_order_seq:  int 经纪公司报单编号
        :param relative_order_sys_id: str, length:21 相关报单
        :param branch_id: str, length:9 营业部编号
        :param trade_amount: double 成交数量
        :param is_etf: c++ : int python: bool 是否ETF
        """
        super(OrderClass, self).__init__(*args, **kwargs)
        self.order_local_id = order_local_id
        self.participant_id = participant_id
        self.client_id = client_id
        self.exchange_inst_id = exchange_inst_id
        self.branch_pbu = branch_pbu
        self.install_id = install_id
        self.order_submit_status = order_submit_status
        self.account_id = account_id
        self.notify_sequence = notify_sequence
        self.trading_day = trading_day
        self.order_sys_id = order_sys_id
        self.order_source = order_source
        self.order_status = order_status
        self.order_type = order_type
        self.volume_traded = volume_traded
        self.volume_total = volume_total
        self.insert_date = insert_date
        self.insert_time = insert_time
        self.active_time = active_time
        self.suspend_time = suspend_time
        self.update_time = update_time
        self.cancel_time = cancel_time
        self.active_trader_id = active_trader_id
        self.clearing_part_id = clearing_part_id
        self.sequence_no = sequence_no
        self.front_id = front_id
        self.session_id = session_id
        self.user_product_info = user_product_info
        self.status_msg = status_msg
        self.active_user_id = active_user_id
        self.broker_order_seq = broker_order_seq
        self.relative_order_sys_id = relative_order_sys_id
        self.branch_id = branch_id
        self.trade_amount = trade_amount
        self.is_etf = is_etf


class OrderActionClass(object):
    """
    报单操作

    操作标志 action_flag:
        删除: SECURITY_FTDC_AF_Delete '0'
        修改: SECURITY_FTDC_AF_Modify '3'

    报单操作状态 order_action_status:
        已经提交: SECURITY_FTDC_OAS_Submitted 'a'
        已经接受: SECURITY_FTDC_OAS_Accepted 'b'
        已经被拒绝: SECURITY_FTDC_OAS_Rejected 'c'

    """

    def __init__(self, broker_id, investor_id, order_action_ref, order_ref, request_id, front_id, session_id,
                 exchange_id, action_flag, limit_price, volume_change, action_date, action_time, branch_pbu,
                 install_id, order_local_id, action_local_id, participant_id, client_id, business_unit,
                 order_action_status, user_id, branch_id, status_msg, instrument_id):
        """

        :param broker_id: str,length:11  经纪公司代码
        :param investor_id: str,length:15 投资者代码
        :param order_action_ref: int 报单操作引用
        :param order_ref: str,length:13 报单引用
        :param request_id: int 请求编号
        :param front_id: int 前置编号
        :param session_id: int 会话编号
        :param exchange_id: str,length:9 交易所代码
        :param action_flag: str,length:1 操作标志
        :param limit_price: double 价格
        :param volume_change: int 数量变化
        :param action_date:  str ,length:9 操作日期
        :param action_time: str ,length:9 操作时间
        :param branch_pbu: str,length:21 交易所交易员代码
        :param install_id: int 安装编号
        :param order_local_id: str, length:13 本地报单编号
        :param action_local_id: str, length:13 操作本地编号
        :param participant_id: str,length:11 会员代码
        :param client_id: str,length:21 客户代码
        :param business_unit: str,length:21 业务单元
        :param order_action_status: str, length:1 报单操作状态
        :param user_id: str,length:16 用户代码
        :param branch_id: str,length:9 营业部编号
        :param status_msg: str,length:81 状态信息
        :param instrument_id: str,length:31 合约代码

        """
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.order_action_ref = order_action_ref
        self.order_ref = order_ref
        self.request_id = request_id
        self.front_id = front_id
        self.session_id = session_id
        self.exchange_id = exchange_id
        self.action_flag = action_flag
        self.limit_price = limit_price
        self.volume_change = volume_change
        self.action_date = action_date
        self.action_time = action_time
        self.branch_pbu = branch_pbu
        self.install_id = install_id
        self.order_local_id = order_local_id
        self.action_local_id = action_local_id
        self.participant_id = participant_id
        self.client_id = client_id
        self.business_unit = business_unit
        self.order_action_status = order_action_status
        self.user_id = user_id
        self.branch_id = branch_id
        self.status_msg = status_msg
        self.instrument_id = instrument_id


class ErrOrderClass(object):
    """
    错误报单
    """

    def __init__(self):
        pass
        #
        # struct ErrOrderClass
        # {
        # 经纪公司代码
        # 	TSecurityFtdcBrokerIDType	BrokerID;
        # 	投资者代码
        # 	TSecurityFtdcInvestorIDType	InvestorID;
        # 	合约代码
        # 	TSecurityFtdcInstrumentIDType	InstrumentID;
        # 	报单引用
        # 	TSecurityFtdcOrderRefType	OrderRef;
        # 	用户代码
        # 	TSecurityFtdcUserIDType	UserID;
        # 	交易所代码
        # 	TSecurityFtdcExchangeIDType	ExchangeID;
        # 	报单价格条件
        # 	TSecurityFtdcOrderPriceTypeType	OrderPriceType;
        # 	买卖方向
        # 	TSecurityFtdcDirectionType	Direction;
        # 	组合开平标志
        # 	TSecurityFtdcCombOffsetFlagType	CombOffsetFlag;
        # 	组合投机套保标志
        # 	TSecurityFtdcCombHedgeFlagType	CombHedgeFlag;
        # 	价格
        # 	TSecurityFtdcStockPriceType	LimitPrice;
        # 	数量
        # 	TSecurityFtdcVolumeType	VolumeTotalOriginal;
        # 	有效期类型
        # 	TSecurityFtdcTimeConditionType	TimeCondition;
        # 	GTD日期
        # 	TSecurityFtdcDateType	GTDDate;
        # 	成交量类型
        # 	TSecurityFtdcVolumeConditionType	VolumeCondition;
        # 	最小成交量
        # 	TSecurityFtdcVolumeType	MinVolume;
        # 	触发条件
        # 	TSecurityFtdcContingentConditionType	ContingentCondition;
        # 	止损价
        # 	TSecurityFtdcPriceType	StopPrice;
        # 	强平原因
        # 	TSecurityFtdcForceCloseReasonType	ForceCloseReason;
        # 	自动挂起标志
        # 	TSecurityFtdcBoolType	IsAutoSuspend;
        # 	业务单元
        # 	TSecurityFtdcBusinessUnitType	BusinessUnit;
        # 	请求编号
        # 	TSecurityFtdcRequestIDType	RequestID;
        # 	用户强评标志
        # 	TSecurityFtdcBoolType	UserForceClose;
        # 	错误代码
        # 	TSecurityFtdcErrorIDType	ErrorID;
        # 	错误信息
        # 	TSecurityFtdcErrorMsgType	ErrorMsg;
        # };
        #
        # 错误报单操作
        # struct ErrOrderActionClass
        # {
        # 	经纪公司代码
        # 	TSecurityFtdcBrokerIDType	BrokerID;
        # 	投资者代码
        # 	TSecurityFtdcInvestorIDType	InvestorID;
        # 	报单操作引用
        # 	TSecurityFtdcOrderActionRefType	OrderActionRef;
        # 	报单引用
        # 	TSecurityFtdcOrderRefType	OrderRef;
        # 	请求编号
        # 	TSecurityFtdcRequestIDType	RequestID;
        # 	前置编号
        # 	TSecurityFtdcFrontIDType	FrontID;
        # 	会话编号
        # 	TSecurityFtdcSessionIDType	SessionID;
        # 	交易所代码
        # 	TSecurityFtdcExchangeIDType	ExchangeID;
        # 	操作标志
        # 	TSecurityFtdcActionFlagType	ActionFlag;
        # 	价格
        # 	TSecurityFtdcPriceType	LimitPrice;
        # 	数量变化
        # 	TSecurityFtdcVolumeType	VolumeChange;
        # 	操作日期
        # 	TSecurityFtdcDateType	ActionDate;
        # 	操作时间
        # 	TSecurityFtdcTimeType	ActionTime;
        # 	交易所交易员代码
        # 	TSecurityFtdcTraderIDType	BranchPBU;
        # 	安装编号
        # 	TSecurityFtdcInstallIDType	InstallID;
        # 	本地报单编号
        # 	TSecurityFtdcOrderLocalIDType	OrderLocalID;
        # 	操作本地编号
        # 	TSecurityFtdcOrderLocalIDType	ActionLocalID;
        # 	会员代码
        # 	TSecurityFtdcParticipantIDType	ParticipantID;
        # 	客户代码
        # 	TSecurityFtdcClientIDType	ClientID;
        # 	业务单元
        # 	TSecurityFtdcBusinessUnitType	BusinessUnit;
        # 	报单操作状态
        # 	TSecurityFtdcOrderActionStatusType	OrderActionStatus;
        # 	用户代码
        # 	TSecurityFtdcUserIDType	UserID;
        # 	营业部编号
        # 	TSecurityFtdcBranchIDType	BranchID;
        # 	状态信息
        # 	TSecurityFtdcErrorMsgType	StatusMsg;
        # 	合约代码
        # 	TSecurityFtdcInstrumentIDType	InstrumentID;
        # 	错误代码
        # 	TSecurityFtdcErrorIDType	ErrorID;
        # 	错误信息
        # 	TSecurityFtdcErrorMsgType	ErrorMsg;
        # };
        #
        # 成交
        # struct TradeClass
        # {
        # 	经纪公司代码
        # 	TSecurityFtdcBrokerIDType	BrokerID;
        # 	投资者代码
        # 	TSecurityFtdcInvestorIDType	InvestorID;
        # 	合约代码
        # 	TSecurityFtdcInstrumentIDType	InstrumentID;
        # 	报单引用
        # 	TSecurityFtdcOrderRefType	OrderRef;
        # 	用户代码
        # 	TSecurityFtdcUserIDType	UserID;
        # 	交易所代码
        # 	TSecurityFtdcExchangeIDType	ExchangeID;
        # 	成交编号
        # 	TSecurityFtdcTradeIDType	TradeID;
        # 	买卖方向
        # 	TSecurityFtdcDirectionType	Direction;
        # 	报单编号
        # 	TSecurityFtdcOrderSysIDType	OrderSysID;
        # 	会员代码
        # 	TSecurityFtdcParticipantIDType	ParticipantID;
        # 	客户代码
        # 	TSecurityFtdcClientIDType	ClientID;
        # 	交易角色
        # 	TSecurityFtdcTradingRoleType	TradingRole;
        # 	合约在交易所的代码
        # 	TSecurityFtdcExchangeInstIDType	ExchangeInstID;
        # 	开平标志
        # 	TSecurityFtdcOffsetFlagType	OffsetFlag;
        # 	投机套保标志
        # 	TSecurityFtdcHedgeFlagType	HedgeFlag;
        # 	价格
        # 	TSecurityFtdcStockPriceType	Price;
        # 	数量
        # 	TSecurityFtdcVolumeType	Volume;
        # 	成交时期
        # 	TSecurityFtdcDateType	TradeDate;
        # 	成交时间
        # 	TSecurityFtdcTimeType	TradeTime;
        # 	成交类型
        # 	TSecurityFtdcTradeTypeType	TradeType;
        # 	成交价来源
        # 	TSecurityFtdcPriceSourceType	PriceSource;
        # 	交易所交易员代码
        # 	TSecurityFtdcTraderIDType	BranchPBU;
        # 	本地报单编号
        # 	TSecurityFtdcOrderLocalIDType	OrderLocalID;
        # 	结算会员编号
        # 	TSecurityFtdcParticipantIDType	ClearingPartID;
        # 	业务单元
        # 	TSecurityFtdcBusinessUnitType	BusinessUnit;
        # 	序号
        # 	TSecurityFtdcSequenceNoType	SequenceNo;
        # 	成交来源
        # 	TSecurityFtdcTradeSourceType	TradeSource;
        # 	交易日
        # 	TSecurityFtdcDateType	TradingDay;
        # 	经纪公司报单编号
        # 	TSecurityFtdcSequenceNoType	BrokerOrderSeq;
        # };
        #
        # 投资者持仓
        # struct InvestorPositionClass
        # {
        # 	合约代码
        # 	TSecurityFtdcInstrumentIDType	InstrumentID;
        # 	经纪公司代码
        # 	TSecurityFtdcBrokerIDType	BrokerID;
        # 	投资者代码
        # 	TSecurityFtdcInvestorIDType	InvestorID;
        # 	持仓多空方向
        # 	TSecurityFtdcPosiDirectionType	PosiDirection;
        # 	投机套保标志
        # 	TSecurityFtdcHedgeFlagType	HedgeFlag;
        # 	持仓日期
        # 	TSecurityFtdcPositionDateType	PositionDate;
        # 	上日持仓
        # 	TSecurityFtdcVolumeType	YdPosition;
        # 	今日持仓
        # 	TSecurityFtdcVolumeType	Position;
        # 	多头冻结
        # 	TSecurityFtdcVolumeType	LongFrozen;
        # 	空头冻结
        # 	TSecurityFtdcVolumeType	ShortFrozen;
        # 	开仓冻结金额
        # 	TSecurityFtdcMoneyType	LongFrozenAmount;
        # 	开仓冻结金额
        # 	TSecurityFtdcMoneyType	ShortFrozenAmount;
        # 	开仓量
        # 	TSecurityFtdcVolumeType	OpenVolume;
        # 	平仓量
        # 	TSecurityFtdcVolumeType	CloseVolume;
        # 	开仓金额
        # 	TSecurityFtdcMoneyType	OpenAmount;
        # 	平仓金额
        # 	TSecurityFtdcMoneyType	CloseAmount;
        # 	持仓成本
        # 	TSecurityFtdcMoneyType	PositionCost;
        # 	冻结的资金
        # 	TSecurityFtdcMoneyType	FrozenCash;
        # 	资金差额
        # 	TSecurityFtdcMoneyType	CashIn;
        # 	手续费
        # 	TSecurityFtdcMoneyType	Commission;
        # 	上次结算价
        # 	TSecurityFtdcPriceType	PreSettlementPrice;
        # 	本次结算价
        # 	TSecurityFtdcPriceType	SettlementPrice;
        # 	交易日
        # 	TSecurityFtdcDateType	TradingDay;
        # 	开仓成本
        # 	TSecurityFtdcMoneyType	OpenCost;
        # 	交易所保证金
        # 	TSecurityFtdcMoneyType	ExchangeMargin;
        # 	今日持仓
        # 	TSecurityFtdcVolumeType	TodayPosition;
        # 	过户费
        # 	TSecurityFtdcMoneyType	TransferFee;
        # 	印花税
        # 	TSecurityFtdcMoneyType	StampTax;
        # 	今日申购赎回数量
        # 	TSecurityFtdcVolumeType	TodayPurRedVolume;
        # 	折算率
        # 	TSecurityFtdcRatioType	ConversionRate;
        # 	折算金额
        # 	TSecurityFtdcMoneyType	ConversionAmount;
        # 	证券价值
        # 	TSecurityFtdcMoneyType	StockValue;
        # 	交易所代码
        # 	TSecurityFtdcExchangeIDType	ExchangeID;
        # 	AccountID
        # 	TSecurityFtdcAccountIDType	AccountID;
        # 	质押入库数量
        # 	TSecurityFtdcVolumeType	PledgeInPosition;
        # 	正回购使用的标准券数量
        # 	TSecurityFtdcVolumeType	RepurchasePosition;
        # 	ETF申赎空头冻结
        # 	TSecurityFtdcVolumeType	PurRedShortFrozen;
        # 	融资买入出数量
        # 	TSecurityFtdcVolumeType	MarginTradeVolume;
        # 	融资买入金额
        # 	TSecurityFtdcMoneyType	MarginTradeAmount;
        # 	融资买入冻结数量
        # 	TSecurityFtdcVolumeType	MarginTradeFrozenVolume;
        # 	融资买入冻结金额
        # 	TSecurityFtdcMoneyType	MarginTradeFrozenAmount;
        # 	融资买入盈亏
        # 	TSecurityFtdcMoneyType	MarginTradeConversionProfit;
        # 	融券卖出数量
        # 	TSecurityFtdcVolumeType	ShortSellVolume;
        # 	融券卖出金额
        # 	TSecurityFtdcMoneyType	ShortSellAmount;
        # 	融券卖出冻结数量
        # 	TSecurityFtdcVolumeType	ShortSellFrozenVolume;
        # 	融券卖出冻结金额
        # 	TSecurityFtdcMoneyType	ShortSellFrozenAmount;
        # 	融券卖出盈亏
        # 	TSecurityFtdcMoneyType	ShortSellConversionProfit;
        # 	融券总市值
        # 	TSecurityFtdcMoneyType	SSStockValue;
        # 	今日融资持仓
        # 	TSecurityFtdcVolumeType	TodayMTPosition;
        # 	今日融券持仓
        # 	TSecurityFtdcVolumeType	TodaySSPosition;
        # 	历史持仓开仓成本
        # 	TSecurityFtdcMoneyType	YdOpenCost;
        # };