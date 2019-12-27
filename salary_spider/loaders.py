from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, SelectJmes

def get_job_title(self, jobs, loader_context=None):
    for job in jobs:
        job_title_id = job["jobTitle"]["id"].replace("JobTitle:", "")
        yield loader_context.get(int(job_title_id))

class GlassdoorJobLoader(ItemLoader):
    job_title_in = get_job_title
    median_base_salary_in = MapCompose(SelectJmes("medianBasePay"))
    min_base_salary_in = MapCompose(SelectJmes("minBasePay"))
    max_base_salary_in = MapCompose(SelectJmes("maxBasePay"))
    pay_period_in = MapCompose(SelectJmes("payPeriod"))
    sample_size_in = MapCompose(SelectJmes("count"))
    employer_name_in = MapCompose(SelectJmes("name"))
    employer_size_in = MapCompose(SelectJmes("size"))
    employer_sector_in = MapCompose(SelectJmes("sector"))
    employer_industry_in = MapCompose(SelectJmes("industry"))
    employer_location_in = MapCompose(SelectJmes("location"))
    employer_location_type_in = MapCompose(SelectJmes("locationType"))

    default_output_processor = TakeFirst()


