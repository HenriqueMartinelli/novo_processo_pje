import requests 
import json
import time
import urllib
import base64

from bs4 import BeautifulSoup
from init import BaseRequest
from upload import Upload
from parties import Parties
from login import Login
from schemes.scheme import SCHEME
from datetime import datetime
from convert_bs64 import get_extension

class MainClientException(Exception):
    pass

class Pje_pet(BaseRequest, Login, Upload, Parties):

    @BaseRequest.screen_decorator("Login")
    def validate_login(self, username, password, cookies=None):
        self.switch_to_screen("Login")
        self.session = requests.session()
        if cookies:
            if self.append_cookies_in_session(cookies=cookies):
                return self.session.cookies
        return self.login(username=username, password=password)


    @BaseRequest.screen_decorator("CreateProcess")
    def create_process(self):
        for key, value in self.inputs.get("dados_iniciais").items():
            self.inputs[key] = value
        html_viewstate = self.session.request('GET',  self.inputs['URL_BASE'] + '/Processo/cadastrar.seam?newInstance=true')
        self.inputs['url_process'] = html_viewstate.url

        soup = BeautifulSoup(html_viewstate.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        process_link = self.find_locator('CreateProcess', 'requests', inputs=self.inputs)
        self.inputs['url_process'] = self.inputs['domain'] + process_link.headers['location']
        return  self.switch_to_screen("SetSubject")


    @BaseRequest.screen_decorator("SetSubject")
    def set_subject(self, subjects:list):
        scheme = getattr(SCHEME, self.current_screen)(inputs=self.inputs)
        headers = scheme['GlobalForm']['headers']
        page = self.session.get(self.inputs['url_process'], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        self.inputs["assuntoCompleto"] = soup.select_one('label[for*="assuntoCompleto"]')['for']
        self.inputs["codAssuntoTrf"] = soup.select_one('label[for*="codAssuntoTrf"]')['for']

        self.queue_subject(subjects)
        self.switch_to_screen("SetFeatures")
        return self.switch_to_screen("SetFeatures")
    

    def queue_subject(self, subjects:list):
        for subject in subjects:
            self.inputs['num_subject'] = subject
            return self.find_locator('SetSubject', 'requests', inputs=self.inputs)


    @BaseRequest.screen_decorator("SetFeatures")
    def set_features(self):
        self.find_locator('SetFeatures', 'requests', inputs=self.inputs)
        return self.switch_to_screen("SetParties")


    """
    Para cada parte de cada polo irá adicionar a lista de variaveis
    variavel > result, irá ser adcionado ao json passada na api e ser enviada de volta ao webHook
    """
    @BaseRequest.screen_decorator("SetParties")
    def set_parties(self):
        inputs = self.inputs.copy()
        for ativo in self.inputs['polo_ativo']:
            inputs['polo'] = 'PoloAtivo'
            inputs['vicParte'] = 'supResertarVincPartePA'
            for key, value in ativo.items():
                inputs[key] = value
            result = self.add_part(inputsParties=inputs)
            print(result)
            # ativo.update(result)
        
        for cpf_passivo in self.inputs['polo_passivo']:
            inputs['polo'] = 'PoloPassivo'
            inputs['vicParte'] = 'supResetarVincPartePP'
            for key, value in cpf_passivo.items():
                inputs[key] = value
            result = self.add_part(inputsParties=inputs)
            print(result)
            # cpf_passivo.update(result)
            

    @BaseRequest.screen_decorator("UploadFiles")
    def upload_files(self, num_termo, file_options:list):
        for file in file_options:
            self.change_screen()
            # mime, mimetype, file_size = get_extension(file['b64Content'])
            # decode_file = base64.b64decode(file['b64Content'])
            self.find_text(num_termo=num_termo, num_anexo=file['tipo_anexo'])
            self.prepare_upload()

            decode_file = base64.b64decode(file['b64Content'])
            response = self.send_upload(filename=file['filename'],
                file=decode_file, mime='application/pdf', file_size=82318.0)
        return response
    

    def start(self, content, file_options):
        # self.session = session
        self.switch_to_screen("CreateProcess")
        self.create_process()
        self.set_subject(content['subjects'])
        self.set_features()
        self.set_parties()
        # self.switch_to_screen("ScheduleRequestForm")
        # self.upload_files(num_termo=content['tipo'], file_options=file_options)


        