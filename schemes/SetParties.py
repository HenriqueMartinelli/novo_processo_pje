def scheme_SetParties(inputs:dict()):
    return {
        "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Referer': inputs.get('url_process'),
                            'Host': 'pje2g.tjba.jus.br',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            },

                            
                "payload": {} 
                        },
        "expected_message": {
                            "index": [2, 5],
                            "expected_text": '',
                            "not_expected_url": "",
                            "expected_url": "",
                            "not_expected": ["Não foi possível recuperar", "Erro inesperado, por favor tente novamente.", "Termo não encontrado", "Termo nã£o encontrado"],
                            "text_area": [
                                {"tag": "span", "type": "class", "value": "rich-messages-label"},
                                {"tag": "td", "type": "class", "value": "rich-sb-cell-padding"},
                                {"tag": "ul", "type": "class", "value": "alert alert-danger"}
                                    ]}, 

        "SetParties": {
            "requests": [
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'tabPartes': 'tabPartes',
                                    'ajaxSingle': 'tabPartes',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'regionPartes',
                                    f'formVincular{inputs.get("polo")}': f'formVincular{inputs.get("polo")}',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    f'formVincular{inputs.get("polo")}:{inputs.get("vicParte")}': f'formVincular{inputs.get("polo")}:supResertarVincParte{inputs.get("vicParte")}',
                                    f'ajaxSingle': f'formVincular{inputs.get("polo")}:toolBarGroupVincular{inputs.get("polo")}',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },

                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'F',
                                    'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                                    'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': inputs.get('cpf'),
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'preCadastroPessoaFisicaForm:pesquisarDocumentoPrincipal': 'preCadastroPessoaFisicaForm:pesquisarDocumentoPrincipal',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },

                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:preCadastroPessoaFisicaRegion',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'F',
                                    'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                                    'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': inputs.get('cpf'),
                                    'preCadastroPessoaFisicaForm:dsNomeCivil': inputs.get('name'),
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'preCadastroPessoaFisicaForm:btnConfirmarCadastro': 'preCadastroPessoaFisicaForm:btnConfirmarCadastro',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },
                                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'regionAssociarParte',
                                    'preCadastroPessoaFisicaForm:dsNomeCivil': inputs.get('name'),
                                    'autoScroll': '',
                                    'formInserirParteProcesso:tpParteAlteracao': 0,
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',

                                    'autoScroll': '',
                                    'formInserirParteProcesso:enderecoUsuario': 'formInserirParteProcesso:enderecoUsuario',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },


                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    inputs.get('formInserirParteProcessos'): inputs.get('formInserirParteProcessos'),
                                    'ajaxSingle': inputs.get('formInserirParteProcessos'),
                                    'inputvalue':inputs.get('cep'),
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',


                                },
                        "headers":{},
                        "params": {}
                            },

                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('EndereconomeLogradouro'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '0',
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': '',
                                    'ajaxSingle': inputs.get('formInserirParteProcessos'),
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',
                                    inputs.get('GridTabList'): inputs.get('GridTabList'),
                                    f'{inputs.get("GridTabList")}:_link_hidden_': '' ,
                                    f'{inputs.get("GridTabList")}:j_idcl': '',
                                    'AJAX:EVENTS_COUNT': '1',
                                    inputs.get('formInserirParteProcessosFinal'): inputs.get('formInserirParteProcessosFinal'),

                                },
                        "headers":{},
                        "params": {}
                            },

                            {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': inputs.get("estado"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': inputs.get("cidade"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': inputs.get("bairro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': inputs.get("logradouro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': '200',
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': inputs.get("endereco"),
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get('GridTabList'): inputs.get('GridTabList'),
                                    f'{inputs.get("GridTabList")}:_link_hidden_': '' ,
                                    f'{inputs.get("GridTabList")}:j_idcl': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecobtnGravarEndereco': 'formInserirParteProcesso:cadastroPartePessoaEnderecobtnGravarEndereco',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',
                                    'autoScroll': '', 
                                    'formInserirParteProcesso:comboRepresentanteDecoration:comboRepresentante': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                    inputs.get('comboParteSigilosa'): 'false',

                                },
                        "headers":{},
                        "params": {}
                            },
                                                {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'regionAssociarParte',
                                    'formInserirParteProcesso:tpParteAlteracao': '0',
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'javax.faces.ViewState': inputs.get('ViewState'),


                                },
                        "headers":{},
                        "params": {}
                            },
                            

                {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'regionAssociarParte',
                                    'formInserirParteProcesso:tpParteAlteracao': '0',
                                    'formInserirParteProcesso:nomeSocial': '',
                                    'formInserirParteProcesso:nomeDecoration:nome': inputs.get('name'),
                                    'formInserirParteProcesso:nomeParteDecoration:nomeParte': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                    'formInserirParteProcesso:nomeGenitorDecoration:nomeGenitor': inputs.get('nomeGenitor'),
                                    'formInserirParteProcesso:dataObitoDecoration:dataObitoInputDate': inputs.get('data_obito'),
                                    'formInserirParteProcesso:dataObitoDecoration:dataObitoInputCurrentDate': '05/2023',
                                    'formInserirParteProcesso:etniaDecoration:etnia': inputs.get('etnia'),
                                    'formInserirParteProcesso:estadoCivilDecoration:estadoCivil': inputs.get('estado_civil'),
                                    'formInserirParteProcesso:escolaridadeDecoration:escolaridade': inputs.get('escolaridade'),
                                    inputs.get('idProfissaoAdv'): inputs.get('profissao'),
                                    inputs.get('_selection'): '',
                                    'formInserirParteProcesso:selectPaisNacionalidadeDecoration:selectPaisNacionalidade': inputs.get('nacionalidade'),
                                    inputs.get('comboParteSigilosa'): 'false',
                                    'formInserirParteProcesso:comboRepresentanteDecoration:comboRepresentante': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formInserirParteProcesso:btnInserirParteProcesso': 'formInserirParteProcesso:btnInserirParteProcesso',
                                    'ajaxSingle': 'formInserirParteProcesso:btnInserirParteProcesso',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'formResetarVinculacaoPartes': 'formResetarVinculacaoPartes',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    f'formResetarVinculacaoPartes:reRender{inputs.get("polo")}': f'formResetarVinculacaoPartes:reRender{inputs.get("polo")}',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            }
            ]
        },
        "EditEndress": {
            "requests": [
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get("AjaxRequest"),
                                    inputs.get("GridTabList"): inputs.get("GridTabList"),
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    inputs.get("GridTabListComplete"): inputs.get("GridTabListComplete"),
                                    'firstResult': '0',
                                    'page': '1',
                                    'ajaxSingle': inputs.get("GridTabListComplete"),
                                    'AJAX:EVENTS_COUNT': '1'},
                        "headers":{},
                        "params": {}
                            },

                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': inputs.get("estado"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': inputs.get("cidade"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': inputs.get("bairro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': inputs.get("logradouro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': inputs.get('numeroEndereco'),
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': inputs.get("endereco"),
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get('GridTabList'): inputs.get('GridTabList'),
                                    f'{inputs.get("GridTabList")}:_link_hidden_': '' ,
                                    f'{inputs.get("GridTabList")}:j_idcl': '',
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEndereco': 'formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEndereco',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',
                                    'formInserirParteProcesso:comboRepresentanteDecoration:comboRepresentante': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue'},
                        "headers":{},
                        "params": {}
                    },

                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': inputs.get("estado"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': inputs.get("cidade"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': inputs.get("bairro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': inputs.get("logradouro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': inputs.get('numeroEndereco'),
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': inputs.get("endereco"),
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get('GridTabList'): inputs.get('GridTabList'),
                                    f'{inputs.get("GridTabList")}:_link_hidden_': '' ,
                                    f'{inputs.get("GridTabList")}:j_idcl': '',
                                    inputs.get("formInserirParte"): inputs.get("formInserirParte"),
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',},
                        "headers":{},
                        "params": {}
                    },
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': inputs.get("estado"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': inputs.get("cidade"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': inputs.get("bairro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': inputs.get("logradouro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': inputs.get('numeroEndereco'),
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': inputs.get("endereco"),
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get('GridTabList'): inputs.get('GridTabList'),
                                    f'{inputs.get("GridTabList")}:_link_hidden_': '' ,
                                    f'{inputs.get("GridTabList")}:j_idcl': '',
                                    "formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEnderecoSim": "formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEnderecoSim",
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',},
                        "headers":{},
                        "params": {}
                    }
            ]},
        "SetAndress": {
            "requests": [
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': inputs.get("formInserirParte"),
                                    inputs.get("GridTabList"): inputs.get("GridTabList"),
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    inputs.get("GridTabListComplete"): inputs.get("GridTabListComplete"),
                                    'firstResult': '0',
                                    'page': '1',
                                    'ajaxSingle': inputs.get("GridTabListComplete"),
                                    'AJAX:EVENTS_COUNT': '1'},
                        "headers":{},
                        "params": {}
                            },
                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'regionPartes',
                                    f'formVincular{inputs.get("polo")}': f'formVincular{inputs.get("polo")}',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    f'formVincular{inputs.get("polo")}:{inputs.get("vicParte")}': f'formVincular{inputs.get("polo")}:supResertarVincParte{inputs.get("vicParte")}',
                                    f'ajaxSingle': f'formVincular{inputs.get("polo")}:toolBarGroupVincular{inputs.get("polo")}',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },

                                                {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:preCadastroPessoaFisicaRegion',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'A',
                                    'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                                    'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': '',
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'ajaxSingle': 'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:supTipoPessoa':'preCadastroPessoaFisicaForm:tipoPessoaDecoration:supTipoPessoa',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },

                                                                            {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'A',

                                    f'{inputs.get("formInserirParte")}:pessoaAutoridadeSuggest':'A FAZENDA PUBLICA DO ESTADO DA BAHIA',
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    f'{inputs.get("formInserirParteProcessos")}_selection': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'ajaxSingle': inputs.get("formInserirParteProcessos"),
                                    inputs.get("formInserirParteProcessos"): inputs.get("formInserirParteProcessos"),
                                    'inputvalue': 'A FAZENDA PUBLICA DO ESTADO DA BAHIA',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },


                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'A',

                                    f'{inputs.get("formInserirParte")}:pessoaAutoridadeSuggest':'A FAZENDA PUBLICA DO ESTADO DA BAHIA',
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    f'{inputs.get("formInserirParteProcessos")}_selection': '0',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'ajaxSingle': inputs.get("formInserirParteProcessosFinal"),
                                    inputs.get("formInserirParteProcessosFinal"): inputs.get("formInserirParteProcessosFinal"),
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },

                                                    {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'A',

                                    f'{inputs.get("formInserirParte")}:pessoaAutoridadeSuggest':'A FAZENDA PUBLICA DO ESTADO DA BAHIA',
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    f'{inputs.get("formInserirParteProcessos")}_selection': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'preCadastroPessoaFisicaForm:btnConfirmarCadastro': 'preCadastroPessoaFisicaForm:btnConfirmarCadastro',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },
                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "files": {},
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'A',

                                    f'{inputs.get("formInserirParte")}:pessoaAutoridadeSuggest':'A FAZENDA PUBLICA DO ESTADO DA BAHIA',
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'autoScroll': '',
                                    f'{inputs.get("formInserirParteProcessos")}_selection': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formInserirParteProcesso:btnInserirParteProcesso': 'formInserirParteProcesso:btnInserirParteProcesso',
                                    'ajaxSingle': 'formInserirParteProcesso:btnInserirParteProcesso',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "headers":{},
                        "params": {}
                            },

                            ],
                    }
       
    }