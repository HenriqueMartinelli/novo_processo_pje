import requests 
import json
import base64
import urllib
from bs4 import BeautifulSoup
from anticaptchaofficial.hcaptchaproxyless import *
from schemes.scheme import SCHEME
from datetime import datetime


class Upload():
    def prepare_upload(self):
        response = self.find_locator('PrepareUpload', 'requests', index=0, inputs=self.inputs)
        jsonString = response.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':")[1].split(',')[0]
        self.inputs['AjaxRequest'] =  str(jsonString).replace("'", '')
        self.inputs.update(self.search_inputs(response))
        return self.change_screen()


    def change_screen(self):
        get_page_process = self.find_locator("EnterScreen", 'requests', index=0, inputs=self.inputs)
        self.inputs['ViewState'] = get_page_process.find('input', {'name': 'javax.faces.ViewState'})['value']
        screen = self.find_locator("EnterScreen", 'requests', index=1, inputs=self.inputs)
        return self.inputs.update(self.search_inputs(screen))
    

    def send_upload(self, filename, file, mime:str, file_size, mimetype):
        filename = filename
        arquivo = filename + mimetype
        self.inputs['filename'] = filename
        
        payload = {
                    'AJAXREQUEST': self.inputs['AjaxRequest'],
                    'quantidadeProcessoDocumento': self.inputs['qtdDoc'],
                    'jsonProcessoDocumento': {"array":json.dumps([{'nome': arquivo, 'tamanho': int(str(file_size).split('.')[0]), 'mime': mime}])},
                    'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
                    'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
                    'AJAX:EVENTS_COUNT': '1'}

    
        payload, headers = self.update_form(payload=payload, headers={})
        self.request(method='POST', 
                    url=f"{self.inputs['URL_BASE']}/Processo/update.seam",
                    payload=payload,  headers=headers, 
                    params={}, decode=True, files={})
        
        self.inputs['file_upload'] = {arquivo: file}

        response_upload = self.find_locator('UploadFiles', 'requests',  inputs=self.inputs)
        result = self.event_expected("UploadFiles", response_upload)
        if not result.get('erro'):
            return result
        return result


