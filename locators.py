from selenium.webdriver.common.by import By

class HOME:
    REQUEST = (By.CSS_SELECTOR, 'span[data-key="url"]')
    RESPONSE_STATUS = (By.CSS_SELECTOR, 'span[data-key="response-code"]')
    RESPONSE_BODY = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')
    REQUEST_DATA = (By.CSS_SELECTOR, 'span.string')
    HEROKU = (By.CSS_SELECTOR, 'a[href="https://www.heroku.com/"]')
    SWAGGER = (By.CSS_SELECTOR, 'a[href="/api-docs"]')
    SUPPORT_REQUEST = (By.CSS_SELECTOR, 'a[href="#support-heading"]')
    FIELD_PAYMENT = (By.CSS_SELECTOR, 'input[name="oneTimeAmount"]')
    BUTTON_SUPPORT = (By.CSS_SELECTOR, 'form#supportForm button')
    SUMM_SUPPORT = (By.CSS_SELECTOR, 'span#ProductSummary-totalAmount')
    MONTH_SUPPORT_PAY = (By.CSS_SELECTOR, 'input#supportRecurring')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input#mce-EMAIL')

class SUBSCRIBE:
    BUTTON_UPGRATE = (By.CSS_SELECTOR, 'button#trigger-pro')
    BUTTON_SUBSCRIBE_HOME_PAGE = (By.CSS_SELECTOR, 'input#mc-embedded-subscribe')
    SUBSCRIPTION_CONFIRMATION_TEXT = (By.CSS_SELECTOR, 'div#templateBody')

class REQUESTFIELDS:
    USERS = (By.CSS_SELECTOR, 'li[data-id="users"]')
    USERS_SINGLE = (By.CSS_SELECTOR, 'li[data-id="users-single"]')
    USERS_SINGLE_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="users-single-not-found"]')
    UNKNOWN = (By.CSS_SELECTOR, 'li[data-id="unknown"]')
    UNKNOWN_SINGLE = (By.CSS_SELECTOR, 'li[data-id="unknown-single"]')
    UNKNOWN_SINGLE_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="unknown-single-not-found"]')
    POST = (By.CSS_SELECTOR, 'li[data-id="post"]')
    PUT = (By.CSS_SELECTOR, 'li[data-id="put"]')
    PATCH = (By.CSS_SELECTOR, 'li[data-id="patch"]')
    DELETE = (By.CSS_SELECTOR, 'li[data-id="delete"]')
    REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-successful"]')
    REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-unsuccessful"]')
    LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-successful"]')
    LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-unsuccessful"]')
    DELAY = (By.CSS_SELECTOR, 'li[data-id="delay"]')

