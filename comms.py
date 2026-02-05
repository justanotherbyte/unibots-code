from smbus2 import SMBus

bus = SMBus(1)

SLAVE_ADDRESS = 0x08

def pad_value(value: float) -> str:
  padded = f"{value:.2f}"
  if int(padded.split(".")[0]) < 100:
    padded = "0" + padded

  return padded

def send_esp32(data: bytes):
  bus.write_i2c_block_data(SLAVE_ADDRESS, 0, list(data))

def send_packet(
    left_motor_speed: int,
    right_motor_speed: int,
    raise_platform: bool
):
  # send_esp32("L".encode("ascii"))
  send_esp32(left_motor_speed.to_bytes(length=1, byteorder="big", signed=True))
  # send_esp32("R".encode("ascii"))
  # send_esp32(right_motor_speed.to_bytes(length=1, byteorder="big", signed=True))

import time

while True:
  send_packet(64, 67, True)
  time.sleep(0.5)