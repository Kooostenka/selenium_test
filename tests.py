from YandexPages import SearchHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    assert yandex_main_page.enter_word("Тензор")
    assert yandex_main_page.check_suggest()
    yandex_main_page.click_on_the_search_button()
    links = yandex_main_page.check_five_links()
    assert "tensor.ru" in links


def test_yandex_images(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинки" in elements

    yandex_main_page.go_to_images()
    window = yandex_main_page.remember_second_window()
    yandex_main_page.switch(window)
    current_url = yandex_main_page.get_url()
    assert 'https://yandex.ru/images/' in current_url

    name_category = yandex_main_page.get_name_first_category()
    yandex_main_page.click_on_first_category()
    search_text = yandex_main_page.get_search_text()
    category_url = yandex_main_page.get_url()
    assert name_category == search_text

    yandex_main_page.click_on_first_image()
    img1_url = yandex_main_page.get_url()
    assert category_url != img1_url

    yandex_main_page.go_forward()
    img2_url = yandex_main_page.get_url()
    assert img2_url != img1_url

    yandex_main_page.go_back()
    img3_url = yandex_main_page.get_url()
    assert img1_url == img3_url

