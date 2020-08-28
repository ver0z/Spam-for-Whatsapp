from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "!!!Bon jour"
        self.grupos = ["Zz", "Team Cry lol"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagem(self):
        # <span dir="auto" title="Photonics" class="_3ko75 _5h6Y_ _3Whw5">Photonics</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        print("asdasdasda")
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for i in range(0, 20):

            for grupo in self.grupos:
                grupo = self.driver.find_element_by_xpath(f'//span[@title="{grupo}"]')
                time.sleep(2)
                grupo.click()
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                time.sleep(2)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
                time.sleep(2)
                botao_enviar.click()
                time.sleep(3)
            time.sleep(10)

bot_zap = WhatsappBot()
bot_zap.EnviarMensagem()