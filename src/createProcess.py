from urllib.parse import urlparse
from urllib.parse import parse_qs

class CreateProcess():
    
    def add_variables_to_inputs(self, inputs):
        self.CreateInputs = inputs
        for key, value in inputs.get("dados_iniciais").items():
            self.CreateInputs[key] = value
        self.enter_page_register_process()

    def enter_page_register_process(self):
        get_variables_register = self.find_locator("ScreenRegister", 'requests', index=0, inputs=self.CreateInputs)
        self.CreateInputs["ViewState"] = get_variables_register.find('input', {'name': 'javax.faces.ViewState'})['value']

    def create_process(self):
        process_link = self.find_locator('CreateProcess', 'requests', inputs=self.CreateInputs)
        url_process = self.inputs['domain'] + process_link.headers['location']
        
        parsed_url = urlparse(url_process)
        self.inputs['idProcess'] = parse_qs(parsed_url.query).get("idProcesso")[0]
        return url_process
