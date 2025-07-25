#  Python Terrain Analysis Toolkit

This project is a **command-line Python script** for performing fundamental **geomorphometric analysis** on Digital Elevation Models (DEMs). It was built to automate the repetitive task of calculating key terrain parameters, forming a basis for more advanced **geoinformatics** and **remote sensing analysis**.

The script takes a single DEM file and generates three core terrain parameter maps: **Slope**, **Aspect**, and **Hillshade**.

---

##  What It Does

- **Calculates Slope**: Determines the steepness of the terrain at every point.  
- **Determines Aspect**: Finds the compass direction each slope is facing.  
- **Generates Hillshade**: Creates a 3D-like shaded relief map for visualization.  
- **Keeps Things Organized**: Saves all output maps into a **timestamped folder** for each run.  
- **Logs Everything**: Automatically creates a **CSV log file** recording:
  - Timestamp of the run  
  - Minimum and maximum elevation of the input DEM  

---

##  Tech Stack

- **Python 3**  
- **Rasterio** – For handling GeoTIFF files and maintaining projection metadata.  
- **NumPy** – For high-performance numerical computation on elevation matrices.  

---

## How to Get It Running

### 1️⃣ Install the prerequisites

Make sure you have Python 3 installed. Then run:

```bash
pip install rasterio numpy
````

---

### 2️⃣ Clone this repository

```bash
git clone https://github.com/TheAstralVeil/Python-Terrain-Analysis-Toolkit.git
cd Python-Terrain-Analysis-Toolkit
```

---

### 3️⃣ Configure your DEM path

Open the `geomorph_analyzer.py` file and scroll to the bottom. Change the path of the `dem_file` variable to point to your own `.tif` DEM file:

```python
if __name__ == "__main__":
    # --- Point this to your DEM file! ---
    dem_file = r"C:\path\to\your\dem.tif"

    # Run the analysis
    process_dem(dem_file)
```

---

### 4️⃣ Run the script

Navigate to the project directory in your terminal and execute:

```bash
python geomorph_analyzer.py
```

If successful, you'll see a **"Success!"** message with the name of the output folder.

---

##  What's Next?

This toolkit is a great starting point. Future features could include:

*  **More Parameters**: Add advanced terrain metrics like *Curvature*, *TWI*, or *Stream Power Index*.
*  **Batch Processing**: Support for processing folders of DEMs at once.
*  **Command-Line Interface**: Use `argparse` to allow file paths to be passed via command line.
*  **Quick Previews**: Use `matplotlib` to automatically preview generated maps after processing.

---

##  License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.




Quick Previews: Using matplotlib to generate a quick plot of the output maps right after the script finishes.

License

This project is licensed under the MIT License.
