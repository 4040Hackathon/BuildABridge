from pathlib import Path
import requests


def download_opentopography_dem(
    api_key: str,
    output_file: str | Path,
    demtype: str = "COP30",
    south: float = -90,
    north: float = 90,
    west: float = -180,
    east: float = 180,
    output_format: str = "GTiff",
    timeout: int = 300,
) -> Path:
    """
    Lädt ein DEM-Raster von OpenTopography Global DEM API herunter.

    Parameters
    ----------
    api_key : str
        Dein OpenTopography API Key.
    output_file : str | Path
        Zielpfad, z.B. "global_dem.tif".
    demtype : str
        DEM-Typ, z.B.:
        - "SRTMGL3"   für SRTM 90m
        - "SRTMGL1"   für SRTM 30m
        - "AW3D30"    für ALOS World 3D 30m
        - "NASADEM"   für NASADEM
        - "COP30"     für Copernicus DEM 30m
        - "COP90"     für Copernicus DEM 90m
        - "SRTM15Plus" für globale Bathymetrie/Topographie
    south, north, west, east : float
        Bounding Box in WGS84-Koordinaten.
        Für global: south=-90, north=90, west=-180, east=180.
    output_format : str
        Ausgabeformat, typischerweise "GTiff".
    timeout : int
        Timeout in Sekunden.

    Returns
    -------
    Path
        Pfad zur gespeicherten Datei.
    """

    url = "https://portal.opentopography.org/API/globaldem"

    params = {
        "demtype": demtype,
        "south": south,
        "north": north,
        "west": west,
        "east": east,
        "outputFormat": output_format,
        "API_Key": api_key,
    }

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(
        url,
        params=params,
        stream=True,
        timeout=timeout,
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"OpenTopography API Fehler {response.status_code}:\n"
            f"{response.text}"
        )

    content_type = response.headers.get("Content-Type", "")

    if "application/json" in content_type or "text" in content_type:
        text = response.text[:1000]
        raise RuntimeError(
            "Die API hat keine Rasterdatei zurückgegeben. "
            f"Antwort:\n{text}"
        )

    with output_file.open("wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    return output_file