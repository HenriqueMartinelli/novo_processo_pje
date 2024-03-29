import json
import urllib
import requests
import traceback

from bs4 import BeautifulSoup
from schemes.scheme import SCHEME
from datetime import datetime


class BaseRequest:
    def __init__(self):
        self.inputs = {'qtdDoc': 0}

    def set_global_variable(self, content: dict, instancia=int):
        self.instancia = instancia
        URL_1 = 'https://pje.tjba.jus.br/pje'
        URL_2 = 'https://pje2g.tjba.jus.br/pje'

        self.inputs['URL_BASE'] = URL_1 if self.instancia in (
            1, '1') else URL_2
        self.inputs['domain'] = self.inputs['URL_BASE'].split('br')[0] + 'br'
        for key, value in content.items():
            self.inputs[key] = value

    def search_inputs(self, content):
        try:
            return {
                "cid": content.find('input', {'name': 'cid'})['value'],
                "mimes": content.find('input', {'name': 'mimes'})['value'],
                "mimesEhSizes": content.find('input', {'name': 'mimesEhSizes'})['value'],
                "AjaxRequest": content.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':'")[1].split("',")[0],
                "qtdDoc": content.find('input', {'id': 'quantidadeProcessoDocumento'})['value'],
                "ViewState": content.find('input', {'name': 'javax.faces.ViewState'})['value']
            }
        except:
            return {"ViewState": content.find('input', {'name': 'javax.faces.ViewState'})['value']}

    def switch_to_screen(self, screen: str):
        self.current_screen = screen

    def event_expected(self, screen, response):
        data = getattr(SCHEME, screen)(inputs=self.inputs)["expected_message"]
        soup = BeautifulSoup(response.content, "html.parser")

        for selector in data.get('text_area'):
            text_result = soup.find(
                selector['tag'], {selector['type']: selector['value']})
            if text_result:
                text_result = text_result.text.strip().lower()
                if data['expected_text'] in text_result and data['expected_text'] != "":
                    return {'msg': text_result, 'error': False, 'response': response, 'forced': False}
                for text in data['not_expected']:
                    if text.lower() in text_result:
                        return {'msg': text_result, 'error': True, response: response, 'forced': False}

        if data['not_expected_url'] in response.text and screen == 'UploadFiles':
            return {'msg': "URl error confirmed", 'error': True, 'response': response}
        if data['expected_url'] != []:
            for url_expected in data['expected_url']:
                if url_expected in response.url:
                    return self.returnMsg(error=False, response=response, forced=False)
        else:
            return True

    def returnMsg(self, inputs=None, error=False, msg=None):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        if error:
            event = {
                "error": True,
                "msg": msg,
                "created_at": dt_string,
                "idTarefa": inputs.get("idTarefa"),
            }
        else:
            event = {
                "polo_ativo": inputs['polo_ativo'],
                "polo_passivo": inputs['polo_passivo'],
                "uploads": inputs['files'],
                "created_at": dt_string,
                "idTarefa": inputs.get("idTarefa"),
                "url": inputs.get('url_process'),
                "idProcesso": inputs['idProcess'],
                "check": inputs.get("check")
            }
        return event
        # requests.request("POST", url=self.URL_WOOK, json=event, timeout=10)

    @staticmethod
    def screen_decorator(screen: str):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if self.current_screen != screen:
                    raise Exception(
                        f"Need to be on {screen} screen: {self.current_screen}")
                return func(self, *args, **kwargs)
            return wrapper
        return decorator

    def find_text(self, num_termo=str, num_anexo=str):
        try:
            js_process = self.open_json()
            js_anexo = self.open_json(json_name="anexo")
            return self.inputs.update({'num_termo': num_termo, 'ipDesc': js_process[num_termo],
                                       "num_anexo": num_anexo, 'ipDescAnexo': js_anexo[num_anexo]})
        except Exception as e:
            raise RuntimeError(f'number is not in the json: {e}')

    def open_json(self, json_name=None):
        if json_name == "anexo":
            filename = f"itens_anexo_{self.instancia}"
        else:
            filename = f"itens_{self.instancia}"
        with open(f'json_files/{filename}.json') as f:
            return json.load(f)

    def request(self, method, url, decode: bool, headers=None, payload=None, params=None, files=None):
        if decode:
            payload = urllib.parse.urlencode(
                payload, quote_via=urllib.parse.quote)
        if files:
            del headers['Content-Type']
        if not method:
            method = 'POST'
            return self.session.post(url=url, params=params,
                                     headers=headers, data=payload, files=files)
        return self.session.request(method, url=url, params=params,
                                    headers=headers, data=payload, files=files)
    

    def update_form(self, payload, headers):
        scheme = getattr(SCHEME, self.current_screen)(inputs=self.inputs)
        payloadUpdate = scheme['GlobalForm']['payload']
        headersUpdate = scheme['GlobalForm']['headers']
        payloadUpdate.update(payload), headersUpdate.update(headers)
        return payloadUpdate, headersUpdate

    def find_locator(self, locator: str, element: str, index=None, inputs=dict(),):
        screen = self.current_screen
        if index is not None:
            expected_event = getattr(SCHEME, screen)(
                inputs=self.inputs).get("expected_message")
            datas = [getattr(SCHEME, screen)(inputs=inputs)
                     [locator][element][index]]
        else:
            expected_event = None
            datas = getattr(SCHEME, screen)(inputs=inputs)[locator][element]

        resultSearch = self.search_data(
            datas=datas, index=index, expected_event=expected_event)
        return self.verify_error(result=resultSearch)

    def verify_error(self, result):
        if type(result) is tuple:
            if result[1] is not None:
                if result[1].get('error') is True:
                    raise RuntimeError(result[1])
            return result[0]
        return result

    def return_error(self, error):
        if type(error) is RuntimeError:
            return {
                "erro": True, "msg": error, "screen": self.current_screen
            }
        return {
            "error": True, "msg": traceback.format_exc(), "screen": self.current_screen
        }

    def search_data(self, datas, index, expected_event):
        for data in datas:
            if data.get('update_form'):
                data['payload'], data['headers'] = self.update_form(
                    payload=data['payload'], headers=data['headers'])

            response = self.request(method=data.get('method'),
                                    url=data.get('url'), payload=data.get('payload'),
                                    headers=data.get('headers'), params=data.get('params'),
                                    decode=data.get('decode'), files=data.get('files'))
            if index is not None:
                soup = BeautifulSoup(response.content, "html.parser")
                if expected_event:
                    result = next(
                        (True for num in expected_event['index'] if str(index) in str(num)), False)
                    if result:
                        event = self.event_expected(
                            self.current_screen, response)
                        return soup, event
                return soup

        return response
