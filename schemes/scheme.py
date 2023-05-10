from schemes.CreateProcess import scheme_CreateProcess
from schemes.SetFeatures import scheme_SetFeatures
from schemes.SetSubject import scheme_SetSubjects
from schemes.SetParties import scheme_SetParties
from schemes.ScheduleRequestForm import scheme_ScheduleRequestForm

class SCHEME:
    def SetParties(inputs):
        return scheme_SetParties(inputs=inputs)

    def SetSubject(inputs):
        return scheme_SetSubjects(inputs=inputs)

    def SetFeatures(inputs):
        return scheme_SetFeatures(inputs=inputs)

    def ScheduleRequestForm(inputs):
        return scheme_ScheduleRequestForm(inputs=inputs)

    def CreateProcess(inputs):
        return scheme_CreateProcess(inputs=inputs)