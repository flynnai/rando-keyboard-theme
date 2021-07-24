from playwright.sync_api import sync_playwright
import random
import json


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://coolors.co/palettes/trending')
    page.set_viewport_size({ 'width': 1600, 'height': 1200 })
    print(f'Visiting page "{page.title()}" ...')

    print('Getting rid of some modals...')    
    page.click('#modal-fabrizio > div > div.modal_cell > div > a')
    page.click('#whats-new > div > div.modal_cell > div > a.modal_button-left.modal_close-btn.link.link--secondary > i')

    print('Waiting for the HTML to render...')
    page.wait_for_selector('.explore-palettes_col')
    all_color_tiles = page.query_selector_all('.explore-palettes_col')
    print(f'Found {len(all_color_tiles)} themes. Choosing one...')
    
    palette_handle = all_color_tiles[random.randint(0, len(all_color_tiles) - 1)]
    palette_handle.evaluate(
        """
        node => node.querySelector('.link.link--secondary.explore-palette_info_stat_more-btn').click()
        """
    )

    # print('Waiting for the ')
    # page.wait_for_selector('body > div.popover.popover--nav.is-top > div > nav > ul > li:nth-child(6) > a')
    print('Clicking through the export menu...')
    page.evaluate(
        """
        document.querySelector('body > div.popover.popover--nav.is-top > div > nav > ul > li:nth-child(6) > a').click()
        """
    )
    page.click('#palette-exporter_code-btn')

    print('Got it! Grabbing the HTML for the color array...')
    colors_str = page.query_selector('#text-viewer_text > span.hljs-selector-attr').inner_html()

    print('Boom. Parsing the color array...')
    colors = json.loads(colors_str)

    for color in colors:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)

        print(f'rgb({r},{g},{b})')

    import time
    time.sleep(8000)