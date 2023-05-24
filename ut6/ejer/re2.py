# Escriba un programa en Python que encuentre todas las URLs en un texto dado.

import re


def find_url(url: str) -> list[str]:
    regex = r"\b[https$]\S*[^,\s\w]*"
    result = re.findall(regex, url)
    return result


print(
    find_url(
        """Esta es mi url: https://aprendepython.es/stdlib/text_processing/re/ Esta es mi otra url: https://www.google.com/search?client=firefox-b-e&q=que+caracteres+no+est%C3%A1n+permitidos+en+una+url"""
    )
)
