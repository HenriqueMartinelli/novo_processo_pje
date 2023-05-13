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
        return self.switch_to_screen("ScheduleRequestForm")


    def change_screen(self):
        payload = {'AJAXREQUEST': '_viewRoot',
        'javax.faces.ViewState': self.inputs['ViewState'],
        'novoAnexo': 'novoAnexo',
        'AJAX:EVENTS_COUNT': '1'}

        payload = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        data = f'AJAXREQUEST=_viewRoot&javax.faces.ViewState={self.inputs.get("ViewState")}&novoAnexo=novoAnexo&AJAX%3AEVENTS_COUNT=1&'

        scheme = getattr(SCHEME, "ScheduleRequestForm")(inputs=self.inputs)
        # headers = scheme['GlobalForm']['headers']
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'JSESSIONID=U0uMMCcB5Jxphh_9kS2kRs_zb6futieG11R1TN22.pje2gapp013; MO=P; PJE-TJBA-2G-StickySessionRule=pje2gapp013:pje-tjba-2g; ADC_CONN_539B3595F4E=1CCB344C0CEA4805793978C186FF9161020B1E5FCC7E9C49A6ED496145AB28173AEF777156AE364C; ADC_REQ_2E94AF76E7=2278CD030E33F1BF63D38121121AE1C9047FAD79B638795F951EF7EF52BB8A21E6C6B4A94B70D969; _gid=GA1.3.385867627.1682344664; _ga_MXB38QL6YC=GS1.1.1682344664.1.0.1682344664.0.0.0; _ga=GA1.1.1363809521.1682344664',
            'Origin': 'https://pje.tjba.jus.br',
            'Referer': self.inputs['url_process'],
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        change = self.session.post(f"{self.inputs['URL_BASE']}/Processo/update.seam", headers=headers, data=data)
        print(change.url)
        return change
    
        
    def get_url_process(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'JSESSIONID=U0uMMCcB5Jxphh_9kS2kRs_zb6futieG11R1TN22.pje2gapp013; MO=P; PJE-TJBA-2G-StickySessionRule=pje2gapp013:pje-tjba-2g; ADC_CONN_539B3595F4E=1CCB344C0CEA4805793978C186FF9161020B1E5FCC7E9C49A6ED496145AB28173AEF777156AE364C; ADC_REQ_2E94AF76E7=2278CD030E33F1BF63D38121121AE1C9047FAD79B638795F951EF7EF52BB8A21E6C6B4A94B70D969',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }



        response = self.session.get(self.inputs['url_process'], headers=headers)
        url_id = response.url
        print(url_id)
        soup = BeautifulSoup(response.content, "html.parser")
        self.inputs['ViewState'] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        return self.change_screen()


    def send_upload(self, filename, file, mime:str, file_size,):
        response = BeautifulSoup(self.get_url_process().content, "html.parser")
        self.inputs.update(self.search_inputs(response))
        mime='application/pdf'
        file_size=82318.0 


        filename = filename
        arquivo = filename + ".pdf"
        
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
        
        files = {filename + '.pdf': file}
        self.inputs['files'] = files
        self.inputs['filename'] = filename
    
        return self.find_locator('ScheduleRequestForm', 'requests',  inputs=self.inputs)

        self.add_payload_form(index=0)
        self.add_payload_form(index=1)
        self.add_payload_form(index=2)
        return self.add_payload_form(index=3)

