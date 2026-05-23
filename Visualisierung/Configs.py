config = {
    "version": "v1",
    "config": {

        "mapState": {
            "latitude": 47.360222,
            "longitude": 8.544444,
            "zoom": 13,
            "bearing": 0,
            "pitch": 0
        },

        "visState": {
            "filters": [
                {
                    "dataId": ["Reisezeitdifferenz"],
                    "id": "zeitdifferenz_filter",
                    "name": ["differenz"],
                    "type": "range",
                    "value": [-587, -1],
                    "plotType": {
                        "type": "histogram"
                    },
                    "animationWindow": "free",
                    "yAxis": None,
                    "view": "side",
                    "speed": 1,
                    "enabled": True
                }
            ],
            "layers": [
# ---------------------------------------------------
# Zeitdifferenz Layer
# ---------------------------------------------------

        {
            "id": "zeitdifferenz_layer",
            "type": "geojson",

            "config": {
                "dataId": "Reisezeitdifferenz",
                "label": "Ersparte Reisedifferenz",

                "columns": {
                    "geojson": "_geojson"
                },

                "isVisible": True,

                "color": [183, 136, 94],
                "highlightColor": [255, 235, 170, 255],

                "visConfig": {
                    "opacity": 0.8,
                    "strokeOpacity": 0.8,
                    "thickness": 1.1,

                    "strokeColorRange": {
                        "colors": [
                            "#FF1A1A",
                            "#FF8C3A",
                            "#F2C94C",
                            "#E8ED99"
                        ],
                        "name": "Zeitdifferenz",
                        "type": "custom",
                        "category": "Custom"
                    },

                    "stroked": True,
                    "filled": False,
                    "enable3d": False,
                    "allowHover": True
                }
            },

            "visualChannels": {
                "colorField": None,
                "colorScale": "quantile",

                "strokeColorField": {
                    "name": "differenz",
                    "type": "integer"
                },
                "strokeColorScale": "quantize",

                "sizeField": None,
                "sizeScale": "linear",

                "heightField": None,
                "heightScale": "linear",

                "radiusField": None,
                "radiusScale": "linear"
            }
        },
# ---------------------------------------------------
# Heatmap Layer
# ---------------------------------------------------

        {
            "id": "heatmap_layer",
            "type": "geojson",

            "config": {
                "dataId": "Heat",
                "label": "Strassenauslastung",

                "columns": {
                    "geojson": "_geojson"
                },

                "isVisible": True,

                "color": [179, 173, 158],
                "highlightColor": [255, 210, 120, 255],

                "visConfig": {
                    "opacity": 0.8,
                    "strokeOpacity": 0.8,

                    # Basisdicke
                    "thickness": 1,

                    "strokeColor": [179, 173, 158],

                    # Linienbreite Bereich
                    "sizeRange": [0.2, 3.2],

                    "strokeColorRange": {
                        "colors": [
                            "#F2F2F2",
                            "#D9D9D9",
                            "#A6A6A6",
                            "#595959"
                        ],
                        "name": "Greyscale Traffic",
                        "type": "custom",
                        "category": "Custom"
                    },

                    "stroked": True,
                    "filled": False,
                    "enable3d": False,
                    "allowHover": True
                }
            },

            "visualChannels": {

                "colorField": None,
                "colorScale": "quantile",

                # Farbe nach Auslastung
                "strokeColorField": {
                    "name": "heat_m",
                    "type": "integer"
                },
                "strokeColorScale": "quantile",

                # Dicke nach Auslastung
                "sizeField": {
                    "name": "heat_m",
                    "type": "integer"
                },
                "sizeScale": "sqrt",

                "heightField": None,
                "heightScale": "linear",

                "radiusField": None,
                "radiusScale": "linear"
            }
        },
# # ---------------------------------------------------
# # Routen Layer
# # ---------------------------------------------------

#                 {
#                     "id": "routen_layer",
#                     "type": "geojson",

#                     "config": {
#                         "dataId": "Trajectories",
#                         "label": "Routen",

#                         "columns": {
#                             "geojson": "_geojson"
#                         },

#                         "isVisible": True,

#                         "visConfig": {
#                             "opacity": 1,
#                             "strokeOpacity": 1,
#                             "thickness": 1,

#                             "strokeColor": [179, 173, 158],

#                             "sizeRange": [0, 2],
# # ----------------------------------------------------
#                         "strokeColorRange": {
#                             "colors": [
#                                 "#8E0152",
#                                 "#F5C3E0",
#                                 "#C7E79F",
#                                 "#276419"
#                             ],
#                             "name": "PiYG",
#                             "type": "diverging",
#                             "category": "ColorBrewer"
#                         },
# # ----------------------------------------------------
#                             "stroked": True,
#                             "filled": False,
#                             "enable3d": False,
#                             "allowHover": True
#                         }
#                     },

#                     "visualChannels": {

#                         "strokeColorField": {
#                             "name": "length",
#                             "type": "real"
#                         },

#                         "strokeColorScale": "quantile",

#                         "sizeField": {
#                             "name": "length",
#                             "type": "real"
#                         },

#                         "sizeScale": "log",

#                         "heightField": None,
#                         "heightScale": "linear",

#                         "radiusField": None,
#                         "radiusScale": "linear",

#                         "colorField": None
#                     }
#                 },

# ---------------------------------------------------
# Bridges Layer
# ---------------------------------------------------

                {
                    "id": "bridges_layer",
                    "type": "geojson",

                    "config": {
                        "dataId": "Bridges",
                        "label": "Bridges",

                        "columns": {
                            "geojson": "_geojson"
                        },

                        "isVisible": True,
                        "color": [150, 152, 176],
                        "highlightColor": [210, 220, 235, 255],

                        "visConfig": {
                            "opacity": 1,
                            "strokeOpacity": 1,
                            "thickness": 1.5,

                            "strokeColor": [150, 152, 176],

                            "stroked": True,
                            "filled": False,

                            "enable3d": False,
                            "allowHover": True
                        }
                    },

                    "visualChannels": {

                        "colorField": None,
                        "colorScale": "quantile",

                        "strokeColorField": None,
                        "strokeColorScale": "quantile",

                        "sizeField": None,
                        "sizeScale": "linear",

                        "heightField": None,
                        "heightScale": "linear",

                        "radiusField": None,
                        "radiusScale": "linear"
                    }
                },

# ---------------------------------------------------
# Tunnels Layer
# ---------------------------------------------------

                {
                    "id": "tunnels_layer",
                    "type": "geojson",

                    "config": {
                        "dataId": "Tunnels",
                        "label": "Tunnels",

                        "columns": {
                            "geojson": "_geojson"
                        },

                        "isVisible": True,
                        "color": [140, 120, 100],
                        "highlightColor": [205, 180, 150, 255],


                        "visConfig": {
                            "opacity": 1,
                            "strokeOpacity": 1,
                            "thickness": 1.5,

                            "strokeColor": [140, 120, 100],

                            "stroked": True,
                            "filled": False,

                            "enable3d": False,
                            "allowHover": True
                        }
                    },

                    "visualChannels": {

                        "colorField": None,
                        "colorScale": "quantile",

                        "strokeColorField": None,
                        "strokeColorScale": "quantile",

                        "sizeField": None,
                        "sizeScale": "linear",

                        "heightField": None,
                        "heightScale": "linear",

                        "radiusField": None,
                        "radiusScale": "linear"
                    }
                },
# ---------------------------------------------------
# Stadt Perimeter Layer
# ---------------------------------------------------

                {
                    "id": "stadt_perimeter_layer",
                    "type": "geojson",

                    "config": {
                        "dataId": "Stadt Perimeter",
                        "label": "Stadt Perimeter",

                        "columns": {
                            "geojson": "_geojson"
                        },

                        "isVisible": True,

                        "color": [110, 140, 235],

                        "highlightColor": [140, 170, 255, 120],

                        "visConfig": {

                            "opacity": 0.005,
                            "strokeOpacity": 0.8,
                            "thickness": 1,

                            "strokeColor": [35, 60, 170],

                            "stroked": True,
                            "filled": True,

                            "enable3d": False,
                            "allowHover": True
                        }
                    },

                    "visualChannels": {

                        "colorField": None,
                        "colorScale": "quantile",

                        "strokeColorField": None,
                        "strokeColorScale": "quantile",

                        "sizeField": None,
                        "sizeScale": "linear",

                        "heightField": None,
                        "heightScale": "linear",

                        "radiusField": None,
                        "radiusScale": "linear"
                    }
                }

            ],

# ---------------------------------------------------
# Tooltips
# ---------------------------------------------------

            "interactionConfig": {
            "tooltip": {
                "enabled": True,
                "compareMode": False,
                "compareType": "absolute",
                "fieldsToShow": {

                    "Tunnels": [
                        {"name": "tunnel", "format": None},
                        {"name": "name", "format": None},
                        {"name": "length", "format": ".2f"}
                    ],

                    "Bridges": [
                        {"name": "name", "format": None},
                        {"name": "length", "format": ".2f"}
                    ],

                    "City_Polygon": [
                        {"name": "name", "format": None}
                    ],

                    "Strassenauslastung": [
                        {"name": "heat_m", "format": ".2f"}
                    ],

                    "ersparte Reisezeit": [
                        {"name": "differenz", "format": ".2f"}
                    ]

                }
            }
        }
        }
    }
}
