class Parties():
    def get_variables_partie(self, inputsParties):
        self.inputsParties = inputsParties
        getVariables = self.find_locator("SetParties", 'requests', index=0, inputs=self.inputsParties)
        self.inputsParties.update({
            "_form_partes": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).form['id'],
            "complete_id_partes": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).script['id'],
            "id_form_partes_total": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).find('script')['id']
            })
        return self.get_name_partie()

    def get_name_partie(self):
        self.find_locator("SetParties", 'requests', index=1, inputs=self.inputsParties)
        self.findCpf = self.find_locator("SetParties", 'requests', index=2, inputs=self.inputsParties)
        if self.findCpf.find("span", {"class": "rich-messages-label"}):
            if "não foi possível recuperar" in self.findCpf.find("span", {"class": "rich-messages-label"}).text.lower().strip():
                # raise ValueError("CPF NÃO ENCONTRADO")
                print('nao encontrado')
                return 
        resultSearch = self.findCpf.select_one("[id*='divResultadoPesquisaPessoa']").findAll('input')
        for result in resultSearch:
            if result.get('value'):
                self.inputsParties['name'] = result['value']
                print(self.inputsParties['name'])
                return self.set_person()
        print("erro")
        return "ERRO"


    def set_person(self):
        setPerson = self.find_locator("SetParties", 'requests', index=3, inputs=self.inputsParties)
        self.inputsParties['idProfissaoAdv'] = setPerson.select_one('[for*=profissaoAdv]')['for']
        self.inputsParties['_selection'] = setPerson.select_one('[id*=_selection]')['id']
        self.inputsParties['comboParteSigilosa'] = setPerson.select_one('[for*=comboParteSigilosa]')['for']
        return self.change_to_screen_add_andress()
    
    
    def change_to_screen_add_andress(self):
        setAndress = self.find_locator("SetParties", 'requests', index=4, inputs=self.inputsParties)
        self.inputs.update({
            "formInserirParteProcessosFinal": setAndress.select_one("div:nth-child(1) > div.value.col-sm-12 > div:nth-child(3) > script").text.split("parameters':{")[1].split("'")[1],
            "formInserirParteProcessos": setAndress.select_one('table[id*="suggest"]')["id"].split(':suggest')[0],
            "formInserirParte": setAndress.select_one('div[id*="fieldcadastroPartePessoaEnderecoCEPDiv"]')["id"].split(':field')[0],
            "AjaxRequest": self.get_ajaxRequest(setAndress),
            "GridTabList":  setAndress.select_one("input[name*='GridTabList']")['value'],
        })
        return self.verify_andress()

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
        print('novo endereco')
        self.getLogradouro = self.find_locator("SetParties", 'requests', index=5, inputs=self.inputsParties)
        if self.getLogradouro.find('td', {'class': 'rich-sb-cell-padding'}) in "Termo não encontrado":
            print("Cep Não encontrado")
            return 
        self.inputsParties['EndereconomeLogradouro'] = self.getLogradouro.select_one('span[id*="colunaSugestaoEnderecoLogradouro"]').text
        getEndress = self.find_locator("SetParties", 'requests', index=6, inputs=self.inputsParties)
        self.get_variable_new_andress(content=getEndress)
        self.find_locator("SetParties", 'requests', index=7, inputs=self.inputsParties)
        self.find_locator("SetParties", 'requests', index=8, inputs=self.inputsParties)
        return self.add_partie_to_process()


    def get_variable_new_andress(self, content):
           return self.inputsParties.update({
                "EndereconomeLogradouroselect_one": content.select_one('span[id*="colunaSugestaoEnderecoLogradouro"]').text,
                "bairro": content.select_one('input[id*="nomeBairro"]').get('value'),
                "estado": content.select_one('input[id*="nomeEstado"]').get('value'),
                "logradouro": content.select_one('input[id*="nomeLogradouro"]').get('value'),
                "cidade": content.select_one('input[id*="nomeCidade"]').get('value'),
                "endereco": content.select_one('input[id*="Enderecocomplemento"]').get('value')
            })


    def add_partie_to_process(self):
        self.find_locator("SetParties", 'requests', index=9, inputs=self.inputsParties)
        self.find_locator("SetParties", 'requests', index=10, inputs=self.inputsParties)

    