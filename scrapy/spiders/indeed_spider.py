# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from Indeed.items import IndeedItem
import pandas as pd
import re


class IndeedSpider(Spider):
    name = 'Indeed_spider'
    allowed_urls = ['https://www.indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=Python&l=New+York,+NY&radius=100']
    response = requests.get(url)
    text = BeautifulSoup(response.txt, 'html.parser')

    def parse(self, response):
        # Find all the table rows
        rows = response.xpath('//*[@id="resultsCol"]/nav/div')[1:]



        for row in rows:
            title = row.xpath('//*[@id="jl_1cef3c761b0d68a0"]').extract_first()
            company = row.xpath('./td[1]//text()').extract_first()
            location = row.xpath('//*[@id="p_1cef3c761b0d68a0"]/div[1]/span').extract_first()
            salary = row.xpath('//*[@id="p_efc03b7145839e9f"]/div[2]/span/span').extract_first()
            rating = row.xpath('//*[@id="p_1cef3c761b0d68a0"]/div[1]/div[1]/span[2]/a/span').extract_first()
            urgent_hiring = row.xpath('//*[@id="pj_a57edd8146e99caa"]/table/tbody/tr/td[3]').extract_first()
            link = row.xpath('//*[@id="p_1cef3c761b0d68a0"]').extract_first()

            
            # Initialize a new WikiItem instance for each movie.
            item = IndeedItem()
            item['title'] = title
            item['company'] = company
            item['location'] = location
            item['salary'] = salary
            item['rating'] = rating
            item['urgent hiring'] = urgent_hiring
            item['link'] = link
            yield item
