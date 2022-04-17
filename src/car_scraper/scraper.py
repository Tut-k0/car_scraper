import asyncio

# TODO: Move BeautifulSoup to the export python file.
from bs4 import BeautifulSoup
from pyppeteer import launch

from options import args

URL = 'https://www.autotempest.com/results?'


def main() -> None:
    arguments = args()

    parameter = generate_parameter(arguments)

    asyncio.run(scrape(URL, parameter=parameter))


def generate_parameter(parameters: dict) -> str:
    # TODO: Validate make and model actually exists.
    param_list = []
    for arg, value in parameters.items():
        if value is not None:
            if isinstance(value, str):
                param_list.append(f'{arg}={value.lower()}&')
            else:
                param_list.append(f'{arg}={value}&')

    return "".join(param_list)


async def scrape(url: str, parameter: str) -> None:
    browser = await launch(autoClose=False)
    page = await browser.newPage()
    await page.goto(url + parameter)
    page_content = await page.content()

    # TODO: Get the useful information out of the page.
    soup = BeautifulSoup(page_content, features="html.parser")
    print(soup.find(id='cm-results').get_text)

    await browser.close()


if __name__ == '__main__':
    main()
