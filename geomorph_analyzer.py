import rasterio as rio
import numpy as np
import os
import datetime
import csv

def derive_slope(dem_array):
    """Derives slope from a DEM array."""
    gy, gx = np.gradient(dem_array)
    slope_rad = np.arctan(np.sqrt(gx**2 + gy**2))
    slope_deg = np.degrees(slope_rad)
    return slope_deg

def derive_aspect(dem_array):
    """Derives aspect from a DEM array."""
    gy, gx = np.gradient(dem_array)
    aspect_rad = np.arctan2(gy, gx)
    aspect_deg = np.degrees(aspect_rad)
    # Ensure aspect is 0-360, not -180 to 180
    aspect_deg[aspect_deg < 0] += 360
    return aspect_deg

def derive_hillshade(slope, aspect, altitude=45, azimuth=315):
    """Derives hillshade from slope and aspect arrays."""
    # Note: altitude is angle from horizon, zenith is angle from vertical.
    zenith_deg = 90 - altitude
    # Convert all our angles to radians for numpy's trig functions
    azimuth_rad = np.radians(azimuth)
    zenith_rad = np.radians(zenith_deg)
    slope_rad = np.radians(slope)
    aspect_rad = np.radians(aspect)
    # The actual hillshade formula, scaled to a 0-255 byte range for images.
    hillshade = 255 * ( (np.cos(zenith_rad) * np.cos(slope_rad)) +
                        (np.sin(zenith_rad) * np.sin(slope_rad) * np.cos(azimuth_rad - aspect_rad)) )
    return hillshade

def process_dem(dem_filepath):
    """Main function to run the full terrain analysis."""
    
    # Create a unique output directory for this run.
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = f"Analysis_{timestamp}"
    os.makedirs(out_dir, exist_ok=True)
    
    try:
        with rio.open(dem_filepath) as src:
            dem_array = src.read(1)
            # Copy the metadata profile for georeferencing.
            profile = src.meta.copy()

            # Get some basic stats for the log.
            min_elev = np.nanmin(dem_array)
            max_elev = np.nanmax(dem_array)

            # --- Derive and save terrain parameters ---
            slope = derive_slope(dem_array)
            aspect = derive_aspect(dem_array)
            hillshade = derive_hillshade(slope, aspect)
            
            # A dictionary to hold the data arrays and desired filenames
            outputs = {
                "slope": slope,
                "aspect": aspect,
                "hillshade": hillshade
            }

            for name, data_array in outputs.items():
                out_path = os.path.join(out_dir, f"{name}.tif")
                with rio.open(out_path, 'w', **profile) as dst:
                    dst.write(data_array.astype(rio.float32), 1)

            # --- Write a log file for our records ---
            log_path = os.path.join(out_dir, "run_log.csv")
            log_data = [timestamp, dem_filepath, min_elev, max_elev]
            
            with open(log_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "input_file", "min_elevation", "max_elevation"])
                writer.writerow(log_data)
            
            print(f"Success! Outputs saved to: ./{out_dir}")

    except FileNotFoundError:
        print(f"\nError: Couldn't find the file at '{dem_filepath}'")
    except Exception as e:
        print(f"\nSomething went wrong: {e}")

# This is the standard entry point for a Python script.
if __name__ == "__main__":
    # Define the path to your input DEM file here.
    dem_file = r"C:\Users\Astral\Documents\DEM.tif"
    
    # Let's go!
    process_dem(dem_file)