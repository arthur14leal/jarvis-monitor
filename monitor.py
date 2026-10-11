
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

BUSCAS = {
    "GTA 6": "GTA 6",
    "Games e atualizacoes": "videogames jogos atualizacoes",
    "Noticias gerais": "noticias Brasil",
}

def buscar_noticias(categoria, pesquisa):
    consulta = urllib.parse.quote(pesquisa)
    url = (
        "https://news.google.com/rss/search?q="
        + consulta
        + "&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    )

    pedido = urllib.request.Request(
        url,
        headers={"User-Agent": "JARVIS-NewsMonitor/1.0"}
    )

    with urllib.request.urlopen(pedido, timeout=20) as resposta:
        raiz = ET.fromstring(resposta.read())

    itens = raiz.findall("./channel/item")

    print("\n### " + categoria + " ###")

    if not itens:
        print("Nenhuma noticia encontrada.")
        return

    for item in itens[:5]:
        titulo = item.findtext("title", "Sem titulo")
        link = item.findtext("link", "")
        data = item.findtext("pubDate", "Data indisponivel")

        print("\n- " + titulo)
        print("  Data: " + data)
        print("  Link: " + link)

def main():
    print("=" * 45)
    print("JARVIS - MONITOR DE NOTICIAS")
    print("Consulta iniciada:", datetime.now().strftime("%d/%m/%Y %H:%M"))
    print("=" * 45)

    for categoria, pesquisa in BUSCAS.items():
        try:
            buscar_noticias(categoria, pesquisa)
        except Exception as erro:
            print("\nErro em", categoria + ":", str(erro))

    print("\nMonitor finalizado.")

if __name__ == "__main__":
    main()
