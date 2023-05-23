def scheme_SetParts(inputs: dict()):
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
            "payload": {'javax.faces.ViewState': inputs.get('ViewState')}
        },
        "expected_message": {
            "index": [2, 5],
            "expected_text": '',
            "not_expected_url": "",
            "expected_url": "",
                            "not_expected": ["Não foi possível recuperar", "Erro inesperado, por favor tente novamente.", "Termo não encontrado", "Termo nã£o encontrado",
                                             "Erro ao consultar"],
                            "text_area": [
                                {"tag": "span", "type": "class",
                                    "value": "rich-messages-label"},

                                {"tag": "td", "type": "class",
                                    "value": "rich-sb-cell-padding"},
                                {"tag": "ul", "type": "class",
                                    "value": "alert alert-danger"}
            ]},

        "EnterScreen": {
            "requests": [{
                "method": "GET",
                "url": f"{inputs.get('url_process')}",
                "update_form": False,
                "payload": {
                },
                "headers": {
                    'Accept': '*/*',
                    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Origin': inputs.get('domain'),
                    'Host': 'pje2g.tjba.jus.br',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                }}]},
        "SetParts": {
            "requests": [
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': '_viewRoot',
                        'tabPartes': 'tabPartes',
                        'ajaxSingle': 'tabPartes',

                    },
                    "headers": {},
                },
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "decode": True,
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': 'regionPartes',
                        f'formVincular{inputs.get("polo")}': f'formVincular{inputs.get("polo")}',
                        f'formVincular{inputs.get("polo")}:{inputs.get("vicParte")}': f'formVincular{inputs.get("polo")}:supResertarVincParte{inputs.get("vicParte")}',
                        f'ajaxSingle': f'formVincular{inputs.get("polo")}:toolBarGroupVincular{inputs.get("polo")}',

                    },
                    "headers": {},
                },

                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                        'destino': '',
                        'tipoPessoa': '',
                        'isBrasileiro': '',
                        'tipoEspecializado': '',
                        'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'F',
                        'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                        'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': inputs.get('cpf'),
                        "preCadastroPessoaFisicaForm:OABDecoration:preCadastroPessoaFisica_nrOAB": inputs.get('oab'),
                        "preCadastroPessoaFisicaForm:OABDecoration:preCadastroPessoaFisica_ufOAB": inputs.get("oab_uf"),
                        'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                        "preCadastroPessoaFisicaForm:btnPesquisarAdvogado": "preCadastroPessoaFisicaForm:btnPesquisarAdvogado",
                        'preCadastroPessoaFisicaForm:pesquisarDocumentoPrincipal': 'preCadastroPessoaFisicaForm:pesquisarDocumentoPrincipal',

                    },
                    "headers": {},
                },

                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': 'preCadastroPessoaFisicaForm:preCadastroPessoaFisicaRegion',
                        'destino': '',
                        'tipoPessoa': '',
                        'isBrasileiro': '',
                        'tipoEspecializado': '',
                        'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'F',
                        'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                        'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': inputs.get('cpf'),
                        "preCadastroPessoaFisicaForm:OABDecoration:preCadastroPessoaFisica_nrOAB": inputs.get('oab'),
                        "preCadastroPessoaFisicaForm:OABDecoration:preCadastroPessoaFisica_ufOAB": inputs.get("oab_uf"),
                        'preCadastroPessoaFisicaForm:dsNomeCivil': inputs.get('name'),
                        'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                        'preCadastroPessoaFisicaForm:btnConfirmarCadastro': 'preCadastroPessoaFisicaForm:btnConfirmarCadastro',

                    },
                    "headers": {},
                },
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': 'regionAssociarParte',
                        'preCadastroPessoaFisicaForm:dsNomeCivil': inputs.get('name'),
                        'formInserirParteProcesso:tpParteAlteracao': 0,
                        'formInserirParteProcesso': 'formInserirParteProcesso',

                        'formInserirParteProcesso:enderecoUsuario': 'formInserirParteProcesso:enderecoUsuario',

                    },
                    "headers": {},
                },
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': inputs.get('AjaxRequest'),
                        f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                        'formInserirParteProcesso': 'formInserirParteProcesso',
                        f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                        'formInserirParteProcesso:tpParteAlteracao': '0',
                        inputs.get('formInserirParteProcessos'): inputs.get('formInserirParteProcessos'),
                        'ajaxSingle': inputs.get('formInserirParteProcessos'),
                        'inputvalue': inputs.get('cep'),



                    },
                    "headers": {},
                },

                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': inputs.get('AjaxRequest'),
                        f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('EndereconomeLogradouro'),
                        'formInserirParteProcesso': 'formInserirParteProcesso',
                        f'{inputs.get("formInserirParteProcessos")}_selection':  '0',
                        'formInserirParteProcesso:tpParteAlteracao': '0',
                        'ajaxSingle': inputs.get('formInserirParteProcessos'),

                        inputs.get('GridTabList'): inputs.get('GridTabList'),
                        f'{inputs.get("GridTabList")}:_link_hidden_': '',
                        f'{inputs.get("GridTabList")}:j_idcl': '',

                        inputs.get('formInserirParteProcessosFinal'): inputs.get('formInserirParteProcessosFinal'),

                    },
                    "headers": {},
                },

                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': inputs.get('AjaxRequest'),
                        f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                        'formInserirParteProcesso': 'formInserirParteProcesso',
                        'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': inputs.get("estado"),
                        'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': inputs.get("cidade"),
                        'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': inputs.get("bairro"),
                        'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': inputs.get("logradouro"),
                        'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': inputs.get("numeroEndereco"),
                        'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': inputs.get("endereco"),
                        'formInserirParteProcesso:tpParteAlteracao': '0',
                        f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                        inputs.get('GridTabList'): inputs.get('GridTabList'),
                        f'{inputs.get("GridTabList")}:_link_hidden_': '',
                        f'{inputs.get("GridTabList")}:j_idcl': '',
                        'formInserirParteProcesso:cadastroPartePessoaEnderecobtnGravarEndereco': 'formInserirParteProcesso:cadastroPartePessoaEnderecobtnGravarEndereco',

                        'autoScroll': '',
                        'formInserirParteProcesso:comboRepresentanteDecoration:comboRepresentante': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                        inputs.get('comboParteSigilosa'): 'false',

                    },
                    "headers": {},
                },
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': 'regionAssociarParte',
                        'formInserirParteProcesso:tpParteAlteracao': '0',
                        'formInserirParteProcesso': 'formInserirParteProcesso',


                    },
                    "headers": {},
                },


                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "decode": True,
                    "update_form": True,
                    "payload": {
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
                        'formInserirParteProcesso:btnInserirParteProcesso': 'formInserirParteProcesso:btnInserirParteProcesso',
                        'ajaxSingle': 'formInserirParteProcesso:btnInserirParteProcesso',

                    },
                    "headers": {},
                },
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "decode": True,
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': '_viewRoot',
                        'formResetarVinculacaoPartes': 'formResetarVinculacaoPartes',
                        f'formResetarVinculacaoPartes:reRender{inputs.get("polo")}': f'formResetarVinculacaoPartes:reRender{inputs.get("polo")}',

                    },
                    "headers": {},
                }
            ]
        },
        "AddOptionsParts": {
            "requests": [
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        "AJAXREQUEST": "regionAssociarParte",
                        inputs.get("id_select"): inputs.get("id_select"),
                        'javax.faces.ViewState': inputs.get('ViewState'),
                        inputs.get("id_select_complete"): inputs.get("tipo_parte"),
                        "ajaxSingle": inputs.get("id_select_complete"),
                        "autoScroll": "",
                        inputs.get("similarityGroupingId"): inputs.get("similarityGroupingId"),
                        "AJAX:EVENTS_COUNT": "1"},
                    "headers": {},
                },]
        },
        "EditAddress": {
            "requests": [
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "decode": True,
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': inputs.get("AjaxRequest"),
                        inputs.get("GridTabList"): inputs.get("GridTabList"),
                        inputs.get("GridTabListComplete"): inputs.get("GridTabListComplete"),
                        'firstResult': '0',
                        'page': '1',
                        'ajaxSingle': inputs.get("GridTabListComplete"),
                    },
                    "headers": {},
                },

                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
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
                        f'{inputs.get("GridTabList")}:_link_hidden_': '',
                        f'{inputs.get("GridTabList")}:j_idcl': '',
                        'formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEndereco': 'formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEndereco',

                        'formInserirParteProcesso:comboRepresentanteDecoration:comboRepresentante': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue'},
                    "headers": {},
                },

                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
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
                        f'{inputs.get("GridTabList")}:_link_hidden_': '',
                        f'{inputs.get("GridTabList")}:j_idcl': '',
                        inputs.get("formInserirParte"): inputs.get("formInserirParte"),
                    },
                    "headers": {},
                },
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
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
                        f'{inputs.get("GridTabList")}:_link_hidden_': '',
                        f'{inputs.get("GridTabList")}:j_idcl': '',
                        "formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEnderecoSim": "formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEnderecoSim",
                    },
                    "headers": {},
                }
            ]},
    }
