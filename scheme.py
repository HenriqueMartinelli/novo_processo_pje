# Dictionary with the description of the site screens,
# each screen has an indication of screen, available actions and elements for interaction

def SCHEME(inputs=dict(), files=None, username=None, password=None, captcha=None):
    return {
        "Login": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/logar.seam",
                            "decode": False,
                            "update_form": False,
                            "files": {},
                            "payload":{
                                        'username': username,
                                        'password': password,
                                        'newPassword1': '',
                                        'newPassword2': '',
                                        'g-recaptcha-response': captcha, 
                                        'h-captcha-response': captcha,
                                    },
                            "headers": {
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                                        'Origin': inputs.get('domain'),
                                        'Referer': f"{inputs.get('URL_BASE')}/login.seam?loginComCertificado=false",
                                        },
                            "params": {}
                            }],
                "expected_message": {
                                "tag": "span", "type": "class", "value": "rich-messages-label",
                                "expected_text": '',
                                "not_expected_url": "",
                                "expected_url": "QuadroAviso/listViewQuadroAvisoMensagem.seam",
                                "not_expected": ["A verificação de captcha"]},
                    },
        "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': 'https://pje.tjba.jus.br',
                            'Referer': inputs.get('url_process'),
                            'Host': 'pje.tjba.jus.br',
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
                            "files": files,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                        'processoTrfForm': 'processoTrfForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo': '1861',
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
                            "files": files,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo': '1861',
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
                                        'processoTrfForm': 'processoTrfForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo': '156',
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
                            "files": files,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo': '1861',
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo': '156',
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': '204',
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
                            "files": files,
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'processoTrfForm:classeJudicial:j_id173:areaDireitoCombo': '1861',
                                        'processoTrfForm:classeJudicial:jurisdicaoComboDecoration:jurisdicaoCombo': '156',
                                        'processoTrfForm:classeJudicial:classeJudicialComboDecoration:classeJudicialCombo': '204',
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
                        },
        "SetSubject": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": False,
                            "update_form": True,
                            "headers": {},
                            "files": {},
                            "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'r_processoAssuntoListList:0:j_id366:j_id367': 'r_processoAssuntoListList:0:j_id366:j_id367',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'r_processoAssuntoListList:0:j_id366:j_id367:j_id368': 'r_processoAssuntoListList:0:j_id366:j_id367:j_id368',
                                    'AJAX:EVENTS_COUNT': '1'
                                        },
                            "params": {}
                                }],
                        },

        "SetFeatures": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": False,
                            "update_form": True,
                            "files": {},
                            "headers": {},
                            "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'processoPrioridadeProcesso': 'processoPrioridadeProcesso',
                                    'ajaxSingle': 'processoPrioridadeProcesso',
                                    'AJAX:EVENTS_COUNT': '1',
                                        },
                            "params": {}
                            },
                            {
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": False,
                            "update_form": True,
                            "files": {},
                            "headers": {},
                            "payload":{
                                    'AJAXREQUEST': inputs.get('AJAXREQUEST'),
                                    'formAdicionarCaracteristicasProcesso:solicitadoJuizo100PorCentoDigital:solicitadoJuizo100PorCentoDigitalDecoration:solicitadoJuizo100PorCentoDigitalSelectOneRadio': inputs.get('Juizo100PorCentoDigital'),
                                    'formAdicionarCaracteristicasProcesso:justicaGratuita:justicaGratuitaDecoration:justicaGratuitaSelectOneRadio':inputs.get('justicaGratuita'),
                                    'formAdicionarCaracteristicasProcesso:tutelaLiminar:tutelaLiminarDecoration:tutelaLiminarSelectOneRadio': inputs.get('tutelaLiminar'),
                                    'formAdicionarCaracteristicasProcesso:valorCausa:valorCausaDecoration:valorCausa': inputs.get('valorCausa'),
                                    'formAdicionarCaracteristicasProcesso': 'formAdicionarCaracteristicasProcesso',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formAdicionarCaracteristicasProcesso:salvaCaracteristicaProcessoButton': 'formAdicionarCaracteristicasProcesso:salvaCaracteristicaProcessoButton',
                                    'AJAX:EVENTS_COUNT': '1'
                                    },
                            "params": {}
                            },
                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "headers": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'frmSegredoSig': 'frmSegredoSig',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'frmSegredoSig:selectOneRadio': 'true',
                                    f'frmSegredoSig:{inputs.get("frmSegredoSig")}': f'frmSegredoSig:{inputs.get("frmSegredoSig")}',
                                    'ajaxSingle': 'frmSegredoSig:selectOneRadio',
                                    'AJAX:EVENTS_COUNT': '1'
                                    
                                },
                        "params": {}
                            },
                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "headers": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'frmSegredoSig': 'frmSegredoSig',
                                    'frmSegredoSig:selectOneRadio': 'true',
                                    f'frmSegredoSig:{inputs.get("frmSegredoSig_option")}:observacaoSegredo': inputs.get("frmSegredoSig_lei") ,
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'frmSegredoSig:grvSegredo': 'frmSegredoSig:grvSegredo',
                                    'AJAX:EVENTS_COUNT': '1'},
                                    
                        "params": {}
                        },
                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "headers": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcesso': inputs.get('prioridadeProcesso'),
                                    'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcessoSupport': 'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcessoSupport',
                                    'ajaxSingle': 'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcesso',
                                    'formAddPrioridadeProcesso': 'formAddPrioridadeProcesso',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                        "params": {}
                            },
                        {
                        "method": "POST", 
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "decode": False,
                        "update_form": True,
                        "files": {},
                        "headers": {},
                        "payload":{
                                'AJAXREQUEST': '_viewRoot',
                                'javax.faces.ViewState': inputs.get('ViewState'),
                                'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcesso': inputs.get('prioridadeProcesso'),
                                'formAddPrioridadeProcesso': 'formAddPrioridadeProcesso',
                                'formAddPrioridadeProcesso:save': 'formAddPrioridadeProcesso:save',
                                'AJAX:EVENTS_COUNT': '1'},
                        "params": {}
                            }]
                    },
        
    }
