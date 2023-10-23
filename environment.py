from driver import Driver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.add_remove import Add_Remove

# keyword context - depinde de contextul in care rulam textele , fiind versiunea free , dupa context. nu apar sugestii
# before_all se executa inainte
def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.add_remove = Add_Remove()

#dupa ce ruleaza toate testele
def after_all(context):
    context.browser.close()
