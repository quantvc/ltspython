#include "MdAPI.h"
#include "struct.h"

static PyObject *create_MdApi(PyObject * self, PyObject * args) {

    char *path;

    if (!PyArg_ParseTuple(args, "s", &path)) {
        return NULL;
    }
    PyClassObject *api = CSecurityFtdcMdApi::CreateFtdcMdApi(path);

}

static PyObject *Md_Init(PyObject * self, PyObject * args) {

    api->Init();

    Py_INCREF(Py_None);

    return Py_None;
}

static PyObject *Md_Release(PyObject * self, PyObject * args) {

    api->Release();
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *Md_Join(PyObject * self, PyObject * args) {

    PyObject *response =  Py_BuildValue("i",api->Join());

    return response;
}

static PyObject *Md_RegisterFront(PyObject * self, PyObject * args) {

    char * ipAddress;
    if(!PyArg_ParseTuple(args,"s",&ip)){
     return NULL;
    }
    api -> RegisterFront(ipAddress);

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *Md_RegisterSpi(PyObject * self, PyObject * args) {

    PyObject *py_spi;
    if(!PyArg_ParseTuple(args,"O",&py_spi)){
        return NULL;
    }
    CSecurityFtdcMdSpi *spi = new MdSpiWrapper(py_spi);
    api ->RegisterSpi(spi);

    Py_DECREF(py_spi);
    Py_INCREF(Py_None);

    return Py_None;
}

static PyObject *Md_SubscribeMarketData(PyObject * self, PyObject * args) {

    PyObject *instruments = PyTuple_GetItem(args,0);
    PyObject *exchangeid = PyTuple_GetItem(args,1);
    char *exchange = PyString_AsString(exchangeid);
    int length = PySequence_Length(instruments);

    char **inst_list = (char **)calloc(length,sizeof(char *));
    for(int i=0;i<length;i++)
    {
        inst_list[i] = PyString_AsString(PySequence_GetItem(instruments,i));

    }

    api ->SubscribeMarketData(inst_list,length,exchange);
    free(inst_list);
    free(exchange);
    Py_DECREF(instruments);
    Py_DECREF(exchangeid);

    Py_INCREF(Py_None);
    return Py_None;

}

static PyObject *Md_UnSubscribeMarketData(PyObject * self, PyObject * args) {

    PyObject *instruments = PyTuple_GetItem(args,0);
    PyObject *exchangeid = PyTuple_GetItem(args,1);

    char *exchange = PyString_AsString(exchangeid);

    int length = PySequence_Length(instruments);

    char **inst_list= (char **)calloc(length,sizeof(char *));

    for(int i=0;i<length;i++)
    {
        inst_list[i] = PyString_AsString(PySequence_GetItem(instruments,i));
    }

    api->UnSubscribeMarketData(inst_list,length,exchange);

    free(inst_list);
    free(exchange);

    Py_DECREF(instruments);
    Py_DECREF(exchangeid);
    Py_INCREF(Py_None);
    return Py_None;

}


static PyObject *Md_ReqUserLogin(PyObject * self, PyObject * args) {

    PyObject *py_login;
    int requestid;
    if(!PyArg_ParseTuple(args,"Oi",&py_login,&requestid))
    {
        return NULL;
    }

    CSecurityFtdcReqUserLoginField *login_field = from_CSecurityFtdcReqUserLoginField(py_login);
    PyObject *response = Py_BuildValue("i",api->ReqUserLogin(login_field,requestid));

    free(login_field);
    Py_DECREF(py_login);
    return response;
}

static PyObject *Md_ReqUserLogout(PyObject * self, PyObject * args) {

    PyObject *py_logout;
    int logoutid;
    if(!PyArg_ParseTuple(args,"Oi",&py_logout,&logoutid))
    {
        return NULL;
    }
    CSecurityFtdcUserLogoutField *logout_field = from_CSecurityFtdcUserLogoutField(py_logout);
    PyObject *response = Py_BuildValue("i",api->ReqUserLogout(logout_field,logoutid));

    free(logout_field);
    Py_DECREF(py_logout);
    return response;

}


static PyMethodDef MdMethods[] = {
        {"create_MdApi",          create_MdApi,             METH_VARARGS},
        {"ReqUserLogin",          Md_ReqUserLogin,          METH_VARARGS},
        {"ReqUserLogout",         Md_ReqUserLogout,         METH_VARARGS},
        {"Init",                  Md_Init,                  METH_VARARGS},
        {"Join",                  Md_Join,                  METH_VARARGS},
        {"Release",               Md_Release,               METH_VARARGS},
        {"SubscribeMarketData",   Md_SubscribeMarketData,   METH_VARARGS},
        {"UnSubscribeMarketData", Md_UnSubscribeMarketData, METH_VARARGS},
        {"RegisterSpi",           Md_RegisterSpi,           METH_VARARGS},
        {"RegisterFront",         Md_RegisterFront,         METH_VARARGS},
        {NULL,                    NULL,                     0}, /* sentinel */
         /*a value of 0 means that an obsolete variant of PyArg_ParseTuple() is used.*/
};


#ifndef PyMODINIT_FUNC	/* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif

# todo fix __declspec(dllexport)

PyMODINIT_FUNC init_Md(void) {
    Py_InitModule("md_api", MdMethods);
    PyEval_InitThreads();
}

