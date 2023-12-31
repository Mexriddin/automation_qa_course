class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = ('css selector', 'button#tabButton')
    NEW_WINDOW_BUTTON = ('css selector', 'button#windowButton')
    HEADING_IN_PAGE = ('css selector', 'h1#sampleHeading')


class AlertsPageLocators:
    ALERT_BUTTON = ('css selector', 'button#alertButton')
    TIMER_ALERT_BUTTON = ('css selector', 'button#timerAlertButton')
    CONFIRM_ALERT_BUTTON = ('css selector', 'button#confirmButton')
    PROMPT_ALERT_BUTTON = ('css selector', 'button#promtButton')

    CONFIRM_RESULT = ('css selector', 'span#confirmResult')
    PROMPT_RESULT = ('css selector', 'span#promptResult')