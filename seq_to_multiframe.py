import pydicom
import numpy as np
import os
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
    new_dicom.Rows, new_dicom.Columns, new_dicom.NumberOfFrames = pixel_array.shape
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
    
def combine_dicom():
    # Specify the directory containing DICOM files
    dicom_dir = '/Users/yaellyshkow/Desacc/polar_transformation/PolarTransform/dicom_files'

    # Load DICOM files
    dicom_files = [pydicom.dcmread(os.path.join(dicom_dir, filename)) for filename in sorted(os.listdir(dicom_dir))]

    # Extract pixel data and stack into a 3D numpy array
    stacked_volume = np.stack([df.pixel_array for df in dicom_files])
    return stacked_volume
    


def main():
    # Example usage
    # input_files = [f"/Users/yaellyshkow/Desacc/polar_transformation/PolarTransform/dicom_files/result_{i}.dcm" for i in range(80)]
    # output_file = "/Users/yaellyshkow/Desktop/pleaseeee.dcm"
    stacked_volume = combine_dicom()
    new_dicom = create_dicom_dataset(stacked_volume)

    # Save the DICOM dataset to a file
    save_dicom_file(new_dicom, "/Users/yaellyshkow/Desktop/pleaseeee.dcm")

if __name__ == "__main__":
    main()