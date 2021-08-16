from google_search_utils import getPageContent, savePageResponse, searchWeb


def test_search():
    results = searchWeb()
    assert len(results) == 5


def test_getPageContent():
    response = getPageContent("http://www.trainigpeaks.com")
    assert response.status_code == 200


def test_savePage():
    # from pathlib import Path
    import os

    filename = "test_file"
    response = getPageContent("http://www.trainigpeaks.com")
    savePageResponse("http://www.trainigpeaks.com", response, filename)
    assert os.path.isfile("./saved/{}.html".format(filename))
    os.remove("./saved/{}.html".format(filename))
