import logging
import threading
import time

import requests
from googlesearch import search
from six.moves.urllib.parse import quote


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


def getPageContent(web_page_url):
    """given an url, gets the page content and returns a response

    Args:
        web_page_url ([type]): [valid string representing an url]

    Returns:
        [type]: [request response]
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    response = requests.get(url=web_page_url, headers=headers)
    return response


def savePageResponse(web_page_url, response, filename):
    """given an url a page response and a string saves to file the page content

    Args:
        web_page_url ([string]): [description]
        response ([requests response]): [request response ]
        filename ([string]): [string representing a filename]
    """
    page_content = response.text
    with open("./saved/{}.html".format(filename), "w", encoding="utf8") as fp:
        fp.write(page_content)

    logging.info("Save web page content " + web_page_url + " successfully.")


def getSavePage(url):
    """function that wraps getPageContent, parseDomainName and savePageResponse
    to implement multi threading


    Args:
        url ([str]): [valid string representing an url]
    """
    response = getPageContent(url)
    filename = parseDomainName(url)
    savePageResponse(url, response, filename)


def parseDomainName(url):
    """given an url return a strings that will be used to save the page as html file

    Args:
        url ([str]): [valid string representing an url]

    Returns:
        [str]: [string representing the filename]
    """
    filename = quote(url, "")

    return filename


if __name__ == "__main__":
    start = time.time()
    urls = searchWeb()

    print("Elapsed Time: %s" % (time.time() - start))
    print(urls)

    start = time.time()
    threads = [threading.Thread(target=getSavePage, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("Elapsed Time: %s" % (time.time() - start))
