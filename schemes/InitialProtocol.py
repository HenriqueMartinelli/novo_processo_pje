def scheme_InitialProtocol(inputs:dict()):
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
        "EnterScreen":{
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
                            }},
                {
                    "url": f"{inputs.get('URL_BASE')}/Processo/update.seam",
                    "update_form": False,
                    "decode": True,
                    "payload":{
                        'AJAXREQUEST': '_viewRoot',
                        'javax.faces.ViewState': inputs.get('ViewState'),
                        "informativo": "informativo",
                        "ajaxSingle": "informativo",
                        'AJAX:EVENTS_COUNT': '1'},
                    "headers": {
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Origin': inputs.get('domain'),
                            'Referer': inputs.get('url_process'),
                            'Host': inputs.get('domain').split('//')[1],
                            }}
                ]}
    }