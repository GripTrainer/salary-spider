import re
import json
import scrapy

from salary_spider.items import GlassdoorJob
from salary_spider.loaders import GlassdoorJobLoader
from decimal import Decimal


class GlassdoorSpider(scrapy.Spider):

    name = "glassdoor"
    start_urls = [
        "https://www.glassdoor.com/Salaries/new-zealand-salary-SRCH_IL.0,11_IN186.htm"
    ]

    def parse(self, response):
        """
        Parses the search results page and 
        returns requests to employer pages and more search requests

        @url https://www.glassdoor.com/Salaries/new-zealand-salary-SRCH_IL.0,11_IN186.htm
        @returns requests 10
        """
        for company in response.css(".tightVert.padBotSm a"):
            yield response.follow(company, callback=self.parse_employer)

        for search in response.css(".pagingControls a"):
            yield response.follow(search)

    def parse_employer(self, response):
        """
        Parses a employer page extracting information about the company
        and jobs in the company

        @url https://www.glassdoor.com/Salary/Datacom-Systems-New-Zealand-Salaries-EI_IE539827.0,15_IL.16,27_IN186.htm
        @returns items 20
        @returns requests 3
        """
        for page in response.css(".pagination__PaginationStyle__page a"):
            yield response.follow(page, callback=self.parse_employer)


        employer = re.search(r"'employer' : ({[^}]+})", response.text)[1]
        employer = employer.replace("'", '"')
        employer = json.loads(employer)

        job_titles = re.findall('{"id":\d+,"text":"[^"]+","__typename":"JobTitle"}', response.text)
        job_titles = [json.loads(job) for job in job_titles]
        job_title_dict = {job["id"]: job["text"] for job in job_titles}

        job_salaries = re.findall('{"currency".*?"__typename":"EmployerSalary"}', response.text)
        job_salaries = [json.loads(job, parse_float=Decimal) for job in job_salaries]

        for job in job_salaries:
            il = GlassdoorJobLoader(item=GlassdoorJob())
            il.context = job_title_dict
            il.add_value("job_title", job)
            il.add_value("median_base_salary", job)
            il.add_value("min_base_salary", job)
            il.add_value("max_base_salary", job)
            il.add_value("sample_size", job)
            il.add_value("employer_name", employer)
            il.add_value("employer_size", employer)
            il.add_value("employer_sector", employer)
            il.add_value("employer_industry", employer)
            il.add_value("employer_location", employer)
            il.add_value("employer_location_type", employer)
            yield il.load_item()
