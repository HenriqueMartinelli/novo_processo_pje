
class InitialProtocol():
    def scraping_process(self):
        infos = dict()
        get_page_process = self.find_locator("EnterScreen", 'requests', index=0, inputs=self.inputs)
        self.inputs['ViewState'] = get_page_process.find('input', {'name': 'javax.faces.ViewState'})['value']
        self.page = self.find_locator("EnterScreen", 'requests', index=1, inputs=self.inputs)

        self.inputs["check_infos"] = self.extract_infos(content=self.page)
        self.inputs["check_details"] = self.extract_details(content=self.page)
        self.inputs["check_document"] = self.extract_document(content=self.page)


    def extract_infos(self, content):
        infos_process = content.select_one("#processoViewSdiv > div.rich-panel > div.rich-panel-body > table")
        result = self.extract_for_line(content=infos_process.findAll("td"))
        return result


    def extract_details(self, content):
        details_process = content.select_one("#pagina > div.clearfix > div.rich-panel > div.rich-panel-body > table")
        result = self.extract_for_line(content=details_process.findAll("td"))
        return result


    def extract_document(self, content):
        documents = content.select_one("[id*='processoDocumentoGridList']")
        files_confirmed = dict()
        for select in documents.select("[id*='processoDocumentoGridList']"):
            if select.get('href') and "AprocessoDocumentoBinHome" in select.get("href"):

                texts = select['onclick'].split("idPdf")[1].split("'")[0]
                tipo, name = texts.split("(")[0], texts.split("(")[1].replace(")", "")
                files_confirmed.update({ "name_file":name, "type_file": tipo})
        return files_confirmed

                
    def extract_for_line(self, content):
        extract = dict()
        for td in content:
            td_contents = td.contents
            name = td_contents[0].text
            for content in td_contents[1:]:
                value = content.text.strip()
                if value == "":
                    continue
                extract.update({name: value})
        return extract
    


    # polo_ativo = list()
# ativo = tds[1].findAll("a")

# for part in ativo:
#     polo_ativo.append(part.text)

# polo_passivo = list()
# ativo = tds[2].findAll("a")
# for part in ativo:
#     polo_passivo.append(part.text)
