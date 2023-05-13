
class Parties():
    def add_part(self, inputsParties):
        self.inputsParties = inputsParties
        # try:
        variables = self.get_variables_part(inputsParties)
        self.inputsParties.update(variables)
        self.get_name_part(inputsParties)
        setAndress = self.change_to_screen_add_andress()
        self.verify_andress(setAndress)
        return self.add_parts_to_process()
        # except Exception as error:
        #     return self.return_error(error=error)


    def get_variables_part(self, inputsParties):
        getVariables = self.find_locator("SetParties", 'requests', index=0, inputs=inputsParties)
        return {
                "_form_partes": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).form['id'],
                "complete_id_partes": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).script['id'],
                "id_form_partes_total": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).find('script')['id']}


    def get_name_part(self, inputsParties):
        self.find_locator("SetParties", 'requests', index=1, inputs=inputsParties)
        self.findCpf = self.find_locator("SetParties", 'requests', index=2, inputs=inputsParties)
        resultSearch = self.findCpf.select_one("[id*='divResultadoPesquisaPessoa']").findAll('input')
        for result in resultSearch:
            if result.get('value'):
                inputsParties['name'] = result['value']
                return self.set_person()
        raise RuntimeError({"Error": "Cpf Not found"})
        

    def set_person(self):
        setPerson = self.find_locator("SetParties", 'requests', index=3, inputs=self.inputsParties)
        self.inputsParties['idProfissaoAdv'] = setPerson.select_one('[for*=profissaoAdv]')['for']
        self.inputsParties['_selection'] = setPerson.select_one('[id*=_selection]')['id']
        self.inputsParties['comboParteSigilosa'] = setPerson.select_one('[for*=comboParteSigilosa]')['for']
        
    
    
    def change_to_screen_add_andress(self):
        setAndress = self.find_locator("SetParties", 'requests', index=4, inputs=self.inputsParties)
        jsonString = setAndress.select_one('table[id*="AdicionarEndereco_shifted"]')['onclick']
        AjaxRequest =  str(jsonString).split("containerId':")[1].split(',')[0].replace("'", '')
        self.inputsParties.update({
            "formInserirParteProcessosFinal": setAndress.select_one("div:nth-child(1) > div.value.col-sm-12 > div:nth-child(3) > script").text.split("parameters':{")[1].split("'")[1],
            "formInserirParteProcessos": setAndress.select_one('table[id*="suggest"]')["id"].split(':suggest')[0],
            "formInserirParte": setAndress.select_one('div[id*="fieldcadastroPartePessoaEnderecoCEPDiv"]')["id"].split(':field')[0],
            "AjaxRequest": AjaxRequest,
            "GridTabList":  setAndress.select_one("input[name*='GridTabList']")['value']})
        return setAndress


    def verify_andress(self, content):
        table_andress = content.select_one('tbody[id*="cadastroPartePessoaEndereco"]')
        for tr in table_andress.findAll('tr'):
            if self.inputsParties['cep'] == tr.findAll('td')[2].span.text:
                self.inputsParties['GridTabList'] = tr.findAll('td')[0].form['id']
                self.inputsParties['GridTabListComplete']=  tr.findAll('td')[0].a['id']
                return self.edit_andress()
        return self.new_andress()


    def edit_andress(self):
        print('editando')
        return self.find_locator('EditEndress', 'requests', inputs=self.inputsParties)


    def new_andress(self):
        self.getLogradouro = self.find_locator("SetParties", 'requests', index=5, inputs=self.inputsParties)
        self.inputsParties['EndereconomeLogradouro'] = self.getLogradouro.select_one('span[id*="colunaSugestaoEnderecoLogradouro"]').text
        getEndress = self.find_locator("SetParties", 'requests', index=6, inputs=self.inputsParties)
        self.get_variable_new_andress(content=getEndress)
        self.find_locator("SetParties", 'requests', index=7, inputs=self.inputsParties)
        return self.find_locator("SetParties", 'requests', index=8, inputs=self.inputsParties)


    def get_variable_new_andress(self, content):
           return self.inputsParties.update({
                "EndereconomeLogradouroselect_one": content.select_one('span[id*="colunaSugestaoEnderecoLogradouro"]').text,
                "bairro": content.select_one('input[id*="nomeBairro"]').get('value'),
                "estado": content.select_one('input[id*="nomeEstado"]').get('value'),
                "logradouro": content.select_one('input[id*="nomeLogradouro"]').get('value'),
                "cidade": content.select_one('input[id*="nomeCidade"]').get('value'),
                "endereco": content.select_one('input[id*="Enderecocomplemento"]').get('value')})


    def add_parts_to_process(self):
        self.h = self.find_locator("SetParties", 'requests', index=9, inputs=self.inputsParties)
        self.findPartie = self.find_locator("SetParties", 'requests', index=10, inputs=self.inputsParties)
        parts_in_process = self.findPartie.select_one(f"[id*='gridPartes{self.inputsParties['polo']}List']")
        for parts in parts_in_process:
             part = parts.find("span", {"class": "text-bold"})
             if part:
                if self.inputsParties['name'] in part.text.strip():
                    return self.appendPartie(msg=f"Added part:{part.text}", screen="SetParties", error=False)
        return self.appendPartie(msg=f"part not found", screen="SetParties", error=True)


    def appendPartie(self, msg, error, screen, response=200):
        if not screen:
            screen = self.current_screen
        if msg:
            return {
                    "screen": screen,
                    "msg": msg,
                    "error": error,
                    "status_code": response}

    