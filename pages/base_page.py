from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 10000
    
    def click(self, selector: str):
        self.page.click(selector)
        return self
    
    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)
        return self
    
    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)
    
    def is_visible(self, selector: str, timeout: int = None) -> bool:
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=timeout or self.timeout)
            return True
        except:
            return False
    
    def wait_for_url(self, url_part: str):
        self.page.wait_for_url(f"**/{url_part}")
        return self