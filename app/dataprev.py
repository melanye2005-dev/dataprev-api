from playwright.sync_api import sync_playwright

class DataprevBrowser:

    def __init__(self):
        self.p = sync_playwright().start()

        self.browser = self.p.chromium.launch(
            headless=False,
            channel="chrome"
        )

        self.context = self.browser.new_context(
            client_certificates=[{
                "origin": "https://iam.gerid.dataprev.gov.br",
                "certPath": "cert/cert.pem",
                "keyPath": "cert/key.pem"
            }]
        )

        self.page = self.context.new_page()

        self._login()

    def _login(self):

        self.page.goto("https://iam.gerid.dataprev.gov.br/cas/login")

        self.page.get_by_text("Entrar com Certificado Digital").click()

        self.page.wait_for_load_state("networkidle")

        self.page.goto("https://ecoportal.dataprev.gov.br/emprestimos/consultar-emprestimos")

        self.page.get_by_role("button", name="Acessar o Portal do e-Consignado").click()

        self.page.wait_for_load_state("networkidle")

        self.page.get_by_role("link", name="Consultar Empréstimo").click()


    def consultar(self, contrato: str):

        self.page.get_by_role("textbox", name="Número Contrato*").fill(str(contrato))

        with self.page.expect_response(
            lambda r: "consultar-emprestimo" in r.url
        ) as resp:

            self.page.get_by_role("button", name="Consultar").click()

        response = resp.value

        return response.json()


    def close(self):

        self.browser.close()
        self.p.stop()