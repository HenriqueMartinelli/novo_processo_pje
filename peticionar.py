import requests
import base64

from bs4 import BeautifulSoup
from init import BaseRequest
from src.upload import Upload
from src.parts import Parts
from src.login import Login
from src.subject import Subject
from src.createProcess import CreateProcess
from schemes.scheme import SCHEME
from datetime import datetime
from src.utils.convert_bs64 import get_extension


class MainClientException(Exception):
    pass


class Pje_pet(BaseRequest, Login, CreateProcess, Upload, Parts, Subject):

    @BaseRequest.screen_decorator("Login")
    def validate_login(self, username, password, cookies=None):
        self.session = requests.session()
        if cookies:
            if self.append_cookies_in_session(cookies=cookies):
                return self.session.cookies
        return self.login(username=username, password=password)

    @BaseRequest.screen_decorator("CreateProcess")
    def register_process(self):
        inputs = self.inputs.copy()
        self.add_variables_to_inputs(inputs=inputs)
        self.inputs['url_process'] = self.create_process()
        return self.switch_to_screen("SetSubject")

    @BaseRequest.screen_decorator("SetSubject")
    def set_subject(self, subjects: list):
        self.add_subject()
        result = self.queue_subject(subjects=subjects)
        return self.switch_to_screen("SetFeatures")

    @BaseRequest.screen_decorator("SetFeatures")
    def set_features(self):
        for key, value in self.inputs['features'].items():
            self.inputs[key] = value
        self.find_locator('SetFeatures', 'requests', inputs=self.inputs)
        return self.switch_to_screen("SetParts")

    """
    Para cada parte de cada polo irá adicionar a lista de variaveis
    variavel > result, irá ser adcionado ao json passada na api e ser enviada de volta ao webHook
    """
    @BaseRequest.screen_decorator("SetParts")
    def set_parts(self):
        inputs = self.inputs.copy()

        for ativo in self.inputs['polo_ativo']:
            inputs['polo'] = 'PoloAtivo'
            inputs['vicParte'] = 'supResertarVincPartePA'
            for key, value in ativo.items():
                inputs[key] = value
            result = self.add_part(inputs=inputs)
            ativo.update(result)

        for cpf_passivo in self.inputs['polo_passivo']:
            inputs['polo'] = 'PoloPassivo'
            inputs['vicParte'] = 'supResetarVincPartePP'
            for key, value in cpf_passivo.items():
                inputs[key] = value
            result = self.add_part(inputs=inputs)
            cpf_passivo.update(result)
        return self.switch_to_screen("UploadFiles")

    @BaseRequest.screen_decorator("UploadFiles")
    def upload_files(self, num_termo, file_options: list):
        for file in file_options:
            self.change_screen()
            mime, mimetype, file_size = get_extension(file['b64Content'])
            self.find_text(num_termo=num_termo, num_anexo=file['tipo_anexo'])
            self.prepare_upload()

            decode_file = base64.b64decode(file['b64Content'])
            result = self.send_upload(filename=file['filename'],
                                      file=decode_file, mime=mime, file_size=file_size, mimetype=mimetype)

            file.update(result)
            del file['b64Content']
        return self.switch_to_screen("InitialProtocol")

    def start(self, content, file_options):
        self.switch_to_screen("CreateProcess")
        self.register_process()
        self.set_subject(content['subjects'])
        self.set_features()
        self.set_parts()
        self.upload_files(num_termo=content['tipo'], file_options=file_options)
        self.returnMsg(inputs=self.inputs)
