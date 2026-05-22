import geopandas as gpd
import numpy as np
import geopandas as gpd
from shapely import linestrings, points


def process_region(
    input_path="data/Admin_Boundaries/regions.shp",
    output_polygon_path="output/City_Polygon.json",
    target_crs="EPSG:3857",
    buffer_distance=5
):
    """
    Reads a WorldMove Administrative Area Dataset, reprojects it, creates a buffered union polygon,
    and exports the results as GeoJSON files.

    Parameters
    ----------
    input_path : str
        Path to the input shapefile.
    output_polygon_path : str
        Output path for the polygon GeoJSON.
    target_crs : str
        CRS used for reprojection.
    buffer_distance : float
        Buffer distance applied to buffered Polygon.
    """

    # Read data
    region = gpd.read_file(input_path)
    region_proj = region.to_crs("EPSG:3857")

    # Create buffered union polygon
    polygon_gdf = gpd.GeoDataFrame(
        geometry=[region_proj.buffer(5).union_all()],
        crs=region_proj.crs
    )

    polygon_buffered = polygon_gdf.buffer(buffer_distance)
    
    # Reproject
    if polygon_gdf.crs != target_crs:
        polygon_gdf = polygon_gdf.to_crs(target_crs)
        polygon_buffered = polygon_buffered.to_crs(target_crs)
        print(f"Regions reprojected to {target_crs}")
    else:
        print(f"Regions in crs {region.crs}")

    # Export polygon
    polygon_gdf.to_file(output_polygon_path, driver="GeoJSON")

    print("Prozess abgeschlossen.")

    return region_proj, polygon_gdf, polygon_buffered


def load_trajectory_lines(npz_path, polygon=None, crs_output=3857, max_distance=70000, randomise=False):
    """
    Load trajectory dataset and create:
    - point GeoDataFrame
    - line GeoDataFrame connecting consecutive trajectory points

    Parameters
    ----------
    npz_path : str
        Path to trajectories.npz
    polygon : shapely geometry, optional
        Polygon used for clipping trajectories
    crs_points : str
        CRS of lon/lat coordinates
    crs_projected : int/str
        Metric CRS for line operations
    max_distance : int
        Maximum length of single trajectorie linesegments

    Returns
    -------
    gdf_traj : GeoDataFrame
        Point trajectories
    gdf_lines : GeoDataFrame
        Consecutive trajectory segments
    """

    # ── Load data ──────────────────────────────────────────────────────────
    data = np.load(npz_path, allow_pickle=True)

    # create Dictionnary from Grid entries
    grid_dict = {
        int(k): v           # define key-Value pair
        for k, v in data["grid"].item().items()     # assign key-value
    }

    # creates numpy-array from trajecotrie entries
    trajectories = data["traj"]

    # ── Expand trajectories ───────────────────────────────────────────────
    n_traj, n_steps = trajectories.shape
    crs_input="EPSG:4326"

    traj_idx = np.repeat(np.arange(n_traj), n_steps)        # creates index for trajectories. creates n_steps times the same index for n timesteps
    step_idx = np.tile(np.arange(n_steps), n_traj)      # creates n_traj times the index 0-n_steps
    cell_ids = trajectories.ravel()     # creates onedimensional array from cell ids

    # coordinates lookup
    coords = np.array([grid_dict[c] for c in cell_ids])     # loops through every cell_id c in cell_ids and writes the according coordinates to the array

    lons = coords[:, 0]
    lats = coords[:, 1]

    point_geom = points(
        np.stack([lons, lats], axis=1)
    )
    print(point_geom)

    if randomise:
    # random latitude offset (~1 km)
        lat_offset = 1000 / 111320

    # random longitude offset (~1 km at current latitude)
        lon_offset = 1000 / (
            111320 * np.cos(np.radians(lats.mean()))
        )

        random_lat = np.random.uniform(
            -lat_offset,
            lat_offset,
            len(lats)
        )

        random_lon = np.random.uniform(
            -lon_offset,
            lon_offset,
            len(lons)
        )

        lats += random_lat
        lons += random_lon

    # ── Point GeoDataFrame ────────────────────────────────────────────────
    gdf_traj = gpd.GeoDataFrame(
        {
            "traj_idx": traj_idx,
            "step": step_idx,
            "cell_id": cell_ids,
            "lon": lons,
            "lat": lats,
        },
        geometry=gpd.points_from_xy(lons, lats),
        crs=crs_input,
    )

    # project to output CRS
    gdf_traj = gdf_traj.to_crs(crs_output)

    # optional clipping
    if polygon is not None:
        gdf_traj = gdf_traj.clip(polygon, keep_geom_type=True)

    # ── Build LineStrings ─────────────────────────────────────────────────
    gdf_traj = gdf_traj.sort_values(["traj_idx", "step"])

    xy = np.column_stack([
        gdf_traj.geometry.x.to_numpy(),
        gdf_traj.geometry.y.to_numpy()
    ])

    traj_ids = gdf_traj["traj_idx"].to_numpy()

    # identify valid consecutive pairs
    valid = traj_ids[:-1] == traj_ids[1:]

    starts = xy[:-1][valid]
    ends = xy[1:][valid]

    geometries = linestrings(
        np.stack([starts, ends], axis=1)
    )

    gdf_lines = gpd.GeoDataFrame(
        {
            "traj_idx": traj_ids[:-1][valid],
            "start_x": list(starts[:,0]),
            "start_y": list(starts[:,1]),
            "end_x": list(ends[:,0]),
            "end_y": list(ends[:,1]),
        },
        geometry=geometries,
        crs=gdf_traj.crs,
    )

    # remove zero-length lines
    gdf_lines["len"] = gdf_lines.length
    gdf_lines = gdf_lines[gdf_lines["len"] > 0]

    return gdf_traj, gdf_lines