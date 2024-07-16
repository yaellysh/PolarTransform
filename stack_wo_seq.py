import numpy as np
from PIL import Image
import os
import pydicom
from datetime import datetime

def create_dicom_dataset(stacked_volume):
    # Create a new DICOM dataset
    new_dicom = pydicom.Dataset()

    # Set mandatory DICOM tags
    new_dicom.PatientName = "Anonymous"
    new_dicom.PatientID = "123456"
    new_dicom.Modality = "OT"
    new_dicom.StudyDate = datetime.now().strftime('%Y%m%d')
    new_dicom.StudyTime = datetime.now().strftime('%H%M%S')
    new_dicom.PixelSpacing = [1.0, 1.0]
    new_dicom.SliceThickness = 1.0
    new_dicom.ImagePositionPatient = [0.0, 0.0, 0.0]
    new_dicom.ImageOrientationPatient = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0]

    # Convert stacked_volume to uint16 (assuming it's in a suitable format)
    pixel_array = stacked_volume.astype(np.uint16)

    # Set image-specific tags
    # print(pixel_array.shape)
    new_dicom.NumberOfFrames, new_dicom.Rows, new_dicom.Columns  = pixel_array.shape
    new_dicom.BitsAllocated = 16
    new_dicom.BitsStored = 16
    new_dicom.HighBit = 15
    new_dicom.PixelRepresentation = 0  # unsigned integer

    # Set pixel data
    new_dicom.PixelData = pixel_array.tobytes()
    new_dicom.is_little_endian = True
    new_dicom.is_implicit_VR = False

    return new_dicom

def save_dicom_file(dataset, filename):
    # Save the dataset to a DICOM file
    dataset.save_as(filename)

def combine_png_files(png_dir):
    # Load PNG files
    png_files = [np.array(Image.open(os.path.join(png_dir, filename))) for filename in sorted(os.listdir(png_dir)) if filename.endswith('.png')]

    # Stack PNG images into a 3D numpy array
    stacked_volume = np.stack(png_files)
    return stacked_volume

def main():
    # Specify the directory containing PNG files
    png_dir = "/Users/yaellyshkow/Desacc/polar_transformation/PolarTransform/transformed_images"

    # Combine PNG files into a stacked volume
    stacked_volume = combine_png_files(png_dir)

    # Create a DICOM dataset from the stacked volume
    new_dicom = create_dicom_dataset(stacked_volume)

    # Save the DICOM dataset to a file
    save_dicom_file(new_dicom, "/Users/yaellyshkow/Desktop/pleaseeee.dcm")

if __name__ == "__main__":
    main()
