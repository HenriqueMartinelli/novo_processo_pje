from bs4 import BeautifulSoup


class Subject():
    def add_subject(self):
        get_variables_subject = self.find_locator(
            "EnterProcess", 'requests', index=0, inputs=self.inputs)
        self.inputs.update(self.variables_subject(
            content=get_variables_subject))

    def variables_subject(self, content):
        return {
            "ViewState": content.find('input', {'name': 'javax.faces.ViewState'})['value'],
            "assuntoCompleto": content.select_one('label[for*="assuntoCompleto"]')['for'],
            "codAssuntoTrf": content.select_one('label[for*="codAssuntoTrf"]')['for']}

    def queue_subject(self, subjects: list):
        try:
            result = list()
            for subject in subjects:
                self.inputs['num_subject'] = subject
                response_subject = self.find_locator(
                    'SetSubject', 'requests', inputs=self.inputs)
                subject_resp = self.find_subject_in_response(
                    content=response_subject.content, subject=subject)
                result.append(subject_resp)
            return result
        except Exception as error:
            raise ValueError(self.return_error(error=error))

    def find_subject_in_response(self, content, subject):
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find("tbody", {"id": "l_processoAssuntoListList:tb"})
        for tr in table.findAll("tr"):
            subject_number = tr.findAll("td")[1].text.strip()
            subject_name = tr.findAll("td")[3].text.strip()
            if subject == subject_number:
                return {"msg": f"Added subject:{subject_number}, {subject_name}", "screen": "SetParties", "error": False}
        raise RuntimeError({"msg": f"Subject not found",
                           "screen": "SetParties", "error": True})
