from steganogan import SteganoGAN
from steganogan.critics import BasicCritic
from steganogan.decoders import DenseDecoder
from steganogan.encoders import DenseEncoder
from steganogan.loader import DataLoader
 
import numpy as np
import argparse

steganogan = SteganoGAN.load(architecture='dense')

def get_parse():
    parser = argparse.ArgumentParser(description="SteganoGAN")

    parser.add_argument(
        "--mode",
        type=str,
        default="encode",
        help=f"Choose mode: Encode or Decode",
    )

    parser.add_argument(
        "--input",
        type=str,
        default="./default.png",
        help=f"Locate the input (default *.png)",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="./hide.png",
        help=f"Locate the output",
    )

    args = parser.parse_args()

    return args

def encode(input, output, message):
    steganogan.encode(input, output, message)
    print("-------------Successfully encode image----------")

def decode(input):
    steganogan.decode(input)

if __name__ == "__main__":
    arg = get_parse()

    if(arg.mode == "encode"):
        print("------------------Encoding image----------------")
        message = input("Enter message: ")
        encode(arg.input, arg.output, message)

    if(arg.mode == "decode"):
        print("------------------Decode image------------------")
        decode(arg.input)