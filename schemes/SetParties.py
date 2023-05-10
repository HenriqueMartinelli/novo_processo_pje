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

                            
            "payload": {            
                                    'formInserirParteProcesso:nomeSocial': '',
                                    'destino': '',
                                    'tipoPessoa': '',
                                    'isBrasileiro': '',
                                    'tipoEspecializado': '',
                                    'preCadastroPessoaFisicaForm:tipoPessoaDecoration:tipoPessoa': 'F',
                                    'preCadastroPessoaFisicaForm:isBrasileiroDecoration:isBrasileiroSelectOneRadio': 'true',
                                    'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': inputs.get('cpf'),
                                    'preCadastroPessoaFisicaForm': 'preCadastroPessoaFisicaForm',
                                    'formInserirParteProcesso:nomeDecoration:nome': inputs.get('name'),
                                    'formInserirParteProcesso:nomeGenitorDecoration:nomeGenitor': inputs.get('nomeGenitor'),
                                    'formInserirParteProcesso:dataObitoDecoration:dataObitoInputDate': inputs.get('data_obito'),
                                    'formInserirParteProcesso:dataObitoDecoration:dataObitoInputCurrentDate': '05/2023',
                                    'formInserirParteProcesso:etniaDecoration:etnia': inputs.get('etnia'),
                                    'formInserirParteProcesso:estadoCivilDecoration:estadoCivil': inputs.get('estado_civil'),
                                    'formInserirParteProcesso:escolaridadeDecoration:escolaridade': inputs.get('escolaridade'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeEstadoDecoration:cadastroPartePessoaEndereconomeEstado': inputs.get("estado"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeCidadeDecoration:cadastroPartePessoaEndereconomeCidade': inputs.get("cidade"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeBairroDecoration:cadastroPartePessoaEndereconomeBairro': inputs.get("bairro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconomeLogradouroDecoration:cadastroPartePessoaEndereconomeLogradouro': inputs.get("logradouro"),
                                    'formInserirParteProcesso:cadastroPartePessoaEndereconumeroEnderecoDecoration:cadastroPartePessoaEndereconumeroEndereco': inputs.get('numeroEndereco'),
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecocomplementoDecoration:cadastroPartePessoaEnderecocomplemento': inputs.get("endereco"),
                                    inputs.get('idProfissaoAdv'): inputs.get('profissao'),
                                    inputs.get('_selection'): '',
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso:tpParteAlteracao': '0',   
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get('GridTabList'): inputs.get('GridTabList'),
                                    f'{inputs.get("GridTabList")}:_link_hidden_': '' ,
                                    f'{inputs.get("GridTabList")}:j_idcl': '',
                                    'formInserirParteProcesso:selectPaisNacionalidadeDecoration:selectPaisNacionalidade': inputs.get('nacionalidade'),
                                    inputs.get('comboParteSigilosa'): 'false',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    } 
                        },
        "SetParties": {
            "requests": [
                    {                       
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'tabPartes': 'tabPartes',
                                    'ajaxSingle': 'tabPartes',
                                },
                        "headers":{},
                            },
                    {
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        "payload":{
                                    'AJAXREQUEST': 'regionPartes',
                                    f'formVincular{inputs.get("polo")}': f'formVincular{inputs.get("polo")}',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    f'formVincular{inputs.get("polo")}:{inputs.get("vicParte")}': f'formVincular{inputs.get("polo")}:supResertarVincParte{inputs.get("vicParte")}',
                                    f'ajaxSingle': f'formVincular{inputs.get("polo")}:toolBarGroupVincular{inputs.get("polo")}',
                                },
                        "headers":{},
                            },

                    {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:regionDocumentoPrincipal',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'preCadastroPessoaFisicaForm:pesquisarDocumentoPrincipal': 'preCadastroPessoaFisicaForm:pesquisarDocumentoPrincipal',
                                },
                        "headers":{},
                        
                            },

                    {  
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "payload":{
                                    'AJAXREQUEST': 'preCadastroPessoaFisicaForm:preCadastroPessoaFisicaRegion',
                                    'preCadastroPessoaFisicaForm:preCadastroPessoaFisica_nrCPFDecoration:preCadastroPessoaFisica_nrCPF': inputs.get('cpf'),
                                    'preCadastroPessoaFisicaForm:dsNomeCivil': inputs.get('name'),                                    
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'preCadastroPessoaFisicaForm:btnConfirmarCadastro': 'preCadastroPessoaFisicaForm:btnConfirmarCadastro',
                                },
                        "headers":{},
                            },
                                        {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "payload":{
                                    'AJAXREQUEST': 'regionAssociarParte',
                                    'preCadastroPessoaFisicaForm:dsNomeCivil': inputs.get('name'),  
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'formInserirParteProcesso:enderecoUsuario': 'formInserirParteProcesso:enderecoUsuario',
                                },
                        "headers":{},
                            },


                        {
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get('formInserirParteProcessos'): inputs.get('formInserirParteProcessos'),
                                    'ajaxSingle': inputs.get('formInserirParteProcessos'),
                                    'inputvalue':inputs.get('cep'),
                                    'javax.faces.ViewState': inputs.get('ViewState'),


                                },
                        "headers":{},
                        
                            },

                        {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('EndereconomeLogradouro'),
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '0',
                                    'ajaxSingle': inputs.get('formInserirParteProcessos'),
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',
                                    inputs.get('formInserirParteProcessosFinal'): inputs.get('formInserirParteProcessosFinal'),

                                },
                        "headers":{},
                        
                            },

                            {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecobtnGravarEndereco': 'formInserirParteProcesso:cadastroPartePessoaEnderecobtnGravarEndereco',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'AJAX:EVENTS_COUNT': '1',
                                    inputs.get('comboParteSigilosa'): 'false',

                                },
                        "headers":{},
                        
                            },
                                                {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': 'regionAssociarParte',
                                    'formInserirParteProcesso:tpParteAlteracao': '0',
                                    'formInserirParteProcesso': 'formInserirParteProcesso',
                                    'javax.faces.ViewState': inputs.get('ViewState'),


                                },
                        "headers":{},
                        
                            },
                            

                {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': 'regionAssociarParte',
                                    inputs.get('comboParteSigilosa'): 'false',
                                    'formInserirParteProcesso': 'formInserirParteProcesso',           
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formInserirParteProcesso:btnInserirParteProcesso': 'formInserirParteProcesso:btnInserirParteProcesso',
                                    'ajaxSingle': 'formInserirParteProcesso:btnInserirParteProcesso',
                                },
                        "headers":{},
                        
                            },
                    {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'formResetarVinculacaoPartes': 'formResetarVinculacaoPartes',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    f'formResetarVinculacaoPartes:reRender{inputs.get("polo")}': f'formResetarVinculacaoPartes:reRender{inputs.get("polo")}',
                                },
                        "headers":{},
                        
                            }
            ]
        },
        "EditEndress": {
            "requests": [
                    {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": True,
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': inputs.get("AjaxRequest"),
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'firstResult': '0',
                                    'page': '1',
                                    'ajaxSingle': inputs.get("GridTabListComplete"),
},
                        "headers":{},
                        
                            },

                    {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",                      
                        "update_form": True,                       
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    'formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEndereco': 'formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEndereco',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formInserirParteProcesso:comboRepresentanteDecoration:comboRepresentante': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue'},
                        "headers":{},
                        
                    },

                    {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    inputs.get("formInserirParte"): inputs.get("formInserirParte"),
                                    'javax.faces.ViewState': inputs.get('ViewState'),
},
                        "headers":{},
                        
                    },
                    {
                        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        
                        "update_form": True,
                        
                        "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
                                    f'{inputs.get("formInserirParte")}:cadastroPartePessoaEnderecoCEP': inputs.get('cep'),
                                    f'{inputs.get("formInserirParteProcessos")}_selection':  '',
                                    "formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEnderecoSim": "formInserirParteProcesso:cadastroPartePessoaEnderecobtnAtualizarEnderecoSim",
                                    'javax.faces.ViewState': inputs.get('ViewState')},
                        "headers":{},
                        
                    }
            ]},
       
    }