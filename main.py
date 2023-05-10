import requests 
import json
import time
import urllib
import base64

from bs4 import BeautifulSoup
from anticaptchaofficial.hcaptchaproxyless import *
from init import BaseRequest
from upload import Upload
from parties import Parties
from schemes.scheme import SCHEME
from datetime import datetime
from convert_bs64 import get_extension

class MainClientException(Exception):
    pass

class Pje_pet(BaseRequest, Upload, Parties):
    def antiCaptcha(self):
        solver = hCaptchaProxyless()
        solver.set_verbose(1)
        solver.set_key("fa901ee28ac52b82d466a87985a19092")
        solver.set_website_url("https://pje.tjba.jus.br/")
        solver.set_website_key('4098ab2e-d12a-40a8-b836-46df3b32df3f')
        result = solver.solve_and_return_solution()
        return result


    def login(self, username, password, session) -> str:
        self.switch_to_screen("Login")
        for i in range(3):
            self.session = session
            captcha = self.antiCaptcha()
            response_login = self.find_locator('requests', username=username, 
                                        password=password, captcha=captcha, inputs=self.inputs)
            login = self.event_expected("Login", response_login)
            if not login:
                break
        if login:
            raise ValueError('Error in login requests')
        
        return self.switch_to_screen("SearchLinks")



    @BaseRequest.screen_decorator("CreateProcess")
    def create_process(self):
        for key, value in self.inputs.get("dados_iniciais").items():
            self.inputs[key] = value
        html_viewstate = self.session.request('GET',  self.inputs['URL_BASE'] + '/Processo/cadastrar.seam?newInstance=true')
        print(self.inputs['URL_BASE'] + 'Processo/cadastrar.seam?newInstance=true')
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
        # jsonString = screenFeatures.find('a', {'class': 'ml-5 mt-15'})['onclick'].split("containerId':")[1].split(',')[0]
        # self.inputs['AjaxRequest'] =  str(jsonString).replace("'", '')
        # self.inputs['frmSegredoSig'] = screenFeatures.find('input', {'id' : 'frmSegredoSig:selectOneRadio:0'})['onclick'].split('frmSegredoSig:')[1].split("'")[0]
        # print('passei')
        # self.find_locator('SetFeatures', 'requests', index=1, inputs=self.inputs)
        # frmSegredoSig = self.find_locator('SetFeatures', 'requests', index=2, inputs=self.inputs)
        # self.inputs['frmSegredoSig_option'] = frmSegredoSig.select_one('#frmSegredoSig\:observacaoSegredoDiv > div > div.name')['id']

        # self.find_locator('SetFeatures', 'requests', index=3, inputs=self.inputs)
        # self.find_locator('SetFeatures', 'requests', index=4, inputs=self.inputs)
        # self.find_locator('SetFeatures', 'requests', index=5, inputs=self.inputs)
        return self.switch_to_screen("SetParties")


    @BaseRequest.screen_decorator("ScheduleRequestForm")
    def schedule_request(self, filename, file, mime:str, file_size):
        payload = {
                    'AJAXREQUEST': self.inputs['AjaxRequest'],
                    'quantidadeProcessoDocumento': self.inputs['qtdDoc'],
                    'jsonProcessoDocumento': {"array":json.dumps([{'nome': filename + ".pdf", 'tamanho': int(str(file_size).split('.')[0]), 'mime': mime}])},
                    'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
                    'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
                    'AJAX:EVENTS_COUNT': '1'}

    
        payload, headers = self.update_forms(payload=payload, headers={})
        self.request(method='POST', 
                    url=f"{self.inputs['URL_BASE']}/Processo/update.seam",
                    payload=payload,  headers=headers, 
                    params={}, decode=True, files={})

        files = {filename + '.pdf': file}
        self.inputs['files'] = files
        self.inputs['filename'] = filename
        response = self.find_locator('ScheduleRequestForm', 'requests',  inputs=self.inputs)
        self.switch_to_screen("ScheduleRequestForm")
        return response


    @BaseRequest.screen_decorator("SetParties")
    def set_parties(self):
        inputs = self.inputs.copy()
        for ativo in self.inputs['polo_ativo']:
            inputs['polo'] = 'PoloAtivo'
            inputs['vicParte'] = 'supResertarVincPartePA'
            for key, value in ativo.items():
                inputs[key] = value
            self.get_variables_partie(inputsParties=inputs)

        for cpf_passivo in self.inputs['polo_passivo']:
            inputs['polo'] = 'PoloPassivo'
            inputs['vicParte'] = 'supResetarVincPartePP'
            for key, value in cpf_passivo.items():
                inputs[key] = value
            self.get_variables_partie(inputsParties=inputs)


    def upload_files(self, num_termo, file_options:list):
    
        for file in file_options:
            scheme = getattr(SCHEME, "ScheduleRequestForm")(inputs=self.inputs)
            headers = scheme['GlobalForm']['headers']
            page = self.session.get(self.inputs['url_process'], headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")
            self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
            self.change_screen()
            # mime, mimetype, file_size = get_extension(file['b64Content'])
            # decode_file = base64.b64decode(file['b64Content'])
            self.find_text(num_termo=num_termo, num_anexo=file['tipo_anexo'])
            self.prepare_upload()


            # response = self.schedule_request(filename=f"{file_options['filename']}{mimetype}", file=decode_file, 
            #                                 mime=mime, file_size=file_size)
            print(file)
            decode_file = base64.b64decode(file['b64Content'])
            response = self.send_upload(filename=file['filename'],
                file=decode_file, mime='application/pdf', file_size=82318.0)
        return response
    

    def start(self, content, file_options, session):
        self.session = session
        self.switch_to_screen("CreateProcess")
        self.create_process()
        self.set_subject(content['subjects'])
        self.set_features()
        # return self.set_parties()
        self.switch_to_screen("ScheduleRequestForm")
        self.upload_files(num_termo=content['tipo'], file_options=file_options)
        # self.switch_to_screen("SetFeatures")


        # self.upload_files(num_termo=content['tipo'], file_options=file_options)
        