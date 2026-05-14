from playwright.async_api import async_playwright

async def login():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context(
            client_certificates=[
                {
                    "origin": "https://iam.gerid.dataprev.gov.br",
                    "certPath": "cert/cert.pem",
                    "keyPath": "cert/key.pem"
                }
            ]
        )

        page = await context.new_page()

        await page.goto("https://iam.gerid.dataprev.gov.br/cas/login")

        print("Página de login carregada")

        # clicar no botão de certificado
        await page.get_by_text("Entrar com Certificado Digital").click()

        # esperar o redirecionamento para o portal
        await page.wait_for_url("https://ecoportal.dataprev.gov.br/**")

        print("Login realizado")

        await page.wait_for_timeout(7000)

        print("url atual: ", page.url)

        await browser.close()

        

