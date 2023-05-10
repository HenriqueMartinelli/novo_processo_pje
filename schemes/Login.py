def scheme_Login(inputs:dict()):
    return {
                "Login": {
                "requests": [{
                            "method": "POST", 
                            "url": f"{inputs.get('URL_BASE')}/logar.seam",
                            "decode": False,
                            "update_form": False,
                            "files": {},
                            "payload":{
                                        'username': inputs.get('username'),
                                        'password': inputs.get("password"),
                                        'newPassword1': '',
                                        'newPassword2': '',
                                        'g-recaptcha-response': inputs.get("captcha"), 
                                        'h-captcha-response': inputs.get("captcha"),
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
                                "not_expected": ["A verificação de captcha"]}

                }
    }