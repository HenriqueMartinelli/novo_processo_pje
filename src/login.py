from anticaptchaofficial.hcaptchaproxyless import *

class Login():
    def antiCaptcha(self):
        solver = hCaptchaProxyless()
        solver.set_verbose(1)
        solver.set_key("fa901ee28ac52b82d466a87985a19092")
        solver.set_website_url("https://pje.tjba.jus.br/")
        solver.set_website_key('af4fc5a3-1ac5-4e6d-819d-324d412a5e9d')
        result = solver.solve_and_return_solution()
        return result

    
    def append_cookies_in_session(self, cookies:dict):
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookies)
        test_response = self.find_locator("TestSession", 'requests', inputs=self.inputs)
        if "/painel_usuario/advogado.seam" in test_response.url:
            return True
        return False

    def login(self, username, password) :
        self.inputs.update({
            "username": username,
            "password": password
        })
        for i in range(3):
            self.session = session
            self.inputs.update({
            "username": username,
            "password": password,
            "captcha": self.antiCaptcha()
            })
            response_login = self.find_locator("Login", 'requests', inputs=self.inputs)
            login = self.event_expected("Login", response_login)
            if not login:
                break
        if login:
            raise ValueError('Error in login requests')
        
        return self.session.cookies  