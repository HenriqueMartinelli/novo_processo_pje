
class Parts():

    """
    Estrutura de chamadas dessa classe
    Caso acontece erro irá enviar a função que trata erros
    """

    def add_part(self, inputs):
        try:
            self.inputsParts = inputs
            variables = self.get_variables_part(inputs)
            self.inputsParts.update(variables)
            self.get_name_part(inputs)
            setAndress = self.change_to_screen_add_andress()
            dict_andress = self.verify_andress(setAndress)
            return self.add_parts_to_process(content=dict_andress)
        except Exception as error:
            raise ValueError(self.return_error(error=error))

    """
    Adicionando a json de variaveis as variaveis global desse form
    """

    def get_variables_part(self, inputsParts):
        getVariables = self.find_locator(
            "SetParts", 'requests', index=0, inputs=inputsParts)
        return {
            "_form_partes": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).form['id'],
            "complete_id_partes": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).script['id'],
            "id_form_partes_total": getVariables.find('table', {'id': 'mpAssociarParteProcessoContentTable'}).find('script')['id']}

    """
    Tenta acha o cpf da parte
    Se não achar retorno um erro dizendo > "Cpf Not found"
    """

    def get_name_part(self, inputsParts):
        optionsPart = self.find_locator("SetParts", 'requests', index=1, inputs=inputsParts)
        if not optionsPart.find("div", {"id": "panelPasso1_header"}):
            self.add_option_part(content=optionsPart)

        findCpf = self.find_locator("SetParts", 'requests', index=2, inputs=inputsParts)
        resultSearch = findCpf.select_one("[id*='divResultadoPesquisaPessoa']").findAll('input')
        for result in resultSearch:
            if result.get('value'):
                inputsParts['name'] = result['value']
                return self.set_person()
        raise RuntimeError({"Error": "Cpf Not found"})

    """
    Irá procurar todas opções de partes e selecionar a partir do texto que foi enviado=tipo_parte
    """

    def add_option_part(self, content):
        options = content.findAll("option")
        type_part = self.inputsParts['tipo_parte']
        for option in options:
            if option.text == type_part.upper():
                self.inputsParts.update(
                    {
                        "tipo_parte": option['value'],
                        "id_select_complete": content.select_one("#divTipoPartePolo").find("select")['name'],
                        "id_select": content.select_one("#divTipoPartePolo").find("form")['id'],
                        "similarityGroupingId": content.select_one("#divTipoPartePolo").find("select")['onchange'].split("similarityGroupingId':'")[1].split("'")[0]})

                return self.find_locator("AddOptionsParts", 'requests', index=0, inputs=self.inputsParts)
        options = [option.text for option in options]
        raise RuntimeError(
            {"Error": f"Option: {type_part} not found in select options: {options}"})

    """
    Confirmando cpf irá adicionar essa parte as variaveis do formulario
    """

    def set_person(self):
        setPerson = self.find_locator(
            "SetParts", 'requests', index=3, inputs=self.inputsParts)
        self.person = setPerson
        self.inputsParts['idProfissaoAdv'] = setPerson.select_one(
            '[for*=profissao]')['for']
        self.inputsParts['_selection'] = setPerson.select_one(
            '[id*=_selection]')['id']
        self.inputsParts['comboParteSigilosa'] = setPerson.select_one(
            '[for*=comboParteSigilosa]')['for']

    """
    Irá passar a screen de adicionar endereço e adicionando variaveis usadas nessa screen
    """

    def change_to_screen_add_andress(self):
        setAndress = self.find_locator(
            "SetParts", 'requests', index=4, inputs=self.inputsParts)
        jsonString = setAndress.select_one(
            'table[id*="AdicionarEndereco_shifted"]')['onclick']
        AjaxRequest = str(jsonString).split("containerId':")[
            1].split(',')[0].replace("'", '')
        
        self.inputsParts.update({
            "formInserirParteProcessosFinal": setAndress.select_one("div:nth-child(1) > div.value.col-sm-12 > div:nth-child(3) > script").text.split("parameters':{")[1].split("'")[1],
            "formInserirParteProcessos": setAndress.select_one('table[id*="suggest"]')["id"].split(':suggest')[0],
            "formInserirParte": setAndress.select_one('div[id*="fieldcadastroPartePessoaEnderecoCEPDiv"]')["id"].split(':field')[0],
            "AjaxRequest": AjaxRequest,
            "GridTabList":  setAndress.select_one("input[name*='GridTabList']")['value']})
        return setAndress

    """
    Verifica se já existe o cpf no perfil do cpf cadastrado > caso sim, irá editar com os parametros enviados
    Caso não exista, irá cadastrar um novo
     """

    def verify_andress(self, content):
        is_found = self.find_andress(content=content)
        if is_found.get("check_cep"):
            self.edit_andress()
            return_screen_andress = self.change_to_screen_add_andress()
            return self.find_andress(content=return_screen_andress, ConfirmedRegister=True)
        self.new_andress()
        return_screen_andress = self.change_to_screen_add_andress()
        return self.find_andress(content=return_screen_andress, ConfirmedRegister=True)

    def find_andress(self, content, ConfirmedRegister=False):
        table_andress = content.select_one(
            'tbody[id*="cadastroPartePessoaEndereco"]')
        for tr in table_andress.findAll('tr'):
            if self.inputsParts['cep'] == tr.findAll('td')[2].span.text:
                tds = tr.findAll('td')
                self.inputsParts['GridTabList'] = tr.findAll('td')[
                    0].form['id']
                self.inputsParts['GridTabListComplete'] = tr.findAll('td')[
                    0].a['id']

                return {
                    "check_cep": True,
                    "cep": tds[2].text,
                    "Logradouro": tds[3].text,
                    "Número": tds[4].text,
                    "Complemento": tds[5].text
                }
        if ConfirmedRegister:
            raise RuntimeError({"Error": "Cep not found in andress list"})
        return {
            "check_cep": False
        }

    """
    Editando o endereco que faz check com cep passado, editando para novo endereço com o mesmo cep
    """

    def edit_andress(self):
        return self.find_locator('EditAddress', 'requests', inputs=self.inputsParts)

    """
    Cadastrando um novo endereco
    Termo não encontrado, erro > cep não foi Encontrado    
    """

    def new_andress(self):
        self.getLogradouro = self.find_locator("SetParts", 'requests', index=5, inputs=self.inputsParts)

        self.inputsParts['EndereconomeLogradouro'] = self.getLogradouro.select_one(
            'span[id*="colunaSugestaoEnderecoLogradouro"]').text
        getaddress = self.find_locator("SetParts", 'requests', index=6, inputs=self.inputsParts)
        # self.get_variable_new_andress(content=getaddress)
        self.find_locator("SetParts", 'requests',
                          index=7, inputs=self.inputsParts)
        return self.find_locator("SetParts", 'requests', index=8, inputs=self.inputsParts)

    """
    Função que tentar achar variaveis de retorno do cep passado
    """

    def get_variable_new_andress(self, content):
        return self.inputsParts.update({
            "bairro": content.select_one('input[id*="nomeBairro"]').get('value'),
            "estado": content.select_one('input[id*="nomeEstado"]').get('value'),
            "logradouro": content.select_one('input[id*="nomeLogradouro"]').get('value'),
            "cidade": content.select_one('input[id*="nomeCidade"]').get('value'),
            "endereco": content.select_one('input[id*="Enderecocomplemento"]').get('value')})

    """
    PASSO final irá confirmar todos os atributos passados e resetar a screen e retornando ao ponto zero.
    Quando resetado a screen irá tentar achar os nomes da partes e confirmar qual cpf enviado está na pagina.
    """

    def add_parts_to_process(self, content):
        self.h = self.find_locator( "SetParts", 'requests', index=9, inputs=self.inputsParts)
        self.findPartie = self.find_locator("SetParts", 'requests', index=10, inputs=self.inputsParts)
        parts_in_process = self.findPartie.select( f"[id*='gridPartes{self.inputsParts['polo']}List']")
        for parts in parts_in_process:
            self.partes_proc = parts_in_process
            part = parts.find("span", {"class": "text-bold"})
            if part:
                if self.inputsParts['name'] in part.text.strip():
                    return self.appendPart(msg=f"Added part:{part.text}", screen="SetParts", error=False,
                                           contentAddress=content)
        raise RuntimeError(
            {"Error": f"part not found: {self.inputsParts.get('cpf')}"})

    def appendPart(self, msg, error, screen, contentAddress, response=200):
        if not screen:
            screen = self.current_screen
        if msg:
            return {
                "screen": screen,
                "msg": msg,
                "error": error,
                "status_code": response,
                "address_registered": contentAddress}
