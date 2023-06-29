def scheme_SetPartsCnpj(inputs: dict()):
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
                        f'ajaxSingle': f'formVincular{inputs.get("polo")}:toolBarGroupVincular{inputs.get("polo")}'},
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
                        "preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa": "J",
                        "preCadastroPessoaFisicaForm:isOrgaoPublico1Decoration:isOrgaoPublico1SelectOneRadio": inputs.get("orgao_publico"),
                        "preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPJDecoration:preCadastroPessoaFisica_nrCPJ": inputs.get("cnpj"),
                        'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
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
                        'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': "J",
                        "preCadastroPessoaFisicaForm:isOrgaoPublico1Decoration:isOrgaoPublico1SelectOneRadio": inputs.get("orgao_publico"),
                        "preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPJDecoration:preCadastroPessoaFisica_nrCPJ": inputs.get("cnpj"),
                        "preCadastroPessoaFisicaForm:dsNomePJDecoration:dsNomePJ": inputs.get('name'),
                        "preCadastroPessoaFisicaForm:dsNomeFantasiaDecoration:dsNomeFantasia": inputs.get('name'),
                        'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                        'preCadastroPessoaFisicaForm:btnConfirmarCadastro': 'preCadastroPessoaFisicaForm:btnConfirmarCadastro',

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
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:nomeParteDecoration:nomeParte': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:idCadastroPPJnomeFantasiaDecoration:idCadastroPPJnomeFantasia': inputs.get("name"),
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:idCadastroPPJnomeResponsavelDecoration:idCadastroPPJnomeResponsavel': '',
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:idCadastroPPJdataFimAtividadeDecoration:idCadastroPPJdataFimAtividadeInputDate': '',
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:idCadastroPPJdataFimAtividadeDecoration:idCadastroPPJdataFimAtividadeInputCurrentDate': '06/23',
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm': 'formInserirParteProcesso:idCadastroPPJInfoPessoalForm',
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:j_idcl': '',
                        'formInserirParteProcesso:idCadastroPPJInfoPessoalForm:_link_hidden_': '',
                        inputs.get('comboParteSigilosa'): 'false',
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
    "ChangeScreenPerson": {
            "requests": [
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": True,
                    "payload": {
                        'AJAXREQUEST': 'preCadastroPessoaFisicaForm:preCadastroPessoaFisicaRegion',
                        'destino': '',
                        'tipoPessoa': '',
                        'isBrasileiro': '',
                        'tipoEspecializado': '',
                        "preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa": inputs.get("tipo_pessoa"),
                        'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                        'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                        "ajaxSingle": "preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa",
                        "preCadastroPessoaFisicaForm:tipoPessoaDecoration:supTipoPessoa": "preCadastroPessoaFisicaForm:tipoPessoaDecoration:supTipoPessoa",
                    },
                    "headers": {},
                },]
        },
    }    
    
