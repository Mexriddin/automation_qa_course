class TextBoxPageLocators:
    # form fields
    FULL_NAME = ('id', 'userName')
    EMAIL = ('id', 'userEmail')
    CURRENT_ADDRESS = ('id', 'currentAddress')
    PERMANENT_ADDRESS = ('id', 'permanentAddress')
    SUBMIT_BUTTON = ('id', 'submit')

    # created from
    CREATED_FULL_NAME = ('id', 'name')
    CREATED_EMAIL = ('id', 'email')
    CREATED_CURRENT_ADDRESS = ('css selector', '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = ('css selector', '#output #permanentAddress')
