import scrapy
from scrapy.loader import ItemLoader
from scrapy_demo.items import Product

class QuotesSpider(scrapy.Spider):
    name = "ukr_pravda"
    allowed_domains = ["pravda.com.ua"]

    start_urls = [
        'http://blogs.pravda.com.ua',
    ]


    def parse_article(self, response):
        # Store data from page
        l = ItemLoader(Product(), response)
        l.add_css("author", '.bauthor a::text')
        l.add_css("title", ".bpost h1::text")
        l.add_css("description", '.description::text')
        l.add_css("text", '.bpost p::text')
        l.add_css("date_of_publish", '.fblock .bdate::text')
        l.add_css("img", '.bpost img::attr(src)')
        l.add_css("tag", '.list2 li a::text')
        l.add_value("url", response.url)
        yield l.load_item()


    def parse(self, response):
        for href in response.css("a.bpost0::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_article)

        for href in response.css(".next a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse)

        """
        Write in the file all data
        with open('blog_data.txt', 'a') as f:
            title_list = l.get_output_value('title')
            author_list = l.get_output_value('author')
            description_list = l.get_output_value('description')
            date_list = l.get_output_value('date_of_publish')
            text_list = l.get_output_value('text')
            tag_list = l.get_output_value("tag")
            img_list = l.get_output_value('img')

            str = ""
            for author in author_list:
                str += author.encode('utf-8')
            f.write('author: {0}, '.format(str))

            for date in date_list:
                f.write('date_of_publish: {0},'.format(date.encode('utf-8')))

            str1 = ""
            for title in title_list:
                str1 += title.encode('utf-8')
            f.write('title: {0},\n'.format(str1))

            str3 = ""
            for text in text_list:
                str3 += text.encode('utf-8')
            f.write('text: {0},\n'.format(str3))

            str5 = ""
            for img in img_list:
                str5 += img.encode('utf-8') + ","
            f.write('text: {0},\n'.format(str5))

            str4 = ""
            for tag in tag_list:
                str4 += tag.encode('utf-8') + ","
            f.write('tag: {0}, '.format(str4))

            str2 = ""
            for description in description_list:
                str2 += description.encode('utf-8')
            f.write('description: {0}\n'.format(str2))
            """






