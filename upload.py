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
        'javax.faces.ViewState': self.inputs.get('ViewState'),
        'novoAnexo': 'novoAnexo',
        'AJAX:EVENTS_COUNT': '1'}

        payload = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        scheme = getattr(SCHEME, "ScheduleRequestForm")(inputs=self.inputs)
        headers = scheme['GlobalForm']['headers']
        change = self.session.post(f"{self.inputs['URL_BASE']}/Processo/update.seam", headers=headers, data=payload)
        return change


    def send_upload(self, filename, file, mime:str, file_size,):
        print('comecou')
        file_size = 82318.0
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
        soup = BeautifulSoup(response.content, "html.parser")
        ViewState =  soup.find('input', {'name': 'javax.faces.ViewState'})['value']

        url_base = 'https://pje.tjba.jus.br/'

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'JSESSIONID=U0uMMCcB5Jxphh_9kS2kRs_zb6futieG11R1TN22.pje2gapp013; MO=P; PJE-TJBA-2G-StickySessionRule=pje2gapp013:pje-tjba-2g; ADC_CONN_539B3595F4E=1CCB344C0CEA4805793978C186FF9161020B1E5FCC7E9C49A6ED496145AB28173AEF777156AE364C; ADC_REQ_2E94AF76E7=2278CD030E33F1BF63D38121121AE1C9047FAD79B638795F951EF7EF52BB8A21E6C6B4A94B70D969; _gid=GA1.3.385867627.1682344664; _ga_MXB38QL6YC=GS1.1.1682344664.1.0.1682344664.0.0.0; _ga=GA1.1.1363809521.1682344664',
            'Origin': 'https://pje.tjba.jus.br',
            'Referer': url_id,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = f'AJAXREQUEST=_viewRoot&javax.faces.ViewState={ViewState}&novoAnexo=novoAnexo&AJAX%3AEVENTS_COUNT=1&'

        change_tela = self.session.post(f'{url_base}pje/Processo/update.seam', headers=headers, data=data)
        soup = BeautifulSoup(change_tela.content, "html.parser")

        cid = soup.find('input', {'name': 'cid'})['value']
        mimes = soup.find('input', {'name': 'mimes'})['value']
        mimesEhSizes =  soup.find('input', {'name': 'mimesEhSizes'})['value']
        AjaxRequest =  soup.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':'")[1].split("',")[0]
        qtdDoc = soup.find('input', {'id': 'quantidadeProcessoDocumento'})['value']
        ViewState =  soup.find('input', {'name': 'javax.faces.ViewState'})['value']
        
        self.inputs['cid'] = cid
        self.inputs['AjaxRequest'] = AjaxRequest
        self.inputs['ViewState'] = ViewState
        self.inputs['qtdDoc']= qtdDoc
        self.inputs['mimesEhSizes'] = mimesEhSizes
        self.inputs['mimes'] = mimes



        payload_init = {
            'AJAXREQUEST': AjaxRequest,
            'formularioUpload': 'formularioUpload',
            'cbTDDecoration:cbTD': '39',
            'ipDescDecoration:ipDesc': 'Petição Inicial',
            'raTipoDocPrincipal': 'HTML',
            'docPrincipalEditorTextArea': '<p>anexo</p>',
            'ipNroDecoration:ipNro': '',
            'context': '/pje',
            'cid': cid,
            'mimes': mimes,
            'mimesEhSizes': mimesEhSizes,
            'tipoDocLoteSuperior': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
            'javax.faces.ViewState': ViewState} 

        headers_init = {
            'Accept': '*/*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://pje.tjba.jus.br',
            'Host': 'pje.tjba.jus.br',
            'Referer': url_id,
        }

        mime='application/pdf'
        file_size=82318.0 


        filename = filename
        arquivo = filename + ".pdf"
        payload = payload_init

        payload.update({
                'AJAXREQUEST': AjaxRequest,
            'quantidadeProcessoDocumento': qtdDoc,
            'jsonProcessoDocumento': {"array":json.dumps([{'nome': arquivo, 'tamanho': int(str(file_size).split('.')[0]), 'mime': mime}])},
            'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
            'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
            'AJAX:EVENTS_COUNT': '1'})
        files = {filename + '.pdf': file}
        self.inputs['files'] = files
        self.inputs['filename'] = filename
        return self.find_locator('ScheduleRequestForm', 'requests', inputs=self.inputs)

        payload_decode = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)

        r = self.session.post(
            url=f'{url_base}pje/Processo/update.seam',
            headers=headers_init,
            data=payload_decode,
            )

        payload = payload_init
        payload.update({
            'j_id673:0:ordem': '2',
            'j_id673:0:numeroDoc': '',
            'quantidadeProcessoDocumento': qtdDoc,
            f'j_id673:{qtdDoc}:tipoDoc': '0',
            f'j_id673:{qtdDoc}:j_id704': f'j_id673:{qtdDoc}:j_id704',
            'ajaxSingle': f'j_id673:{qtdDoc}:tipoDoc',
            'AJAX:EVENTS_COUNT': '1'
            })

        payload_decode = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        
        response_2 = self.session.post(
            url=f'{url_base}pje/Processo/update.seam',
            params={},
            files={},
            headers=headers_init,
            data=payload_decode,
        )
        if arquivo in response_2.text:
            print('esta aqui')

        headers = headers_init
        headers.update({
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
        })
        del headers['Content-Type']

        payload = payload_init

        payload.update({
            'j_id202': 'Salvar',
            'j_id673:0:ordem': '2',
            'j_id673:0:tipoDoc': '0',
            'j_id673:0:descDoc': filename,
            'j_id673:0:numeroDoc': '',
            'quantidadeProcessoDocumento': qtdDoc,
        })

        params = {
            'cid': cid,
            'isLibreOffice': 'undefined',
            }
        files = {filename + '.pdf': file}
        self.inputs['files'] = files
        self.inputs['filename'] = filename
        upload =self.find_locators('ScheduleRequestForm', 'requests', inputs=self.inputs)


        payload = payload_init
        payload.update({
            'j_id673:0:ordem': '2',
            'j_id673:0:numeroDoc': '',
            'quantidadeProcessoDocumento': qtdDoc,
            f'j_id673:{qtdDoc}:commandLinkAtualizarComboTipoDocumento': f'j_id673:{qtdDoc}:commandLinkAtualizarComboTipoDocumento',
            'ajaxSingle': f'j_id673:{qtdDoc}:commandLinkAtualizarComboTipoDocumento',
            'AJAX:EVENTS_COUNT': '1'})
            

        payload_decode = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        self.session.post(
            url=f'{url_base}pje/Processo/update.seam',
            headers=headers_init,
            params={},
            files={},
            data=payload_decode,
        )

        payload = payload_init
        payload.update({
            'j_id673:0:numeroDoc': '',
            f'j_id673:{qtdDoc}:commandLinkGravar': f'j_id673:{qtdDoc}:commandLinkGravar',
            'ajaxSingle': f'j_id673:{qtdDoc}:commandLinkGravar',
            'AJAX:EVENTS_COUNT': '1'})


        payload_decode = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        headers_init = {
            'Accept': '*/*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://pje.tjba.jus.br',
            'Host': 'pje.tjba.jus.br',
            'Referer': url_id,
        }
        response_5 = self.session.post(
            f'{url_base}pje/Processo/update.seam',
            headers=headers_init,
            params={},
            files={},
            data=payload_decode,
        )
        print('terminou')
        if 'Erro ao tentar' in response_5.text.lower():
            print('NAO FOI')
        if 'finalizado' in response_5.text.lower():
            print('ENVIADO')

        # payload = {
        #             'quantidadeProcessoDocumento': self.inputs['qtdDoc'],
        #             'jsonProcessoDocumento': {"array":json.dumps([{'nome': filename, 'tamanho': int(str(file_size).split('.')[0]), 'mime': mime}])},
        #             'acaoAjaxAdicionarProcessoDocumento': 'acaoAjaxAdicionarProcessoDocumento',
        #             'ajaxSingle': 'acaoAjaxAdicionarProcessoDocumento',
        #             'AJAX:EVENTS_COUNT': '1'}

        # payload, headers = self.update_form(payload=payload, headers={})
        # self.request(method='POST', 
        #             url=f"{self.inputs['URL_BASE']}/Processo/CadastroPeticaoAvulsa/peticaoPopUp.seam",
        #             payload=payload,  headers=headers, 
        #             params={}, decode=True, files={})

        # files = {filename: file}
        # return self.find_locator('requests', arquivo=filename, files=files, inputs=self.inputs)

    # def send(self, file_options):
    #     print('está aki')

    #         print(file)
    #         decode_file = base64.b64decode(file['b64Content'])
    #         response = self.send_upload(filename=file['filename'],
    #             file=decode_file, mime='application/pdf', file_size=82318.0)


    # @BaseRequest.screen_decorator("PrepareUpload")
    # def prepare_upload(self):
    #     self.send_editor_text_area()
    #     self.inputs.update(self.search_inputs(self.peticionarHTML.content))
    #     self.switch_to_screen("ScheduleRequestForm")


    # def send_editor_text_area(self):
    #     soup = BeautifulSoup(self.peticionarHTML.content, "html.parser")
    #     self.inputs["ViewState"] = soup.find('input', {'name': 'javax.faces.ViewState'})['value']
    #     self.find_locator('requests', inputs=self.inputs)
    #     data = SCHEME(inputs=self.inputs)["SearchLinks"]["requests"][3]
    #     self.peticionarHTML = self.request(method=data['method'], 
    #                                         url=data['url'], payload=data['payload'], 
    #                                         headers=data['headers'], params=data['params'],
    #                                         decode=data['decode'], files=data['files'])


    # def start(self, content, mimetype, file, mime, file_size, cont, file_options):
    #     self.cont = cont
    #     self.inputs.update(file_options)
    #     self.find_text(num_termo=content['tipo'], num_anexo=file_options['tipo_anexo'])
    #     self.switch_to_screen("SearchLinks")
    #     self.search_links(content['idProcesso'].strip())
    #     self.prepare_upload()
    #     response = self.schedule_request(filename=f"{file_options['filename']}{mimetype}", file=file, 
    #                                      mime=mime, file_size=file_size)
    #     self.event_expected("ScheduleRequestForm", response)

  

