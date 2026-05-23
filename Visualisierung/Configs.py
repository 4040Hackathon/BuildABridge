config = {
    "version": "v1",
    "config": {

        "mapState": {
            "latitude": 47.3769,
            "longitude": 8.47,
            "zoom": 10,
            "bearing": 0,
            "pitch": 0
        },

        "visState": {

            "layers": [
# ---------------------------------------------------
# Routen Layer
# ---------------------------------------------------

                {
                    "id": "routen_layer",
                    "type": "geojson",

                    "config": {
                        "dataId": "Trajectories",
                        "label": "Routen",

                        "columns": {
                            "geojson": "_geojson"
                        },

                        "isVisible": True,

                        "visConfig": {
                            "opacity": 1,
                            "strokeOpacity": 1,
                            "thickness": 1,

                            "strokeColor": [179, 173, 158],

                            "sizeRange": [0, 2],
# ----------------------------------------------------
                        "strokeColorRange": {
                            "colors": [
                                "#8E0152",
                                "#F5C3E0",
                                "#C7E79F",
                                "#276419"
                            ],
                            "name": "PiYG",
                            "type": "diverging",
                            "category": "ColorBrewer"
                        },
# ----------------------------------------------------
                            "stroked": True,
                            "filled": False,
                            "enable3d": False,
                            "allowHover": True
                        }
                    },

                    "visualChannels": {

                        "strokeColorField": {
                            "name": "length",
                            "type": "real"
                        },

                        "strokeColorScale": "quantile",

                        "sizeField": {
                            "name": "length",
                            "type": "real"
                        },

                        "sizeScale": "log",

                        "heightField": None,
                        "heightScale": "linear",

                        "radiusField": None,
                        "radiusScale": "linear",

                        "colorField": None
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

                        "highlightColor": [252, 242, 26, 255],

                        "visConfig": {

                            "opacity": 0.12,
                            "strokeOpacity": 1,
                            "thickness": 1.5,

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
                },

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

                        "visConfig": {
                            "opacity": 1,
                            "strokeOpacity": 1,
                            "thickness": 1,

                            "strokeColor": [180, 210, 230],

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

                        "visConfig": {
                            "opacity": 1,
                            "strokeOpacity": 1,
                            "thickness": 1,

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
                }
            ],

# ---------------------------------------------------
# Tooltips
# ---------------------------------------------------

            "interactionConfig": {

                "tooltip": {

                    "fieldsToShow": {

                        "Trajectories": [
                            {"name": "osmid", "format": None},
                            {"name": "highway", "format": None},
                            {"name": "maxspeed", "format": None},
                            {"name": "length", "format": None}
                        ],

                        "Bridges": [
                            {"name": "osmid", "format": None},
                            {"name": "bridge", "format": None},
                            {"name": "highway", "format": None}
                        ],

                        "Tunnels": [
                            {"name": "osmid", "format": None},
                            {"name": "tunnel", "format": None},
                            {"name": "highway", "format": None}
                        ]
                    },

                    "enabled": True
                }
            }
        }
    }
}


#alte version 

# config = {
#     "version": "v1",
#     "config": {
        
#         "mapState": {
#             "latitude": 47.3769,
#             "longitude": 8.47,
#             "zoom": 10,
#             "bearing": 0,
#             "pitch": 0
#         },
#         "visState": {
#                 "layers": [
#                     {
#                     "id": "f2xnwa",
#                     "type": "geojson",
#                     "config": {
#                         "dataId": "Trajectories",
#                         "columnMode": "geojson",
#                         "label": "Routen",
#                         "color": [137, 218, 193],
#                         "highlightColor": [252, 242, 26, 255],
#                         "columns": {
#                             "geojson": "_geojson"
#                         },
#                         "isVisible": True,
#                         "visConfig": {
#                             "opacity": 0.8,
#                             "strokeOpacity": 0.8,
#                             "thickness": 0.5,
#                             "strokeColor": [179, 173, 158],
#                             "colorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "strokeColorRange": {
#                                 "colors": [
#                                     "#184E77",
#                                     "#146E96",
#                                     "#0090AF",
#                                     "#36B5A5",
#                                     "#90D392",
#                                     "#D9ED92"
#                                 ],
#                                 "name": "SummerSky",
#                                 "type": "sequential",
#                                 "category": "Uber"
#                             },
#                             "radius": 10,
#                             "sizeRange": [0, 10],
#                             "radiusRange": [0, 50],
#                             "heightRange": [0, 500],
#                             "elevationScale": 5,
#                             "stroked": True,
#                             "filled": False,
#                             "enable3d": False,
#                             "wireframe": False,
#                             "fixedHeight": False,
#                             "allowHover": True
#                         },
#                         "hidden": False,
#                         "textLabel": [
#                             {
#                                 "field": None,
#                                 "color": [255, 255, 255],
#                                 "size": 18,
#                                 "weight": 400,
#                                 "offset": [0, 0],
#                                 "anchor": "start",
#                                 "alignment": "center",
#                                 "outlineWidth": 0,
#                                 "outlineColor": [255, 0, 0, 255],
#                                 "background": False,
#                                 "backgroundColor": [0, 0, 200, 255]
#                             }
#                         ]
#                     },
#                     "visualChannels": {
#                         "colorField": None,
#                         "colorScale": "quantile",
#                         "strokeColorField": {
#                             "name": "len",
#                             "type": "real"
#                         },
#                         "strokeColorScale": "quantile",
#                         "sizeField": None,
#                         "sizeScale": "linear",
#                         "heightField": None,
#                         "heightScale": "linear",
#                         "radiusField": None,
#                         "radiusScale": "linear"
#                     }
#                 },
# {
#                     "id": "03jpx2d",
#                     "type": "geojson",
#                     "config": {
#                         "dataId": "Stadt Perimeter",
#                         "columnMode": "geojson",
#                         "label": "Stadt Perimeter",
#                         "color": [22, 42, 101],
#                         "highlightColor": [252, 242, 26, 255],
#                         "columns": {
#                             "geojson": "_geojson"
#                         },
#                         "isVisible": True,
#                         "visConfig": {
#                             "opacity": 0.05,
#                             "strokeOpacity": 0.35,
#                             "thickness": 0.35,
#                             "strokeColor": [221, 178, 124],
#                             "colorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "strokeColorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "radius": 10,
#                             "sizeRange": [0, 10],
#                             "radiusRange": [0, 50],
#                             "heightRange": [0, 500],
#                             "elevationScale": 5,
#                             "stroked": True,
#                             "filled": True,
#                             "enable3d": False,
#                             "wireframe": False,
#                             "fixedHeight": False,
#                             "allowHover": True
#                         },
#                         "hidden": False,
#                         "textLabel": [
#                             {
#                                 "field": None,
#                                 "color": [255, 255, 255],
#                                 "size": 18,
#                                 "weight": 400,
#                                 "offset": [0, 0],
#                                 "anchor": "start",
#                                 "alignment": "center",
#                                 "outlineWidth": 0,
#                                 "outlineColor": [255, 0, 0, 255],
#                                 "background": False,
#                                 "backgroundColor": [0, 0, 200, 255]
#                             }
#                         ]
#                     },
#                     "visualChannels": {
#                         "colorField": None,
#                         "colorScale": "quantile",
#                         "strokeColorField": None,
#                         "strokeColorScale": "quantile",
#                         "sizeField": None,
#                         "sizeScale": "linear",
#                         "heightField": None,
#                         "heightScale": "linear",
#                         "radiusField": None,
#                         "radiusScale": "linear"
#                     }
#                 }
#             ],
#         "interactionConfig": {
#             "tooltip": {
#                 "fieldsToShow": {
#                     "Trajectories": [
#                         {"name": "traj_idx", "format": None},
#                         {"name": "start_x", "format": None},
#                         {"name": "start_y", "format": None},
#                         {"name": "end_x", "format": None},
#                         {"name": "end_y", "format": None}
#                     ]
#                     },
#                     "enabled": True
#                 }
#             }
#         }
#     }
# }

# config = {
#     "version": "v1",
#     "config": {
#         "visState": {
#             "filters": [],
            # "layers": [
            #     {
            #         "id": "f2xnwa",
            #         "type": "geojson",
            #         "config": {
            #             "dataId": "Trajectories",
            #             "columnMode": "geojson",
            #             "label": "trajectories_lines_s_4326",
            #             "color": [137, 218, 193],
            #             "highlightColor": [252, 242, 26, 255],
            #             "columns": {
            #                 "geojson": "_geojson"
            #             },
            #             "isVisible": True,
            #             "visConfig": {
            #                 "opacity": 0.8,
            #                 "strokeOpacity": 0.8,
            #                 "thickness": 0.5,
            #                 "strokeColor": [179, 173, 158],
            #                 "colorRange": {
            #                     "name": "Global Warming",
            #                     "type": "sequential",
            #                     "category": "Uber",
            #                     "colors": [
            #                         "#4C0035",
            #                         "#880030",
            #                         "#B72F15",
            #                         "#D6610A",
            #                         "#EF9100",
            #                         "#FFC300"
            #                     ]
            #                 },
            #                 "strokeColorRange": {
            #                     "colors": [
            #                         "#184E77",
            #                         "#146E96",
            #                         "#0090AF",
            #                         "#36B5A5",
            #                         "#90D392",
            #                         "#D9ED92"
            #                     ],
            #                     "name": "SummerSky",
            #                     "type": "sequential",
            #                     "category": "Uber"
            #                 },
            #                 "radius": 10,
            #                 "sizeRange": [0, 10],
            #                 "radiusRange": [0, 50],
            #                 "heightRange": [0, 500],
            #                 "elevationScale": 5,
            #                 "stroked": True,
            #                 "filled": False,
            #                 "enable3d": False,
            #                 "wireframe": False,
            #                 "fixedHeight": False,
            #                 "allowHover": True
            #             },
            #             "hidden": False,
            #             "textLabel": [
            #                 {
            #                     "field": None,
            #                     "color": [255, 255, 255],
            #                     "size": 18,
            #                     "weight": 400,
            #                     "offset": [0, 0],
            #                     "anchor": "start",
            #                     "alignment": "center",
            #                     "outlineWidth": 0,
            #                     "outlineColor": [255, 0, 0, 255],
            #                     "background": False,
            #                     "backgroundColor": [0, 0, 200, 255]
            #                 }
            #             ]
            #         },
            #         "visualChannels": {
            #             "colorField": None,
            #             "colorScale": "quantile",
            #             "strokeColorField": {
            #                 "name": "len",
            #                 "type": "real"
            #             },
            #             "strokeColorScale": "quantile",
            #             "sizeField": None,
            #             "sizeScale": "linear",
            #             "heightField": None,
            #             "heightScale": "linear",
            #             "radiusField": None,
            #             "radiusScale": "linear"
            #         }
            #     }
            # ],
#             "effects": [],
#             "annotations": [],
#             "interactionConfig": {
#                 "tooltip": {
#                     "fieldsToShow": {
#                         "Trajectories": [
#                             {"name": "traj_idx", "format": None},
#                             {"name": "start_x", "format": None},
#                             {"name": "start_y", "format": None},
#                             {"name": "end_x", "format": None},
#                             {"name": "end_y", "format": None}
#                         ]
#                     },
#                     "compareMode": False,
#                     "compareType": "absolute",
#                     "enabled": True
#                 },
#                 "brush": {
#                     "size": 0.5,
#                     "enabled": False
#                 },
#                 "geocoder": {
#                     "limitSearch": False,
#                     "enabled": False
#                 },
#                 "coordinate": {
#                     "enabled": False
#                 }
#             },
#             "layerBlending": "normal",
#             "overlayBlending": "normal",
#             "splitMaps": [],
#             "animationConfig": {
#                 "currentTime": None,
#                 "speed": 1
#             },
#             "editor": {
#                 "features": [],
#                 "visible": True
#             }
#         },
#         "mapState": {
#             "bearing": 0,
#             "dragRotate": False,
#             "latitude": 47.358702202038764,
#             "longitude": 8.497729579060806,
#             "pitch": 0,
#             "zoom": 10.556459779366337,
#             "isSplit": False,
#             "isViewportSynced": True,
#             "isZoomLocked": False,
#             "splitMapViewports": [],
#             "maxPitch": 60
#         },
#         "mapStyle": {
#             "styleType": "dark-matter",
#             "topLayerGroups": {},
#             "visibleLayerGroups": {
#                 "label": True,
#                 "road": True,
#                 "border": False,
#                 "building": True,
#                 "water": True,
#                 "land": True,
#                 "3d building": False
#             },
#             "threeDBuildingColor": [
#                 15.035172933000911,
#                 15.035172933000911,
#                 15.035172933000911
#             ],
#             "backgroundColor": [0, 0, 0],
#             "mapStyles": {}
#         },
#         "uiState": {
#             "mapControls": {
#                 "mapLegend": {
#                     "active": False
#                 }
#             },
#             "locale": "en"
#         }
#     }
# }


#Mit City_perimeter

# config = {
#     "version": "v1",
#     "config": {
#         "visState": {
#             "filters": [],
#             "layers": [
#                 {
#                     "id": "03jpx2d",
#                     "type": "geojson",
#                     "config": {
#                         "dataId": "dloyuo",
#                         "columnMode": "geojson",
#                         "label": "City_Polygon",
#                         "color": [22, 42, 101],
#                         "highlightColor": [252, 242, 26, 255],
#                         "columns": {
#                             "geojson": "_geojson"
#                         },
#                         "isVisible": True,
#                         "visConfig": {
#                             "opacity": 0.13,
#                             "strokeOpacity": 0.8,
#                             "thickness": 0.5,
#                             "strokeColor": [221, 178, 124],
#                             "colorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "strokeColorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "radius": 10,
#                             "sizeRange": [0, 10],
#                             "radiusRange": [0, 50],
#                             "heightRange": [0, 500],
#                             "elevationScale": 5,
#                             "stroked": True,
#                             "filled": True,
#                             "enable3d": False,
#                             "wireframe": False,
#                             "fixedHeight": False,
#                             "allowHover": True
#                         },
#                         "hidden": False,
#                         "textLabel": [
#                             {
#                                 "field": None,
#                                 "color": [255, 255, 255],
#                                 "size": 18,
#                                 "weight": 400,
#                                 "offset": [0, 0],
#                                 "anchor": "start",
#                                 "alignment": "center",
#                                 "outlineWidth": 0,
#                                 "outlineColor": [255, 0, 0, 255],
#                                 "background": False,
#                                 "backgroundColor": [0, 0, 200, 255]
#                             }
#                         ]
#                     },
#                     "visualChannels": {
#                         "colorField": None,
#                         "colorScale": "quantile",
#                         "strokeColorField": None,
#                         "strokeColorScale": "quantile",
#                         "sizeField": None,
#                         "sizeScale": "linear",
#                         "heightField": None,
#                         "heightScale": "linear",
#                         "radiusField": None,
#                         "radiusScale": "linear"
#                     }
#                 },
#                 {
#                     "id": "f2xnwa",
#                     "type": "geojson",
#                     "config": {
#                         "dataId": "grd71",
#                         "columnMode": "geojson",
#                         "label": "trajectories_lines_s_4326",
#                         "color": [137, 218, 193],
#                         "highlightColor": [252, 242, 26, 255],
#                         "columns": {
#                             "geojson": "_geojson"
#                         },
#                         "isVisible": True,
#                         "visConfig": {
#                             "opacity": 0.8,
#                             "strokeOpacity": 0.8,
#                             "thickness": 0.5,
#                             "strokeColor": [179, 173, 158],
#                             "colorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "strokeColorRange": {
#                                 "colors": [
#                                     "#184E77",
#                                     "#146E96",
#                                     "#0090AF",
#                                     "#36B5A5",
#                                     "#90D392",
#                                     "#D9ED92"
#                                 ],
#                                 "name": "SummerSky",
#                                 "type": "sequential",
#                                 "category": "Uber"
#                             },
#                             "radius": 10,
#                             "sizeRange": [0, 2],
#                             "radiusRange": [0, 50],
#                             "heightRange": [0, 500],
#                             "elevationScale": 5,
#                             "stroked": True,
#                             "filled": False,
#                             "enable3d": False,
#                             "wireframe": False,
#                             "fixedHeight": False,
#                             "allowHover": True
#                         },
#                         "hidden": False,
#                         "textLabel": [
#                             {
#                                 "field": None,
#                                 "color": [255, 255, 255],
#                                 "size": 18,
#                                 "weight": 400,
#                                 "offset": [0, 0],
#                                 "anchor": "start",
#                                 "alignment": "center",
#                                 "outlineWidth": 0,
#                                 "outlineColor": [255, 0, 0, 255],
#                                 "background": False,
#                                 "backgroundColor": [0, 0, 200, 255]
#                             }
#                         ]
#                     },
#                     "visualChannels": {
#                         "colorField": None,
#                         "colorScale": "quantile",
#                         "strokeColorField": {
#                             "name": "len",
#                             "type": "real"
#                         },
#                         "strokeColorScale": "quantile",
#                         "sizeField": {
#                             "name": "len",
#                             "type": "real"
#                         },
#                         "sizeScale": "linear",
#                         "heightField": None,
#                         "heightScale": "linear",
#                         "radiusField": None,
#                         "radiusScale": "linear"
#                     }
#                 }
#             ],
#             "effects": [],
#             "annotations": [],
#             "interactionConfig": {
#                 "tooltip": {
#                     "fieldsToShow": {
#                         "grd71": [
#                             {"name": "traj_idx", "format": None},
#                             {"name": "start_x", "format": None},
#                             {"name": "start_y", "format": None},
#                             {"name": "end_x", "format": None},
#                             {"name": "end_y", "format": None}
#                         ],
#                         "dloyuo": []
#                     },
#                     "compareMode": False,
#                     "compareType": "absolute",
#                     "enabled": True
#                 },
#                 "brush": {
#                     "size": 0.5,
#                     "enabled": False
#                 },
#                 "geocoder": {
#                     "limitSearch": False,
#                     "enabled": False
#                 },
#                 "coordinate": {
#                     "enabled": False
#                 }
#             },
#             "layerBlending": "normal",
#             "overlayBlending": "normal",
#             "splitMaps": [],
#             "animationConfig": {
#                 "currentTime": None,
#                 "speed": 1
#             },
#             "editor": {
#                 "features": [],
#                 "visible": True
#             }
#         },
#         "mapState": {
#             "bearing": 0,
#             "dragRotate": False,
#             "latitude": 47.39938949882818,
#             "longitude": 8.529940638749368,
#             "pitch": 0,
#             "zoom": 16.22426687366379,
#             "isSplit": False,
#             "isViewportSynced": True,
#             "isZoomLocked": False,
#             "splitMapViewports": [],
#             "maxPitch": 60
#         },
#         "mapStyle": {
#             "styleType": "dark-matter",
#             "topLayerGroups": {},
#             "visibleLayerGroups": {
#                 "label": True,
#                 "road": True,
#                 "border": False,
#                 "building": True,
#                 "water": True,
#                 "land": True,
#                 "3d building": False
#             },
#             "threeDBuildingColor": [
#                 15.035172933000911,
#                 15.035172933000911,
#                 15.035172933000911
#             ],
#             "backgroundColor": [0, 0, 0],
#             "mapStyles": {}
#         },
#         "uiState": {
#             "mapControls": {
#                 "mapLegend": {
#                     "active": False
#                 }
#             },
#             "locale": "en"
#         }
#     }
# }

# new colour routen

# config = {
#     "version": "v1",
#     "config": {
#         "visState": {
#             "filters": [],
#             "layers": [
#                 {
#                     "id": "gnj7c55",
#                     "type": "geojson",
#                     "config": {
#                         "dataId": "grd71",
#                         "columnMode": "geojson",
#                         "label": "new layer",
#                         "color": [231, 159, 213],
#                         "highlightColor": [252, 242, 26, 255],
#                         "columns": {
#                             "geojson": "_geojson"
#                         },
#                         "isVisible": False,
#                         "visConfig": {
#                             "opacity": 0.8,
#                             "strokeOpacity": 0.8,
#                             "thickness": 0.5,
#                             "strokeColor": [30, 150, 190],
#                             "colorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "strokeColorRange": {
#                                 "name": "Global Warming",
#                                 "type": "sequential",
#                                 "category": "Uber",
#                                 "colors": [
#                                     "#4C0035",
#                                     "#880030",
#                                     "#B72F15",
#                                     "#D6610A",
#                                     "#EF9100",
#                                     "#FFC300"
#                                 ]
#                             },
#                             "radius": 10,
#                             "sizeRange": [0, 10],
#                             "radiusRange": [0, 50],
#                             "heightRange": [0, 500],
#                             "elevationScale": 5,
#                             "stroked": True,
#                             "filled": False,
#                             "enable3d": False,
#                             "wireframe": False,
#                             "fixedHeight": False,
#                             "allowHover": True
#                         },
#                         "hidden": False,
#                         "textLabel": [
#                             {
#                                 "field": None,
#                                 "color": [255, 255, 255],
#                                 "size": 18,
#                                 "weight": 400,
#                                 "offset": [0, 0],
#                                 "anchor": "start",
#                                 "alignment": "center",
#                                 "outlineWidth": 0,
#                                 "outlineColor": [255, 0, 0, 255],
#                                 "background": False,
#                                 "backgroundColor": [0, 0, 200, 255]
#                             }
#                         ]
#                     },
#                     "visualChannels": {
#                         "colorField": None,
#                         "colorScale": "quantile",
#                         "strokeColorField": {
#                             "name": "len",
#                             "type": "real"
#                         },
#                         "strokeColorScale": "quantile",
#                         "sizeField": None,
#                         "sizeScale": "linear",
#                         "heightField": None,
#                         "heightScale": "linear",
#                         "radiusField": None,
#                         "radiusScale": "linear"
#                     }
#                 },
#                 {
#                     "id": "85kkd7",
#                     "type": "line",
#                     "config": {
#                         "dataId": "grd71",
#                         "columnMode": "points",
#                         "label": "trajectories_lines_s_4326",
#                         "color": [137, 218, 193],
#                         "highlightColor": [252, 242, 26, 255],
#                         "columns": {
#                             "lat0": "start_y",
#                             "lng0": "start_x",
#                             "lat1": "end_y",
#                             "lng1": "end_x"
#                         },
#                         "isVisible": True,
#                         "visConfig": {
#                             "opacity": 0.8,
#                             "thickness": 1,
#                             "colorRange": {
#                                 "colors": [
#                                     "#8E0152",
#                                     "#F5C3E0",
#                                     "#C7E79F",
#                                     "#276419"
#                                 ],
#                                 "name": "PiYG",
#                                 "type": "diverging",
#                                 "category": "ColorBrewer"
#                             },
#                             "sizeRange": [0, 5],
#                             "targetColor": None,
#                             "elevationScale": 5
#                         },
#                         "hidden": False,
#                         "textLabel": [
#                             {
#                                 "field": None,
#                                 "color": [255, 255, 255],
#                                 "size": 18,
#                                 "weight": 400,
#                                 "offset": [0, 0],
#                                 "anchor": "start",
#                                 "alignment": "center",
#                                 "outlineWidth": 0,
#                                 "outlineColor": [255, 0, 0, 255],
#                                 "background": False,
#                                 "backgroundColor": [0, 0, 200, 255]
#                             }
#                         ]
#                     },
#                     "visualChannels": {
#                         "colorField": {
#                             "name": "len",
#                             "type": "real"
#                         },
#                         "colorScale": "quantile",
#                         "sizeField": {
#                             "name": "len",
#                             "type": "real"
#                         },
#                         "sizeScale": "log"
#                     }
#                 }
#             ],
#             "effects": [],
#             "annotations": [],
#             "interactionConfig": {
#                 "tooltip": {
#                     "fieldsToShow": {
#                         "grd71": [
#                             {"name": "traj_idx", "format": None},
#                             {"name": "start_x", "format": None},
#                             {"name": "start_y", "format": None},
#                             {"name": "end_x", "format": None},
#                             {"name": "end_y", "format": None}
#                         ]
#                     },
#                     "compareMode": False,
#                     "compareType": "absolute",
#                     "enabled": True
#                 },
#                 "brush": {
#                     "size": 0.5,
#                     "enabled": False
#                 },
#                 "geocoder": {
#                     "limitSearch": False,
#                     "enabled": False
#                 },
#                 "coordinate": {
#                     "enabled": False
#                 }
#             },
#             "layerBlending": "normal",
#             "overlayBlending": "normal",
#             "splitMaps": [],
#             "animationConfig": {
#                 "currentTime": None,
#                 "speed": 1
#             },
#             "editor": {
#                 "features": [],
#                 "visible": True
#             }
#         },
#         "mapState": {
#             "bearing": 0,
#             "dragRotate": False,
#             "latitude": 47.40116403933529,
#             "longitude": 8.51041723080349,
#             "pitch": 0,
#             "zoom": 11.821230996880724,
#             "isSplit": False,
#             "isViewportSynced": True,
#             "isZoomLocked": False,
#             "splitMapViewports": [],
#             "maxPitch": 60
#         },
#         "mapStyle": {
#             "styleType": "dark-matter",
#             "topLayerGroups": {},
#             "visibleLayerGroups": {
#                 "label": True,
#                 "road": True,
#                 "border": False,
#                 "building": True,
#                 "water": True,
#                 "land": True,
#                 "3d building": False
#             },
#             "threeDBuildingColor": [
#                 15.035172933000911,
#                 15.035172933000911,
#                 15.035172933000911
#             ],
#             "backgroundColor": [0, 0, 0],
#             "mapStyles": {}
#         },
#         "uiState": {
#             "mapControls": {
#                 "mapLegend": {
#                     "active": False
#                 }
#             },
#             "locale": "en"
#         }
#     }
# }