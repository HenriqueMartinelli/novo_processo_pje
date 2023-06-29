from schemes.CreateProcess import scheme_CreateProcess
from schemes.SetFeatures import scheme_SetFeatures
from schemes.SetSubject import scheme_SetSubjects
from schemes.SetParts import scheme_SetParts
from schemes.UploadFiles import scheme_UploadFiles
from schemes.Login import scheme_Login
from schemes.SetPartsCnpj import scheme_SetPartsCnpj


class SCHEME:
    def SetParts(inputs):
        return scheme_SetParts(inputs=inputs)

    def SetSubject(inputs):
        return scheme_SetSubjects(inputs=inputs)

    def SetFeatures(inputs):
        return scheme_SetFeatures(inputs=inputs)

    def UploadFiles(inputs):
        return scheme_UploadFiles(inputs=inputs)

    def CreateProcess(inputs):
        return scheme_CreateProcess(inputs=inputs)
    
    def Login(inputs):
        return scheme_Login(inputs=inputs)
    
    def SetPartsCnpj(inputs):
        return scheme_SetPartsCnpj(inputs=inputs)

    