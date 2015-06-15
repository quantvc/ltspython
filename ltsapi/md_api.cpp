#include "MdAPI.h"
#include "trader_struct.h"

static PyObject *create_MdApi(PyObject * self, PyObject * args) {

    char *path;

    if (!PyArg_ParseTuple(args, "s", &path)) {
        return NULL;
    }
    PyObject *api = CSecurityFtdcMdApi::CreateFtdcMdApi(path);

    return api;

}

static PyObject *Md_Init(PyObject * self, PyObject * args) {

    PyObject *api = PyTuple_GetItem(args, 0);

    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;

    api->Init();

    Py_XDECREF(api);
    Py_INCREF(Py_None);

    return Py_None;
}

static PyObject *Md_Release(PyObject * self, PyObject * args) {

    PyObject *api = PyTuple_GetItem(args, 0);

    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;

    api->Release();

    Py_XDECREF(api);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *Md_Join(PyObject * self, PyObject * args) {

    PyObject *api = PyTuple_GetItem(args, 0);

    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;

    PyObject *response = Py_BuildValue("i", api->Join());

    Py_XDECREF(api);
    return response;
}

static PyObject *Md_RegisterFront(PyObject * self, PyObject * args) {


    PyObject *api;
    char *ipAddress;

    if (!PyArg_ParseTuple(args, "Os", &api, &ip)) {
        return NULL;
    }
    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;
    api->RegisterFront(ipAddress);

    Py_XDECREF(api);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *Md_RegisterSpi(PyObject * self, PyObject * args) {


    PyObject *api;
    PyObject *py_spi;
    if (!PyArg_ParseTuple(args, "OO", &api, &py_spi)) {
        return NULL;
    }
    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;

    CSecurityFtdcMdSpi *spi = new MdSpiWrapper(py_spi);
    api->RegisterSpi(spi);
    /* todo fix decref py_spi */
    Py_XDECREF(api);
    Py_XDECREF(py_spi);
    Py_INCREF(Py_None);

    return Py_None;
}

static PyObject *Md_SubscribeMarketData(PyObject * self, PyObject * args) {
    PyObject *api = PyTuple_GetItem(args, 0);

    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;
    PyObject *instruments = PyTuple_GetItem(args, 1);
    PyObject *exchangeid = PyTuple_GetItem(args, 2);
    char *exchange = PyString_AsString(exchangeid);
    int length = PySequence_Length(instruments);

    char **inst_list = (char **) calloc(length, sizeof(char *));
    for (int i = 0; i < length; i++) {
        inst_list[i] = PyString_AsString(PySequence_GetItem(instruments, i));

    }

    api->SubscribeMarketData(inst_list, length, exchange);
    free(inst_list);

    Py_XDECREF(api);
    Py_XDECREF(instruments);
    Py_XDECREF(exchangeid);

    Py_INCREF(Py_None);
    return Py_None;

}

static PyObject *Md_UnSubscribeMarketData(PyObject * self, PyObject * args) {

    PyObject *api = PyTuple_GetItem(args, 0);

    CSecurityFtdcMdApi *api = (CSecurityFtdcMdApi *) api;

    PyObject *instruments = PyTuple_GetItem(args, 1);
    PyObject *exchangeid = PyTuple_GetItem(args, 2);

    char *exchange = PyString_AsString(exchangeid);

    int length = PySequence_Length(instruments);

    char **inst_list = (char **) calloc(length, sizeof(char *));

    for (int i = 0; i < length; i++) {
        inst_list[i] = PyString_AsString(PySequence_GetItem(instruments, i));
    }

    api->UnSubscribeMarketData(inst_list, length, exchange);

    free(inst_list);
    Py_XDECREF(api);
    Py_XDECREF(instruments);
    Py_XDECREF(exchangeid);
    Py_INCREF(Py_None);
    return Py_None;

}


static PyObject *Md_ReqUserLogin(PyObject * self, PyObject * args) {


    PyObject *api;
    PyObject *py_login;
    int requestid;
    if (!PyArg_ParseTuple(args, "OOi", &api, &py_login, &requestid)) {
        return NULL;
    }

    CSecurityFtdcReqUserLoginField *login_field = from_CSecurityFtdcReqUserLoginField(py_login);
    PyObject *response = Py_BuildValue("i", api->ReqUserLogin(login_field, requestid));

    free(login_field);
    Py_XDECREF(api);
    Py_XDECREF(py_login);
    return response;
}

static PyObject *Md_ReqUserLogout(PyObject * self, PyObject * args) {
    PyObject *api;
    PyObject *py_logout;
    int logoutid;

    if (!PyArg_ParseTuple(args, "OOi", &api, &py_logout, &logoutid)) {
        return NULL;
    }
    CSecurityFtdcUserLogoutField *logout_field = from_CSecurityFtdcUserLogoutField(py_logout);
    PyObject *response = Py_BuildValue("i", api->ReqUserLogout(logout_field, logoutid));

    free(logout_field);
    Py_XDECREF(api);
    Py_XDECREF(py_logout);
    return response;

}

#ifndef PyMODINIT_FUNC    /* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif

# todo fix __declspec(dllexport)

PyMODINIT_FUNC init_Md() {

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
    Py_InitModule("md_api", MdMethods);
    PyEval_InitThreads();
}

