from functions import *


if __name__ == '__main__':

    # variables
    weaviate_url = 'http://weaviate:11550' # change to local ip
    efConstruction_array = [64]
    maxConnections_array = [64]
    CPUs = 16
    ef_array = [64, 128, 256, 512]

    benchmark_file_array = [
        ['sift-128-euclidean.hdf5', 'l2-squared']
    ]   
 
    # Starts the actual benchmark, prints "completed" when done
    run_the_benchmarks(weaviate_url, CPUs, efConstruction_array, maxConnections_array, ef_array, benchmark_file_array)
