#!/usr/bin/python
# -*- coding: utf-8 -*-

# 异常类
class ComprehendError(Exception):
    def __init__(self, code, errmsg):
        self.code = code
        self.errmsg = errmsg
        Exception.__init__(self)

    def msg(self, msg):
        if msg:return ComprehendError(self.code, self.errmsg)
        return ComprehendError(8,"unknow error")
# 声明
# 成功
success=ComprehendError(0,"null")
# 通用失败
fail=ComprehendError(1,"fail")
# 参数无效
invalidParameter=ComprehendError(2,"invalid parameter")
# 不支持
noSupport=ComprehendError(3,"no support")
# 不存在
noExist=ComprehendError(4,"no exist")
# 超时
timeout=ComprehendError(5,"timeout")
# 繁忙
busy=ComprehendError(6,"busy")
# 缺少参数
missParameter=ComprehendError(7,"miss parameter")
# 系统错误(通用错误)
systemError=ComprehendError(8,"system error")
# 密码错误
invalidPassword=ComprehendError(9,"invalid password")
# 编码失败
encodeFailed=ComprehendError(10,"encode failed")
# 数据库操作失败
dbOpertationFailed=ComprehendError(11,"db error")
# 已占用
occupied=ComprehendError(12,"occupied")
# session不存在
noSession = ComprehendError(13,'cannot find session')
#没有找到
noFound = ComprehendError(14, "no found")
#已经存在
isExisted = ComprehendError(15, "is existed")
#已经锁定
isLocked = ComprehendError(16, "staff is locked")
#已经过期
isExpired = ComprehendError(17, "is expired")
#无效的账户
invalidUser = ComprehendError(18, "invalid user")

