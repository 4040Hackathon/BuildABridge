"""
Hilfsfunktionen zum interaktiven Bearbeiten eines unprojizierten OSMnx-Graphen
in Jupyter.

Workflow im Notebook:
    from src.utils_edit_graph import init_map, handle_click, get_edited_graph

    m = init_map(bbox, G)
    m.on_interaction(handle_click)
    m

Danach:
    G = get_edited_graph()

Hinweis:
Der Graph bleibt durchgehend unprojiziert (typisch EPSG:4326). Für die Länge
neu gezeichneter Kanten wird eine geodätische Distanz berechnet; es wird kein
zweiter/projizierter Graph angelegt.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

import geopandas as gpd
import osmnx as ox
from shapely.geometry import LineString
from pyproj import Geod
from ipyleaflet import GeoJSON, Map, Marker, Polyline, basemaps


# Modulzustand für den Jupyter-Click-Handler
m: Optional[Map] = None
G = None
_edge_layer: Optional[GeoJSON] = None
_node_layer: Optional[GeoJSON] = None
_edit_mode = "add"

_clicked_points: list[tuple[float, float]] = []
_clicked_markers: list[Marker] = []
_clicked_lines: list[Polyline] = []
_deleted_lines: list[Polyline] = []
_created_edges: list[tuple[Any, Any, Any]] = []
_geod = Geod(ellps="WGS84")


def _edge_key(graph, u, v, key=None):
    """Ermittelt den zuletzt angelegten Edge-Key, falls NetworkX None zurückgibt."""
    if key is not None:
        return key
    if graph.has_edge(u, v):
        edge_data = graph.get_edge_data(u, v)
        if isinstance(edge_data, dict) and edge_data:
            return list(edge_data.keys())[-1]
    return None


def _remove_edge(graph, u, v, key=None) -> None:
    """Entfernt eine Edge robust aus DiGraph oder MultiDiGraph."""
    if graph is None or not graph.has_edge(u, v):
        return

    try:
        if key is None:
            graph.remove_edge(u, v)
        else:
            graph.remove_edge(u, v, key=key)
    except TypeError:
        graph.remove_edge(u, v)
    except Exception:
        # Falls der gespeicherte Key nicht mehr existiert, nichts erzwingen.
        pass


def _geometry_to_geojson(geometry, crs: str = "EPSG:4326") -> dict:
    """Verpackt eine Shapely-Geometrie als GeoJSON-FeatureCollection."""
    gdf = gpd.GeoDataFrame(geometry=[geometry], crs=crs)
    return json.loads(gdf.to_json())


def _graph_to_layers(graph):
    """Konvertiert Graph-Nodes und -Edges nach GeoJSON-Layern für ipyleaflet."""
    nodes, edges = ox.graph_to_gdfs(graph)

    hover_style = {
        "color": "yellow",
        "fillColor": "yellow",
        "fillOpacity": 1.0,
    }

    edge_layer = GeoJSON(
        data=json.loads(edges.to_json()),
        style={"color": "gray", "weight": 1},
        name="Strassen / Edges",
    )

    node_layer = GeoJSON(
        data=json.loads(nodes.to_json()),
        point_style={
            "radius": 3,
            "color": "blue",
            "fillColor": "blue",
            "fillOpacity": 0.8,
            "weight": 1,
        },
        hover_style=hover_style,
        name="Knoten / Nodes",
    )

    return node_layer, edge_layer


def _refresh_graph_layers() -> None:
    """Aktualisiert die sichtbaren Node-/Edge-Layer nach Graph-Änderungen."""
    if G is None:
        return

    nodes, edges = ox.graph_to_gdfs(G)

    if _edge_layer is not None:
        _edge_layer.data = json.loads(edges.to_json())

    if _node_layer is not None:
        _node_layer.data = json.loads(nodes.to_json())


def _edge_length_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """Berechnet die geodätische Länge in Metern zwischen zwei Lon/Lat-Punkten."""
    _, _, distance = _geod.inv(lon1, lat1, lon2, lat2)
    return float(distance)


def reset_edit_state(remove_edges: bool = True) -> None:
    """
    Setzt Marker, Linien und optional die erzeugten Custom-Edges zurück.
    """
    global _clicked_points, _clicked_markers, _clicked_lines, _created_edges

    if m is not None:
        for marker in list(_clicked_markers):
            try:
                m.remove_layer(marker)
            except Exception:
                pass

        for line in list(_clicked_lines):
            try:
                m.remove_layer(line)
            except Exception:
                pass

        for line in list(_deleted_lines):
            try:
                m.remove_layer(line)
            except Exception:
                pass

    if remove_edges:
        for graph, u, v, key in reversed(_created_edges):
            _remove_edge(graph, u, v, key)

    _clicked_points.clear()
    _clicked_markers.clear()
    _clicked_lines.clear()
    _deleted_lines.clear()
    _created_edges.clear()
    _refresh_graph_layers()


def init_map(
    bbox_or_polygon,
    graph,
    *,
    zoom: int = 13,
    show_bbox: bool = True,
    copy_graph: bool = False,
):
    """
    Initialisiert die Leaflet-Karte und speichert den unprojizierten Graphen
    für den Click-Handler.

    Parameter
    ---------
    bbox_or_polygon:
        Shapely-Geometrie oder GeoDataFrame in EPSG:4326. Dient zur Zentrierung
        und optional als Rahmenanzeige.
    graph:
        OSMnx/NetworkX-Graph in EPSG:4326 bzw. mit Lon/Lat-Node-Koordinaten.
    zoom:
        Start-Zoom der Karte.
    show_bbox:
        Zeichnet die übergebene Geometrie als orange Outline.
    copy_graph:
        Wenn True, wird eine Kopie des Graphen bearbeitet. Standardmässig wird
        der übergebene Graph direkt bearbeitet, damit `G` im Notebook aktualisiert ist.
    """
    global m, G, _edge_layer, _node_layer

    reset_edit_state(remove_edges=False)

    G = graph.copy() if copy_graph else graph
    nodes, _ = ox.graph_to_gdfs(G)

    # Zentrum bevorzugt aus bbox/polygon bestimmen, sonst aus Nodes.
    try:
        if isinstance(bbox_or_polygon, gpd.GeoDataFrame):
            center_geom = bbox_or_polygon.to_crs(epsg=4326).union_all().centroid
        else:
            center_geom = gpd.GeoSeries([bbox_or_polygon], crs="EPSG:4326").centroid.iloc[0]
        center_lat, center_lon = center_geom.y, center_geom.x
    except Exception:
        center_lat = nodes.geometry.y.mean()
        center_lon = nodes.geometry.x.mean()

    m = Map(
        center=(center_lat, center_lon),
        zoom=zoom,
        basemap=basemaps.OpenStreetMap.Mapnik,
    )

    _node_layer, _edge_layer = _graph_to_layers(G)
    m.add_layer(_edge_layer)
    m.add_layer(_node_layer)

    if show_bbox and bbox_or_polygon is not None:
        try:
            if isinstance(bbox_or_polygon, gpd.GeoDataFrame):
                geom = bbox_or_polygon.to_crs(epsg=4326).union_all()
            else:
                geom = bbox_or_polygon
            bbox_layer = GeoJSON(
                data=_geometry_to_geojson(geom, crs="EPSG:4326"),
                style={"color": "orange", "weight": 2, "fillOpacity": 0.0},
                name="Gebiet",
            )
            m.add_layer(bbox_layer)
        except Exception:
            pass

    return m


def set_edit_mode(mode: str) -> None:
    """
    Setzt den Kartenmodus: "add" für Edge hinzufügen, "delete" für Edge löschen.
    """
    global _edit_mode

    if mode not in {"add", "delete"}:
        raise ValueError('mode muss "add" oder "delete" sein.')

    _edit_mode = mode
    _clicked_points.clear()


def create_bridge(click1: tuple[float, float], click2: tuple[float, float]) -> dict:
    """
    Erstellt zwischen zwei Kartenklicks eine bidirektionale Custom-Edge.

    click1/click2 sind Leaflet-Koordinaten als (lat, lon).
    Der gespeicherte Graph bleibt unprojiziert; die Kanten-Geometrie ist eine
    LineString-Geometrie mit (lon, lat)-Koordinaten.
    """
    if m is None or G is None:
        raise RuntimeError("Bitte zuerst init_map(..., G) ausführen.")

    # OSMnx erwartet bei unprojizierten Graphen X=lon und Y=lat.
    node1 = ox.distance.nearest_nodes(G, X=click1[1], Y=click1[0])
    node2 = ox.distance.nearest_nodes(G, X=click2[1], Y=click2[0])

    lon1 = float(G.nodes[node1]["x"])
    lat1 = float(G.nodes[node1]["y"])
    lon2 = float(G.nodes[node2]["x"])
    lat2 = float(G.nodes[node2]["y"])

    line = LineString([(lon1, lat1), (lon2, lat2)])
    length = _edge_length_m(lon1, lat1, lon2, lat2)

    attrs_common = {
        "length": length,
        "custom_edge": True,
        "osmid": "custom_bridge",
        "name": "custom_bridge",
        "highway": "custom",
        "oneway": False,
    }

    key = G.add_edge(node1, node2, geometry=line, **attrs_common)
    _created_edges.append((G, node1, node2, _edge_key(G, node1, node2, key)))

    key = G.add_edge(
        node2,
        node1,
        geometry=LineString([(lon2, lat2), (lon1, lat1)]),
        **attrs_common,
    )
    _created_edges.append((G, node2, node1, _edge_key(G, node2, node1, key)))

    bridge_line = Polyline(
        locations=[(lat1, lon1), (lat2, lon2)],
        color="red",
        weight=5,
        name="Neue Brücke",
    )
    _clicked_lines.append(bridge_line)
    m.add_layer(bridge_line)
    _refresh_graph_layers()

    return {
        "node1": node1,
        "node2": node2,
        "length": length,
        "geometry": line,
    }


def delete_nearest_edge(click: tuple[float, float], *, remove_reverse: bool = True) -> dict:
    """
    Löscht die Edge, die dem Kartenklick am nächsten liegt.

    click ist eine Leaflet-Koordinate als (lat, lon). Bei bidirektionalen
    Strassen wird standardmässig auch die Gegenrichtung entfernt.
    """
    if m is None or G is None:
        raise RuntimeError("Bitte zuerst init_map(..., G) ausführen.")

    lat, lon = click
    nearest = ox.distance.nearest_edges(G, X=lon, Y=lat)

    if len(nearest) == 3:
        u, v, key = nearest
    else:
        u, v = nearest
        key = None

    data = G.get_edge_data(u, v, key) if key is not None and G.is_multigraph() else G.get_edge_data(u, v)
    if G.is_multigraph() and isinstance(data, dict) and key is None:
        key, data = next(iter(data.items()))

    geometry = None
    if isinstance(data, dict):
        geometry = data.get("geometry")

    if geometry is None:
        geometry = LineString([
            (float(G.nodes[u]["x"]), float(G.nodes[u]["y"])),
            (float(G.nodes[v]["x"]), float(G.nodes[v]["y"])),
        ])

    _remove_edge(G, u, v, key)

    removed = [(u, v, key)]
    if remove_reverse and G.has_edge(v, u):
        reverse_data = G.get_edge_data(v, u)
        if G.is_multigraph() and isinstance(reverse_data, dict):
            for reverse_key in list(reverse_data.keys()):
                _remove_edge(G, v, u, reverse_key)
                removed.append((v, u, reverse_key))
        else:
            _remove_edge(G, v, u)
            removed.append((v, u, None))

    line = Polyline(
        locations=[(lat_, lon_) for lon_, lat_ in geometry.coords],
        color="orange",
        weight=6,
        opacity=0.8,
        dash_array="6",
        name="Geloeschte Edge",
    )
    _deleted_lines.append(line)
    m.add_layer(line)
    _refresh_graph_layers()

    return {"removed_edges": removed, "geometry": geometry}


def handle_click(**kwargs) -> None:
    """
    Click-Handler für `m.on_interaction(handle_click)`.
    Je zwei Klicks erzeugen eine neue Custom-Edge.
    """
    if kwargs.get("type") != "click":
        return

    if m is None:
        raise RuntimeError("Bitte zuerst init_map(..., G) ausführen.")

    lat, lon = kwargs.get("coordinates")

    if _edit_mode == "delete":
        delete_nearest_edge((lat, lon))
        return

    # Nach je zwei Klicks sind die Punkte zurückgesetzt; alte Marker entfernen.
    if len(_clicked_points) == 0:
        for marker in list(_clicked_markers):
            try:
                m.remove_layer(marker)
            except Exception:
                pass
        _clicked_markers.clear()

    _clicked_points.append((lat, lon))

    marker = Marker(location=(lat, lon))
    _clicked_markers.append(marker)
    m.add_layer(marker)

    if len(_clicked_points) == 2:
        create_bridge(_clicked_points[0], _clicked_points[1])
        _clicked_points.clear()


def get_edited_graph():
    """
    Gibt den bearbeiteten, unprojizierten Graphen zurück.
    """
    if G is None:
        raise RuntimeError("Bitte zuerst init_map(..., G) ausführen.")
    return G


def get_custom_edges():
    """
    Gibt alle manuell erzeugten Edges als GeoDataFrame zurück.
    """
    graph = get_edited_graph()
    _, edges = ox.graph_to_gdfs(graph)

    if "custom_edge" not in edges.columns:
        return edges.iloc[0:0].copy()

    return edges[edges["custom_edge"].fillna(False)].copy()


def save_edited_graph(
    graph_path: str | Path = "output/G_edit.graphml",
    custom_edges_path: str | Path | None = "output/custom_edges.geojson",
):
    """
    Speichert den bearbeiteten Graphen und optional die manuell erzeugten Edges.
    """
    graph = get_edited_graph()
    graph_path = Path(graph_path)
    graph_path.parent.mkdir(parents=True, exist_ok=True)
    ox.save_graphml(graph, filepath=graph_path)

    saved = {"graph": graph_path}

    if custom_edges_path is not None:
        custom_edges = get_custom_edges()
        custom_edges_path = Path(custom_edges_path)
        custom_edges_path.parent.mkdir(parents=True, exist_ok=True)
        if custom_edges.empty:
            custom_edges_path.write_text(
                json.dumps({"type": "FeatureCollection", "features": []}),
                encoding="utf-8",
            )
        else:
            custom_edges.to_file(custom_edges_path, driver="GeoJSON")
        saved["custom_edges"] = custom_edges_path

    return saved


def undo_last_bridge() -> None:
    """
    Entfernt die zuletzt erzeugte Brücke, also beide Richtungen im Graphen.
    """
    global _created_edges

    # Eine Brücke erzeugt zwei Edges: hin und zurück.
    for _ in range(min(2, len(_created_edges))):
        graph, u, v, key = _created_edges.pop()
        _remove_edge(graph, u, v, key)

    if m is not None and _clicked_lines:
        line = _clicked_lines.pop()
        try:
            m.remove_layer(line)
        except Exception:
            pass

    _refresh_graph_layers()


def clear_custom_edges() -> None:
    """
    Entfernt alle manuell erzeugten Brücken/Custom-Edges und Kartenlinien.
    """
    reset_edit_state(remove_edges=True)
