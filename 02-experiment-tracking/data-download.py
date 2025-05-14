# Scrip that imports NYC data for Yellow Taxi data fro Jan - Feb from 2023 only
import os
from time import time

def main():
 
    url_1 = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet'
    url_2 = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-02.parquet'
    url_list = [url_1, url_2]
    destination_folder = './data/'

    print('DOWNLOAD Script started, {}')
    for url in url_list:
        print(f'DOWNLADING Data,  {url}')
        parquet_name = f"{destination_folder}/{url.split('/')[-1]}"
        t_start = time()
        os.system(f"wget {url} -O {parquet_name}")

        #df = pd.read_parquet(csv_name)
        t_end = time()
        print('Elapsed time, took %.3f seconds' % (t_end-t_start))
        print(f'Output URL: {parquet_name}')


if __name__ == "__main__":
    main()
