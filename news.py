class News:

    def __init__(self, url, title, content):
        self.url = url
        self.title = title
        self.content = content

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content
