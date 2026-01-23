from smbus2 import SMBus

bus = SMBus(1)

def pad_value(value: float) -> str:
  padded = f"{value:.4f}"
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


import time

while True:
  send_packet(0x08, "hello");
  time.sleep(1)