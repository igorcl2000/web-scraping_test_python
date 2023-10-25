# Web Scraping Kabum

Este é um projeto de web scraping em Python que coleta informações sobre produtos em uma loja online, Kabum. O script extrai dados sobre produtos, como marca e preço, e armazena essas informações em um arquivo CSV para análise posterior.

## Como Funciona

O script utiliza as bibliotecas Requests e BeautifulSoup para fazer solicitações HTTP à página da Kabum, analisar o HTML e extrair os dados dos produtos. Ele percorre várias páginas de produtos, dependendo da quantidade total de itens disponíveis, para garantir que todos os produtos sejam coletados.

## Requisitos

- Python 3.x
- Bibliotecas: requests, BeautifulSoup, pandas.
