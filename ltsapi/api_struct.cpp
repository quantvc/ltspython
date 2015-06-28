#include "api_struct.h"

static PyObject *mod = NULL;

PyObject *register_struct(PyObject * self, PyObject * args) {
    mod = PyTuple_GetItem(args, 0);
    Py_INCREF(Py_None);
    return Py_None;
}



PyObject *new_CSecurityFtdcRspInfoField(CSecurityFtdcRspInfoField * p) {

    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }

    return PyObject_CallMethod(mod, "CSecurityFtdcRspInfoField", "is",
                               p->ErrorID, p->ErrorMsg);

}

CSecurityFtdcRspInfoField *from_CSecurityFtdcRspInfoField(PyObject * p) {
    CSecurityFtdcRspInfoField *t = (CSecurityFtdcRspInfoField *) calloc(1, sizeof(CSecurityFtdcRspInfoField));
    memset(t, 0, sizeof(CSecurityFtdcRspInfoField));
    t->ErrorID = PyInt_AsLong(PyObject_GetAttrString(p, "ErrorID"));
    strcpy(t->ErrorMsg, PyString_AsString(PyObject_GetAttrString(p, "ErrorMsg")));

    return t;
}


PyObject *new_CSecurityFtdcRspUserLoginField(CSecurityFtdcRspUserLoginField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, "CSecurityFtdcRspUserLoginField", "sssssiis",
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
}

PyObject *new_CSecurityFtdcUserLogoutField(CSecurityFtdcUserLogoutField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, "CSecurityFtdcUserLogoutField", "ss",
                               p->BrokerID, p->UserID);
}

CSecurityFtdcUserLogoutField *from_CSecurityFtdcUserLogoutField(PyObject * p) {
    CSecurityFtdcUserLogoutField *t = (CSecurityFtdcUserLogoutField *) calloc(1, sizeof(CSecurityFtdcUserLogoutField));
    memset(t, 0, sizeof(CSecurityFtdcUserLogoutField));
    strcpy(t->BrokerID, PyString_AsString(PyObject_GetAttrString(p, "BrokerID")));
    strcpy(t->UserID, PyString_AsString(PyObject_GetAttrString(p, "UserID")));

    return t;
}



PyObject *new_CSecurityFtdcSpecificInstrumentField(CSecurityFtdcSpecificInstrumentField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, "CSecurityFtdcSpecificInstrumentField", "ss",
                               p->InstrumentID, p->ExchangeID);
}

CSecurityFtdcSpecificInstrumentField *from_CSecurityFtdcSpecificInstrumentField(PyObject * p) {
    CSecurityFtdcSpecificInstrumentField *t = (CSecurityFtdcSpecificInstrumentField *) calloc(1,
                                                                                              sizeof(CSecurityFtdcSpecificInstrumentField));
    memset(t, 0, sizeof(CSecurityFtdcSpecificInstrumentField));
    strcpy(t->InstrumentID, PyString_AsString(PyObject_GetAttrString(p, "InstrumentID")));
    strcpy(t->ExchangeID, PyString_AsString(PyObject_GetAttrString(p, "ExchangeID")));

    return t;
}


PyObject *new_CSecurityFtdcDepthMarketDataField(CSecurityFtdcDepthMarketDataField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, "CSecurityFtdcDepthMarketDataField",
                               "ssssdddddddiddddddddsididididididididididids",
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
}


PyObject *new_CSecurityFtdcReqUserLoginField(CSecurityFtdcReqUserLoginField * p) {
    if (p == NULL) {
        Py_INCREF(Py_None);
        return Py_None;

    }
    return PyObject_CallMethod(mod, "CSecurityFtdcReqUserLoginField", "sssssssssss",
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
}
