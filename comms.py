from smbus2 import SMBus

bus = SMBus(1)

SLAVE_ADDRESS = 0x08

def pad_value(value: float) -> str:
  padded = f"{value:.2f}"
  if int(padded.split(".")[0]) < 100:
    padded = "0" + padded

  return padded

def create_data_packet(
    left_motor_speed: float,
    right_motor_speed: float,
    raise_platform: bool
) -> str:
  lm_speed = pad_value(left_motor_speed)
  rm_speed = pad_value(right_motor_speed)

  return f"L{lm_speed}R{rm_speed}P{int(raise_platform)}"


def send_packet(address: int, packet: str):
  data = list(packet.encode("utf-8"))
  bus.write_i2c_block_data(address, 0, data)

def send_esp32(data: bytes):
  bus.write_i2c_block_data(SLAVE_ADDRESS, 0, list(data))

def send_packet(
    left_motor_speed: int,
    right_motor_speed: int,
    raise_platform: bool
):
  send_esp32("L".encode("ascii"))
  send_esp32(left_motor_speed.to_bytes(length=1, byteorder="little", signed=True))
  send_esp32("R".encode("ascii"))
  send_esp32(right_motor_speed.to_bytes(length=1, byteorder="little", signed=True))

import time

while True:
  packet = create_data_packet(2.3, 4.3, False)
  send_packet(64, 67, True)
  time.sleep(1)