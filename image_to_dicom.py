# https://pydicom.github.io/pydicom/stable/auto_examples/input_output/plot_write_dicom.html: code for creating new empty dicom file
# https://github.com/amine0110/convert-images-from-jpr-or-png-into-dicom/blob/main/jpt_into_dicom.py: code for adding image to existing dicom file

import datetime
import tempfile
import numpy as np
import pydicom
from PIL import Image
from pydicom.dataset import FileDataset, FileMetaDataset
from pydicom.uid import UID

def create_file_metadata() -> FileMetaDataset:
    # print("Setting file meta information...")
    # Populate required values for file meta information
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = UID('1.2.840.10008.5.1.4.1.1.2') # arbitrary UID, change later/ get from metadata??
    file_meta.MediaStorageSOPInstanceUID = UID("1.2.3")
    file_meta.ImplementationClassUID = UID("1.2.3.4")
    return file_meta

def create_dataset(filename, file_meta):
    # Create the FileDataset instance (initially no data elements, but file_meta supplied)
    ds = FileDataset(filename, {},
                 file_meta=file_meta, preamble=b"\0" * 128)

    # Add the data elements -- not trying to set all required here. Check DICOM standard
    ds.PatientName = "Test^Firstname"
    ds.PatientID = "123456"

    # Set the transfer syntax
    ds.is_little_endian = True
    ds.is_implicit_VR = True

    # Set creation date/time
    dt = datetime.datetime.now()
    ds.ContentDate = dt.strftime('%Y%m%d')
    timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
    ds.ContentTime = timeStr
    return ds

def save_as_big_little_endian(endianess: str, ds, filename):
    if endianess == 'little':
        ds.save_as(filename)
    elif endianess == "big":
        ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRBigEndian
        ds.is_little_endian = False
        ds.is_implicit_VR = False
        ds.save_as(filename)
    else:
        return None

def update_dataset_with_image(ds, image_path):
    jpg_image = Image.open(image_path)  # the PNG or JPG file to be replaced

    # Ensure the image is in grayscale mode
    if jpg_image.mode != 'L':
        jpg_image = jpg_image.convert('L')

    np_image = np.array(jpg_image, dtype=np.uint8)

    # Update the dataset with image data
    ds.Rows = jpg_image.height
    ds.Columns = jpg_image.width
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.SamplesPerPixel = 1
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.PixelRepresentation = 0
    ds.PixelData = np_image.tobytes()

    # Sets the Value Representation of the pixel data to 'OB' (Other Byte), for 8-bit data so the DICOM file writes the pixel data correctly
    ds[(0x7fe0, 0x0010)].VR = 'OB'
    return ds

def main():
    suffix = '.dcm'
    filename_little_endian = tempfile.NamedTemporaryFile(suffix=suffix).name
    filename_big_endian = tempfile.NamedTemporaryFile(suffix=suffix).name

    print("Setting file meta information...")
    file_meta = create_file_metadata()

    print("Setting dataset values...")
    ds = create_dataset(filename_little_endian, file_meta)

    save_as_big_little_endian("little", ds, filename_little_endian)
    save_as_big_little_endian("big", ds, filename_big_endian)

    image_path = "/Users/yaellyshkow/Desacc/polar_transformation/PolarTransform/transformed_images/polar_image_0.png"
    ds = update_dataset_with_image(ds, image_path)

    output_filename = '/Users/yaellyshkow/Desktop/result_gray.dcm'
    ds.save_as(output_filename)
    print(f"Final DICOM file saved as {output_filename}")

if __name__ == "__main__":
    main()