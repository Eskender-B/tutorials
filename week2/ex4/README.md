## Exercise4: Practice image processing with OpenCV
- Check out [OpenCV Python Tutorials](https://docs.opencv.org/4.5.3/d6/d00/tutorial_py_root.html)
- Create virtual environment
- `python3 -m venv color_change`
- Activate virtual environment
- `source color_change/bin/activate`
- Install OpenCV while in virtual environment (only once)
- `pip3 install opencv-python`

- Run the two color change scripts as:
- `python3 color_change_inrange.py image1.png --input_hex=00b274 --output_hex=C17A00 --output=output.png`
- `python3 color_change_histogram.py image1.png --output_hex=C17A00 --output=output.png`