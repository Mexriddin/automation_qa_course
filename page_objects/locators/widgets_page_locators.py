class AccordianPageLocators:
    SECTION_FIRST = ('id', "section1Heading")
    SECTION_CONTENT_FIRST = ('xpath', '//*[@id="section1Content"]/p[1]')
    SECTION_FIRST_CHECKER = ('xpath', '//*[@id="section1Heading"]/following-sibling::*[@class="collapse show"]')
    SECTION_SECOND = ('id', "section2Heading")
    SECTION_CONTENT_SECOND = ('xpath', '//*[@id="section2Content"]/p[1]')
    SECTION_SECOND_CHECKER = ('xpath', '//*[@id="section2Heading"]/following-sibling::*[@class="collapse show"]')
    SECTION_THIRD = ('id', "section3Heading")
    SECTION_CONTENT_THIRD = ('xpath', '//*[@id="section3Content"]/p[1]')
    SECTION_THIRD_CHECKER = ('xpath', '//*[@id="section3Heading"]/following-sibling::*[@class="collapse show"]')


class AutoCompletePageLocators:
    MULTI_INPUT = ('css selector', 'input[id=autoCompleteMultipleInput]')
    MULTI_VALUE = ('css selector', '.auto-complete__multi-value__label')
    DELETE_BTN_MULTI_VALUE = ('css selector', '.auto-complete__multi-value__remove')