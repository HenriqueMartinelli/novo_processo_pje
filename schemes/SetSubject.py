def scheme_SetSubjects(inputs:dict()):
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
        "EnterProcess":{
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
                            'Referer': inputs.get('url_process'),
                            'Origin': inputs.get('domain'),
                            'Host': inputs.get('domain').split('//')[1],
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                            }}]},
        "SetSubject": {
                "requests": [{
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "update_form": True,
                            "decode": False,
                            "headers": {},
                            "payload":{
                                        'AJAXREQUEST': '_viewRoot',
                                        'r_processoAssuntoListSearchForm:page': '1',
                                        'r_processoAssuntoListSearchForm:searching': 'true',
                                        inputs.get('assuntoCompleto'): '',
                                        inputs.get('codAssuntoTrf'): inputs.get('num_subject'),
                                        'r_processoAssuntoListSearchForm': 'r_processoAssuntoListSearchForm',
                                        'autoScroll': '',
                                        'javax.faces.ViewState': inputs.get('ViewState'),
                                        'r_processoAssuntoListSearchForm:search': 'r_processoAssuntoListSearchForm:search',
                                        'AJAX:EVENTS_COUNT': '1'
                                        },
                                },
                            {
                            "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                            "decode": False,
                            "update_form": True,
                            "headers": {},
                            "payload":{
                                    'AJAXREQUEST': '_viewRoot',
                                    'r_processoAssuntoListList:0:j_id366:j_id367': 'r_processoAssuntoListList:0:j_id366:j_id367',
                                    'autoScroll': '',
                                    'javax.faces.ViewState': inputs.get('ViewState'),
                                    'r_processoAssuntoListList:0:j_id366:j_id367:j_id368': 'r_processoAssuntoListList:0:j_id366:j_id367:j_id368',
                                    'AJAX:EVENTS_COUNT': '1'
                                        },
                                }],
                        }}