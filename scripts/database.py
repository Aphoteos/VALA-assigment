import csv
import os.path
import self_made_timer


class database_csv:
    def __init__(self):
        # Set the path to database file
        dir_path = os.path.dirname(__file__)
        self.database_file = f'{dir_path}/prime_factor_database.csv'
        self.csv_fields = ['Number', 'Factors']

    def write_csv_headers(self):
        try:
            with open(self.database_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.csv_fields, delimiter='|')
                writer.writeheader()
       
        except Exception as e:
            print(f"Error occured: {e}")

    def save_result_csv(self, number, factors):
        data = [number, ', '.join(map(str,factors))]

        try:
            with open(self.database_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                writer.writerow(data)

        except Exception as e:
            print(f"Error occured: {e}")

    def save_to_database(self, number, factors):
        if os.path.exists(self.database_file):
            print(f'Database {self.database_file} exists. Continuing...')
        else:
            print(f'Database {self.database_file} doesn\'t exists. Creating it now...')
            self.write_csv_headers()
        
        self.save_result_csv(number, factors)

    @self_made_timer.timer_func
    def search_from_database(self, number: str):
        try:
            factors = []

            with open(self.database_file, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter='|')

                for row in reader:
                    if row[0] == str(number):
                        # Found number from database.
                        factors = row[1]
                        break

            return factors
        except Exception as e:
            print(f'Error: {e}')