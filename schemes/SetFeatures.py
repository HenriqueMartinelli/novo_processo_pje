def scheme_SetFeatures(inputs:dict()):
    return {
            "GlobalForm": {
                "headers": {
                            'Accept': '*/*',
                            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Referer': inputs.get('url_process'),
                            'Origin': inputs.get('domain'),
                            'Host': inputs.get('domain').split('//')[1],
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            },
                "payload": {}
                        },
        "SetFeatures": {
                "requests": [{
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "update_form": True,
                            "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'processoPrioridadeProcesso': 'processoPrioridadeProcesso',
                                    'ajaxSingle': 'processoPrioridadeProcesso',
                                    'AJAX:EVENTS_COUNT': '1',
                                        },
                            "headers": {}, 
                            },
                            
                            {
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "update_form": True,
                            "headers": {},
                            "payload":{
                                    'AJAXREQUEST': inputs.get('AjaxRequest'),
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
                            },
                        {
                       
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
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
                        "actions": [ {                                      
                                        "name": "frmSegredoSig_option",
                                        "soup": "#frmSegredoSig\:observacaoSegredoDiv > div > div.name",
                                         "commands": [
                                        {"name": "get_atribute",
                                        "atribute": "id"}]  }]                          },
                        {
                       
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "headers": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'frmSegredoSig': 'frmSegredoSig',
                                    'frmSegredoSig:selectOneRadio': 'true',
                                    f'frmSegredoSig:{inputs.get("frmSegredoSig_option")}:observacaoSegredo': inputs.get("frmSegredoSig_lei") ,
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'frmSegredoSig:grvSegredo': 'frmSegredoSig:grvSegredo',
                                    'AJAX:EVENTS_COUNT': '1'},
                                    
                        },
                        {
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "headers": {},
                        "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcesso': inputs.get('prioridadeProcesso'),
                                    'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcessoSupport': 'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcessoSupport',                                                                       
                                    'ajaxSingle': 'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcesso',
                                    'AJAX:EVENTS_COUNT': '1'
                                },
                            },
                        {        
                        "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                        "update_form": True,
                        "headers": {},
                        "payload":{
                                'AJAXREQUEST': '_viewRoot',
                                'javax.faces.ViewState': inputs.get('ViewState'),
                                'formAddPrioridadeProcesso:prioridadeProcesso:prioridadeProcessoDecoration:prioridadeProcesso': inputs.get('prioridadeProcesso'),
                                'formAddPrioridadeProcesso': 'formAddPrioridadeProcesso',
                                'formAddPrioridadeProcesso:save': 'formAddPrioridadeProcesso:save',
                                'AJAX:EVENTS_COUNT': '1'},
                        
                            }]
                    }}