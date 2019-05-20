import scrapy




class MongolWordSpider(scrapy.Spider):
    name = 'words'

    letters = 'АБВГДЕЁЖЗИКЛМНОӨПРСТУҮФХЦЧШЭЮЯ'
    prefix = 'https://mongoltoli.mn/dictionary/lists/'
    start_urls=[]
    for letter in letters:
        start_urls.append(prefix + letter + '/')
    

    def parse(self, response):
        for word_list in response.css('div.list_bk'):
            for word in word_list.css('div.list_ug'):
                yield {
                    'word':word.css('a.list_color::text').get()
                }
                

        next_page = response.css('li.next a::attr("href")').get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)

    
    