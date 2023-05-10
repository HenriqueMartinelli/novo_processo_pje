import json
import urllib
import requests
from bs4 import BeautifulSoup
from schemes.scheme import SCHEME
from datetime import datetime


class BaseRequest:
    def __init__(self):
        
        self.inputs = {'qtdDoc': 0}
        self.current_screen = str()
        self.total_files = str()
        self.idTarefa = str()
        self.oi = ''


    def set_global_variable(self, content:dict, instancia=int):
        self.instancia = instancia
        # self.total_files = total_files
        # self.idTarefa = idTarefa
        URL_1 = 'https://pje.tjba.jus.br/pje'
        URL_2 = 'https://pje2g.tjba.jus.br/pje'

        # self.instancia = 1 if processo[-4:] != '0000' else 2
        self.inputs['URL_BASE'] = URL_1 if self.instancia in (1, '1') else URL_2
        self.inputs['domain'] = self.inputs['URL_BASE'].split('br')[0] + 'br'
        for key, value in content.items():
            self.inputs[key] = value
           

    def search_inputs(self, content):
        try:
            return {
                "cid" :content.find('input', {'name': 'cid'})['value'],
                "mimes" : content.find('input', {'name': 'mimes'})['value'],
                "mimesEhSizes" : content.find('input', {'name': 'mimesEhSizes'})['value'],
                "AjaxRequest" : content.find('input', {'id': 'commandButtonLoteTipo'})['onclick'].split("containerId':'")[1].split("',")[0],
                "qtdDoc" : content.find('input', {'id': 'quantidadeProcessoDocumento'})['value'],
                "ViewState": content.find('input', {'name': 'javax.faces.ViewState'})['value']
            }
        except:
                {"ViewState": content.find('input', {'name': 'javax.faces.ViewState'})['value']}

    

    def switch_to_screen(self, screen: str):
            self.current_screen = screen


    def event_expected(self, screen, response):
        data = SCHEME(inputs=self.inputs)[screen]['expected_message']
        soup = BeautifulSoup(response.content, "html.parser")

        if data.get('tag') and data.get('tag'):
            text_result = soup.find(data['tag'], {data['type']: data['value']})
            if text_result:
                text_result = text_result.text.strip().lower()
                if data['expected_text'] in text_result and data['expected_text'] != "":
                    return self.returnMsg(msg=text_result, error=False, response=response, forced=False)
                for text in data['not_expected']:
                    if text in text_result:
                        return self.returnMsg(msg=text_result, error=True, response=response, forced=False)
        
        if data['not_expected_url'] in response.text and screen == 'ScheduleRequestForm':
            return self.returnMsg(msg="URl error confirmed", error=True, response=response, forced=False)
        if data['expected_url'] != []:
            for url_expected in data['expected_url']:
                if url_expected in response.url:
                    return self.returnMsg(error=False, response=response, forced=False)
        else:
            return True



    def returnMsg(self, forced:bool, msg=None, error=None, response=None):
        if msg is not None:
            self.files.append({
                            "msg": msg,
                            "error": error,
                            "status_code": response})
        else: 
            return error
        if forced or self.total_files == self.cont: 
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            event = {
                    "event":{  
                    "screen":self.current_screen,
                    "created_at":dt_string,
                    "processo": self.processo,
                    "idTarefa": self.idTarefa,
                    "total_files":self.total_files,
                    "data":self.files
                    }}
            # requests.request("POST", url=self.URL_WOOK, json=event, timeout=10)
    
                

    @staticmethod
    def screen_decorator(screen: str):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if self.current_screen != screen:
                    raise Exception(f"Need to be on {screen} screen: {self.current_screen}")
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
           raise ValueError(f'number is not in the json: {e}')
    
    def open_json(self, json_name=None):
        if json_name == "anexo":
            filename = f"itens_anexo_{self.instancia}"
        else:
            filename = f"itens_{self.instancia}"
        with open(f'json_files/{filename}.json') as f:
            return json.load(f)
    
        
    def request(self, method, url, decode:bool, headers=None, payload=None, params=None, files=None):
                # if self.oi != '':
                #     print(payload)
            # try:
                if decode:
                    payload = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
                if files: 
                    print(headers)
                    del headers['Content-Type']
                if not method: 
                    method = 'POST'
                return self.session.request(method, url=url, params=params,
                                    headers=headers, data=payload, files=files)
            # except:
            #     return "Failed to process the request"

    def get_ajaxRequest(self, content):
        jsonString = content.select_one('table[id*="AdicionarEndereco_shifted"]')['onclick']
        return str(jsonString).split("containerId':")[1].split(',')[0].replace("'", '')

    def update_form(self, payload, headers):

                    
            scheme = getattr(SCHEME, self.current_screen)(inputs=self.inputs)
            payloadUpdate = scheme['GlobalForm']['payload']
            headersUpdate = scheme['GlobalForm']['headers']
            payloadUpdate.update(payload), headersUpdate.update(headers)
            # self.payload.update(payloadUpdate)
            return payloadUpdate, headersUpdate
        

    def find_locator(self, locator:str, element:str, index=None, inputs=dict(),):
        screen = self.current_screen
        if index is not None:
            datas = [getattr(SCHEME, screen)(inputs=inputs)[locator][element][index]]
        else:
            datas = getattr(SCHEME, screen)(inputs=inputs)[locator][element]
        return self.search_data(datas=datas, index=index)
    
    
    def search_data(self, datas, index):
        for data in datas:
            if data.get('update_form'):
                data['payload'], data['headers'] = self.update_form(
                                                        payload=data['payload'], headers=data['headers'])

            response = self.request(method=data.get('method'), 
                         url=data.get('url'), payload=data.get('payload'), 
                         headers=data.get('headers'), params=data.get('params'),
                         decode=data.get('decode'), files=data.get('files'))
        if index is not None: 
            return BeautifulSoup(response.content, "html.parser")
        self.response = response
        return response

    

    # def set_actions(self, actions, content):
    #     soup = BeautifulSoup(content, "html.parser")
    #     for action in actions:
    #         inputName = action['name']
    #         variable = soup.select_one(action['soup'])
    #         print('----________-')
    #         print(action['soup'])
    #         print(variable)
    #         for command in action['commands']:
    #             atribute = command['name']
    #             if atribute == "get_atribute":
    #                 variable = variable[command['atribute']]
    #             if atribute == "split":
    #                 variable = variable.split(command['string_split'])[command['index']]
    #             if atribute == "replace": 
    #                 variable = variable.replace(command['separator'], command['transform'])
    #         print(variable)
    #         self.inputs[inputName] = variable
        
    
    
    def find_locators(self, locator:str, element:str, index=None, inputs=dict()):
        screen = self.current_screen
        if index is not None:
            datas = [getattr(SCHEME, screen)(inputs=inputs)[locator][element][index]]
        else:
            datas = getattr(SCHEME, screen)(inputs=inputs)[locator][element]
        for data in datas:
            if data.get('update_form'):
                data['payload'], data['headers'] = self.update_forms(payload=data['payload'], headers=data['headers'])
            response = self.request(method=data['method'], 
                         url=data['url'], payload=data['payload'], 
                         headers=data['headers'], params=data['params'],
                         decode=data['decode'], files=data['files'])
        return response

                



