import argparse
from coursera_scraper import CourseraScraper


def start():
    """
    get the params from Cmd, and create the cvs file
    """
    parser = argparse.ArgumentParser(
        description="Coursera Scraper parameters Options.", prog="SCRIPT"
    )
    parser.add_argument(
        "--search",
        type=str,
        nargs=1,
        metavar="<Course Name>",
        help="Course search query",
        required=False,
        default=None,
    )
    args = parser.parse_args()
    scraper = CourseraScraper("coursera_courses.csv")
    scraper.scrape_courses(search_keyword=args.search[0])


if __name__ == "__main__":
    start()


