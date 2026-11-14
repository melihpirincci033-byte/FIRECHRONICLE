
import numpy as np

def assign_grid_cells(df, resolution=0.1):
    """
    Assign satellite detections to common geographic cells.

    This is spatial alignment, not sensor calibration.
    """

    result = df.copy()

    result["grid_lat"] = np.floor(
        result["latitude"] / resolution
    ).astype(int)

    result["grid_lon"] = np.floor(
        result["longitude"] / resolution
    ).astype(int)

    return result
