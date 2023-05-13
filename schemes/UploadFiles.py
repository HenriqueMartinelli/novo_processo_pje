def scheme_UploadFiles(inputs:dict()):
    return {
        "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Referer': inputs.get('url_process'),
                            'Host': 'pje.tjba.jus.br',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            },

                            
                "payload": {
                            'AJAXREQUEST': inputs.get('AjaxRequest'),
                            'formularioUpload': 'formularioUpload',
                            'cbTDDecoration:cbTD': inputs.get('num_termo'),
                            'ipDescDecoration:ipDesc': inputs.get('ipDesc'),
                            'raTipoDocPrincipal': 'HTML',
                            'docPrincipalEditorTextArea': '<p>anexo</p>',
                            'ipNroDecoration:ipNro': '',
                            'context': '/pje',
                            'cid': inputs.get('cid'),
                            'mimes': inputs.get('mimes'),
                            'quantidadeProcessoDocumento': inputs.get('qtdDoc'),
                            'j_id673:0:ordem': '2',
                            'j_id673:0:numeroDoc': '',
                            'mimesEhSizes': inputs.get('mimesEhSizes'),
                            'tipoDocLoteSuperior': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                            'javax.faces.ViewState': inputs.get('ViewState')
                            } 
                        },

         "UploadFiles": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
            'j_id673:0:ordem': '2',
            'j_id673:0:numeroDoc': '',
            'quantidadeProcessoDocumento': inputs.get("qtdDoc"),
            f'j_id673:{inputs.get("qtdDoc")}:tipoDoc': '0',
            f'j_id673:{inputs.get("qtdDoc")}:j_id704': f'j_id673:{inputs.get("qtdDoc")}:j_id704',
            'ajaxSingle': f'j_id673:{inputs.get("qtdDoc")}:tipoDoc',
            'AJAX:EVENTS_COUNT': '1'
            },
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/seam/resource/upload",
                            "decode": False,
                            "update_form": True,
                            "files": inputs.get("files"),
                            "payload":{
            'j_id202': 'Salvar',
            'j_id673:0:ordem': '2',
            'j_id673:0:tipoDoc': '0',
            'j_id673:0:descDoc': inputs.get('filename'),
            'j_id673:0:numeroDoc': '',
            'quantidadeProcessoDocumento': inputs.get("qtdDoc"),
        },

                            "headers":{
                                        'X-Requested-With': 'XMLHttpRequest',
                                        'Accept': 'application/json'},
                            "params": {
                                        'cid': inputs.get('cid'),
                                        'isLibreOffice': 'undefined' }
                            },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
            'j_id673:0:ordem': '2',
            'j_id673:0:numeroDoc': '',
            'quantidadeProcessoDocumento': inputs.get("qtdDoc"),
            f'j_id673:{inputs.get("qtdDoc")}:commandLinkAtualizarComboTipoDocumento': f'j_id673:{inputs.get("qtdDoc")}:commandLinkAtualizarComboTipoDocumento',
            'ajaxSingle': f'j_id673:{inputs.get("qtdDoc")}:commandLinkAtualizarComboTipoDocumento',
            'AJAX:EVENTS_COUNT': '1'},
                            "headers": {},
                            "params": {}
                                },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": True,
                            "update_form": True,
                            "files": {},
                            "payload":{
            'j_id673:0:numeroDoc': '',
            f'j_id673:{inputs.get("qtdDoc")}:commandLinkGravar': f'j_id673:{inputs.get("qtdDoc")}:commandLinkGravar',
            'ajaxSingle': f'j_id673:{inputs.get("qtdDoc")}:commandLinkGravar',
            'AJAX:EVENTS_COUNT': '1'},
                            "headers": {
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            },
                            "params": {}
                                }
                            ],

                "expected_message": {
                                "tag": "span", "type": "class", "value": "rich-messages-label",
                                "expected_text": 'finalizado o upload do arquivo',
                                "expected_url": "",
                                "not_expected_url": "/pje/errorUnexpected.seam?",
                                "not_expected": ["Failed to process the request", "Erro ao tentar gravar o arquivo"]},
                        },
        "PrepareUpload": {
                "requests": [
                        {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": True,
                            "update_form": False,
                            "files": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'formularioUpload': 'formularioUpload',
                                        'cbTDDecoration:cbTD': inputs.get('num_termo'),
                                        'ipDescDecoration:ipDesc': inputs.get('ipDesc'),
                                        'ipNroDecoration:ipNro': '',
                                        'raTipoDocPrincipal': 'HTML',
                                        'docPrincipalEditorTextArea': '<p>em anexo</p>',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'j_id652': 'j_id652',
                                        'AJAX:EVENTS_COUNT': '1'
                                    },
                            "headers":{
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Referer': inputs.get('url_process'),
                            'Host': 'pjeg.tjba.jus.br',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            },
                            "params": {}
                                },
                                ],
                        },
        "EnterScreen": {
            "requests": [{
                    "method": "GET", 
                    "url": f"{inputs.get('url_process')}",
                    "update_form": False,
                    "payload":{},
                    "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Host': 'pje.tjba.jus.br',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    }},
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": False,
                    "decode": True,
                    "payload":{
                        'AJAXREQUEST': '_viewRoot',
                        'javax.faces.ViewState': inputs.get('ViewState'),
                        'novoAnexo': 'novoAnexo',
                        'AJAX:EVENTS_COUNT': '1'},
                    "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Referer': inputs.get('url_process'),
                            'Host': 'pje.tjba.jus.br',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            }}
                    
                    
                    ]}


            
    }