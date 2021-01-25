from head_hunter_parser import HeadHunterParser
from save import Save
from stackoverflow_parser import StackoverflowParser

head_hunter_parser = HeadHunterParser('react')
stackoverflow_parser = StackoverflowParser('react')

job_list = head_hunter_parser.get_jobs() + stackoverflow_parser.get_jobs()

Save.save_to_csv(job_list)