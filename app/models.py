class Source:
    """
    Source class to define Source Objects
    """
    def __init__(self,id,name,description):
        self.id = id
        self.name =name
        self.description =description



class Article:
    """
    Source class to define Article Objects
    """
    def __init__(self,source,author,title,description,publishedAt,url,urlToImage):

        self.source =source
        self.author = author
        self.title=title
        self.description =description
        self.publishedAt=publishedAt
        self.url =url
        self.urlToImage=urlToImage
