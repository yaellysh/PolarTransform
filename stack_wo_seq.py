import numpy as np
from PIL import Image
import os
from pydicom.dataset import FileDataset, FileMetaDataset
from pydicom.uid import generate_uid, ExplicitVRLittleEndian, MultiFrameTrueColorSecondaryCaptureImageStorage
from datetime import datetime

def create_dicom_dataset(stacked_volume: np.ndarray, output_im: str):
    # Convert stacked_volume to uint16 (assuming it's in a suitable format)
    pixel_array = stacked_volume.astype(np.uint16)

    # Create a new DICOM dataset
    file_metadata = FileMetaDataset()
    # file_metadata.MediaStorageSOPClassUID = generate_uid()
    file_metadata.MediaStorageSOPClassUID = MultiFrameTrueColorSecondaryCaptureImageStorage
    file_metadata.MediaStorageSOPInstanceUID = generate_uid()
    file_metadata.ImplementationClassUID = generate_uid()
    file_metadata.TransferSyntaxUID = ExplicitVRLittleEndian

    new_dicom = FileDataset(output_im, {}, file_meta=file_metadata, preamble=b"\0" * 128)

    # Set mandatory DICOM tags
    new_dicom.PatientName = "Anonymous"
    new_dicom.PatientID = "123456"
    new_dicom.StudyInstanceUID = generate_uid()
    new_dicom.SeriesInstanceUID = generate_uid()
    new_dicom.SOPInstanceUID = file_metadata.MediaStorageSOPInstanceUID
    new_dicom.SOPClassUID = file_metadata.MediaStorageSOPClassUID

    new_dicom.Modality = "OT"
    new_dicom.StudyDate = datetime.now().strftime('%Y%m%d')
    new_dicom.StudyTime = datetime.now().strftime('%H%M%S')
    new_dicom.PixelSpacing = [1.0, 1.0]
    new_dicom.SliceThickness = 1.0
    new_dicom.ImagePositionPatient = [0.0, 0.0, 0.0]
    new_dicom.ImageOrientationPatient = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0]

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

    new_dicom.SamplesPerPixel = 1
    new_dicom.PhotometricInterpretation = "MONOCHROME2"
    new_dicom.BitsAllocated = 16
    new_dicom.BitsStored = 8
    new_dicom.HighBit = 7
    new_dicom.PixelRepresentation = 0

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
    png_dir = "/Users/yaellyshkow/Desacc/polar_transformation/PolarTransform/transformed_images_2"
    output_im = "/Users/yaellyshkow/Desktop/final_2.dcm"

    # Combine PNG files into a stacked volume
    stacked_volume = combine_png_files(png_dir)

    # Create a DICOM dataset from the stacked volume
    new_dicom = create_dicom_dataset(stacked_volume, output_im)

    # Save the DICOM dataset to a file
    save_dicom_file(new_dicom, output_im)

if __name__ == "__main__":
    main()
