
#include "trader_struct.h"

static PyObject * mod=NULL;
PyObject * register_struct(PyObject * self, PyObject * args){
  mod = PyTuple_GetItem(args,0);
  Py_INCREF(Py_None);
  return Py_None;
}


PyObject *new_CSecurityFtdcRspInfoField(CSecurityFtdcRspInfoField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *)"CSecurityFtdcRspInfoField", (char *)"is",
                               p->ErrorID, p->ErrorMsg);
}

CSecurityFtdcRspInfoField *from_CSecurityFtdcRspInfoField(PyObject * p) {
    CSecurityFtdcRspInfoField *t = (CSecurityFtdcRspInfoField *) calloc(1, sizeof(CSecurityFtdcRspInfoField));
    memset(t, 0, sizeof(CSecurityFtdcRspInfoField));
    t->ErrorID = PyInt_AsLong(PyObject_GetAttrString(p, "ErrorID"));
    strcpy(t->ErrorMsg, PyString_AsString(PyObject_GetAttrString(p, "ErrorMsg")));

    return t;
};

PyObject *new_CSecurityFtdcExchangeField(CSecurityFtdcExchangeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcExchangeField", (char *) "ssc",
                               p->ExchangeID, p->ExchangeName, p->ExchangeProperty);
}

CSecurityFtdcExchangeField *from_CSecurityFtdcExchangeField(PyObject * p) {
    CSecurityFtdcExchangeField *t = (CSecurityFtdcExchangeField *) calloc(1, sizeof(CSecurityFtdcExchangeField));
    memset(t, 0, sizeof(CSecurityFtdcExchangeField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ExchangeName, PyString_AsString(PyObject_GetAttrString(p, "ExchangeName")));
    t->ExchangeProperty = PyString_AsString(PyObject_GetAttrString(p, "ExchangeProperty"))[0];

    return t;
};

PyObject *new_CSecurityFtdcProductField(CSecurityFtdcProductField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcProductField", (char *) "ssscidiiiicci",
                               p->ProductID, p->ProductName, p->ExchangeID, p->ProductClass, p->VolumeMultiple,
                               p->PriceTick, p->MaxMarketOrderVolume, p->MinMarketOrderVolume, p->MaxLimitOrderVolume,
                               p->MinLimitOrderVolume, p->PositionType, p->PositionDateType, p->EFTMinTradeVolume);
}

CSecurityFtdcProductField *from_CSecurityFtdcProductField(PyObject * p) {
    CSecurityFtdcProductField *t = (CSecurityFtdcProductField *) calloc(1, sizeof(CSecurityFtdcProductField));
    memset(t, 0, sizeof(CSecurityFtdcProductField));
    strcpy(t->ProductID, PyString_AsString(PyObject_GetAttrString(p, "ProductID")));
    strcpy(t->ProductName, PyString_AsString(PyObject_GetAttrString(p, "ProductName")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->ProductClass = PyString_AsString(PyObject_GetAttrString(p, "ProductClass"))[0];
    t->VolumeMultiple = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeMultiple"));
    t->PriceTick = PyFloat_AsDouble(PyObject_GetAttrString(p, "PriceTick"));
    t->MaxMarketOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MaxMarketOrderVolume"));
    t->MinMarketOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinMarketOrderVolume"));
    t->MaxLimitOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MaxLimitOrderVolume"));
    t->MinLimitOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinLimitOrderVolume"));
    t->PositionType = PyString_AsString(PyObject_GetAttrString(p, "PositionType"))[0];
    t->PositionDateType = PyString_AsString(PyObject_GetAttrString(p, "PositionDateType"))[0];
    t->EFTMinTradeVolume = PyInt_AsLong(PyObject_GetAttrString(p, "EFTMinTradeVolume"));

    return t;
};

PyObject *new_CSecurityFtdcInstrumentField(CSecurityFtdcInstrumentField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInstrumentField", (char *) "sssssciiiiiiidsssssciciiiscs",
                               p->InstrumentID, p->ExchangeID, p->InstrumentName, p->ExchangeInstID, p->ProductID,
                               p->ProductClass, p->DeliveryYear, p->DeliveryMonth, p->MaxMarketOrderVolume,
                               p->MinMarketOrderVolume, p->MaxLimitOrderVolume, p->MinLimitOrderVolume,
                               p->VolumeMultiple, p->PriceTick, p->CreateDate, p->OpenDate, p->ExpireDate,
                               p->StartDelivDate, p->EndDelivDate, p->InstLifePhase, p->IsTrading, p->PositionType,
                               p->OrderCanBeWithdraw, p->MinBuyVolume, p->MinSellVolume, p->RightModelID,
                               p->PosTradeType, p->MarketID);
}

CSecurityFtdcInstrumentField *from_CSecurityFtdcInstrumentField(PyObject * p) {
    CSecurityFtdcInstrumentField *t = (CSecurityFtdcInstrumentField *) calloc(1, sizeof(CSecurityFtdcInstrumentField));
    memset(t, 0, sizeof(CSecurityFtdcInstrumentField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->InstrumentName, PyString_AsString(PyObject_GetAttrString(p, "InstrumentName")));
    strcpy(t->ExchangeInstID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeInstID")));
    strcpy(t->ProductID, PyString_AsString(PyObject_GetAttrString(p, "ProductID")));
    t->ProductClass = PyString_AsString(PyObject_GetAttrString(p, "ProductClass"))[0];
    t->DeliveryYear = PyInt_AsLong(PyObject_GetAttrString(p, "DeliveryYear"));
    t->DeliveryMonth = PyInt_AsLong(PyObject_GetAttrString(p, "DeliveryMonth"));
    t->MaxMarketOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MaxMarketOrderVolume"));
    t->MinMarketOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinMarketOrderVolume"));
    t->MaxLimitOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MaxLimitOrderVolume"));
    t->MinLimitOrderVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinLimitOrderVolume"));
    t->VolumeMultiple = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeMultiple"));
    t->PriceTick = PyFloat_AsDouble(PyObject_GetAttrString(p, "PriceTick"));
    strcpy(t->CreateDate, PyString_AsString(PyObject_GetAttrString(p, "CreateDate")));
    strcpy(t->OpenDate, PyString_AsString(PyObject_GetAttrString(p, "OpenDate")));
    strcpy(t->ExpireDate, PyString_AsString(PyObject_GetAttrString(p, "ExpireDate")));
    strcpy(t->StartDelivDate, PyString_AsString(PyObject_GetAttrString(p, "StartDelivDate")));
    strcpy(t->EndDelivDate, PyString_AsString(PyObject_GetAttrString(p, "EndDelivDate")));
    t->InstLifePhase = PyString_AsString(PyObject_GetAttrString(p, "InstLifePhase"))[0];
    t->IsTrading = PyInt_AsLong(PyObject_GetAttrString(p, "IsTrading"));
    t->PositionType = PyString_AsString(PyObject_GetAttrString(p, "PositionType"))[0];
    t->OrderCanBeWithdraw = PyInt_AsLong(PyObject_GetAttrString(p, "OrderCanBeWithdraw"));
    t->MinBuyVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinBuyVolume"));
    t->MinSellVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinSellVolume"));
    strcpy(t->RightModelID, PyString_AsString(PyObject_GetAttrString(p, "RightModelID")));
    t->PosTradeType = PyString_AsString(PyObject_GetAttrString(p, "PosTradeType"))[0];
    strcpy(t->MarketID, PyString_AsString(PyObject_GetAttrString(p, "MarketID")));

    return t;
};

PyObject *new_CSecurityFtdcBrokerField(CSecurityFtdcBrokerField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcBrokerField", (char *) "sssi",
                               p->BrokerID, p->BrokerAbbr, p->BrokerName, p->IsActive);
}

CSecurityFtdcBrokerField *from_CSecurityFtdcBrokerField(PyObject * p) {
    CSecurityFtdcBrokerField *t = (CSecurityFtdcBrokerField *) calloc(1, sizeof(CSecurityFtdcBrokerField));
    memset(t, 0, sizeof(CSecurityFtdcBrokerField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->BrokerAbbr, PyString_AsString(PyObject_GetAttrString(p, "BrokerAbbr")));
    strcpy(t->BrokerName, PyString_AsString(PyObject_GetAttrString(p, "BrokerName")));
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));

    return t;
};

PyObject *new_CSecurityFtdcPartBrokerField(CSecurityFtdcPartBrokerField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcPartBrokerField", (char *) "sssi",
                               p->BrokerID, p->ExchangeID, p->ParticipantID, p->IsActive);
}

CSecurityFtdcPartBrokerField *from_CSecurityFtdcPartBrokerField(PyObject * p) {
    CSecurityFtdcPartBrokerField *t = (CSecurityFtdcPartBrokerField *) calloc(1, sizeof(CSecurityFtdcPartBrokerField));
    memset(t, 0, sizeof(CSecurityFtdcPartBrokerField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));

    return t;
};

PyObject *new_CSecurityFtdcInvestorField(CSecurityFtdcInvestorField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInvestorField", (char *) "sssscsiss",
                               p->InvestorID, p->BrokerID, p->InvestorGroupID, p->InvestorName, p->IdentifiedCardType,
                               p->IdentifiedCardNo, p->IsActive, p->SHBranchID, p->SZBranchID);
}

CSecurityFtdcInvestorField *from_CSecurityFtdcInvestorField(PyObject * p) {
    CSecurityFtdcInvestorField *t = (CSecurityFtdcInvestorField *) calloc(1, sizeof(CSecurityFtdcInvestorField));
    memset(t, 0, sizeof(CSecurityFtdcInvestorField));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorGroupID, PyString_AsString(PyObject_GetAttrString(p, "InvestorGroupID")));
    strcpy(t->InvestorName, PyString_AsString(PyObject_GetAttrString(p, "InvestorName")));
    t->IdentifiedCardType = PyString_AsString(PyObject_GetAttrString(p, "IdentifiedCardType"))[0];
    strcpy(t->IdentifiedCardNo, PyString_AsString(PyObject_GetAttrString(p, "IdentifiedCardNo")));
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));
    strcpy(t->SHBranchID, PyString_AsString(PyObject_GetAttrString(p, "SHBranchID")));
    strcpy(t->SZBranchID, PyString_AsString(PyObject_GetAttrString(p, "SZBranchID")));

    return t;
};

PyObject *new_CSecurityFtdcTradingCodeField(CSecurityFtdcTradingCodeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcTradingCodeField", (char *) "ssssissc",
                               p->InvestorID, p->BrokerID, p->ExchangeID, p->ClientID, p->IsActive, p->AccountID,
                               p->PBU, p->ClientType);
}

CSecurityFtdcTradingCodeField *from_CSecurityFtdcTradingCodeField(PyObject * p) {
    CSecurityFtdcTradingCodeField *t = (CSecurityFtdcTradingCodeField *) calloc(1,
                                                                                sizeof(CSecurityFtdcTradingCodeField));
    memset(t, 0, sizeof(CSecurityFtdcTradingCodeField));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ClientID, PyString_AsString(PyObject_GetAttrString(p, "ClientID")));
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    strcpy(t->PBU, PyString_AsString(PyObject_GetAttrString(p, "PBU")));
    t->ClientType = PyString_AsString(PyObject_GetAttrString(p, "ClientType"))[0];

    return t;
};

PyObject *new_CSecurityFtdcSuperUserField(CSecurityFtdcSuperUserField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcSuperUserField", (char *) "sssi",
                               p->UserID, p->UserName, p->Password, p->IsActive);
}

CSecurityFtdcSuperUserField *from_CSecurityFtdcSuperUserField(PyObject * p) {
    CSecurityFtdcSuperUserField *t = (CSecurityFtdcSuperUserField *) calloc(1, sizeof(CSecurityFtdcSuperUserField));
    memset(t, 0, sizeof(CSecurityFtdcSuperUserField));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->UserName, PyString_AsString(PyObject_GetAttrString(p, "UserName")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));

    return t;
};

PyObject *new_CSecurityFtdcSuperUserFunctionField(CSecurityFtdcSuperUserFunctionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcSuperUserFunctionField", (char *) "sc",
                               p->UserID, p->FunctionCode);
}

CSecurityFtdcSuperUserFunctionField *from_CSecurityFtdcSuperUserFunctionField(PyObject * p) {
    CSecurityFtdcSuperUserFunctionField *t = (CSecurityFtdcSuperUserFunctionField *) calloc(1,
                                                                                            sizeof(CSecurityFtdcSuperUserFunctionField));
    memset(t, 0, sizeof(CSecurityFtdcSuperUserFunctionField));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    t->FunctionCode = PyString_AsString(PyObject_GetAttrString(p, "FunctionCode"))[0];

    return t;
};

PyObject *new_CSecurityFtdcBrokerUserField(CSecurityFtdcBrokerUserField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcBrokerUserField", (char *) "ssscii",
                               p->BrokerID, p->UserID, p->UserName, p->UserType, p->IsActive, p->IsUsingOTP);
}

CSecurityFtdcBrokerUserField *from_CSecurityFtdcBrokerUserField(PyObject * p) {
    CSecurityFtdcBrokerUserField *t = (CSecurityFtdcBrokerUserField *) calloc(1, sizeof(CSecurityFtdcBrokerUserField));
    memset(t, 0, sizeof(CSecurityFtdcBrokerUserField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->UserName, PyString_AsString(PyObject_GetAttrString(p, "UserName")));
    t->UserType = PyString_AsString(PyObject_GetAttrString(p, "UserType"))[0];
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));
    t->IsUsingOTP = PyInt_AsLong(PyObject_GetAttrString(p, "IsUsingOTP"));

    return t;
};

PyObject *new_CSecurityFtdcBrokerUserFunctionField(CSecurityFtdcBrokerUserFunctionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcBrokerUserFunctionField", (char *) "ssc",
                               p->BrokerID, p->UserID, p->BrokerFunctionCode);
}

CSecurityFtdcBrokerUserFunctionField *from_CSecurityFtdcBrokerUserFunctionField(PyObject * p) {
    CSecurityFtdcBrokerUserFunctionField *t = (CSecurityFtdcBrokerUserFunctionField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcBrokerUserFunctionField));
    memset(t, 0, sizeof(CSecurityFtdcBrokerUserFunctionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    t->BrokerFunctionCode = PyString_AsString(PyObject_GetAttrString(p, "BrokerFunctionCode"))[0];

    return t;
};

PyObject *new_CSecurityFtdcTradingAccountField(CSecurityFtdcTradingAccountField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcTradingAccountField",
                               (char *) "ssdddddddddddddddddddsddddddddddddddscdddddd",
                               p->BrokerID, p->AccountID, p->PreMortgage, p->PreCredit, p->PreDeposit, p->PreBalance,
                               p->PreMargin, p->InterestBase, p->Interest, p->Deposit, p->Withdraw, p->FrozenMargin,
                               p->FrozenCash, p->FrozenCommission, p->CurrMargin, p->CashIn, p->Commission, p->Balance,
                               p->Available, p->WithdrawQuota, p->Reserve, p->TradingDay, p->Credit, p->Mortgage,
                               p->ExchangeMargin, p->DeliveryMargin, p->ExchangeDeliveryMargin, p->FrozenTransferFee,
                               p->FrozenStampTax, p->TransferFee, p->StampTax, p->ConversionAmount, p->CreditAmount,
                               p->StockValue, p->BondRepurchaseAmount, p->ReverseRepurchaseAmount, p->CurrencyCode,
                               p->AccountType, p->MarginTradeAmount, p->ShortSellAmount, p->MarginTradeProfit,
                               p->ShortSellProfit, p->SSStockValue, p->CreditRatio);
}

CSecurityFtdcTradingAccountField *from_CSecurityFtdcTradingAccountField(PyObject * p) {
    CSecurityFtdcTradingAccountField *t = (CSecurityFtdcTradingAccountField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcTradingAccountField));
    memset(t, 0, sizeof(CSecurityFtdcTradingAccountField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    t->PreMortgage = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreMortgage"));
    t->PreCredit = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreCredit"));
    t->PreDeposit = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreDeposit"));
    t->PreBalance = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreBalance"));
    t->PreMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreMargin"));
    t->InterestBase = PyFloat_AsDouble(PyObject_GetAttrString(p, "InterestBase"));
    t->Interest = PyFloat_AsDouble(PyObject_GetAttrString(p, "Interest"));
    t->Deposit = PyFloat_AsDouble(PyObject_GetAttrString(p, "Deposit"));
    t->Withdraw = PyFloat_AsDouble(PyObject_GetAttrString(p, "Withdraw"));
    t->FrozenMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "FrozenMargin"));
    t->FrozenCash = PyFloat_AsDouble(PyObject_GetAttrString(p, "FrozenCash"));
    t->FrozenCommission = PyFloat_AsDouble(PyObject_GetAttrString(p, "FrozenCommission"));
    t->CurrMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "CurrMargin"));
    t->CashIn = PyFloat_AsDouble(PyObject_GetAttrString(p, "CashIn"));
    t->Commission = PyFloat_AsDouble(PyObject_GetAttrString(p, "Commission"));
    t->Balance = PyFloat_AsDouble(PyObject_GetAttrString(p, "Balance"));
    t->Available = PyFloat_AsDouble(PyObject_GetAttrString(p, "Available"));
    t->WithdrawQuota = PyFloat_AsDouble(PyObject_GetAttrString(p, "WithdrawQuota"));
    t->Reserve = PyFloat_AsDouble(PyObject_GetAttrString(p, "Reserve"));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    t->Credit = PyFloat_AsDouble(PyObject_GetAttrString(p, "Credit"));
    t->Mortgage = PyFloat_AsDouble(PyObject_GetAttrString(p, "Mortgage"));
    t->ExchangeMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "ExchangeMargin"));
    t->DeliveryMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "DeliveryMargin"));
    t->ExchangeDeliveryMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "ExchangeDeliveryMargin"));
    t->FrozenTransferFee = PyFloat_AsDouble(PyObject_GetAttrString(p, "FrozenTransferFee"));
    t->FrozenStampTax = PyFloat_AsDouble(PyObject_GetAttrString(p, "FrozenStampTax"));
    t->TransferFee = PyFloat_AsDouble(PyObject_GetAttrString(p, "TransferFee"));
    t->StampTax = PyFloat_AsDouble(PyObject_GetAttrString(p, "StampTax"));
    t->ConversionAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ConversionAmount"));
    t->CreditAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "CreditAmount"));
    t->StockValue = PyFloat_AsDouble(PyObject_GetAttrString(p, "StockValue"));
    t->BondRepurchaseAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "BondRepurchaseAmount"));
    t->ReverseRepurchaseAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ReverseRepurchaseAmount"));
    strcpy(t->CurrencyCode, PyString_AsString(PyObject_GetAttrString(p, "CurrencyCode")));
    t->AccountType = PyString_AsString(PyObject_GetAttrString(p, "AccountType"))[0];
    t->MarginTradeAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "MarginTradeAmount"));
    t->ShortSellAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ShortSellAmount"));
    t->MarginTradeProfit = PyFloat_AsDouble(PyObject_GetAttrString(p, "MarginTradeProfit"));
    t->ShortSellProfit = PyFloat_AsDouble(PyObject_GetAttrString(p, "ShortSellProfit"));
    t->SSStockValue = PyFloat_AsDouble(PyObject_GetAttrString(p, "SSStockValue"));
    t->CreditRatio = PyFloat_AsDouble(PyObject_GetAttrString(p, "CreditRatio"));

    return t;
};

PyObject *new_CSecurityFtdcLoginForbiddenUserField(CSecurityFtdcLoginForbiddenUserField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcLoginForbiddenUserField", (char *) "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcLoginForbiddenUserField *from_CSecurityFtdcLoginForbiddenUserField(PyObject * p) {
    CSecurityFtdcLoginForbiddenUserField *t = (CSecurityFtdcLoginForbiddenUserField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcLoginForbiddenUserField));
    memset(t, 0, sizeof(CSecurityFtdcLoginForbiddenUserField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcDepthMarketDataField(CSecurityFtdcDepthMarketDataField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcDepthMarketDataField",
                               (char *) "ssssdddddddiddddddddsididididididididididids",
                               p->TradingDay, p->InstrumentID, p->ExchangeID, p->ExchangeInstID, p->LastPrice,
                               p->PreSettlementPrice, p->PreClosePrice, p->PreOpenInterest, p->OpenPrice,
                               p->HighestPrice, p->LowestPrice, p->Volume, p->Turnover, p->OpenInterest, p->ClosePrice,
                               p->SettlementPrice, p->UpperLimitPrice, p->LowerLimitPrice, p->PreDelta, p->CurrDelta,
                               p->UpdateTime, p->UpdateMillisec, p->BidPrice1, p->BidVolume1, p->AskPrice1,
                               p->AskVolume1, p->BidPrice2, p->BidVolume2, p->AskPrice2, p->AskVolume2, p->BidPrice3,
                               p->BidVolume3, p->AskPrice3, p->AskVolume3, p->BidPrice4, p->BidVolume4, p->AskPrice4,
                               p->AskVolume4, p->BidPrice5, p->BidVolume5, p->AskPrice5, p->AskVolume5, p->AveragePrice,
                               p->ActionDay);
}

CSecurityFtdcDepthMarketDataField *from_CSecurityFtdcDepthMarketDataField(PyObject * p) {
    CSecurityFtdcDepthMarketDataField *t = (CSecurityFtdcDepthMarketDataField *) calloc(1,
                                                                                        sizeof(CSecurityFtdcDepthMarketDataField));
    memset(t, 0, sizeof(CSecurityFtdcDepthMarketDataField));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ExchangeInstID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeInstID")));
    t->LastPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LastPrice"));
    t->PreSettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreSettlementPrice"));
    t->PreClosePrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreClosePrice"));
    t->PreOpenInterest = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreOpenInterest"));
    t->OpenPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenPrice"));
    t->HighestPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "HighestPrice"));
    t->LowestPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LowestPrice"));
    t->Volume = PyInt_AsLong(PyObject_GetAttrString(p, "Volume"));
    t->Turnover = PyFloat_AsDouble(PyObject_GetAttrString(p, "Turnover"));
    t->OpenInterest = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenInterest"));
    t->ClosePrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "ClosePrice"));
    t->SettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "SettlementPrice"));
    t->UpperLimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "UpperLimitPrice"));
    t->LowerLimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LowerLimitPrice"));
    t->PreDelta = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreDelta"));
    t->CurrDelta = PyFloat_AsDouble(PyObject_GetAttrString(p, "CurrDelta"));
    strcpy(t->UpdateTime, PyString_AsString(PyObject_GetAttrString(p, "UpdateTime")));
    t->UpdateMillisec = PyInt_AsLong(PyObject_GetAttrString(p, "UpdateMillisec"));
    t->BidPrice1 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice1"));
    t->BidVolume1 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume1"));
    t->AskPrice1 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice1"));
    t->AskVolume1 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume1"));
    t->BidPrice2 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice2"));
    t->BidVolume2 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume2"));
    t->AskPrice2 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice2"));
    t->AskVolume2 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume2"));
    t->BidPrice3 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice3"));
    t->BidVolume3 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume3"));
    t->AskPrice3 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice3"));
    t->AskVolume3 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume3"));
    t->BidPrice4 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice4"));
    t->BidVolume4 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume4"));
    t->AskPrice4 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice4"));
    t->AskVolume4 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume4"));
    t->BidPrice5 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice5"));
    t->BidVolume5 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume5"));
    t->AskPrice5 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice5"));
    t->AskVolume5 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume5"));
    t->AveragePrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "AveragePrice"));
    strcpy(t->ActionDay, PyString_AsString(PyObject_GetAttrString(p, "ActionDay")));

    return t;
};

PyObject *new_CSecurityFtdcInstrumentTradingRightField(CSecurityFtdcInstrumentTradingRightField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInstrumentTradingRightField", (char *) "scssccsc",
                               p->InstrumentID, p->InvestorRange, p->BrokerID, p->InvestorID, p->Direction,
                               p->TradingRight, p->ExchangeID, p->InstrumentRange);
}

CSecurityFtdcInstrumentTradingRightField *from_CSecurityFtdcInstrumentTradingRightField(PyObject * p) {
    CSecurityFtdcInstrumentTradingRightField *t = (CSecurityFtdcInstrumentTradingRightField *) calloc(1,
                                                                                                      sizeof(CSecurityFtdcInstrumentTradingRightField));
    memset(t, 0, sizeof(CSecurityFtdcInstrumentTradingRightField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    t->InvestorRange = PyString_AsString(PyObject_GetAttrString(p, "InvestorRange"))[0];
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    t->TradingRight = PyString_AsString(PyObject_GetAttrString(p, "TradingRight"))[0];
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->InstrumentRange = PyString_AsString(PyObject_GetAttrString(p, "InstrumentRange"))[0];

    return t;
};

PyObject *new_CSecurityFtdcInvestorPositionDetailField(CSecurityFtdcInvestorPositionDetailField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInvestorPositionDetailField",
                               (char *) "sssccssidscsddddiddddsiiid",
                               p->InstrumentID, p->BrokerID, p->InvestorID, p->HedgeFlag, p->Direction, p->OpenDate,
                               p->TradeID, p->Volume, p->OpenPrice, p->TradingDay, p->TradeType, p->ExchangeID,
                               p->Margin, p->ExchMargin, p->LastSettlementPrice, p->SettlementPrice, p->CloseVolume,
                               p->CloseAmount, p->TransferFee, p->StampTax, p->Commission, p->AccountID,
                               p->PledgeInPosition, p->PledgeInFrozenPosition, p->RepurchasePosition, p->Amount);
}

CSecurityFtdcInvestorPositionDetailField *from_CSecurityFtdcInvestorPositionDetailField(PyObject * p) {
    CSecurityFtdcInvestorPositionDetailField *t = (CSecurityFtdcInvestorPositionDetailField *) calloc(1,
                                                                                                      sizeof(CSecurityFtdcInvestorPositionDetailField));
    memset(t, 0, sizeof(CSecurityFtdcInvestorPositionDetailField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->HedgeFlag = PyString_AsString(PyObject_GetAttrString(p, "HedgeFlag"))[0];
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    strcpy(t->OpenDate, PyString_AsString(PyObject_GetAttrString(p, "OpenDate")));
    strcpy(t->TradeID, PyString_AsString(PyObject_GetAttrString(p, "TradeID")));
    t->Volume = PyInt_AsLong(PyObject_GetAttrString(p, "Volume"));
    t->OpenPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenPrice"));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    t->TradeType = PyString_AsString(PyObject_GetAttrString(p, "TradeType"))[0];
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->Margin = PyFloat_AsDouble(PyObject_GetAttrString(p, "Margin"));
    t->ExchMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "ExchMargin"));
    t->LastSettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LastSettlementPrice"));
    t->SettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "SettlementPrice"));
    t->CloseVolume = PyInt_AsLong(PyObject_GetAttrString(p, "CloseVolume"));
    t->CloseAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "CloseAmount"));
    t->TransferFee = PyFloat_AsDouble(PyObject_GetAttrString(p, "TransferFee"));
    t->StampTax = PyFloat_AsDouble(PyObject_GetAttrString(p, "StampTax"));
    t->Commission = PyFloat_AsDouble(PyObject_GetAttrString(p, "Commission"));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    t->PledgeInPosition = PyInt_AsLong(PyObject_GetAttrString(p, "PledgeInPosition"));
    t->PledgeInFrozenPosition = PyInt_AsLong(PyObject_GetAttrString(p, "PledgeInFrozenPosition"));
    t->RepurchasePosition = PyInt_AsLong(PyObject_GetAttrString(p, "RepurchasePosition"));
    t->Amount = PyFloat_AsDouble(PyObject_GetAttrString(p, "Amount"));

    return t;
};

PyObject *new_CSecurityFtdcBondInterestField(CSecurityFtdcBondInterestField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcBondInterestField", (char *) "sssd",
                               p->TradingDay, p->ExchangeID, p->InstrumentID, p->Interest);
}

CSecurityFtdcBondInterestField *from_CSecurityFtdcBondInterestField(PyObject * p) {
    CSecurityFtdcBondInterestField *t = (CSecurityFtdcBondInterestField *) calloc(1,
                                                                                  sizeof(CSecurityFtdcBondInterestField));
    memset(t, 0, sizeof(CSecurityFtdcBondInterestField));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    t->Interest = PyFloat_AsDouble(PyObject_GetAttrString(p, "Interest"));

    return t;
};

PyObject *new_CSecurityFtdcMarketRationInfoField(CSecurityFtdcMarketRationInfoField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketRationInfoField", (char *) "sssi",
                               p->BrokerID, p->InvestorID, p->ExchangeID, p->RationVolume);
}

CSecurityFtdcMarketRationInfoField *from_CSecurityFtdcMarketRationInfoField(PyObject * p) {
    CSecurityFtdcMarketRationInfoField *t = (CSecurityFtdcMarketRationInfoField *) calloc(1,
                                                                                          sizeof(CSecurityFtdcMarketRationInfoField));
    memset(t, 0, sizeof(CSecurityFtdcMarketRationInfoField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->RationVolume = PyInt_AsLong(PyObject_GetAttrString(p, "RationVolume"));

    return t;
};

PyObject *new_CSecurityFtdcInstrumentCommissionRateField(CSecurityFtdcInstrumentCommissionRateField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInstrumentCommissionRateField", (char *) "sscsscdddddddd",
                               p->ExchangeID, p->InstrumentID, p->InvestorRange, p->BrokerID, p->InvestorID,
                               p->Direction, p->StampTaxRateByMoney, p->StampTaxRateByVolume, p->TransferFeeRateByMoney,
                               p->TransferFeeRateByVolume, p->TradeFeeByMoney, p->TradeFeeByVolume, p->MarginByMoney,
                               p->MinTradeFee);
}

CSecurityFtdcInstrumentCommissionRateField *from_CSecurityFtdcInstrumentCommissionRateField(PyObject * p) {
    CSecurityFtdcInstrumentCommissionRateField *t = (CSecurityFtdcInstrumentCommissionRateField *) calloc(1,
                                                                                                          sizeof(CSecurityFtdcInstrumentCommissionRateField));
    memset(t, 0, sizeof(CSecurityFtdcInstrumentCommissionRateField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    t->InvestorRange = PyString_AsString(PyObject_GetAttrString(p, "InvestorRange"))[0];
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    t->StampTaxRateByMoney = PyFloat_AsDouble(PyObject_GetAttrString(p, "StampTaxRateByMoney"));
    t->StampTaxRateByVolume = PyFloat_AsDouble(PyObject_GetAttrString(p, "StampTaxRateByVolume"));
    t->TransferFeeRateByMoney = PyFloat_AsDouble(PyObject_GetAttrString(p, "TransferFeeRateByMoney"));
    t->TransferFeeRateByVolume = PyFloat_AsDouble(PyObject_GetAttrString(p, "TransferFeeRateByVolume"));
    t->TradeFeeByMoney = PyFloat_AsDouble(PyObject_GetAttrString(p, "TradeFeeByMoney"));
    t->TradeFeeByVolume = PyFloat_AsDouble(PyObject_GetAttrString(p, "TradeFeeByVolume"));
    t->MarginByMoney = PyFloat_AsDouble(PyObject_GetAttrString(p, "MarginByMoney"));
    t->MinTradeFee = PyFloat_AsDouble(PyObject_GetAttrString(p, "MinTradeFee"));

    return t;
};

PyObject *new_CSecurityFtdcExcessStockInfoField(CSecurityFtdcExcessStockInfoField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcExcessStockInfoField", (char *) "ssssii",
                               p->BrokerID, p->InvestorID, p->ExchangeID, p->InstrumentID, p->ExcessVolume,
                               p->ExcessFrozenVolume);
}

CSecurityFtdcExcessStockInfoField *from_CSecurityFtdcExcessStockInfoField(PyObject * p) {
    CSecurityFtdcExcessStockInfoField *t = (CSecurityFtdcExcessStockInfoField *) calloc(1,
                                                                                        sizeof(CSecurityFtdcExcessStockInfoField));
    memset(t, 0, sizeof(CSecurityFtdcExcessStockInfoField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    t->ExcessVolume = PyInt_AsLong(PyObject_GetAttrString(p, "ExcessVolume"));
    t->ExcessFrozenVolume = PyInt_AsLong(PyObject_GetAttrString(p, "ExcessFrozenVolume"));

    return t;
};

PyObject *new_CSecurityFtdcTraderOfferField(CSecurityFtdcTraderOfferField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcTraderOfferField", (char *) "ssssiscssssssssss",
                               p->ExchangeID, p->BranchPBU, p->ParticipantID, p->Password, p->InstallID,
                               p->OrderLocalID, p->TraderConnectStatus, p->ConnectRequestDate, p->ConnectRequestTime,
                               p->LastReportDate, p->LastReportTime, p->ConnectDate, p->ConnectTime, p->StartDate,
                               p->StartTime, p->TradingDay, p->BrokerID);
}

CSecurityFtdcTraderOfferField *from_CSecurityFtdcTraderOfferField(PyObject * p) {
    CSecurityFtdcTraderOfferField *t = (CSecurityFtdcTraderOfferField *) calloc(1,
                                                                                sizeof(CSecurityFtdcTraderOfferField));
    memset(t, 0, sizeof(CSecurityFtdcTraderOfferField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));
    t->InstallID = PyInt_AsLong(PyObject_GetAttrString(p, "InstallID"));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));
    t->TraderConnectStatus = PyString_AsString(PyObject_GetAttrString(p, "TraderConnectStatus"))[0];
    strcpy(t->ConnectRequestDate, PyString_AsString(PyObject_GetAttrString(p, "ConnectRequestDate")));
    strcpy(t->ConnectRequestTime, PyString_AsString(PyObject_GetAttrString(p, "ConnectRequestTime")));
    strcpy(t->LastReportDate, PyString_AsString(PyObject_GetAttrString(p, "LastReportDate")));
    strcpy(t->LastReportTime, PyString_AsString(PyObject_GetAttrString(p, "LastReportTime")));
    strcpy(t->ConnectDate, PyString_AsString(PyObject_GetAttrString(p, "ConnectDate")));
    strcpy(t->ConnectTime, PyString_AsString(PyObject_GetAttrString(p, "ConnectTime")));
    strcpy(t->StartDate, PyString_AsString(PyObject_GetAttrString(p, "StartDate")));
    strcpy(t->StartTime, PyString_AsString(PyObject_GetAttrString(p, "StartTime")));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));

    return t;
};

PyObject *new_CSecurityFtdcMDTraderOfferField(CSecurityFtdcMDTraderOfferField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMDTraderOfferField", (char *) "ssssiscssssssssss",
                               p->ExchangeID, p->BranchPBU, p->ParticipantID, p->Password, p->InstallID,
                               p->OrderLocalID, p->TraderConnectStatus, p->ConnectRequestDate, p->ConnectRequestTime,
                               p->LastReportDate, p->LastReportTime, p->ConnectDate, p->ConnectTime, p->StartDate,
                               p->StartTime, p->TradingDay, p->BrokerID);
}

CSecurityFtdcMDTraderOfferField *from_CSecurityFtdcMDTraderOfferField(PyObject * p) {
    CSecurityFtdcMDTraderOfferField *t = (CSecurityFtdcMDTraderOfferField *) calloc(1,
                                                                                    sizeof(CSecurityFtdcMDTraderOfferField));
    memset(t, 0, sizeof(CSecurityFtdcMDTraderOfferField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));
    t->InstallID = PyInt_AsLong(PyObject_GetAttrString(p, "InstallID"));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));
    t->TraderConnectStatus = PyString_AsString(PyObject_GetAttrString(p, "TraderConnectStatus"))[0];
    strcpy(t->ConnectRequestDate, PyString_AsString(PyObject_GetAttrString(p, "ConnectRequestDate")));
    strcpy(t->ConnectRequestTime, PyString_AsString(PyObject_GetAttrString(p, "ConnectRequestTime")));
    strcpy(t->LastReportDate, PyString_AsString(PyObject_GetAttrString(p, "LastReportDate")));
    strcpy(t->LastReportTime, PyString_AsString(PyObject_GetAttrString(p, "LastReportTime")));
    strcpy(t->ConnectDate, PyString_AsString(PyObject_GetAttrString(p, "ConnectDate")));
    strcpy(t->ConnectTime, PyString_AsString(PyObject_GetAttrString(p, "ConnectTime")));
    strcpy(t->StartDate, PyString_AsString(PyObject_GetAttrString(p, "StartDate")));
    strcpy(t->StartTime, PyString_AsString(PyObject_GetAttrString(p, "StartTime")));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));

    return t;
};

PyObject *new_CSecurityFtdcFrontStatusField(CSecurityFtdcFrontStatusField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcFrontStatusField", (char *) "issi",
                               p->FrontID, p->LastReportDate, p->LastReportTime, p->IsActive);
}

CSecurityFtdcFrontStatusField *from_CSecurityFtdcFrontStatusField(PyObject * p) {
    CSecurityFtdcFrontStatusField *t = (CSecurityFtdcFrontStatusField *) calloc(1,
                                                                                sizeof(CSecurityFtdcFrontStatusField));
    memset(t, 0, sizeof(CSecurityFtdcFrontStatusField));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    strcpy(t->LastReportDate, PyString_AsString(PyObject_GetAttrString(p, "LastReportDate")));
    strcpy(t->LastReportTime, PyString_AsString(PyObject_GetAttrString(p, "LastReportTime")));
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));

    return t;
};

PyObject *new_CSecurityFtdcUserSessionField(CSecurityFtdcUserSessionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcUserSessionField", (char *) "iisssssssss",
                               p->FrontID, p->SessionID, p->BrokerID, p->UserID, p->LoginDate, p->LoginTime,
                               p->IPAddress, p->UserProductInfo, p->InterfaceProductInfo, p->ProtocolInfo,
                               p->MacAddress);
}

CSecurityFtdcUserSessionField *from_CSecurityFtdcUserSessionField(PyObject * p) {
    CSecurityFtdcUserSessionField *t = (CSecurityFtdcUserSessionField *) calloc(1,
                                                                                sizeof(CSecurityFtdcUserSessionField));
    memset(t, 0, sizeof(CSecurityFtdcUserSessionField));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->LoginDate, PyString_AsString(PyObject_GetAttrString(p, "LoginDate")));
    strcpy(t->LoginTime, PyString_AsString(PyObject_GetAttrString(p, "LoginTime")));
    strcpy(t->IPAddress, PyString_AsString(PyObject_GetAttrString(p, "IPAddress")));
    strcpy(t->UserProductInfo, PyString_AsString(PyObject_GetAttrString(p, "UserProductInfo")));
    strcpy(t->InterfaceProductInfo, PyString_AsString(PyObject_GetAttrString(p, "InterfaceProductInfo")));
    strcpy(t->ProtocolInfo, PyString_AsString(PyObject_GetAttrString(p, "ProtocolInfo")));
    strcpy(t->MacAddress, PyString_AsString(PyObject_GetAttrString(p, "MacAddress")));

    return t;
};

PyObject *new_CSecurityFtdcOrderField(CSecurityFtdcOrderField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcOrderField",
                               (char *) "ssssssccsssicscicdcisisssssicsissccciissssssssiiissisissdi",
                               p->BrokerID, p->InvestorID, p->InstrumentID, p->OrderRef, p->UserID, p->ExchangeID,
                               p->OrderPriceType, p->Direction, p->CombOffsetFlag, p->CombHedgeFlag, p->LimitPrice,
                               p->VolumeTotalOriginal, p->TimeCondition, p->GTDDate, p->VolumeCondition, p->MinVolume,
                               p->ContingentCondition, p->StopPrice, p->ForceCloseReason, p->IsAutoSuspend,
                               p->BusinessUnit, p->RequestID, p->OrderLocalID, p->ParticipantID, p->ClientID,
                               p->ExchangeInstID, p->BranchPBU, p->InstallID, p->OrderSubmitStatus, p->AccountID,
                               p->NotifySequence, p->TradingDay, p->OrderSysID, p->OrderSource, p->OrderStatus,
                               p->OrderType, p->VolumeTraded, p->VolumeTotal, p->InsertDate, p->InsertTime,
                               p->ActiveTime, p->SuspendTime, p->UpdateTime, p->CancelTime, p->ActiveTraderID,
                               p->ClearingPartID, p->SequenceNo, p->FrontID, p->SessionID, p->UserProductInfo,
                               p->StatusMsg, p->UserForceClose, p->ActiveUserID, p->BrokerOrderSeq,
                               p->RelativeOrderSysID, p->BranchID, p->TradeAmount, p->IsETF);
}

CSecurityFtdcOrderField *from_CSecurityFtdcOrderField(PyObject * p) {
    CSecurityFtdcOrderField *t = (CSecurityFtdcOrderField *) calloc(1, sizeof(CSecurityFtdcOrderField));
    memset(t, 0, sizeof(CSecurityFtdcOrderField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->OrderPriceType = PyString_AsString(PyObject_GetAttrString(p, "OrderPriceType"))[0];
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    strcpy(t->CombOffsetFlag, PyString_AsString(PyObject_GetAttrString(p, "CombOffsetFlag")));
    strcpy(t->CombHedgeFlag, PyString_AsString(PyObject_GetAttrString(p, "CombHedgeFlag")));
    strcpy(t->LimitPrice, PyString_AsString(PyObject_GetAttrString(p, "LimitPrice")));
    t->VolumeTotalOriginal = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeTotalOriginal"));
    t->TimeCondition = PyString_AsString(PyObject_GetAttrString(p, "TimeCondition"))[0];
    strcpy(t->GTDDate, PyString_AsString(PyObject_GetAttrString(p, "GTDDate")));
    t->VolumeCondition = PyString_AsString(PyObject_GetAttrString(p, "VolumeCondition"))[0];
    t->MinVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinVolume"));
    t->ContingentCondition = PyString_AsString(PyObject_GetAttrString(p, "ContingentCondition"))[0];
    t->StopPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "StopPrice"));
    t->ForceCloseReason = PyString_AsString(PyObject_GetAttrString(p, "ForceCloseReason"))[0];
    t->IsAutoSuspend = PyInt_AsLong(PyObject_GetAttrString(p, "IsAutoSuspend"));
    strcpy(t->BusinessUnit, PyString_AsString(PyObject_GetAttrString(p, "BusinessUnit")));
    t->RequestID = PyInt_AsLong(PyObject_GetAttrString(p, "RequestID"));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->ClientID, PyString_AsString(PyObject_GetAttrString(p, "ClientID")));
    strcpy(t->ExchangeInstID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeInstID")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    t->InstallID = PyInt_AsLong(PyObject_GetAttrString(p, "InstallID"));
    t->OrderSubmitStatus = PyString_AsString(PyObject_GetAttrString(p, "OrderSubmitStatus"))[0];
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    t->NotifySequence = PyInt_AsLong(PyObject_GetAttrString(p, "NotifySequence"));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->OrderSysID, PyString_AsString(PyObject_GetAttrString(p, "OrderSysID")));
    t->OrderSource = PyString_AsString(PyObject_GetAttrString(p, "OrderSource"))[0];
    t->OrderStatus = PyString_AsString(PyObject_GetAttrString(p, "OrderStatus"))[0];
    t->OrderType = PyString_AsString(PyObject_GetAttrString(p, "OrderType"))[0];
    t->VolumeTraded = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeTraded"));
    t->VolumeTotal = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeTotal"));
    strcpy(t->InsertDate, PyString_AsString(PyObject_GetAttrString(p, "InsertDate")));
    strcpy(t->InsertTime, PyString_AsString(PyObject_GetAttrString(p, "InsertTime")));
    strcpy(t->ActiveTime, PyString_AsString(PyObject_GetAttrString(p, "ActiveTime")));
    strcpy(t->SuspendTime, PyString_AsString(PyObject_GetAttrString(p, "SuspendTime")));
    strcpy(t->UpdateTime, PyString_AsString(PyObject_GetAttrString(p, "UpdateTime")));
    strcpy(t->CancelTime, PyString_AsString(PyObject_GetAttrString(p, "CancelTime")));
    strcpy(t->ActiveTraderID, PyString_AsString(PyObject_GetAttrString(p, "ActiveTraderID")));
    strcpy(t->ClearingPartID, PyString_AsString(PyObject_GetAttrString(p, "ClearingPartID")));
    t->SequenceNo = PyInt_AsLong(PyObject_GetAttrString(p, "SequenceNo"));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->UserProductInfo, PyString_AsString(PyObject_GetAttrString(p, "UserProductInfo")));
    strcpy(t->StatusMsg, PyString_AsString(PyObject_GetAttrString(p, "StatusMsg")));
    t->UserForceClose = PyInt_AsLong(PyObject_GetAttrString(p, "UserForceClose"));
    strcpy(t->ActiveUserID, PyString_AsString(PyObject_GetAttrString(p, "ActiveUserID")));
    t->BrokerOrderSeq = PyInt_AsLong(PyObject_GetAttrString(p, "BrokerOrderSeq"));
    strcpy(t->RelativeOrderSysID, PyString_AsString(PyObject_GetAttrString(p, "RelativeOrderSysID")));
    strcpy(t->BranchID, PyString_AsString(PyObject_GetAttrString(p, "BranchID")));
    t->TradeAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "TradeAmount"));
    t->IsETF = PyInt_AsLong(PyObject_GetAttrString(p, "IsETF"));

    return t;
};

PyObject *new_CSecurityFtdcOrderActionField(CSecurityFtdcOrderActionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcOrderActionField", (char *) "ssisiiiscdisssissssscssss",
                               p->BrokerID, p->InvestorID, p->OrderActionRef, p->OrderRef, p->RequestID, p->FrontID,
                               p->SessionID, p->ExchangeID, p->ActionFlag, p->LimitPrice, p->VolumeChange,
                               p->ActionDate, p->ActionTime, p->BranchPBU, p->InstallID, p->OrderLocalID,
                               p->ActionLocalID, p->ParticipantID, p->ClientID, p->BusinessUnit, p->OrderActionStatus,
                               p->UserID, p->BranchID, p->StatusMsg, p->InstrumentID);
}

CSecurityFtdcOrderActionField *from_CSecurityFtdcOrderActionField(PyObject * p) {
    CSecurityFtdcOrderActionField *t = (CSecurityFtdcOrderActionField *) calloc(1,
                                                                                sizeof(CSecurityFtdcOrderActionField));
    memset(t, 0, sizeof(CSecurityFtdcOrderActionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->OrderActionRef = PyInt_AsLong(PyObject_GetAttrString(p, "OrderActionRef"));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    t->RequestID = PyInt_AsLong(PyObject_GetAttrString(p, "RequestID"));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->ActionFlag = PyString_AsString(PyObject_GetAttrString(p, "ActionFlag"))[0];
    t->LimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LimitPrice"));
    t->VolumeChange = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeChange"));
    strcpy(t->ActionDate, PyString_AsString(PyObject_GetAttrString(p, "ActionDate")));
    strcpy(t->ActionTime, PyString_AsString(PyObject_GetAttrString(p, "ActionTime")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    t->InstallID = PyInt_AsLong(PyObject_GetAttrString(p, "InstallID"));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));
    strcpy(t->ActionLocalID, PyString_AsString(PyObject_GetAttrString(p, "ActionLocalID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->ClientID, PyString_AsString(PyObject_GetAttrString(p, "ClientID")));
    strcpy(t->BusinessUnit, PyString_AsString(PyObject_GetAttrString(p, "BusinessUnit")));
    t->OrderActionStatus = PyString_AsString(PyObject_GetAttrString(p, "OrderActionStatus"))[0];
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->BranchID, PyString_AsString(PyObject_GetAttrString(p, "BranchID")));
    strcpy(t->StatusMsg, PyString_AsString(PyObject_GetAttrString(p, "StatusMsg")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcErrOrderField(CSecurityFtdcErrOrderField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcErrOrderField", (char *) "ssssssccsssicscicdcisiiis",
                               p->BrokerID, p->InvestorID, p->InstrumentID, p->OrderRef, p->UserID, p->ExchangeID,
                               p->OrderPriceType, p->Direction, p->CombOffsetFlag, p->CombHedgeFlag, p->LimitPrice,
                               p->VolumeTotalOriginal, p->TimeCondition, p->GTDDate, p->VolumeCondition, p->MinVolume,
                               p->ContingentCondition, p->StopPrice, p->ForceCloseReason, p->IsAutoSuspend,
                               p->BusinessUnit, p->RequestID, p->UserForceClose, p->ErrorID, p->ErrorMsg);
}

CSecurityFtdcErrOrderField *from_CSecurityFtdcErrOrderField(PyObject * p) {
    CSecurityFtdcErrOrderField *t = (CSecurityFtdcErrOrderField *) calloc(1, sizeof(CSecurityFtdcErrOrderField));
    memset(t, 0, sizeof(CSecurityFtdcErrOrderField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->OrderPriceType = PyString_AsString(PyObject_GetAttrString(p, "OrderPriceType"))[0];
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    strcpy(t->CombOffsetFlag, PyString_AsString(PyObject_GetAttrString(p, "CombOffsetFlag")));
    strcpy(t->CombHedgeFlag, PyString_AsString(PyObject_GetAttrString(p, "CombHedgeFlag")));
    strcpy(t->LimitPrice, PyString_AsString(PyObject_GetAttrString(p, "LimitPrice")));
    t->VolumeTotalOriginal = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeTotalOriginal"));
    t->TimeCondition = PyString_AsString(PyObject_GetAttrString(p, "TimeCondition"))[0];
    strcpy(t->GTDDate, PyString_AsString(PyObject_GetAttrString(p, "GTDDate")));
    t->VolumeCondition = PyString_AsString(PyObject_GetAttrString(p, "VolumeCondition"))[0];
    t->MinVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinVolume"));
    t->ContingentCondition = PyString_AsString(PyObject_GetAttrString(p, "ContingentCondition"))[0];
    t->StopPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "StopPrice"));
    t->ForceCloseReason = PyString_AsString(PyObject_GetAttrString(p, "ForceCloseReason"))[0];
    t->IsAutoSuspend = PyInt_AsLong(PyObject_GetAttrString(p, "IsAutoSuspend"));
    strcpy(t->BusinessUnit, PyString_AsString(PyObject_GetAttrString(p, "BusinessUnit")));
    t->RequestID = PyInt_AsLong(PyObject_GetAttrString(p, "RequestID"));
    t->UserForceClose = PyInt_AsLong(PyObject_GetAttrString(p, "UserForceClose"));
    t->ErrorID = PyInt_AsLong(PyObject_GetAttrString(p, "ErrorID"));
    strcpy(t->ErrorMsg, PyString_AsString(PyObject_GetAttrString(p, "ErrorMsg")));

    return t;
};

PyObject *new_CSecurityFtdcErrOrderActionField(CSecurityFtdcErrOrderActionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcErrOrderActionField", (char *) "ssisiiiscdisssissssscssssis",
                               p->BrokerID, p->InvestorID, p->OrderActionRef, p->OrderRef, p->RequestID, p->FrontID,
                               p->SessionID, p->ExchangeID, p->ActionFlag, p->LimitPrice, p->VolumeChange,
                               p->ActionDate, p->ActionTime, p->BranchPBU, p->InstallID, p->OrderLocalID,
                               p->ActionLocalID, p->ParticipantID, p->ClientID, p->BusinessUnit, p->OrderActionStatus,
                               p->UserID, p->BranchID, p->StatusMsg, p->InstrumentID, p->ErrorID, p->ErrorMsg);
}

CSecurityFtdcErrOrderActionField *from_CSecurityFtdcErrOrderActionField(PyObject * p) {
    CSecurityFtdcErrOrderActionField *t = (CSecurityFtdcErrOrderActionField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcErrOrderActionField));
    memset(t, 0, sizeof(CSecurityFtdcErrOrderActionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->OrderActionRef = PyInt_AsLong(PyObject_GetAttrString(p, "OrderActionRef"));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    t->RequestID = PyInt_AsLong(PyObject_GetAttrString(p, "RequestID"));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->ActionFlag = PyString_AsString(PyObject_GetAttrString(p, "ActionFlag"))[0];
    t->LimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LimitPrice"));
    t->VolumeChange = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeChange"));
    strcpy(t->ActionDate, PyString_AsString(PyObject_GetAttrString(p, "ActionDate")));
    strcpy(t->ActionTime, PyString_AsString(PyObject_GetAttrString(p, "ActionTime")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    t->InstallID = PyInt_AsLong(PyObject_GetAttrString(p, "InstallID"));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));
    strcpy(t->ActionLocalID, PyString_AsString(PyObject_GetAttrString(p, "ActionLocalID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->ClientID, PyString_AsString(PyObject_GetAttrString(p, "ClientID")));
    strcpy(t->BusinessUnit, PyString_AsString(PyObject_GetAttrString(p, "BusinessUnit")));
    t->OrderActionStatus = PyString_AsString(PyObject_GetAttrString(p, "OrderActionStatus"))[0];
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->BranchID, PyString_AsString(PyObject_GetAttrString(p, "BranchID")));
    strcpy(t->StatusMsg, PyString_AsString(PyObject_GetAttrString(p, "StatusMsg")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    t->ErrorID = PyInt_AsLong(PyObject_GetAttrString(p, "ErrorID"));
    strcpy(t->ErrorMsg, PyString_AsString(PyObject_GetAttrString(p, "ErrorMsg")));

    return t;
};

PyObject *new_CSecurityFtdcTradeField(CSecurityFtdcTradeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcTradeField", (char *) "ssssssscssscsccsissccssssicsi",
                               p->BrokerID, p->InvestorID, p->InstrumentID, p->OrderRef, p->UserID, p->ExchangeID,
                               p->TradeID, p->Direction, p->OrderSysID, p->ParticipantID, p->ClientID, p->TradingRole,
                               p->ExchangeInstID, p->OffsetFlag, p->HedgeFlag, p->Price, p->Volume, p->TradeDate,
                               p->TradeTime, p->TradeType, p->PriceSource, p->BranchPBU, p->OrderLocalID,
                               p->ClearingPartID, p->BusinessUnit, p->SequenceNo, p->TradeSource, p->TradingDay,
                               p->BrokerOrderSeq);
}

CSecurityFtdcTradeField *from_CSecurityFtdcTradeField(PyObject * p) {
    CSecurityFtdcTradeField *t = (CSecurityFtdcTradeField *) calloc(1, sizeof(CSecurityFtdcTradeField));
    memset(t, 0, sizeof(CSecurityFtdcTradeField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->TradeID, PyString_AsString(PyObject_GetAttrString(p, "TradeID")));
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    strcpy(t->OrderSysID, PyString_AsString(PyObject_GetAttrString(p, "OrderSysID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->ClientID, PyString_AsString(PyObject_GetAttrString(p, "ClientID")));
    t->TradingRole = PyString_AsString(PyObject_GetAttrString(p, "TradingRole"))[0];
    strcpy(t->ExchangeInstID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeInstID")));
    t->OffsetFlag = PyString_AsString(PyObject_GetAttrString(p, "OffsetFlag"))[0];
    t->HedgeFlag = PyString_AsString(PyObject_GetAttrString(p, "HedgeFlag"))[0];
    strcpy(t->Price, PyString_AsString(PyObject_GetAttrString(p, "Price")));
    t->Volume = PyInt_AsLong(PyObject_GetAttrString(p, "Volume"));
    strcpy(t->TradeDate, PyString_AsString(PyObject_GetAttrString(p, "TradeDate")));
    strcpy(t->TradeTime, PyString_AsString(PyObject_GetAttrString(p, "TradeTime")));
    t->TradeType = PyString_AsString(PyObject_GetAttrString(p, "TradeType"))[0];
    t->PriceSource = PyString_AsString(PyObject_GetAttrString(p, "PriceSource"))[0];
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));
    strcpy(t->ClearingPartID, PyString_AsString(PyObject_GetAttrString(p, "ClearingPartID")));
    strcpy(t->BusinessUnit, PyString_AsString(PyObject_GetAttrString(p, "BusinessUnit")));
    t->SequenceNo = PyInt_AsLong(PyObject_GetAttrString(p, "SequenceNo"));
    t->TradeSource = PyString_AsString(PyObject_GetAttrString(p, "TradeSource"))[0];
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    t->BrokerOrderSeq = PyInt_AsLong(PyObject_GetAttrString(p, "BrokerOrderSeq"));

    return t;
};

PyObject *new_CSecurityFtdcInvestorPositionField(CSecurityFtdcInvestorPositionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInvestorPositionField",
                               (char *) "sssccciiiiddiiddddddddsddiddidddssiiiididdididddiid",
                               p->InstrumentID, p->BrokerID, p->InvestorID, p->PosiDirection, p->HedgeFlag,
                               p->PositionDate, p->YdPosition, p->Position, p->LongFrozen, p->ShortFrozen,
                               p->LongFrozenAmount, p->ShortFrozenAmount, p->OpenVolume, p->CloseVolume, p->OpenAmount,
                               p->CloseAmount, p->PositionCost, p->FrozenCash, p->CashIn, p->Commission,
                               p->PreSettlementPrice, p->SettlementPrice, p->TradingDay, p->OpenCost, p->ExchangeMargin,
                               p->TodayPosition, p->TransferFee, p->StampTax, p->TodayPurRedVolume, p->ConversionRate,
                               p->ConversionAmount, p->StockValue, p->ExchangeID, p->AccountID, p->PledgeInPosition,
                               p->RepurchasePosition, p->PurRedShortFrozen, p->MarginTradeVolume, p->MarginTradeAmount,
                               p->MarginTradeFrozenVolume, p->MarginTradeFrozenAmount, p->MarginTradeConversionProfit,
                               p->ShortSellVolume, p->ShortSellAmount, p->ShortSellFrozenVolume,
                               p->ShortSellFrozenAmount, p->ShortSellConversionProfit, p->SSStockValue,
                               p->TodayMTPosition, p->TodaySSPosition, p->YdOpenCost);
}

CSecurityFtdcInvestorPositionField *from_CSecurityFtdcInvestorPositionField(PyObject * p) {
    CSecurityFtdcInvestorPositionField *t = (CSecurityFtdcInvestorPositionField *) calloc(1,
                                                                                          sizeof(CSecurityFtdcInvestorPositionField));
    memset(t, 0, sizeof(CSecurityFtdcInvestorPositionField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->PosiDirection = PyString_AsString(PyObject_GetAttrString(p, "PosiDirection"))[0];
    t->HedgeFlag = PyString_AsString(PyObject_GetAttrString(p, "HedgeFlag"))[0];
    t->PositionDate = PyString_AsString(PyObject_GetAttrString(p, "PositionDate"))[0];
    t->YdPosition = PyInt_AsLong(PyObject_GetAttrString(p, "YdPosition"));
    t->Position = PyInt_AsLong(PyObject_GetAttrString(p, "Position"));
    t->LongFrozen = PyInt_AsLong(PyObject_GetAttrString(p, "LongFrozen"));
    t->ShortFrozen = PyInt_AsLong(PyObject_GetAttrString(p, "ShortFrozen"));
    t->LongFrozenAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "LongFrozenAmount"));
    t->ShortFrozenAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ShortFrozenAmount"));
    t->OpenVolume = PyInt_AsLong(PyObject_GetAttrString(p, "OpenVolume"));
    t->CloseVolume = PyInt_AsLong(PyObject_GetAttrString(p, "CloseVolume"));
    t->OpenAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenAmount"));
    t->CloseAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "CloseAmount"));
    t->PositionCost = PyFloat_AsDouble(PyObject_GetAttrString(p, "PositionCost"));
    t->FrozenCash = PyFloat_AsDouble(PyObject_GetAttrString(p, "FrozenCash"));
    t->CashIn = PyFloat_AsDouble(PyObject_GetAttrString(p, "CashIn"));
    t->Commission = PyFloat_AsDouble(PyObject_GetAttrString(p, "Commission"));
    t->PreSettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreSettlementPrice"));
    t->SettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "SettlementPrice"));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    t->OpenCost = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenCost"));
    t->ExchangeMargin = PyFloat_AsDouble(PyObject_GetAttrString(p, "ExchangeMargin"));
    t->TodayPosition = PyInt_AsLong(PyObject_GetAttrString(p, "TodayPosition"));
    t->TransferFee = PyFloat_AsDouble(PyObject_GetAttrString(p, "TransferFee"));
    t->StampTax = PyFloat_AsDouble(PyObject_GetAttrString(p, "StampTax"));
    t->TodayPurRedVolume = PyInt_AsLong(PyObject_GetAttrString(p, "TodayPurRedVolume"));
    t->ConversionRate = PyFloat_AsDouble(PyObject_GetAttrString(p, "ConversionRate"));
    t->ConversionAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ConversionAmount"));
    t->StockValue = PyFloat_AsDouble(PyObject_GetAttrString(p, "StockValue"));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    t->PledgeInPosition = PyInt_AsLong(PyObject_GetAttrString(p, "PledgeInPosition"));
    t->RepurchasePosition = PyInt_AsLong(PyObject_GetAttrString(p, "RepurchasePosition"));
    t->PurRedShortFrozen = PyInt_AsLong(PyObject_GetAttrString(p, "PurRedShortFrozen"));
    t->MarginTradeVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MarginTradeVolume"));
    t->MarginTradeAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "MarginTradeAmount"));
    t->MarginTradeFrozenVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MarginTradeFrozenVolume"));
    t->MarginTradeFrozenAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "MarginTradeFrozenAmount"));
    t->MarginTradeConversionProfit = PyFloat_AsDouble(PyObject_GetAttrString(p, "MarginTradeConversionProfit"));
    t->ShortSellVolume = PyInt_AsLong(PyObject_GetAttrString(p, "ShortSellVolume"));
    t->ShortSellAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ShortSellAmount"));
    t->ShortSellFrozenVolume = PyInt_AsLong(PyObject_GetAttrString(p, "ShortSellFrozenVolume"));
    t->ShortSellFrozenAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "ShortSellFrozenAmount"));
    t->ShortSellConversionProfit = PyFloat_AsDouble(PyObject_GetAttrString(p, "ShortSellConversionProfit"));
    t->SSStockValue = PyFloat_AsDouble(PyObject_GetAttrString(p, "SSStockValue"));
    t->TodayMTPosition = PyInt_AsLong(PyObject_GetAttrString(p, "TodayMTPosition"));
    t->TodaySSPosition = PyInt_AsLong(PyObject_GetAttrString(p, "TodaySSPosition"));
    t->YdOpenCost = PyFloat_AsDouble(PyObject_GetAttrString(p, "YdOpenCost"));

    return t;
};

PyObject *new_CSecurityFtdcSyncDepositField(CSecurityFtdcSyncDepositField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcSyncDepositField", (char *) "sssdis",
                               p->DepositSeqNo, p->BrokerID, p->InvestorID, p->Deposit, p->IsForce, p->AccountID);
}

CSecurityFtdcSyncDepositField *from_CSecurityFtdcSyncDepositField(PyObject * p) {
    CSecurityFtdcSyncDepositField *t = (CSecurityFtdcSyncDepositField *) calloc(1,
                                                                                sizeof(CSecurityFtdcSyncDepositField));
    memset(t, 0, sizeof(CSecurityFtdcSyncDepositField));
    strcpy(t->DepositSeqNo, PyString_AsString(PyObject_GetAttrString(p, "DepositSeqNo")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->Deposit = PyFloat_AsDouble(PyObject_GetAttrString(p, "Deposit"));
    t->IsForce = PyInt_AsLong(PyObject_GetAttrString(p, "IsForce"));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));

    return t;
};

PyObject *new_CSecurityFtdcQryExchangeField(CSecurityFtdcQryExchangeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryExchangeField", (char *) "s",
                               p->ExchangeID);
}

CSecurityFtdcQryExchangeField *from_CSecurityFtdcQryExchangeField(PyObject * p) {
    CSecurityFtdcQryExchangeField *t = (CSecurityFtdcQryExchangeField *) calloc(1,
                                                                                sizeof(CSecurityFtdcQryExchangeField));
    memset(t, 0, sizeof(CSecurityFtdcQryExchangeField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
};

PyObject *new_CSecurityFtdcQryProductField(CSecurityFtdcQryProductField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryProductField", (char *) "s",
                               p->ProductID);
}

CSecurityFtdcQryProductField *from_CSecurityFtdcQryProductField(PyObject * p) {
    CSecurityFtdcQryProductField *t = (CSecurityFtdcQryProductField *) calloc(1, sizeof(CSecurityFtdcQryProductField));
    memset(t, 0, sizeof(CSecurityFtdcQryProductField));
    strcpy(t->ProductID, PyString_AsString(PyObject_GetAttrString(p, "ProductID")));

    return t;
};

PyObject *new_CSecurityFtdcQryInstrumentField(CSecurityFtdcQryInstrumentField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryInstrumentField", (char *) "ssss",
                               p->InstrumentID, p->ExchangeID, p->ExchangeInstID, p->ProductID);
}

CSecurityFtdcQryInstrumentField *from_CSecurityFtdcQryInstrumentField(PyObject * p) {
    CSecurityFtdcQryInstrumentField *t = (CSecurityFtdcQryInstrumentField *) calloc(1,
                                                                                    sizeof(CSecurityFtdcQryInstrumentField));
    memset(t, 0, sizeof(CSecurityFtdcQryInstrumentField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ExchangeInstID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeInstID")));
    strcpy(t->ProductID, PyString_AsString(PyObject_GetAttrString(p, "ProductID")));

    return t;
};

PyObject *new_CSecurityFtdcQryBrokerField(CSecurityFtdcQryBrokerField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryBrokerField", (char *) "s",
                               p->BrokerID);
}

CSecurityFtdcQryBrokerField *from_CSecurityFtdcQryBrokerField(PyObject * p) {
    CSecurityFtdcQryBrokerField *t = (CSecurityFtdcQryBrokerField *) calloc(1, sizeof(CSecurityFtdcQryBrokerField));
    memset(t, 0, sizeof(CSecurityFtdcQryBrokerField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));

    return t;
};

PyObject *new_CSecurityFtdcQryPartBrokerField(CSecurityFtdcQryPartBrokerField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryPartBrokerField", (char *) "sss",
                               p->ExchangeID, p->BrokerID, p->ParticipantID);
}

CSecurityFtdcQryPartBrokerField *from_CSecurityFtdcQryPartBrokerField(PyObject * p) {
    CSecurityFtdcQryPartBrokerField *t = (CSecurityFtdcQryPartBrokerField *) calloc(1,
                                                                                    sizeof(CSecurityFtdcQryPartBrokerField));
    memset(t, 0, sizeof(CSecurityFtdcQryPartBrokerField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));

    return t;
};

PyObject *new_CSecurityFtdcQryInvestorField(CSecurityFtdcQryInvestorField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryInvestorField", (char *) "ss",
                               p->BrokerID, p->InvestorID);
}

CSecurityFtdcQryInvestorField *from_CSecurityFtdcQryInvestorField(PyObject * p) {
    CSecurityFtdcQryInvestorField *t = (CSecurityFtdcQryInvestorField *) calloc(1,
                                                                                sizeof(CSecurityFtdcQryInvestorField));
    memset(t, 0, sizeof(CSecurityFtdcQryInvestorField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));

    return t;
};

PyObject *new_CSecurityFtdcQryTradingCodeField(CSecurityFtdcQryTradingCodeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryTradingCodeField", (char *) "ssss",
                               p->BrokerID, p->InvestorID, p->ExchangeID, p->ClientID);
}

CSecurityFtdcQryTradingCodeField *from_CSecurityFtdcQryTradingCodeField(PyObject * p) {
    CSecurityFtdcQryTradingCodeField *t = (CSecurityFtdcQryTradingCodeField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcQryTradingCodeField));
    memset(t, 0, sizeof(CSecurityFtdcQryTradingCodeField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ClientID, PyString_AsString(PyObject_GetAttrString(p, "ClientID")));

    return t;
};

PyObject *new_CSecurityFtdcQrySuperUserField(CSecurityFtdcQrySuperUserField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQrySuperUserField", (char *) "s",
                               p->UserID);
}

CSecurityFtdcQrySuperUserField *from_CSecurityFtdcQrySuperUserField(PyObject * p) {
    CSecurityFtdcQrySuperUserField *t = (CSecurityFtdcQrySuperUserField *) calloc(1,
                                                                                  sizeof(CSecurityFtdcQrySuperUserField));
    memset(t, 0, sizeof(CSecurityFtdcQrySuperUserField));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcQrySuperUserFunctionField(CSecurityFtdcQrySuperUserFunctionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQrySuperUserFunctionField", (char *) "s",
                               p->UserID);
}

CSecurityFtdcQrySuperUserFunctionField *from_CSecurityFtdcQrySuperUserFunctionField(PyObject * p) {
    CSecurityFtdcQrySuperUserFunctionField *t = (CSecurityFtdcQrySuperUserFunctionField *) calloc(1,
                                                                                                  sizeof(CSecurityFtdcQrySuperUserFunctionField));
    memset(t, 0, sizeof(CSecurityFtdcQrySuperUserFunctionField));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcQryBrokerUserField(CSecurityFtdcQryBrokerUserField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryBrokerUserField", (char *) "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcQryBrokerUserField *from_CSecurityFtdcQryBrokerUserField(PyObject * p) {
    CSecurityFtdcQryBrokerUserField *t = (CSecurityFtdcQryBrokerUserField *) calloc(1,
                                                                                    sizeof(CSecurityFtdcQryBrokerUserField));
    memset(t, 0, sizeof(CSecurityFtdcQryBrokerUserField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcQryBrokerUserFunctionField(CSecurityFtdcQryBrokerUserFunctionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryBrokerUserFunctionField", (char *) "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcQryBrokerUserFunctionField *from_CSecurityFtdcQryBrokerUserFunctionField(PyObject * p) {
    CSecurityFtdcQryBrokerUserFunctionField *t = (CSecurityFtdcQryBrokerUserFunctionField *) calloc(1,
                                                                                                    sizeof(CSecurityFtdcQryBrokerUserFunctionField));
    memset(t, 0, sizeof(CSecurityFtdcQryBrokerUserFunctionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcQryTradingAccountField(CSecurityFtdcQryTradingAccountField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryTradingAccountField", (char *) "ss",
                               p->BrokerID, p->InvestorID);
}

CSecurityFtdcQryTradingAccountField *from_CSecurityFtdcQryTradingAccountField(PyObject * p) {
    CSecurityFtdcQryTradingAccountField *t = (CSecurityFtdcQryTradingAccountField *) calloc(1,
                                                                                            sizeof(CSecurityFtdcQryTradingAccountField));
    memset(t, 0, sizeof(CSecurityFtdcQryTradingAccountField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));

    return t;
};

PyObject *new_CSecurityFtdcQryLoginForbiddenUserField(CSecurityFtdcQryLoginForbiddenUserField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryLoginForbiddenUserField", (char *) "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcQryLoginForbiddenUserField *from_CSecurityFtdcQryLoginForbiddenUserField(PyObject * p) {
    CSecurityFtdcQryLoginForbiddenUserField *t = (CSecurityFtdcQryLoginForbiddenUserField *) calloc(1,
                                                                                                    sizeof(CSecurityFtdcQryLoginForbiddenUserField));
    memset(t, 0, sizeof(CSecurityFtdcQryLoginForbiddenUserField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcQryDepthMarketDataField(CSecurityFtdcQryDepthMarketDataField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryDepthMarketDataField", (char *) "s",
                               p->InstrumentID);
}

CSecurityFtdcQryDepthMarketDataField *from_CSecurityFtdcQryDepthMarketDataField(PyObject * p) {
    CSecurityFtdcQryDepthMarketDataField *t = (CSecurityFtdcQryDepthMarketDataField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcQryDepthMarketDataField));
    memset(t, 0, sizeof(CSecurityFtdcQryDepthMarketDataField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcQryInstrumentTradingRightField(CSecurityFtdcQryInstrumentTradingRightField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryInstrumentTradingRightField", (char *) "ssss",
                               p->ExchangeID, p->BrokerID, p->InvestorID, p->InstrumentID);
}

CSecurityFtdcQryInstrumentTradingRightField *from_CSecurityFtdcQryInstrumentTradingRightField(PyObject * p) {
    CSecurityFtdcQryInstrumentTradingRightField *t = (CSecurityFtdcQryInstrumentTradingRightField *) calloc(1,
                                                                                                            sizeof(CSecurityFtdcQryInstrumentTradingRightField));
    memset(t, 0, sizeof(CSecurityFtdcQryInstrumentTradingRightField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcQryInvestorPositionDetailField(CSecurityFtdcQryInvestorPositionDetailField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryInvestorPositionDetailField", (char *) "sss",
                               p->BrokerID, p->InvestorID, p->InstrumentID);
}

CSecurityFtdcQryInvestorPositionDetailField *from_CSecurityFtdcQryInvestorPositionDetailField(PyObject * p) {
    CSecurityFtdcQryInvestorPositionDetailField *t = (CSecurityFtdcQryInvestorPositionDetailField *) calloc(1,
                                                                                                            sizeof(CSecurityFtdcQryInvestorPositionDetailField));
    memset(t, 0, sizeof(CSecurityFtdcQryInvestorPositionDetailField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcQryBondInterestField(CSecurityFtdcQryBondInterestField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryBondInterestField", (char *) "ss",
                               p->ExchangeID, p->InstrumentID);
}

CSecurityFtdcQryBondInterestField *from_CSecurityFtdcQryBondInterestField(PyObject * p) {
    CSecurityFtdcQryBondInterestField *t = (CSecurityFtdcQryBondInterestField *) calloc(1,
                                                                                        sizeof(CSecurityFtdcQryBondInterestField));
    memset(t, 0, sizeof(CSecurityFtdcQryBondInterestField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcQryMarketRationInfoField(CSecurityFtdcQryMarketRationInfoField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryMarketRationInfoField", (char *) "sss",
                               p->BrokerID, p->InvestorID, p->ExchangeID);
}

CSecurityFtdcQryMarketRationInfoField *from_CSecurityFtdcQryMarketRationInfoField(PyObject * p) {
    CSecurityFtdcQryMarketRationInfoField *t = (CSecurityFtdcQryMarketRationInfoField *) calloc(1,
                                                                                                sizeof(CSecurityFtdcQryMarketRationInfoField));
    memset(t, 0, sizeof(CSecurityFtdcQryMarketRationInfoField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
};

PyObject *new_CSecurityFtdcQryInstrumentCommissionRateField(CSecurityFtdcQryInstrumentCommissionRateField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryInstrumentCommissionRateField", (char *) "ssssc",
                               p->ExchangeID, p->BrokerID, p->InvestorID, p->InstrumentID, p->Direction);
}

CSecurityFtdcQryInstrumentCommissionRateField *from_CSecurityFtdcQryInstrumentCommissionRateField(PyObject * p) {
    CSecurityFtdcQryInstrumentCommissionRateField *t = (CSecurityFtdcQryInstrumentCommissionRateField *) calloc(1,
                                                                                                                sizeof(CSecurityFtdcQryInstrumentCommissionRateField));
    memset(t, 0, sizeof(CSecurityFtdcQryInstrumentCommissionRateField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];

    return t;
};

PyObject *new_CSecurityFtdcQryExcessStockInfoField(CSecurityFtdcQryExcessStockInfoField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryExcessStockInfoField", (char *) "ssss",
                               p->BrokerID, p->InvestorID, p->ExchangeID, p->InstrumentID);
}

CSecurityFtdcQryExcessStockInfoField *from_CSecurityFtdcQryExcessStockInfoField(PyObject * p) {
    CSecurityFtdcQryExcessStockInfoField *t = (CSecurityFtdcQryExcessStockInfoField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcQryExcessStockInfoField));
    memset(t, 0, sizeof(CSecurityFtdcQryExcessStockInfoField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcQryTraderOfferField(CSecurityFtdcQryTraderOfferField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryTraderOfferField", (char *) "sss",
                               p->ExchangeID, p->ParticipantID, p->BranchPBU);
}

CSecurityFtdcQryTraderOfferField *from_CSecurityFtdcQryTraderOfferField(PyObject * p) {
    CSecurityFtdcQryTraderOfferField *t = (CSecurityFtdcQryTraderOfferField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcQryTraderOfferField));
    memset(t, 0, sizeof(CSecurityFtdcQryTraderOfferField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));

    return t;
};

PyObject *new_CSecurityFtdcQryMDTraderOfferField(CSecurityFtdcQryMDTraderOfferField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryMDTraderOfferField", (char *) "sss",
                               p->ExchangeID, p->ParticipantID, p->BranchPBU);
}

CSecurityFtdcQryMDTraderOfferField *from_CSecurityFtdcQryMDTraderOfferField(PyObject * p) {
    CSecurityFtdcQryMDTraderOfferField *t = (CSecurityFtdcQryMDTraderOfferField *) calloc(1,
                                                                                          sizeof(CSecurityFtdcQryMDTraderOfferField));
    memset(t, 0, sizeof(CSecurityFtdcQryMDTraderOfferField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->ParticipantID, PyString_AsString(PyObject_GetAttrString(p, "ParticipantID")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));

    return t;
};

PyObject *new_CSecurityFtdcQryFrontStatusField(CSecurityFtdcQryFrontStatusField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryFrontStatusField", (char *) "i",
                               p->FrontID);
}

CSecurityFtdcQryFrontStatusField *from_CSecurityFtdcQryFrontStatusField(PyObject * p) {
    CSecurityFtdcQryFrontStatusField *t = (CSecurityFtdcQryFrontStatusField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcQryFrontStatusField));
    memset(t, 0, sizeof(CSecurityFtdcQryFrontStatusField));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));

    return t;
};

PyObject *new_CSecurityFtdcQryUserSessionField(CSecurityFtdcQryUserSessionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryUserSessionField", (char *) "iiss",
                               p->FrontID, p->SessionID, p->BrokerID, p->UserID);
}

CSecurityFtdcQryUserSessionField *from_CSecurityFtdcQryUserSessionField(PyObject * p) {
    CSecurityFtdcQryUserSessionField *t = (CSecurityFtdcQryUserSessionField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcQryUserSessionField));
    memset(t, 0, sizeof(CSecurityFtdcQryUserSessionField));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcQryOrderField(CSecurityFtdcQryOrderField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryOrderField", (char *) "sssssss",
                               p->BrokerID, p->InvestorID, p->InstrumentID, p->ExchangeID, p->OrderSysID,
                               p->InsertTimeStart, p->InsertTimeEnd);
}

CSecurityFtdcQryOrderField *from_CSecurityFtdcQryOrderField(PyObject * p) {
    CSecurityFtdcQryOrderField *t = (CSecurityFtdcQryOrderField *) calloc(1, sizeof(CSecurityFtdcQryOrderField));
    memset(t, 0, sizeof(CSecurityFtdcQryOrderField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->OrderSysID, PyString_AsString(PyObject_GetAttrString(p, "OrderSysID")));
    strcpy(t->InsertTimeStart, PyString_AsString(PyObject_GetAttrString(p, "InsertTimeStart")));
    strcpy(t->InsertTimeEnd, PyString_AsString(PyObject_GetAttrString(p, "InsertTimeEnd")));

    return t;
};

PyObject *new_CSecurityFtdcQryOrderActionField(CSecurityFtdcQryOrderActionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryOrderActionField", (char *) "sss",
                               p->BrokerID, p->InvestorID, p->ExchangeID);
}

CSecurityFtdcQryOrderActionField *from_CSecurityFtdcQryOrderActionField(PyObject * p) {
    CSecurityFtdcQryOrderActionField *t = (CSecurityFtdcQryOrderActionField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcQryOrderActionField));
    memset(t, 0, sizeof(CSecurityFtdcQryOrderActionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
};

PyObject *new_CSecurityFtdcQryErrOrderField(CSecurityFtdcQryErrOrderField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryErrOrderField", (char *) "ss",
                               p->BrokerID, p->InvestorID);
}

CSecurityFtdcQryErrOrderField *from_CSecurityFtdcQryErrOrderField(PyObject * p) {
    CSecurityFtdcQryErrOrderField *t = (CSecurityFtdcQryErrOrderField *) calloc(1,
                                                                                sizeof(CSecurityFtdcQryErrOrderField));
    memset(t, 0, sizeof(CSecurityFtdcQryErrOrderField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));

    return t;
};

PyObject *new_CSecurityFtdcQryErrOrderActionField(CSecurityFtdcQryErrOrderActionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryErrOrderActionField", (char *) "ss",
                               p->BrokerID, p->InvestorID);
}

CSecurityFtdcQryErrOrderActionField *from_CSecurityFtdcQryErrOrderActionField(PyObject * p) {
    CSecurityFtdcQryErrOrderActionField *t = (CSecurityFtdcQryErrOrderActionField *) calloc(1,
                                                                                            sizeof(CSecurityFtdcQryErrOrderActionField));
    memset(t, 0, sizeof(CSecurityFtdcQryErrOrderActionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));

    return t;
};

PyObject *new_CSecurityFtdcQryTradeField(CSecurityFtdcQryTradeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryTradeField", (char *) "sssssss",
                               p->BrokerID, p->InvestorID, p->InstrumentID, p->ExchangeID, p->TradeID,
                               p->TradeTimeStart, p->TradeTimeEnd);
}

CSecurityFtdcQryTradeField *from_CSecurityFtdcQryTradeField(PyObject * p) {
    CSecurityFtdcQryTradeField *t = (CSecurityFtdcQryTradeField *) calloc(1, sizeof(CSecurityFtdcQryTradeField));
    memset(t, 0, sizeof(CSecurityFtdcQryTradeField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    strcpy(t->TradeID, PyString_AsString(PyObject_GetAttrString(p, "TradeID")));
    strcpy(t->TradeTimeStart, PyString_AsString(PyObject_GetAttrString(p, "TradeTimeStart")));
    strcpy(t->TradeTimeEnd, PyString_AsString(PyObject_GetAttrString(p, "TradeTimeEnd")));

    return t;
};

PyObject *new_CSecurityFtdcQryInvestorPositionField(CSecurityFtdcQryInvestorPositionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryInvestorPositionField", (char *) "sss",
                               p->BrokerID, p->InvestorID, p->InstrumentID);
}

CSecurityFtdcQryInvestorPositionField *from_CSecurityFtdcQryInvestorPositionField(PyObject * p) {
    CSecurityFtdcQryInvestorPositionField *t = (CSecurityFtdcQryInvestorPositionField *) calloc(1,
                                                                                                sizeof(CSecurityFtdcQryInvestorPositionField));
    memset(t, 0, sizeof(CSecurityFtdcQryInvestorPositionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));

    return t;
};

PyObject *new_CSecurityFtdcQrySyncDepositField(CSecurityFtdcQrySyncDepositField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQrySyncDepositField", (char *) "ss",
                               p->BrokerID, p->DepositSeqNo);
}

CSecurityFtdcQrySyncDepositField *from_CSecurityFtdcQrySyncDepositField(PyObject * p) {
    CSecurityFtdcQrySyncDepositField *t = (CSecurityFtdcQrySyncDepositField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcQrySyncDepositField));
    memset(t, 0, sizeof(CSecurityFtdcQrySyncDepositField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->DepositSeqNo, PyString_AsString(PyObject_GetAttrString(p, "DepositSeqNo")));

    return t;
};

PyObject *new_CSecurityFtdcUserPasswordUpdateField(CSecurityFtdcUserPasswordUpdateField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcUserPasswordUpdateField", (char *) "ssss",
                               p->BrokerID, p->UserID, p->OldPassword, p->NewPassword);
}

CSecurityFtdcUserPasswordUpdateField *from_CSecurityFtdcUserPasswordUpdateField(PyObject * p) {
    CSecurityFtdcUserPasswordUpdateField *t = (CSecurityFtdcUserPasswordUpdateField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcUserPasswordUpdateField));
    memset(t, 0, sizeof(CSecurityFtdcUserPasswordUpdateField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->OldPassword, PyString_AsString(PyObject_GetAttrString(p, "OldPassword")));
    strcpy(t->NewPassword, PyString_AsString(PyObject_GetAttrString(p, "NewPassword")));

    return t;
};

PyObject *new_CSecurityFtdcTradingAccountPasswordUpdateField(CSecurityFtdcTradingAccountPasswordUpdateField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcTradingAccountPasswordUpdateField", (char *) "ssss",
                               p->BrokerID, p->AccountID, p->OldPassword, p->NewPassword);
}

CSecurityFtdcTradingAccountPasswordUpdateField *from_CSecurityFtdcTradingAccountPasswordUpdateField(PyObject * p) {
    CSecurityFtdcTradingAccountPasswordUpdateField *t = (CSecurityFtdcTradingAccountPasswordUpdateField *) calloc(1,
                                                                                                                  sizeof(CSecurityFtdcTradingAccountPasswordUpdateField));
    memset(t, 0, sizeof(CSecurityFtdcTradingAccountPasswordUpdateField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    strcpy(t->OldPassword, PyString_AsString(PyObject_GetAttrString(p, "OldPassword")));
    strcpy(t->NewPassword, PyString_AsString(PyObject_GetAttrString(p, "NewPassword")));

    return t;
};

PyObject *new_CSecurityFtdcManualSyncBrokerUserOTPField(CSecurityFtdcManualSyncBrokerUserOTPField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcManualSyncBrokerUserOTPField", (char *) "sscss",
                               p->BrokerID, p->UserID, p->OTPType, p->FirstOTP, p->SecondOTP);
}

CSecurityFtdcManualSyncBrokerUserOTPField *from_CSecurityFtdcManualSyncBrokerUserOTPField(PyObject * p) {
    CSecurityFtdcManualSyncBrokerUserOTPField *t = (CSecurityFtdcManualSyncBrokerUserOTPField *) calloc(1,
                                                                                                        sizeof(CSecurityFtdcManualSyncBrokerUserOTPField));
    memset(t, 0, sizeof(CSecurityFtdcManualSyncBrokerUserOTPField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    t->OTPType = PyString_AsString(PyObject_GetAttrString(p, "OTPType"))[0];
    strcpy(t->FirstOTP, PyString_AsString(PyObject_GetAttrString(p, "FirstOTP")));
    strcpy(t->SecondOTP, PyString_AsString(PyObject_GetAttrString(p, "SecondOTP")));

    return t;
};

PyObject *new_CSecurityFtdcBrokerUserPasswordField(CSecurityFtdcBrokerUserPasswordField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcBrokerUserPasswordField", (char *) "sss",
                               p->BrokerID, p->UserID, p->Password);
}

CSecurityFtdcBrokerUserPasswordField *from_CSecurityFtdcBrokerUserPasswordField(PyObject * p) {
    CSecurityFtdcBrokerUserPasswordField *t = (CSecurityFtdcBrokerUserPasswordField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcBrokerUserPasswordField));
    memset(t, 0, sizeof(CSecurityFtdcBrokerUserPasswordField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));

    return t;
};

PyObject *new_CSecurityFtdcTradingAccountPasswordField(CSecurityFtdcTradingAccountPasswordField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcTradingAccountPasswordField", (char *) "sss",
                               p->BrokerID, p->AccountID, p->Password);
}

CSecurityFtdcTradingAccountPasswordField *from_CSecurityFtdcTradingAccountPasswordField(PyObject * p) {
    CSecurityFtdcTradingAccountPasswordField *t = (CSecurityFtdcTradingAccountPasswordField *) calloc(1,
                                                                                                      sizeof(CSecurityFtdcTradingAccountPasswordField));
    memset(t, 0, sizeof(CSecurityFtdcTradingAccountPasswordField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));

    return t;
};

PyObject *new_CSecurityFtdcUserRightField(CSecurityFtdcUserRightField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcUserRightField", (char *) "ssci",
                               p->BrokerID, p->UserID, p->UserRightType, p->IsForbidden);
}

CSecurityFtdcUserRightField *from_CSecurityFtdcUserRightField(PyObject * p) {
    CSecurityFtdcUserRightField *t = (CSecurityFtdcUserRightField *) calloc(1, sizeof(CSecurityFtdcUserRightField));
    memset(t, 0, sizeof(CSecurityFtdcUserRightField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    t->UserRightType = PyString_AsString(PyObject_GetAttrString(p, "UserRightType"))[0];
    t->IsForbidden = PyInt_AsLong(PyObject_GetAttrString(p, "IsForbidden"));

    return t;
};

PyObject *new_CSecurityFtdcInvestorAccountField(CSecurityFtdcInvestorAccountField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInvestorAccountField", (char *) "sssici",
                               p->BrokerID, p->InvestorID, p->AccountID, p->IsDefault, p->AccountType, p->IsActive);
}

CSecurityFtdcInvestorAccountField *from_CSecurityFtdcInvestorAccountField(PyObject * p) {
    CSecurityFtdcInvestorAccountField *t = (CSecurityFtdcInvestorAccountField *) calloc(1,
                                                                                        sizeof(CSecurityFtdcInvestorAccountField));
    memset(t, 0, sizeof(CSecurityFtdcInvestorAccountField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    t->IsDefault = PyInt_AsLong(PyObject_GetAttrString(p, "IsDefault"));
    t->AccountType = PyString_AsString(PyObject_GetAttrString(p, "AccountType"))[0];
    t->IsActive = PyInt_AsLong(PyObject_GetAttrString(p, "IsActive"));

    return t;
};

PyObject *new_CSecurityFtdcUserIPField(CSecurityFtdcUserIPField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcUserIPField", (char *) "sssss",
                               p->BrokerID, p->UserID, p->IPAddress, p->IPMask, p->MacAddress);
}

CSecurityFtdcUserIPField *from_CSecurityFtdcUserIPField(PyObject * p) {
    CSecurityFtdcUserIPField *t = (CSecurityFtdcUserIPField *) calloc(1, sizeof(CSecurityFtdcUserIPField));
    memset(t, 0, sizeof(CSecurityFtdcUserIPField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->IPAddress, PyString_AsString(PyObject_GetAttrString(p, "IPAddress")));
    strcpy(t->IPMask, PyString_AsString(PyObject_GetAttrString(p, "IPMask")));
    strcpy(t->MacAddress, PyString_AsString(PyObject_GetAttrString(p, "MacAddress")));

    return t;
};

PyObject *new_CSecurityFtdcBrokerUserOTPParamField(CSecurityFtdcBrokerUserOTPParamField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcBrokerUserOTPParamField", (char *) "sssssiic",
                               p->BrokerID, p->UserID, p->OTPVendorsID, p->SerialNumber, p->AuthKey, p->LastDrift,
                               p->LastSuccess, p->OTPType);
}

CSecurityFtdcBrokerUserOTPParamField *from_CSecurityFtdcBrokerUserOTPParamField(PyObject * p) {
    CSecurityFtdcBrokerUserOTPParamField *t = (CSecurityFtdcBrokerUserOTPParamField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcBrokerUserOTPParamField));
    memset(t, 0, sizeof(CSecurityFtdcBrokerUserOTPParamField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->OTPVendorsID, PyString_AsString(PyObject_GetAttrString(p, "OTPVendorsID")));
    strcpy(t->SerialNumber, PyString_AsString(PyObject_GetAttrString(p, "SerialNumber")));
    strcpy(t->AuthKey, PyString_AsString(PyObject_GetAttrString(p, "AuthKey")));
    t->LastDrift = PyInt_AsLong(PyObject_GetAttrString(p, "LastDrift"));
    t->LastSuccess = PyInt_AsLong(PyObject_GetAttrString(p, "LastSuccess"));
    t->OTPType = PyString_AsString(PyObject_GetAttrString(p, "OTPType"))[0];

    return t;
};

PyObject *new_CSecurityFtdcReqUserLoginField(CSecurityFtdcReqUserLoginField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcReqUserLoginField", (char *) "sssssssssss",
                               p->TradingDay, p->BrokerID, p->UserID, p->Password, p->UserProductInfo,
                               p->InterfaceProductInfo, p->ProtocolInfo, p->MacAddress, p->OneTimePassword,
                               p->ClientIPAddress, p->AuthCode);
}

CSecurityFtdcReqUserLoginField *from_CSecurityFtdcReqUserLoginField(PyObject * p) {
    CSecurityFtdcReqUserLoginField *t = (CSecurityFtdcReqUserLoginField *) calloc(1,
                                                                                  sizeof(CSecurityFtdcReqUserLoginField));
    memset(t, 0, sizeof(CSecurityFtdcReqUserLoginField));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));
    strcpy(t->UserProductInfo, PyString_AsString(PyObject_GetAttrString(p, "UserProductInfo")));
    strcpy(t->InterfaceProductInfo, PyString_AsString(PyObject_GetAttrString(p, "InterfaceProductInfo")));
    strcpy(t->ProtocolInfo, PyString_AsString(PyObject_GetAttrString(p, "ProtocolInfo")));
    strcpy(t->MacAddress, PyString_AsString(PyObject_GetAttrString(p, "MacAddress")));
    strcpy(t->OneTimePassword, PyString_AsString(PyObject_GetAttrString(p, "OneTimePassword")));
    strcpy(t->ClientIPAddress, PyString_AsString(PyObject_GetAttrString(p, "ClientIPAddress")));
    strcpy(t->AuthCode, PyString_AsString(PyObject_GetAttrString(p, "AuthCode")));

    return t;
};

PyObject *new_CSecurityFtdcRspUserLoginField(CSecurityFtdcRspUserLoginField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcRspUserLoginField", (char *) "sssssiis",
                               p->TradingDay, p->LoginTime, p->BrokerID, p->UserID, p->SystemName, p->FrontID,
                               p->SessionID, p->MaxOrderRef);
}

CSecurityFtdcRspUserLoginField *from_CSecurityFtdcRspUserLoginField(PyObject * p) {
    CSecurityFtdcRspUserLoginField *t = (CSecurityFtdcRspUserLoginField *) calloc(1,
                                                                                  sizeof(CSecurityFtdcRspUserLoginField));
    memset(t, 0, sizeof(CSecurityFtdcRspUserLoginField));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->LoginTime, PyString_AsString(PyObject_GetAttrString(p, "LoginTime")));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->SystemName, PyString_AsString(PyObject_GetAttrString(p, "SystemName")));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->MaxOrderRef, PyString_AsString(PyObject_GetAttrString(p, "MaxOrderRef")));

    return t;
};

PyObject *new_CSecurityFtdcUserLogoutField(CSecurityFtdcUserLogoutField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcUserLogoutField", (char *) "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcUserLogoutField *from_CSecurityFtdcUserLogoutField(PyObject * p) {
    CSecurityFtdcUserLogoutField *t = (CSecurityFtdcUserLogoutField *) calloc(1, sizeof(CSecurityFtdcUserLogoutField));
    memset(t, 0, sizeof(CSecurityFtdcUserLogoutField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcLogoutAllField(CSecurityFtdcLogoutAllField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcLogoutAllField", (char *) "iis",
                               p->FrontID, p->SessionID, p->SystemName);
}

CSecurityFtdcLogoutAllField *from_CSecurityFtdcLogoutAllField(PyObject * p) {
    CSecurityFtdcLogoutAllField *t = (CSecurityFtdcLogoutAllField *) calloc(1, sizeof(CSecurityFtdcLogoutAllField));
    memset(t, 0, sizeof(CSecurityFtdcLogoutAllField));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->SystemName, PyString_AsString(PyObject_GetAttrString(p, "SystemName")));

    return t;
};

PyObject *new_CSecurityFtdcForceUserLogoutField(CSecurityFtdcForceUserLogoutField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcForceUserLogoutField", (char *) "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcForceUserLogoutField *from_CSecurityFtdcForceUserLogoutField(PyObject * p) {
    CSecurityFtdcForceUserLogoutField *t = (CSecurityFtdcForceUserLogoutField *) calloc(1,
                                                                                        sizeof(CSecurityFtdcForceUserLogoutField));
    memset(t, 0, sizeof(CSecurityFtdcForceUserLogoutField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
};

PyObject *new_CSecurityFtdcInputOrderField(CSecurityFtdcInputOrderField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInputOrderField", (char *) "ssssssccsssicscicdcisii",
                               p->BrokerID, p->InvestorID, p->InstrumentID, p->OrderRef, p->UserID, p->ExchangeID,
                               p->OrderPriceType, p->Direction, p->CombOffsetFlag, p->CombHedgeFlag, p->LimitPrice,
                               p->VolumeTotalOriginal, p->TimeCondition, p->GTDDate, p->VolumeCondition, p->MinVolume,
                               p->ContingentCondition, p->StopPrice, p->ForceCloseReason, p->IsAutoSuspend,
                               p->BusinessUnit, p->RequestID, p->UserForceClose);
}

CSecurityFtdcInputOrderField *from_CSecurityFtdcInputOrderField(PyObject * p) {
    CSecurityFtdcInputOrderField *t = (CSecurityFtdcInputOrderField *) calloc(1, sizeof(CSecurityFtdcInputOrderField));
    memset(t, 0, sizeof(CSecurityFtdcInputOrderField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->OrderPriceType = PyString_AsString(PyObject_GetAttrString(p, "OrderPriceType"))[0];
    t->Direction = PyString_AsString(PyObject_GetAttrString(p, "Direction"))[0];
    strcpy(t->CombOffsetFlag, PyString_AsString(PyObject_GetAttrString(p, "CombOffsetFlag")));
    strcpy(t->CombHedgeFlag, PyString_AsString(PyObject_GetAttrString(p, "CombHedgeFlag")));
    strcpy(t->LimitPrice, PyString_AsString(PyObject_GetAttrString(p, "LimitPrice")));
    t->VolumeTotalOriginal = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeTotalOriginal"));
    t->TimeCondition = PyString_AsString(PyObject_GetAttrString(p, "TimeCondition"))[0];
    strcpy(t->GTDDate, PyString_AsString(PyObject_GetAttrString(p, "GTDDate")));
    t->VolumeCondition = PyString_AsString(PyObject_GetAttrString(p, "VolumeCondition"))[0];
    t->MinVolume = PyInt_AsLong(PyObject_GetAttrString(p, "MinVolume"));
    t->ContingentCondition = PyString_AsString(PyObject_GetAttrString(p, "ContingentCondition"))[0];
    t->StopPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "StopPrice"));
    t->ForceCloseReason = PyString_AsString(PyObject_GetAttrString(p, "ForceCloseReason"))[0];
    t->IsAutoSuspend = PyInt_AsLong(PyObject_GetAttrString(p, "IsAutoSuspend"));
    strcpy(t->BusinessUnit, PyString_AsString(PyObject_GetAttrString(p, "BusinessUnit")));
    t->RequestID = PyInt_AsLong(PyObject_GetAttrString(p, "RequestID"));
    t->UserForceClose = PyInt_AsLong(PyObject_GetAttrString(p, "UserForceClose"));

    return t;
};

PyObject *new_CSecurityFtdcInputOrderActionField(CSecurityFtdcInputOrderActionField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInputOrderActionField", (char *) "ssisiiiscdissss",
                               p->BrokerID, p->InvestorID, p->OrderActionRef, p->OrderRef, p->RequestID, p->FrontID,
                               p->SessionID, p->ExchangeID, p->ActionFlag, p->LimitPrice, p->VolumeChange, p->UserID,
                               p->InstrumentID, p->BranchPBU, p->OrderLocalID);
}

CSecurityFtdcInputOrderActionField *from_CSecurityFtdcInputOrderActionField(PyObject * p) {
    CSecurityFtdcInputOrderActionField *t = (CSecurityFtdcInputOrderActionField *) calloc(1,
                                                                                          sizeof(CSecurityFtdcInputOrderActionField));
    memset(t, 0, sizeof(CSecurityFtdcInputOrderActionField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    t->OrderActionRef = PyInt_AsLong(PyObject_GetAttrString(p, "OrderActionRef"));
    strcpy(t->OrderRef, PyString_AsString(PyObject_GetAttrString(p, "OrderRef")));
    t->RequestID = PyInt_AsLong(PyObject_GetAttrString(p, "RequestID"));
    t->FrontID = PyInt_AsLong(PyObject_GetAttrString(p, "FrontID"));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));
    t->ActionFlag = PyString_AsString(PyObject_GetAttrString(p, "ActionFlag"))[0];
    t->LimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LimitPrice"));
    t->VolumeChange = PyInt_AsLong(PyObject_GetAttrString(p, "VolumeChange"));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->BranchPBU, PyString_AsString(PyObject_GetAttrString(p, "BranchPBU")));
    strcpy(t->OrderLocalID, PyString_AsString(PyObject_GetAttrString(p, "OrderLocalID")));

    return t;
};

PyObject *new_CSecurityFtdcSpecificInstrumentField(CSecurityFtdcSpecificInstrumentField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcSpecificInstrumentField", (char *) "ss",
                               p->InstrumentID, p->ExchangeID);
}

CSecurityFtdcSpecificInstrumentField *from_CSecurityFtdcSpecificInstrumentField(PyObject * p) {
    CSecurityFtdcSpecificInstrumentField *t = (CSecurityFtdcSpecificInstrumentField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcSpecificInstrumentField));
    memset(t, 0, sizeof(CSecurityFtdcSpecificInstrumentField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
};

PyObject *new_CSecurityFtdcSpecificExchangeField(CSecurityFtdcSpecificExchangeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcSpecificExchangeField", (char *) "s",
                               p->ExchangeID);
}

CSecurityFtdcSpecificExchangeField *from_CSecurityFtdcSpecificExchangeField(PyObject * p) {
    CSecurityFtdcSpecificExchangeField *t = (CSecurityFtdcSpecificExchangeField *) calloc(1,
                                                                                          sizeof(CSecurityFtdcSpecificExchangeField));
    memset(t, 0, sizeof(CSecurityFtdcSpecificExchangeField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataBaseField(CSecurityFtdcMarketDataBaseField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataBaseField", (char *) "sdddd",
                               p->TradingDay, p->PreSettlementPrice, p->PreClosePrice, p->PreOpenInterest, p->PreDelta);
}

CSecurityFtdcMarketDataBaseField *from_CSecurityFtdcMarketDataBaseField(PyObject * p) {
    CSecurityFtdcMarketDataBaseField *t = (CSecurityFtdcMarketDataBaseField *) calloc(1,
                                                                                      sizeof(CSecurityFtdcMarketDataBaseField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataBaseField));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    t->PreSettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreSettlementPrice"));
    t->PreClosePrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreClosePrice"));
    t->PreOpenInterest = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreOpenInterest"));
    t->PreDelta = PyFloat_AsDouble(PyObject_GetAttrString(p, "PreDelta"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataStaticField(CSecurityFtdcMarketDataStaticField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataStaticField", (char *) "dddddddd",
                               p->OpenPrice, p->HighestPrice, p->LowestPrice, p->ClosePrice, p->UpperLimitPrice,
                               p->LowerLimitPrice, p->SettlementPrice, p->CurrDelta);
}

CSecurityFtdcMarketDataStaticField *from_CSecurityFtdcMarketDataStaticField(PyObject * p) {
    CSecurityFtdcMarketDataStaticField *t = (CSecurityFtdcMarketDataStaticField *) calloc(1,
                                                                                          sizeof(CSecurityFtdcMarketDataStaticField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataStaticField));
    t->OpenPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenPrice"));
    t->HighestPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "HighestPrice"));
    t->LowestPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LowestPrice"));
    t->ClosePrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "ClosePrice"));
    t->UpperLimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "UpperLimitPrice"));
    t->LowerLimitPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LowerLimitPrice"));
    t->SettlementPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "SettlementPrice"));
    t->CurrDelta = PyFloat_AsDouble(PyObject_GetAttrString(p, "CurrDelta"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataLastMatchField(CSecurityFtdcMarketDataLastMatchField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataLastMatchField", (char *) "didd",
                               p->LastPrice, p->Volume, p->Turnover, p->OpenInterest);
}

CSecurityFtdcMarketDataLastMatchField *from_CSecurityFtdcMarketDataLastMatchField(PyObject * p) {
    CSecurityFtdcMarketDataLastMatchField *t = (CSecurityFtdcMarketDataLastMatchField *) calloc(1,
                                                                                                sizeof(CSecurityFtdcMarketDataLastMatchField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataLastMatchField));
    t->LastPrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "LastPrice"));
    t->Volume = PyInt_AsLong(PyObject_GetAttrString(p, "Volume"));
    t->Turnover = PyFloat_AsDouble(PyObject_GetAttrString(p, "Turnover"));
    t->OpenInterest = PyFloat_AsDouble(PyObject_GetAttrString(p, "OpenInterest"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataBestPriceField(CSecurityFtdcMarketDataBestPriceField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataBestPriceField", (char *) "didi",
                               p->BidPrice1, p->BidVolume1, p->AskPrice1, p->AskVolume1);
}

CSecurityFtdcMarketDataBestPriceField *from_CSecurityFtdcMarketDataBestPriceField(PyObject * p) {
    CSecurityFtdcMarketDataBestPriceField *t = (CSecurityFtdcMarketDataBestPriceField *) calloc(1,
                                                                                                sizeof(CSecurityFtdcMarketDataBestPriceField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataBestPriceField));
    t->BidPrice1 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice1"));
    t->BidVolume1 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume1"));
    t->AskPrice1 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice1"));
    t->AskVolume1 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume1"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataBid23Field(CSecurityFtdcMarketDataBid23Field * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataBid23Field", (char *) "didi",
                               p->BidPrice2, p->BidVolume2, p->BidPrice3, p->BidVolume3);
}

CSecurityFtdcMarketDataBid23Field *from_CSecurityFtdcMarketDataBid23Field(PyObject * p) {
    CSecurityFtdcMarketDataBid23Field *t = (CSecurityFtdcMarketDataBid23Field *) calloc(1,
                                                                                        sizeof(CSecurityFtdcMarketDataBid23Field));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataBid23Field));
    t->BidPrice2 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice2"));
    t->BidVolume2 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume2"));
    t->BidPrice3 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice3"));
    t->BidVolume3 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume3"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataAsk23Field(CSecurityFtdcMarketDataAsk23Field * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataAsk23Field", (char *) "didi",
                               p->AskPrice2, p->AskVolume2, p->AskPrice3, p->AskVolume3);
}

CSecurityFtdcMarketDataAsk23Field *from_CSecurityFtdcMarketDataAsk23Field(PyObject * p) {
    CSecurityFtdcMarketDataAsk23Field *t = (CSecurityFtdcMarketDataAsk23Field *) calloc(1,
                                                                                        sizeof(CSecurityFtdcMarketDataAsk23Field));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataAsk23Field));
    t->AskPrice2 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice2"));
    t->AskVolume2 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume2"));
    t->AskPrice3 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice3"));
    t->AskVolume3 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume3"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataBid45Field(CSecurityFtdcMarketDataBid45Field * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataBid45Field", (char *) "didi",
                               p->BidPrice4, p->BidVolume4, p->BidPrice5, p->BidVolume5);
}

CSecurityFtdcMarketDataBid45Field *from_CSecurityFtdcMarketDataBid45Field(PyObject * p) {
    CSecurityFtdcMarketDataBid45Field *t = (CSecurityFtdcMarketDataBid45Field *) calloc(1,
                                                                                        sizeof(CSecurityFtdcMarketDataBid45Field));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataBid45Field));
    t->BidPrice4 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice4"));
    t->BidVolume4 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume4"));
    t->BidPrice5 = PyFloat_AsDouble(PyObject_GetAttrString(p, "BidPrice5"));
    t->BidVolume5 = PyInt_AsLong(PyObject_GetAttrString(p, "BidVolume5"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataAsk45Field(CSecurityFtdcMarketDataAsk45Field * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataAsk45Field", (char *) "didi",
                               p->AskPrice4, p->AskVolume4, p->AskPrice5, p->AskVolume5);
}

CSecurityFtdcMarketDataAsk45Field *from_CSecurityFtdcMarketDataAsk45Field(PyObject * p) {
    CSecurityFtdcMarketDataAsk45Field *t = (CSecurityFtdcMarketDataAsk45Field *) calloc(1,
                                                                                        sizeof(CSecurityFtdcMarketDataAsk45Field));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataAsk45Field));
    t->AskPrice4 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice4"));
    t->AskVolume4 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume4"));
    t->AskPrice5 = PyFloat_AsDouble(PyObject_GetAttrString(p, "AskPrice5"));
    t->AskVolume5 = PyInt_AsLong(PyObject_GetAttrString(p, "AskVolume5"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataUpdateTimeField(CSecurityFtdcMarketDataUpdateTimeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataUpdateTimeField", (char *) "ssis",
                               p->InstrumentID, p->UpdateTime, p->UpdateMillisec, p->ActionDay);
}

CSecurityFtdcMarketDataUpdateTimeField *from_CSecurityFtdcMarketDataUpdateTimeField(PyObject * p) {
    CSecurityFtdcMarketDataUpdateTimeField *t = (CSecurityFtdcMarketDataUpdateTimeField *) calloc(1,
                                                                                                  sizeof(CSecurityFtdcMarketDataUpdateTimeField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataUpdateTimeField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->UpdateTime, PyString_AsString(PyObject_GetAttrString(p, "UpdateTime")));
    t->UpdateMillisec = PyInt_AsLong(PyObject_GetAttrString(p, "UpdateMillisec"));
    strcpy(t->ActionDay, PyString_AsString(PyObject_GetAttrString(p, "ActionDay")));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataAveragePriceField(CSecurityFtdcMarketDataAveragePriceField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataAveragePriceField", (char *) "d",
                               p->AveragePrice);
}

CSecurityFtdcMarketDataAveragePriceField *from_CSecurityFtdcMarketDataAveragePriceField(PyObject * p) {
    CSecurityFtdcMarketDataAveragePriceField *t = (CSecurityFtdcMarketDataAveragePriceField *) calloc(1,
                                                                                                      sizeof(CSecurityFtdcMarketDataAveragePriceField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataAveragePriceField));
    t->AveragePrice = PyFloat_AsDouble(PyObject_GetAttrString(p, "AveragePrice"));

    return t;
};

PyObject *new_CSecurityFtdcMarketDataExchangeField(CSecurityFtdcMarketDataExchangeField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcMarketDataExchangeField", (char *) "s",
                               p->ExchangeID);
}

CSecurityFtdcMarketDataExchangeField *from_CSecurityFtdcMarketDataExchangeField(PyObject * p) {
    CSecurityFtdcMarketDataExchangeField *t = (CSecurityFtdcMarketDataExchangeField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcMarketDataExchangeField));
    memset(t, 0, sizeof(CSecurityFtdcMarketDataExchangeField));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
};

PyObject *new_CSecurityFtdcDisseminationField(CSecurityFtdcDisseminationField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcDisseminationField", (char *) "hi",
                               p->SequenceSeries, p->SequenceNo);
}

CSecurityFtdcDisseminationField *from_CSecurityFtdcDisseminationField(PyObject * p) {
    CSecurityFtdcDisseminationField *t = (CSecurityFtdcDisseminationField *) calloc(1,
                                                                                    sizeof(CSecurityFtdcDisseminationField));
    memset(t, 0, sizeof(CSecurityFtdcDisseminationField));
    t->SequenceSeries = PyInt_AsLong(PyObject_GetAttrString(p, "SequenceSeries"));
    t->SequenceNo = PyInt_AsLong(PyObject_GetAttrString(p, "SequenceNo"));

    return t;
};

PyObject *new_CSecurityFtdcInputFundTransferField(CSecurityFtdcInputFundTransferField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcInputFundTransferField", (char *) "sssssdsc",
                               p->BrokerID, p->InvestorID, p->AccountID, p->Password, p->UserID, p->TradeAmount,
                               p->Digest, p->AccountType);
}

CSecurityFtdcInputFundTransferField *from_CSecurityFtdcInputFundTransferField(PyObject * p) {
    CSecurityFtdcInputFundTransferField *t = (CSecurityFtdcInputFundTransferField *) calloc(1,
                                                                                            sizeof(CSecurityFtdcInputFundTransferField));
    memset(t, 0, sizeof(CSecurityFtdcInputFundTransferField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    t->TradeAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "TradeAmount"));
    strcpy(t->Digest, PyString_AsString(PyObject_GetAttrString(p, "Digest")));
    t->AccountType = PyString_AsString(PyObject_GetAttrString(p, "AccountType"))[0];

    return t;
};

PyObject *new_CSecurityFtdcFundTransferField(CSecurityFtdcFundTransferField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcFundTransferField", (char *) "sssssdsiiissscis",
                               p->BrokerID, p->InvestorID, p->AccountID, p->Password, p->UserID, p->TradeAmount,
                               p->Digest, p->SessionID, p->LiberSerial, p->PlateSerial, p->TransferSerial,
                               p->TradingDay, p->TradeTime, p->FundDirection, p->ErrorID, p->ErrorMsg);
}

CSecurityFtdcFundTransferField *from_CSecurityFtdcFundTransferField(PyObject * p) {
    CSecurityFtdcFundTransferField *t = (CSecurityFtdcFundTransferField *) calloc(1,
                                                                                  sizeof(CSecurityFtdcFundTransferField));
    memset(t, 0, sizeof(CSecurityFtdcFundTransferField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->InvestorID, PyString_AsString(PyObject_GetAttrString(p, "InvestorID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    strcpy(t->Password, PyString_AsString(PyObject_GetAttrString(p, "Password")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));
    t->TradeAmount = PyFloat_AsDouble(PyObject_GetAttrString(p, "TradeAmount"));
    strcpy(t->Digest, PyString_AsString(PyObject_GetAttrString(p, "Digest")));
    t->SessionID = PyInt_AsLong(PyObject_GetAttrString(p, "SessionID"));
    t->LiberSerial = PyInt_AsLong(PyObject_GetAttrString(p, "LiberSerial"));
    t->PlateSerial = PyInt_AsLong(PyObject_GetAttrString(p, "PlateSerial"));
    strcpy(t->TransferSerial, PyString_AsString(PyObject_GetAttrString(p, "TransferSerial")));
    strcpy(t->TradingDay, PyString_AsString(PyObject_GetAttrString(p, "TradingDay")));
    strcpy(t->TradeTime, PyString_AsString(PyObject_GetAttrString(p, "TradeTime")));
    t->FundDirection = PyString_AsString(PyObject_GetAttrString(p, "FundDirection"))[0];
    t->ErrorID = PyInt_AsLong(PyObject_GetAttrString(p, "ErrorID"));
    strcpy(t->ErrorMsg, PyString_AsString(PyObject_GetAttrString(p, "ErrorMsg")));

    return t;
};

PyObject *new_CSecurityFtdcQryFundTransferSerialField(CSecurityFtdcQryFundTransferSerialField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    return PyObject_CallMethod(mod, (char *) "CSecurityFtdcQryFundTransferSerialField", (char *) "ssc",
                               p->BrokerID, p->AccountID, p->AccountType);
}

CSecurityFtdcQryFundTransferSerialField *from_CSecurityFtdcQryFundTransferSerialField(PyObject * p) {
    CSecurityFtdcQryFundTransferSerialField *t = (CSecurityFtdcQryFundTransferSerialField *) calloc(1,
                                                                                                    sizeof(CSecurityFtdcQryFundTransferSerialField));
    memset(t, 0, sizeof(CSecurityFtdcQryFundTransferSerialField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->AccountID, PyString_AsString(PyObject_GetAttrString(p, "AccountID")));
    t->AccountType = PyString_AsString(PyObject_GetAttrString(p, "AccountType"))[0];

    return t;
};
