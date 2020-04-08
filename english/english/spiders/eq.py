# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request 
import re
import os
import csv
import glob
from scrapy import Spider
import mysql.connector as mysql

class EqSpider(scrapy.Spider):
    name = 'eq'
    allowed_domains = ['https://www.examveda.com/competitive-english/practice-mcq-question-on-spotting-errors/']
    start_urls = ['https://www.examveda.com/competitive-english/practice-mcq-question-on-spotting-errors/']

    def parse(self, response):
        links =  response.xpath("//ul[@class='more-section']//a/@href").extract()
        links.append('https://www.examveda.com/competitive-english/practice-mcq-question-on-spotting-errors/')
        for i in links:
            yield Request(i, callback=self.extract_question,dont_filter=True)
            
    
    def extract_question(self,response):
        question = response.xpath("//div[@class='row']//h2//text()").extract()
        opt = response.xpath("//div[@class='form-inputs clearfix question-options']//p//label//text()").extract()
        Ans  = response.xpath("//div//strong//text()").extract()

        # Clean Question
        q = [ question[i+1] for i in range(len(question)) if re.findall("\d+\.", question[i]) ]
        clean_q = [re.sub('[^A-Za-z0-9]+', ' ', i) for i in q ]
        clean_q = [i for i in clean_q if i!=" "]

        # Clean Options 
        clean_opt = [opt[i] for i in range(1,len(opt),2)]

        # Clean Answer

        ans = [ i.split()[1] for i in Ans if re.search(r'Option',i)]
        k = 0
        if len(clean_opt)==20:
            for i in range(0,len(clean_q)):
                que = clean_q[i]
                answer = ans[i]
                a = clean_opt[k]
                b = clean_opt[k+1]
                c = clean_opt[k+2]
                d = clean_opt[k+3]
                
                k+=4
                yield{
                
                    'Question':que,
                    'A':a,
                    'B':b,
                    'C':c,
                    'D':d,
                    
                    'Answer':answer,
                
                }
        next_page =  response.xpath("//div[@class='pagination']//a/@href").extract()
        for link in next_page:
             yield Request(link, callback=self.extract_questions,dont_filter=True)
             
    def extract_questions(self,response):
        question = response.xpath("//div[@class='row']//h2//text()").extract()
        opt = response.xpath("//div[@class='form-inputs clearfix question-options']//p//label//text()").extract()
        Ans  = response.xpath("//div//strong//text()").extract()

        # Clean Question
        q = [ question[i+1] for i in range(len(question)) if re.findall("\d+\.", question[i]) ]
        clean_q = [re.sub('[^A-Za-z0-9]+', ' ', i) for i in q ]
        clean_q = [i for i in clean_q if i!=" "]
        # Clean Options 
        clean_opt = [opt[i] for i in range(1,len(opt),2)]

        # Clean Answer

        ans = [ i.split()[1] for i in Ans if re.search(r'Option',i)]
        k = 0
        if len(clean_opt)==20:
            for i in range(0,len(clean_q)):
                que = clean_q[i]
                answer = ans[i]
                a = clean_opt[k]
                b = clean_opt[k+1]
                c = clean_opt[k+2]
                d = clean_opt[k+3]
                k+=4
                yield{
                
                    'Question':que,
                    'A':a,
                    'B':b,
                    'C':c,
                    'D':d,
                   
                    'Answer':answer,
                
                }
        
       
        
       

            
            



