from multiprocessing import Pool
from tqdm import tqdm


from .parse_data import parse_data
from .parse_urls import parse_urls
from .utils import divide_to_batches

def handler():
    list_urls = parse_urls()

    batches = divide_to_batches(list_urls, 2)

    
    with Pool(3) as pool:

        max_ = len(batches)
        with tqdm(total=max_) as pbar:
            for i, _ in enumerate(pool.imap_unordered(parse_data, batches)):
                pbar.update()

        
    
    print("\nall data is parsed!!!")