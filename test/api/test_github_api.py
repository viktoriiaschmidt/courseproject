import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_doesnot_exist(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    # print(r)
    assert r["total_count"] == 42


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emoji_exists(github_api):
    r = github_api.get_emoji()
    assert (
        r["ukraine"]
        == "https://github.githubassets.com/images/icons/emoji/unicode/1f1fa-1f1e6.png?v8"
    )


@pytest.mark.api
def test_commit_exists(github_api):
    r = github_api.get_commit("sergii-butenko-gl", "become-qa-auto-aug2020")
    assert r[0]["commit"]["message"] == "added docker file"


@pytest.mark.api
def test_page_doesnot_exist(github_api):
    r = github_api.get_page("sergii-butenko-gl", "become-qa-auto-aug2020")
    assert r["message"] == "Not Found"
