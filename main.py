import requests 
import json
import time
import urllib
import base64

from bs4 import BeautifulSoup
from anticaptchaofficial.hcaptchaproxyless import *
from init import BaseRequest
from scheme import SCHEME
from datetime import datetime
from convert_bs64 import get_extension

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
        for key, value in self.inputs.get("dados_iniciais").items():
            self.inputs[key] = value
        html_viewstate = self.session.request('GET', 'https://pje.tjba.jus.br/pje/Processo/cadastrar.seam?newInstance=true')
        self.inputs['url_process'] = html_viewstate.url

        soup = BeautifulSoup(html_viewstate.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        process_link = self.find_locator('requests', inputs=self.inputs)
        self.inputs['url_process'] = 'https://pje.tjba.jus.br' + process_link[-1].headers['location']
        return  self.switch_to_screen("SetSubject")


    @BaseRequest.screen_decorator("SetSubject")
    def set_subject(self, subjects:list):
        scheme = SCHEME(inputs=self.inputs)
        headers = scheme['GlobalForm']['headers']
        page = self.session.get(self.inputs['url_process'], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        self.queue_subject(subjects)
        return self.switch_to_screen("SetFeatures")
    

    def queue_subject(self, subjects:list):
        for subject in subjects:
            self.inputs['num_subject'] = subject
            self.find_locator('requests', inputs=self.inputs)


    @BaseRequest.screen_decorator("SetFeatures")
    def set_features(self):

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][0]
        change_features = self.search_data(datas=[data])
        soup = BeautifulSoup(change_features[-1].content, "html.parser")
        jsonString = soup.find('a', {'class': 'ml-5 mt-15'})['onclick'].split("containerId':")[1].split(',')[0]
        self.inputs['AjaxRequest'] =  str(jsonString).replace("'", '')
        print(str(jsonString).replace("'", ''))
        self.inputs['frmSegredoSig'] = soup.find('input', {'id' : 'frmSegredoSig:selectOneRadio:0'})['onclick'].split('frmSegredoSig:')[1].split("'")[0]

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][1]
        self.search_data(datas=[data])
        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][2]
        frmSegredoSig = self.search_data(datas=[data])
        soup = BeautifulSoup(frmSegredoSig[-1].content, "html.parser")
        self.inputs['frmSegredoSig_option'] = soup.select_one('#frmSegredoSig\:observacaoSegredoDiv > div > div.name')['id']

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][3]
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][4]
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)[self.current_screen]["requests"][5]
        self.search_data(datas=[data])
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
        response = self.find_locator('requests', files=files, inputs=self.inputs)
        self.switch_to_screen("PrepareUpload")
        return response


    @BaseRequest.screen_decorator("SetParties")
    def set_parties(self):
        for ativo in self.inputs['polo_ativo']:
            self.inputs['polo'] = 'PoloAtivo'
            self.inputs['vicParte'] = 'supResertarVincPartePA'
            for key, value in ativo.items():
                self.inputs[key] = value
            # if ativo['tipo_pessoa'] == "autoridade":
            #     self.queue_parties_autoridade()


            self.queue_parties()
        for cpf_passivo in self.inputs['polo_passivo']:
            self.inputs['polo'] = 'PoloPassivo'
            self.inputs['vicParte'] = 'supResetarVincPartePP'
            for key, value in cpf_passivo.items():
                self.inputs[key] = value
            self.queue_parties()


    def queue_parties_autoridade(self):
        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][0]
        ready_partes = self.search_data(datas=[data])
        soup = BeautifulSoup(ready_partes[-1].content, "html.parser")
        
        self.inputs['_form_partes'] = soup.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).form['id']
        self.inputs['complete_id_partes'] = soup.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).script['id']
        self.inputs['id_form_partes_total'] = soup.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).find('script')['id']

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][1]
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][2]
        find_cpf = self.search_data(datas=[data])

        soup = BeautifulSoup(find_cpf[-1].content, "html.parser")
        self.inputs['formInserirParteProcessosFinal'] = soup.select_one("#preCadastroPessoaFisicaForm\\:divAutoridade > div.propertyView.col-sm-4 > div.value.col-sm-12 > div > script").text.split("parameters':{")[1].split("'")[1]
        self.inputs['formInserirParteProcessos'] = soup.select_one('table[id*="suggest"]')["id"].split(':suggest')[0]
        self.inputs['formInserirParte'] = soup.select_one('div[id*="fieldpessoaAutoridadeSuggestDiv"]')["id"].split(':field')[0]
        

    def queue_parties(self):
        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][0]
        ready_partes = self.search_data(datas=[data])
        soup = BeautifulSoup(ready_partes[-1].content, "html.parser")
        
        self.inputs['_form_partes'] = soup.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).form['id']
        self.inputs['complete_id_partes'] = soup.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).script['id']
        self.inputs['id_form_partes_total'] = soup.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).find('script')['id']
        
        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][1]
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][2]
        find_cpf = self.search_data(datas=[data])

        soup = BeautifulSoup(find_cpf[-1].content, "html.parser")
        self.inputs['name'] = soup.find('input', {'id': 'preCadastroPessoaFisicaForm:dsNomeCivil'})['value']
        
        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][3]
        set_person = self.search_data(datas=[data])
        soup = BeautifulSoup(set_person[-1].content, "html.parser")
        self.inputs['idProfissaoAdv'] = soup.select_one('[for*=profissaoAdv]')['for']
        self.inputs['_selection'] = soup.select_one('[id*=_selection]')['id']
        self.inputs['comboParteSigilosa'] = soup.select_one('[for*=comboParteSigilosa]')['for']

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][4]
        setEnderec =  self.search_data(datas=[data])
        soup = BeautifulSoup(setEnderec[-1].content, "html.parser")
        self.inputs['formInserirParteProcessosFinal'] = soup.select_one("div:nth-child(1) > div.value.col-sm-12 > div:nth-child(3) > script").text.split("parameters':{")[1].split("'")[1]
        self.inputs['formInserirParteProcessos'] = soup.select_one('table[id*="suggest"]')["id"].split(':suggest')[0]
        self.inputs['formInserirParte'] = soup.select_one('div[id*="fieldcadastroPartePessoaEnderecoCEPDiv"]')["id"].split(':field')[0]
        jsonString = soup.select_one('table[id*="AdicionarEndereco_shifted"]')['onclick'].split("containerId':")[1].split(',')[0]
        self.inputs['AjaxRequest'] =  str(jsonString).replace("'", '')
        self.inputs['GridTabList'] = soup.select_one("input[name*='GridTabList']")['value']

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][5]  
        get_name = self.search_data(datas=[data])
        soup = BeautifulSoup(get_name[-1].content, "html.parser")
        self.inputs['EndereconomeLogradouro'] = soup.select_one('span[id*="colunaSugestaoEnderecoLogradouro"]').text

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][6]  
        result = self.search_data(datas=[data])
        soup = BeautifulSoup(result[-1].content, "html.parser")
        self.inputs['bairro'] = soup.select_one('input[id*="nomeBairro"]')['value']
        self.inputs['estado'] = soup.select_one('input[id*="nomeEstado"]')['value']
        self.inputs['logradouro'] = soup.select_one('input[id*="nomeLogradouro"]')['value']
        self.inputs['cidade'] = soup.select_one('input[id*="nomeCidade"]')['value']
        self.inputs['endereco'] = soup.select_one('input[id*="Enderecocomplemento"]')['value']

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][7]  
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][8]  
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][9]  
        self.search_data(datas=[data])

        data = SCHEME(inputs=self.inputs)["SetParties"]["requests"][10]  
        return self.search_data(datas=[data])


    @BaseRequest.screen_decorator("PrepareUpload")
    def prepare_upload(self):
        response =self.find_locator('requests', inputs=self.inputs)
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


    def upload_files(self, num_termo, file_options:list):
        scheme = SCHEME(inputs=self.inputs)
        headers = scheme['GlobalForm']['headers']
        page = self.session.get(self.inputs['url_process'], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        self.change_screen()

        # self.set_features()
        for file in file_options:
            # mime, mimetype, file_size = get_extension(file['b64Content'])
            # decode_file = base64.b64decode(file['b64Content'])
            self.find_text(num_termo=num_termo, num_anexo=file['tipo_anexo'])
            self.prepare_upload()


            # response = self.schedule_request(filename=f"{file_options['filename']}{mimetype}", file=decode_file, 
            #                                 mime=mime, file_size=file_size)
            decode_file = base64.b64decode(file['b64Content'])
            self.decode = decode_file
            response = self.schedule_request(file['filename'],
                file=decode_file, mime='application/pdf', file_size=82318.0)
        return response

    def start(self, content, file_options, session):
        self.session = session
        self.switch_to_screen("CreateProcess")
        self.create_process()
        self.set_subject(content['subjects'])
        self.set_features()
        self.set_parties()
        self.switch_to_screen("PrepareUpload")
        self.upload_files(num_termo=content['tipo'], file_options=file_options)
        # self.switch_to_screen("SetFeatures")


        # self.upload_files(num_termo=content['tipo'], file_options=file_options)
        