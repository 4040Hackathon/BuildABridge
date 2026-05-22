from shapely.geometry import LineString, MultiLineString
from shapely.ops import linemerge
import geopandas as gpd
import networkx as nx


def get_edge_geometry(G, u, v, weight="travel_time"):
    """
    Holt die Geometrie der Edge u -> v.
    Funktioniert für DiGraph und MultiDiGraph.
    Falls keine Geometry vorhanden ist, wird eine direkte Linie zwischen den Nodes gebaut.
    """

    # MultiDiGraph: mehrere Kanten zwischen u und v möglich
    if G.is_multigraph():
        edge_data = G.get_edge_data(u, v)

        if edge_data is None:
            return None

        # Edge mit kleinstem weight wählen
        key, data = min(
            edge_data.items(),
            key=lambda item: item[1].get(weight, float("inf"))
        )

    # DiGraph: nur eine Kante zwischen u und v
    else:
        data = G.get_edge_data(u, v)

        if data is None:
            return None

    # Falls Edge bereits eine Geometrie hat
    if "geometry" in data and data["geometry"] is not None:
        return data["geometry"]

    # Fallback: Linie zwischen Node-Koordinaten
    x1, y1 = G.nodes[u]["x"], G.nodes[u]["y"]
    x2, y2 = G.nodes[v]["x"], G.nodes[v]["y"]

    return LineString([(x1, y1), (x2, y2)])


def route_nodes_to_geometry(G, route_nodes, weight="travel_time"):
    """
    Wandelt eine Node-Route in eine Liniengeometrie um.
    """

    if route_nodes is None or len(route_nodes) < 2:
        return None

    edge_geoms = []

    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        geom = get_edge_geometry(G, u, v, weight=weight)

        if geom is not None:
            edge_geoms.append(geom)

    if not edge_geoms:
        return None

    # Geometrien zusammenführen, wenn möglich
    merged = linemerge(edge_geoms)

    return merged