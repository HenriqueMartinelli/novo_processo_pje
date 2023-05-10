def scheme_CreateProcess(inputs:dict()):
    return {

            "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Referer': inputs.get('url_process'),
                            'Host': inputs.get('domain'),
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            },

                            
                "payload": {} 
                        },
        "CreateProcess": {
                "requests": [
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/cadastrar.seam",
                            "decode": False,
                            "update_form": True,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                        'processoTrfForm': 'processoTrfForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo': inputs.get('materia'),
                                        'processoTrfForm:classeJudicial:j_id173:j_id184': 'processoTrfForm:classeJudicial:j_id173:j_id184',
                                        'ajaxSingle': 'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo',
                                        'AJAX:EVENTS_COUNT': '1',
                                        },
                            "headers":{},
                            "params": {}
                            },
                        {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/cadastrar.seam",
                            "decode": False,
                            "update_form": True,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo':  inputs.get('materia'),
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                        'processoTrfForm': 'processoTrfForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo':  inputs.get('jurisdicao'),
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:j_id197': 'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:j_id197',
                                        'ajaxSingle': 'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo',
                                        'AJAX:EVENTS_COUNT': '1'},
                            "headers":{},
                            "params": {}
                            },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/cadastrar.seam",
                            "decode": False,
                            "update_form": True,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo':  inputs.get('materia'),
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo':  inputs.get('jurisdicao'),
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo':  inputs.get('classe'),
                                        'processoTrfForm': 'processoTrfForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:j_id211': 'processoTrfForm:classeJudicial:classeJudicialComboDecoration:j_id211',
                                        'AJAX:EVENTS_COUNT': '1'},
                            "headers":{},
                            "params": {}
                            },
                                                        {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/cadastrar.seam",
                            "decode": False,
                            "update_form": True,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo': inputs.get('materia'),
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo': inputs.get('jurisdicao'),
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': inputs.get('classe'),
                                        'processoTrfForm': 'processoTrfForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'processoTrfForm:incluiProcessoButton': 'processoTrfForm:incluiProcessoButton',
                                        'AJAX:EVENTS_COUNT': '1'},
                            "headers":{},
                            "params": {}
                            },
                            ],

                "expected_message": {
                                "tag": "span", "type": "class", "value": "rich-messages-label",
                                "expected_text": 'finalizado o upload do arquivo',
                                "expected_url": "",
                                "not_expected_url": "/pje/errorUnexpected.seam?",
                                "not_expected": ["Failed to process the request", "Erro ao tentar gravar o arquivo"]},
                        }}