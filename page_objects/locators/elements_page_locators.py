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


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = ('xpath', "//button[@title='Expand all']")
    ITEM_LIST = ('css selector', "span.rct-title")

    CHECKED_ITEMS = ('css selector', "svg.rct-icon-check")
    TITLE_ITEM = ('xpath', ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = ('css selector', "span.text-success")


class RadioButtonsPageLocators:
    YES_RADIO_BUTTON = ('xpath', "//label[contains(@class, 'custom-control-label') and @for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = ('xpath', "//label[contains(@class, 'custom-control-label') and @for='impressiveRadio']")
    NO_RADIO_BUTTON = ('xpath', "//label[contains(@class, 'custom-control-label') and @for='noRadio']")
    OUTPUT_RESULT = ('css selector', "span.text-success")


class WebTablesPageLocators:
    # add person
    ADD_BUTTON = ('id', 'addNewRecordButton')
    FIRST_NAME = ('id', 'firstName')
    LAST_NAME = ('id', 'lastName')
    EMAIL = ('id', 'userEmail')
    AGE = ('id', 'age')
    SALARY = ('id', 'salary')
    DEPARTMENT = ('id', 'department')
    SUBMIT_BUTTON = ('id', 'submit')

    # table
    FULL_PEOPLE_LIST = ("css selector", ".rt-tr-group")
    INPUT_SEARCH = ("css selector", "#searchBox")
    EDIT_SPAN = ("css selector", "span[title='Edit']")
    DELETE_SPAN = ("css selector", "span[title='Delete']")
    NO_ROWS_FOUND = ("css selector", "div.rt-noData")
    SELECT_ROWS_PER_PAGE = ("css selector", "select[aria-label='rows per page']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = ("css selector", "button#doubleClickBtn")
    RIGHT_CLICK_BUTTON = ("css selector", "button#rightClickBtn")
    SIMPLE_CLICK_BUTTON = ("xpath", "//button[text()='Click Me']")

    # result
    DOUBLE_CLICK_MESSAGE = ("css selector", "p#doubleClickMessage")
    RIGHT_CLICK_MESSAGE = ("css selector", "p#rightClickMessage")
    SIMPLE_CLICK_MESSAGE = ("css selector", "p#dynamicClickMessage")
