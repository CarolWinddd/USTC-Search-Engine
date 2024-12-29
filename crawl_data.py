import os
from dataclasses import asdict
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from utils import get_args
from crawl import AutoCrawler
from typing import Tuple

class CrawlerConfig:
    use_hbase: bool = False
    multi_threads: bool = True
    crawlers: Tuple[str] = ('teach', 'sse', 'sist', 'scs', 'press', 'mathematics', 'grad')
    save_dir: str = "./cache"

args = get_args(asdict(CrawlerConfig()))
crawlers = args.crawlers
print(crawlers)


if args.multi_threads:
    with ThreadPoolExecutor(len(crawlers)) as t:
        for name in crawlers:
            crawler = AutoCrawler.from_name(name)(args)
            t.submit(
                partial(
                    crawler.crawl_src, 
                    save_path=os.path.join(args.save_dir, name), 
                    host_url=crawler.main_url
                ),
            )
else:
    for name in crawlers:
        print(name)
        crawler = AutoCrawler.from_name(name)(args)
        crawler.crawl_src(save_path=os.path.join(args.save_dir, name), host_url=crawler.main_url)