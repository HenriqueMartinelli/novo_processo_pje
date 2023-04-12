import requests 
import json
import time
from bs4 import BeautifulSoup
from anticaptchaofficial.hcaptchaproxyless import *
from init import BaseRequest
from scheme import SCHEME
from datetime import datetime
import urllib


class MainClientException(Exception):
    pass

class Pje_pet(BaseRequest):
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
        html_viewstate = self.session.request('GET', 'https://pje.tjba.jus.br/pje/Processo/cadastrar.seam?newInstance=true')
        self.inputs['url_process'] = html_viewstate.url

        soup = BeautifulSoup(html_viewstate.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        process_link = self.find_locator('requests', inputs=self.inputs)
        self.inputs['url_process'] = 'https://pje.tjba.jus.br' + process_link[-1].headers['location']
        return  self.switch_to_screen("SetSubject")


    @BaseRequest.screen_decorator("SetSubject")
    def set_subject(self):
        scheme = SCHEME(inputs=self.inputs)
        headers = scheme['GlobalForm']['headers']
        page = self.session.get(self.inputs['url_process'], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        self.find_locator('requests', inputs=self.inputs)

        return self.switch_to_screen("PrepareUpload")
    

    @BaseRequest.screen_decorator("SetFeatures")
    def set_features(self):
        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][0]
        change_features = self.search_data(datas=[data], arquivo=None)
        soup = BeautifulSoup(change_features[-1].content, "html.parser")
        jsonString = soup.find('a', {'class': 'ml-5 mt-15'})['onclick'].split("containerId':")[1].split(',')[0]
        self.inputs['AJAXREQUEST'] =  str(jsonString).replace("'", '')
        self.inputs['frmSegredoSig'] = soup.find('input', {'id' : 'frmSegredoSig:selectOneRadio:0'})['onclick'].split('frmSegredoSig:')[1].split("'")[0]

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][1]
        self.search_data(datas=[data], arquivo=None)
        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][2]
        frmSegredoSig = self.search_data(datas=[data], arquivo=None)
        soup = BeautifulSoup(frmSegredoSig[-1].content, "html.parser")
        self.inputs['frmSegredoSig_option'] = soup.select_one('#frmSegredoSig\:observacaoSegredoDiv > div > div.name')['id']

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][3]
        self.search_data(datas=[data], arquivo=None)

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][4]
        self.search_data(datas=[data], arquivo=None)

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][5]
        self.search_data(datas=[data], arquivo=None)
        return self.switch_to_screen("ScheduleRequestForm")

    @BaseRequest.screen_decorator("ScheduleRequestForm")
    def schedule_request(self, filename, file, mime:str, file_size,):
        payload = {
                    'AJAXREQUEST': self.inputs['AjaxRequest'],
                    'quantidadeProcessoDocumento': self.inputs['qtdDoc'],
                    'jsonProcessoDocumento': {"array":json.dumps([{'nome': filename, 'tamanho': int(str(file_size).split('.')[0]), 'mime': mime}])},
                    'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
                    'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
                    'AJAX:EVENTS_COUNT': '1'}

        payload, headers = self.update_form(payload=payload, headers={})
        scheme = SCHEME(inputs=self.inputs)
        payload.update(scheme['GlobalForm']['payload'])
        self.request(method='POST', 
                    url=f"{self.inputs['URL_BASE']}/Processo/update.seam",
                    payload=payload,  headers=headers, 
                    params={}, decode=True, files={})

        files = {filename: file}
        response = self.find_locator('requests', arquivo=filename, files=files, inputs=self.inputs)
        return response


    @BaseRequest.screen_decorator("PrepareUpload")
    def prepare_upload(self):
        # response  = self.find_locator('requests', inputs=self.inputs)
        response  = self.find_locator('requests', inputs=self.inputs)
        soup = BeautifulSoup(response[-1].content, "html.parser")
        jsonString = soup.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':")[1].split(',')[0]
        self.inputs['AjaxRequest'] =  str(jsonString).replace("'", '')
        self.inputs.update(self.search_inputs(response[-1].content))
        self.switch_to_screen("ScheduleRequestForm")
        return response


    def change_screen(self):
        payload = {'AJAXREQUEST': '_viewRoot',
        'javax.faces.ViewState': self.inputs.get('ViewState'),
        'novoAnexo': 'novoAnexo',
        'AJAX:EVENTS_COUNT': '1'}

        payload = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        scheme = SCHEME(inputs=self.inputs)
        headers = scheme['GlobalForm']['headers']
        
        change = self.session.post("https://pje.tjba.jus.br/pje/Processo/update.seam", headers=headers, data=payload)
        return change


    def start(self, content, mimetype, file, mime, file_size, cont, file_options, session):
        self.session = session
        self.switch_to_screen("CreateProcess")
        self.create_process()
        self.set_subject()
        self.find_text(num_termo=content['tipo'], num_anexo=file_options['tipo_anexo'])
        self.change_screen()
        self.prepare_upload()
  
        response = self.schedule_request(filename=f"{file_options['filename']}{mimetype}", file=file, 
                                         mime=mime, file_size=file_size)
        # self.set_features()

        return response

        # self.switch_to_screen("PrepareUpload")

        # self.prepare_upload()
        # response = self.schedule_request(filename=f"anexo{num}{mimetype}", file=file, 
        #                         num_termo=parametro, mime=mime, file_size=file_size, cont=cont)
        # self.event_expected("ScheduleRequestForm", response)

