#ifndef LTSAPI_TRADER_STRUCT_H
#define LTSAPI_TRADER_STRUCT_H

#include <Python.h>
#include "SecurityFtdcUserApiStruct.h"

PyObject *register_struct(PyObject * self, PyObject * args);


PyObject *new_CSecurityFtdcRspInfoField(CSecurityFtdcRspInfoField * p);
CSecurityFtdcRspInfoField *from_CSecurityFtdcRspInfoField(PyObject * p);

PyObject *new_CSecurityFtdcRspUserLoginField(CSecurityFtdcRspUserLoginField * p);
CSecurityFtdcRspUserLoginField *from_CSecurityFtdcRspUserLoginField(PyObject * p);

PyObject *new_CSecurityFtdcUserLogoutField(CSecurityFtdcUserLogoutField * p);
CSecurityFtdcUserLogoutField *from_CSecurityFtdcUserLogoutField(PyObject * p);


PyObject *new_CSecurityFtdcSpecificInstrumentField(CSecurityFtdcSpecificInstrumentField * p);
CSecurityFtdcSpecificInstrumentField *from_CSecurityFtdcSpecificInstrumentField(PyObject * p);


PyObject *new_CSecurityFtdcDepthMarketDataField(CSecurityFtdcDepthMarketDataField * p);
CSecurityFtdcDepthMarketDataField *from_CSecurityFtdcDepthMarketDataField(PyObject * p);



PyObject *new_CSecurityFtdcReqUserLoginField(CSecurityFtdcReqUserLoginField * p);
CSecurityFtdcReqUserLoginField *from_CSecurityFtdcReqUserLoginField(PyObject * p);





#endif