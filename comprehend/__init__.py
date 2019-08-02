#!/usr/bin/python
# -*- coding: utf-8 -*-
# import assistant
# import log as Logger
# import err

from . import assistant
from . import log as Logger
from . import err
log=Logger.log
def createNamedLog(name):
    return Logger.NamedLog(name)
class Object():
    pass
Timer=assistant.Timer
createThread=assistant.createThread
enableGlobalExcept=assistant.enableGlobalExcept
formatString=assistant.formatString
