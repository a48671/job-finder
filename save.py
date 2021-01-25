import csv


class Save:
    @staticmethod
    def save_to_csv(job_list):
        file = open('jobs.csv', mode='w')
        writer = csv.writer(file)
        writer.writerow(['title', 'link', 'location', 'company', 'salary', 'description'])
        for vacancy in job_list:
            writer.writerow([
                vacancy.title,
                vacancy.link,
                vacancy.location,
                vacancy.company,
                vacancy.salary,
                vacancy.description
            ])
        file.close()
