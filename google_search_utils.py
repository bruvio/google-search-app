import logging

import googlesearch
import requests
from googlesearch import search
from requests.models import Response


def searchWeb(num=5, stop=5, query_string="how to data engineering"):
    """se google api to search the web for a given inpunt string and save resulting url to list

    Args:
        num (int, optional): [num of links to search]. Defaults to 5.
        stop (int, optional): [stop search after finding this much links]. Defaults to 5.
        query_string (str, optional): [string to search]. Defaults to "how to data engineering".

    Returns:
        [list]: [list of urls]
    """

    # to search
    query_resuts = []
    for result in search(query_string, tld="co.in", num=num, stop=stop, pause=2):
        logging.info(result)
        query_resuts.append(result)
    return query_resuts


# google_results("how to data engineering", 5)


def getPageContent(web_page_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    response = requests.get(url=web_page_url, headers=headers)
    return response


def savePageResponse(web_page_url, response, filename):
    page_content = response.text
    with open("./saved/{}.html".format(filename), "w", encoding="utf8") as fp:
        fp.write(page_content)

    logging.info("Save web page content " + web_page_url + " successfully.")


if __name__ == "__main__":
    print(searchWeb())
    rsp = getPageContent("http://www.trainigpeaks.com")
    savePageResponse("http://www.trainigpeaks.com", rsp, "provola")
