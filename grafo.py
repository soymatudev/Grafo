import argparse
import networkx as nx
import matplotlib.pyplot as plt

def getNodesFile(path):
    edges = []
    with open(path, 'r', encoding='utf-8') as fileEd:
        for line in fileEd:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            partes = line.split()
            # origen, destino, etiqueta1, etiqueta2
            if len(partes) >= 4:
                edges.append((partes[0], partes[1], partes[2], partes[3])) 
            elif len(partes) >= 3:
                edges.append((partes[0], partes[1], partes[2], ""))
    return edges


def genGrafo(edges):
    grafo = nx.DiGraph()
    for origen, destino, etiqueta1, etiqueta2 in edges:
        # Si es doble etiqueta la concatenamos
        etiquetaDoble = f"{etiqueta1}/{etiqueta2}" 
        grafo.add_edge(origen, destino, label=etiquetaDoble, label1=etiqueta1, label2=etiqueta2)
    return grafo


def setPdf(Graph, namePdf, inicial=None, finales=None):
    pos = nx.spring_layout(Graph, seed=42)
    plt.figure(figsize=(11, 8.5))

    colorNodes = []
    for n in Graph.nodes():
        if n == inicial:
            colorNodes.append("green")
        elif finales and n in finales:
            colorNodes.append("red")
        else:
            colorNodes.append("lightblue")

    nx.draw(
        Graph, pos,
        with_labels=True,
        node_size=800,
        font_size=10,
        node_color=colorNodes,
        edge_color='gray',
        arrowsize=20
    )

    labels = nx.get_edge_attributes(Graph, "label")
    nx.draw_networkx_edge_labels(
        Graph, pos,
        edge_labels=labels,
        font_color="blue",
        label_pos=0.3
    )

    plt.axis("off")
    plt.tight_layout()
    plt.savefig(namePdf, format="pdf", bbox_inches="tight")
    plt.close()
    print(f"PDF generado: {namePdf}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--edges", help="Archivo con aristas", default="mis_aristas.txt")
    parser.add_argument("--max-edges", type=int, help="Cantidad de aristas por grafo", default=None)
    
    #  Ahora puede recibir múltiples nodos finales distintos
    parser.add_argument("--inicial", help="Estado inicial", default="A")
    parser.add_argument("--finales", nargs="+", help="Estados finales", default=["F"])

    args = parser.parse_args()

    nodes = getNodesFile(args.edges)

    edges = nodes[:args.max_edges] if args.max_edges else nodes
    Graph = genGrafo(edges)
    namePdf = f"./pdfs/automata.pdf"
    setPdf(Graph, namePdf, inicial=args.inicial, finales=args.finales)

    # Impresion de la información del autómata
    statesQ = sorted(list(Graph.nodes()))
    labels = nx.get_edge_attributes(Graph, "label")
    sigma = sorted(set(labels.values()))

    print("\n===== INFORMACIÓN DEL AUTÓMATA =====")
    print("Estados (Q):", statesQ)
    print("Alfabeto (Σ):", sigma)
    print("Estado inicial (q0):", args.inicial)
    print("Estados finales (F):", args.finales)
    print("====================================")


if __name__ == "__main__":
    main()